# Experimental inheritance workflow

Starting with v3.6.3.1, every new experiment must place a **Validated Inheritance** section before its new manipulation. Inventory the established components relevant to the design and classify each as `FROZEN_REUSE`, `INTENTIONALLY_RETESTED`, or `NOT_RELEVANT`.

For every modified component, record why it changes, which previous conclusion no longer applies, and the new validation required. A previous result does not license a silent prompt, parser, model, or sampling change.

Preparation must call `experiments.inheritance.validate` on the effective specification and machine-readable inheritance rows. Freeze that table, exact inherited-source hashes, byte-comparison audits, case selection, parsers, thresholds, and conditional call schedules before inference. Compare reused prompt templates byte for byte after substituting identifiers. Abort on an unexplained difference. New experiments should reuse this validator and supply their own explicit component inventory and comparisons; it does not automatically discover scientific dependencies.

Store the supplied source specification and execution resolutions together. Never overwrite historical frozen sources or results. Keep diagnostic results separate from formal gates, report intentional unrun stages explicitly, and do not replace cases or retry failures based on accuracy. Freeze dynamic prompt builders and placeholders before inference; save the actual prompt hashes and upstream provenance when generated values become available.
