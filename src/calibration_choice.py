"""Identical-prompt free, exact trie-constrained and teacher-forced channels."""
import math
import time

from .experiment_v3 import parse_answer
from .experiment_v3_3 import sha
from .generation.local_hf_adapter import LocalHFAdapter


class CandidateTrie:
    def __init__(self, sequences, eos):
        self.eos = eos
        self.children = {}
        self.terminals = set()
        for seq in sequences:
            seq = tuple(seq)
            if not seq or eos in seq:
                raise ValueError('Invalid candidate token sequence')
            self.terminals.add(seq)
            for i, token in enumerate(seq):
                self.children.setdefault(seq[:i], set()).add(token)
        if len(self.terminals) != len(sequences):
            raise ValueError('Token-identical candidates')

    def allowed(self, prefix):
        prefix = tuple(prefix)
        tokens = set(self.children.get(prefix, ()))
        if prefix in self.terminals:
            tokens.add(self.eos)
        if not tokens:
            raise ValueError('Generated prefix left the candidate trie')
        return sorted(tokens)

    def audit(self):
        reached = set()
        stack = [()]
        while stack:
            prefix = stack.pop()
            for token in self.allowed(prefix):
                if token == self.eos:
                    reached.add(prefix)
                else:
                    stack.append(prefix + (token,))
        if reached != self.terminals:
            raise ValueError('Candidate reachability mismatch')
        return True


def free_fields(raw, names, truncated=False):
    import re
    found = [name for name in names if re.search(r'(?<!\w)' + re.escape(name) + r'(?!\w)', raw)]
    exact = raw.strip() in names and not truncated
    parsed = parse_answer(raw, truncated)
    return dict(raw_text=raw, exact_candidate_only=exact,
                strict_candidate=raw.strip() if exact else None,
                contains_exactly_one_candidate=len(found) == 1,
                contains_multiple_candidates=len(found) > 1,
                mentioned_candidates=found,
                extractable_candidate=found[0] if len(found) == 1 else None,
                out_of_set_name=raw.strip() if not found and parsed['parse_valid'] and not parsed['rejection'] else None,
                truncated=truncated)


class CalibrationAdapter(LocalHFAdapter):
    def render(self, prompt):
        return self.tokenizer.apply_chat_template([dict(role='user', content=prompt)],
                    tokenize=False, add_generation_prompt=True, enable_thinking=False)

    def tokenize_choice(self, rendered, names):
        ids = self.tokenizer.encode(rendered, add_special_tokens=False)
        candidates = [self.tokenizer.encode(name, add_special_tokens=False) for name in names]
        if any(self.tokenizer.decode(seq, skip_special_tokens=False) != name for seq, name in zip(candidates, names)):
            raise ValueError('Candidate tokenization does not decode exactly')
        if any(self.tokenizer.encode(rendered + name, add_special_tokens=False) != ids + seq for name, seq in zip(names, candidates)):
            raise ValueError('Candidate scoring token boundary differs from the rendered chat template')
        trie = CandidateTrie(candidates, self.tokenizer.eos_token_id)
        trie.audit()
        return ids, candidates, trie

    def evaluate(self, prompt, names):
        tc = self.torch
        rendered = self.render(prompt)
        ids, sequences, trie = self.tokenize_choice(rendered, names)
        common = dict(prompt=prompt, rendered_prompt=rendered, prompt_sha256=sha(rendered),
                      candidate_order=names, isolation=dict(fresh_input=True, cross_call_history=False, use_cache=False),
                      seed=42, input_tokens=len(ids))
        inputs = dict(input_ids=tc.tensor([ids], device=self.model.device),
                      attention_mask=tc.ones((1, len(ids)), dtype=tc.long, device=self.model.device))
        def generate(constrained):
            tc.manual_seed(42)
            kwargs = dict(do_sample=False, temperature=None, top_k=None, top_p=None, use_cache=False,
                          max_new_tokens=max(map(len, sequences)) + 1 if constrained else 96,
                          eos_token_id=self.tokenizer.eos_token_id, pad_token_id=self.tokenizer.eos_token_id)
            if constrained:
                def allowed(batch_id, all_ids):
                    prefix = all_ids.tolist()
                    if prefix[:len(ids)] != ids:
                        raise ValueError('Guidance received a changed prompt')
                    return trie.allowed(prefix[len(ids):])
                kwargs['prefix_allowed_tokens_fn'] = allowed
            tc.cuda.synchronize()
            start = time.perf_counter()
            with tc.inference_mode():
                result = self.model.generate(**inputs, **kwargs)
            tc.cuda.synchronize()
            new = result[0, len(ids):].tolist()
            text = self.tokenizer.decode(new, skip_special_tokens=True)
            return dict(raw_text=text, raw_sha256=sha(text), output_token_ids=new,
                        output_tokens=len(new), latency_seconds=time.perf_counter() - start,
                        truncated=len(new) >= kwargs['max_new_tokens'] and new[-1] != self.tokenizer.eos_token_id)
        f = common | generate(False)
        f.update(free_fields(f['raw_text'], names, f['truncated']))
        c = common | generate(True)
        if c['raw_text'] not in names or c['truncated'] or c['output_token_ids'][-1] != self.tokenizer.eos_token_id:
            raise ValueError('Guided choice failed exact-string guarantee')
        if tuple(c['output_token_ids'][:-1]) not in trie.terminals:
            raise ValueError('Guided output used an unregistered token path')
        c.update(selected_candidate=c['raw_text'], exact_allowed_candidate=True,
                 all_candidates_reachable=True, candidate_token_ids=sequences)
        # Score the same candidate tokens used by the trie. Exclude EOS from
        # likelihood sums/means. Right-padding never contributes a scored token.
        length = len(ids) + max(map(len, sequences))
        batch = [ids + seq + [self.tokenizer.eos_token_id] * (length - len(ids) - len(seq)) for seq in sequences]
        masks = [[1] * (len(ids) + len(seq)) + [0] * (length - len(ids) - len(seq)) for seq in sequences]
        tc.cuda.synchronize()
        start = time.perf_counter()
        with tc.inference_mode():
            output = self.model(input_ids=tc.tensor(batch, device=self.model.device),
                                attention_mask=tc.tensor(masks, device=self.model.device), use_cache=False)
            # Select only next-candidate-token positions before float32 softmax.
            logits = output.logits[:, len(ids) - 1:len(ids) - 1 + max(map(len, sequences)), :].float()
            logprobs = logits.log_softmax(-1)
            scores = []
            for i, (name, seq) in enumerate(zip(names, sequences)):
                values = [float(logprobs[i, j, token].item()) for j, token in enumerate(seq)]
                total = sum(values)
                if not math.isfinite(total):
                    raise ValueError('Nonfinite teacher-forced likelihood')
                scores.append(dict(candidate=name, token_ids=seq, token_count=len(seq),
                                   token_logprobs=values, sum_logprob=total, mean_logprob_per_token=total / len(seq)))
        tc.cuda.synchronize()
        ranked = sorted(scores, key=lambda s: (-s['mean_logprob_per_token'], names.index(s['candidate'])))
        l = common | dict(scores=scores, top_candidate_by_mean_logprob=ranked[0]['candidate'],
                          runner_up=ranked[1]['candidate'],
                          margin_mean_logprob=ranked[0]['mean_logprob_per_token'] - ranked[1]['mean_logprob_per_token'],
                          scoring='Teacher forcing; canonical prompt+candidate tokenization; candidate tokens only, EOS excluded; right-padding masked',
                          latency_seconds=time.perf_counter() - start)
        return f, c, l
