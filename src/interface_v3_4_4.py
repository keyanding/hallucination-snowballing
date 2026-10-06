"""v3.4.4 strict natural parser and same-template F / optional C / S adapter."""
import re
from .calibration_choice import CalibrationAdapter, free_fields
from .experiment_v3_3 import sha
import math
import time


def parse_natural(raw, names, truncated=False, aliases=None):
    aliases = aliases or {}
    assert set(aliases.values()) <= set(names)
    assert all(k not in names or k == v for k, v in aliases.items())
    text = raw.strip()
    allowed = dict(zip(names, names)) | aliases
    found = sorted({identity for spelling, identity in allowed.items()
                    if re.search(r'(?<!\w)' + re.escape(spelling) + r'(?!\w)', text)})
    if truncated:
        category = 'TRUNCATED'
    elif text in allowed:
        category = 'IN_SET_VALID'
    elif len(found) > 1:
        category = 'AMBIGUOUS'
    elif not found and re.fullmatch(r"[^\W\d_]+(?:[ .'-][^\W\d_]+){1,5}", text, re.UNICODE) and not any(
            x in text.lower().split() for x in ('unknown', 'cannot', 'answer', 'sorry', 'wait', 'the', 'is', 'none')):
        category = 'OUT_OF_SET'
    else:
        category = 'NONCOMPLIANT'
    return dict(category=category, strict_valid=category == 'IN_SET_VALID',
                identity=allowed[text] if category == 'IN_SET_VALID' else None,
                mentioned_candidates=found, supplementary_identity=found[0] if len(found) == 1 else None)


class InterfaceAdapter(CalibrationAdapter):
    """Same greedy settings and teacher forcing as v3.4.3; N/R never invoke a trie."""
    def evaluate(self, prompt, names, listed=True, free_cap=96):
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
                          max_new_tokens=max(map(len, sequences)) + 1 if constrained else free_cap,
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
        c = None
        if listed:
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
        f.update(parse_natural(f["raw_text"], names, f["truncated"]))
        f.update(max_new_tokens=free_cap, stop_reason="TOKEN_CAP" if f["truncated"] else "EOS")
        for rank, score in enumerate(ranked, 1):
            score["rank"] = rank
        return f, c, l
