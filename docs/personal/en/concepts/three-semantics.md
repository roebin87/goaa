# Core Concept · Three Semantics (human / machine / programming)
> **Semantics**: Human (intent/concept layer · reading)

> **Series**: docs/concepts core-concept series ｜ **Version**: Single version 1.0

---
> **Authority pointer**: this file is the concept-explanation layer (human semantics · lowers the understanding cost); **authority resides in the constitutional layer** (`constitution/basic_law.md` + `constitution/design-principles.md`) — where an explanation conflicts with authority, the authority prevails.

## In one line

The same rule is written three times, in three semantics, each serving its own consumer: **human semantics** (humans can read why), **machine semantics** (AI can read how to execute), **programming semantics** (a machine-verifiable enforcement layer) — anchoring AI's execution drift.

## Why this design

- Human-machine semantics have a structural gap (thought always exceeds physical-layer expression);
- Writing rules in natural language only = AI executes by guessing (drift); writing rules in code only = humans cannot understand (un-reviewable);
- Three semantics = making rules simultaneously "human-reviewable, machine-executable, machine-enforceable."

## Division of labor among the three semantics

| Semantics | Consumer | Form | Responsibility |
|------|--------|------|------|
| Human semantics | human | natural language (MD) | intent / why (Why · reviewable) |
| Machine semantics | AI | structured instructions | execution (How · loadable) |
| Programming semantics | validator / CI | YAML / Schema / code | enforcement (verifiable · written ≠ effective) |

## Concrete forms

- The two constitutional-layer files = human semantics (Design Principles = Why+How · Basic Law = bottom lines);
- `rules/rules.yaml` = programming-semantics instance (rules data-ified, verifiable by the validator);
- The ambiguity-governance mechanism = the gap-handling flow between the three semantics.

## Related

- Concepts: Mother Axiom / falsifier / priority rules
- Mechanisms: ambiguity governance / rule effect gate (validation.md)
