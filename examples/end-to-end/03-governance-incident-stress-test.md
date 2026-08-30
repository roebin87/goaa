# Case 03 · Governance Incident Stress Test (8.21 Rule Conflict Event)
> **Semantics**: Machine (how-to example · operational demonstration)

> Based on the designer's real practice, recording a governance incident and its complete resolution. An incident is not a failure — it's a stress test of the governance system.

## 1. Background

**Time**: August 21, 2026 (late GOAA 1.0, before 2.0 design started)

**System state**: GOAA 1.0 running ~30 days, ~20 rules, memory system established, multi-role collaboration running.

**Incident trigger**: During book production, executor AI encountered two conflicting rules for "chapter title format":
- Rule A (R012, added 8.10): "Chapter titles use level-1 heading (#), centered"
- Rule B (R028, added 8.18): "Chapter titles use level-2 heading (##), left-aligned"

AI chose Rule B (newer = override) without reporting the conflict to the owner.

## 2. Incident Development

### Phase 1: Silent Drift (3 days)
- AI followed Rule B for 3 days, generated 5 chapters with wrong format
- Owner noticed but assumed misremembering the rule
- Incident undetected, execution silently drifted

### Phase 2: Ambiguity Revelation (Day 4)
- Owner clearly remembered "level-1 centered" while reviewing chapter 6
- Owner questioned AI, AI searched rules and found the conflict
- AI submitted conflict to owner for adjudication (correct behavior)

### Phase 3: Localization & Analysis
AI submitted report: conflicting rules identified, impact assessed (5 chapters affected), root cause analyzed (no conflict detection in effect gate), 4 options proposed.

### Phase 4: Human Adjudication
Owner decided:
1. Keep Rule A (original design intent)
2. Retire Rule B (mistakenly added)
3. Fix 5 generated chapters
4. Add "rule conflict detection" as 5th check in effect gate

### Phase 5: Consolidation & Retirement
- Rule B archived to rule-archive/ with reason and adjudicator
- Rule A confirmed with annotation
- New rule "conflict detection" added to effect gate
- Full process recorded in analects layer
- Distill updated with "conflicts must be revealed, AI must not self-adjudicate"

## 3. Root Cause Analysis

**Direct cause**: No conflict detection when Rule B was added.

**Deep causes**:
1. Rule obesity — non-additive principle not enforced early
2. Dual-write legacy — rules written in two places, causing inconsistency
3. AI self-adjudication — defaulted to "new overrides old" without reporting (violates mother axiom)
4. No conflict detection in effect gate (only 4 checks: existence/semantic/reference/Schema)

**Systemic cause**: GOAA 1.0 governance not yet complete, adjudication loop not fully institutionalized.

## 4. Institutional Patches (6 items)

| Patch | Location |
|-------|----------|
| Rule conflict detection (5th effect gate check) | rules/validation.md |
| Conflict must be revealed, AI must not self-adjudicate | rules/rules.yaml |
| Non-additive principle enforced | rules/classification.md |
| Rule retirement mechanism | mechanisms/ |
| Single authority source (no dual-write) | rules/rules.yaml |
| Periodic rule audit (automated) | tools/rule-conflict-check.py |

## 5. Impact on GOAA 2.0

The 8.21 incident was a key turning point from 1.0 to 2.0, directly driving:
1. Adjudication loop institutionalized (5-step standard mechanism)
2. Effect gate expanded to 5 checks
3. Non-additive principle written to constitution
4. Full rule lifecycle management
5. Toolchain completion (rule-conflict-check.py)
6. "Incidents are assets" as core concept

## 6. Review Points

**What worked**: No masking after revelation; complete adjudication process; incident converted to 6 patches; complete records; drove architecture evolution.

**Pitfalls**: Silent drift lasted 3 days; AI self-adjudicated at first; rule obesity; dual-write legacy; no conflict detection.

**If restarting**: Establish conflict detection on day 1; enforce non-additive on day 1; single authority source on day 1; explicit "conflicts must be revealed" rule; periodic audit mechanism.

## 7. Value of the Incident

Superficially a "failure" (5 chapters needed fixing), but from governance perspective a **successful stress test**:
1. Verified adjudication loop works end-to-end
2. Verified "human holds 100% decision rights" is feasible
3. Verified "incidents are assets" — one incident to 6 institutional improvements
4. Verified GOAA's evolution capability

**Core conclusion**: In GOAA, incidents aren't failures — they're "vaccines" for the governance system. Small incident stress tests discover and patch loopholes, preventing larger incidents. This is the core value of governance-oriented architecture: not that errors never happen, but that after errors they can be discovered, adjudicated, consolidated, and evolved.

---

*GOAA · End-to-End Case 03 · Based on real practice · 2026-08-28*
*Incident: 2026-08-21 · Resolution: 2026-08-22 · Patches landed: 2026-08-25*
