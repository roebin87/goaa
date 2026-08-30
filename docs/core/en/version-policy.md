# Version Policy
> **Semantics**: Human (intent/concept layer · reading)

> **Status**: **Effective** (2026-08-29 author final decision · Scheme 3: full open + carefully upheld core principles) — code fully open and evolving with social validation; three core principles carefully upheld, change requires full justification.

---

## 1. Version Strategy: Full Open + Carefully Upholding Core Principles

### 1.1 Code Fully Open (Evolving with Social Validation)

- GOAA code / docs / mechanisms are **fully open-sourced**, evolving continuously with community feedback and social validation;
- Version evolution is driven by the **falsification log**: objection → analysis → human adjudication → consolidation → version update (every closure may power a new version);
- Semantic versioning (SemVer): v0.1.0 (first release) → incrementing per feature evolution and compatibility commitments.

### 1.2 Core Principles (Carefully Upheld)

The three principles below are the foundation of GOAA — we **carefully uphold** them, not lightly changed by reputation or short-term pressure. If change pressure ever arises, it follows the "change proposal → author final decision" path, with full justification before any decision:

| Core Principle | Content | How Upheld |
|---|---|---|
| **Data sovereignty** | Memory and data stay local to the user; no default upload | Change requires public justification and sound reasoning |
| **100% human decision** | Key decision authority rests with the natural person; machines do not self-assume | Change requires public justification and sound reasoning |
| **Governance first** | Governance stands as an independent layer, not attached to execution logic | Change requires public justification and sound reasoning |

> We believe these three principles withstand scrutiny, and we welcome fact-based challenges — if the argument is sound, we are willing to reconsider.

---

## 2. Three-Edition Maintenance Strategy (Proper-Subset Synchronized Evolution)

| Edition | Position | Evolution Rule |
|---|---|---|
| **Lite** | Enlightenment (minimal viable) | Follows Core; only feature layers are trimmed |
| **Personal** | Personal productivity | Follows Core; adds personal-scenario features |
| **Core** | All-outcomes open source (this edition) | Evolution source; proper-subset relation unchanged (Lite ⊂ Personal ⊂ Core) |

- **Upgrade = enabling feature layers**: users move Lite → Personal → Core with no migration cost (copy + enable);
- **Consistency check**: every version update runs the proper-subset monotonicity check to prevent three-edition drift.

---

## 3. Public Commitments

1. **Falsification first**: any claim is falsifiable ([falsification log](falsification-log.md)); version evolution is based on falsification closures;
2. **Continuous disclosure**: the [pre-registered disclosure list](known-limits.md) updates augmentatively; new limits are not hidden;
3. **Author hands-on testing**: the author hands-on tests before every release (no release without passing);
4. **Carefully upheld**: data sovereignty / 100% human decision / governance first — change requires full justification.

---

## 4. Pending Final Decision

- ☐ **Scheme 3 (Full open + principle freezing)** — recommended (this declaration is written accordingly)
- ☐ Other schemes (e.g., full open without freezing / partial open / commercial-license hybrid)

> After the final decision, this declaration changes from "draft" to "effective", with the repository root README updated in sync.

---

*GOAA · Version Policy (Draft) · All-Outcomes Open Source Edition (Core) · 2026-08-28*
