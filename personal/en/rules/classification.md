# Rules · Five-Level Classification (Generic · V1.0 EN)

> Classification determines how strictly a rule must be verified and who approves it. Level 1 is the most sensitive; Level 5 the most ordinary.

## The five levels

| Level | Scope | Approval | Verification |
|-------|-------|----------|--------------|
| L1 Identity-level | System identity / capability boundaries / superior-subordinate | Owner review + three checks | Highest |
| L2 System-level | System files / platform files | Owner instruction + trace | High |
| L3 Rule-level | Rules & mechanisms themselves | Owner confirmation + gate | Gate-verified |
| L4 Content-level | Ordinary documents / content | Machine may propose, owner confirms | Soft check |
| L5 Transient | Temporary notes / drafts | Machine-managed | Light |

## Principles

- Higher levels are never bypassed by lower ones;
- **Rule effect gate** (see `rules/validation.md`): a written rule is not effective until it passes validation;
- Expired rules move to `deprecated_rules` as records — not deleted, not rewritten (full-chain trace).

---

*GOAA rules · Generic V1.0 EN · Single version · 2026-08-26*
