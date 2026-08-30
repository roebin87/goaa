# Rules · Rule Effect Gate (Generic · V1.0 EN)

> **Written ≠ effective.** A rule takes effect only after passing validation — the effect gate is the mechanism that makes "writing" meaningful.

## The gate (three checks)
> **Semantics**: Programming (enforceable rules · machine-checkable execution layer)

1. **Structure check**: the rule file is in place, named per naming rules, located in the right layer;
2. **Semantic sync check**: consistent with the constitution/design-principles wording (no drift);
3. **Mechanism check**: the rule has a corresponding mechanism that verifies its operation (rules↔mechanisms separation);

All three pass → the rule is effective. Any fail → the rule does not take effect (remains draft/pending).

## Lifecycle

```
draft → pending validation → effective → (outdated) → deprecated record
```

- Effective rules are the single source of truth;
- Deprecated rules are preserved as records, never deleted;
- Modifying an effective rule requires the owner's explicit instruction + trace.

## Validator

Run `python3 tools/validator.py` to verify structure, core files, YAML schema, and rule-reference integrity; `--memory` mode checks memory layers and append-only hashes (in a deployed workspace). The actual capability list is declared in `rules.yaml` → `validator_对应` (declaration = implementation, calibrated 2026-08-26).

---

*GOAA rules · Generic V1.0 EN · Single version · 2026-08-26*
