# Multi-Role Collaboration Mechanism (multi-role)
> **Semantics**: Machine (mechanism/translation layer · How)

> **Purpose**: A multi-role division mechanism for personal productivity scenarios — one AI plays different roles under different rule constraints, completing complex production (books/reports/code/research and other deliverables that require "division + review") through **file flow**.
> **Principle**: Multi-role is execution-level division; **adjudication always belongs to the human** (the 100% human decision-rights mother axiom is unchanged).
> **Provenance**: Real practice by the designer (450,000-word book production · 30-day collaboration across four roles: controller/editor/executor/reviewer) — see [examples/end-to-end/01-book-production.md](../../../../examples/end-to-end/01-book-production.md).

---

## 1. Why multi-role is needed

A single-role long run has three unavoidable problems:

1. **Self-review blind spot** — an AI reviewing its own work tends toward self-confirmation ("pseudo-external review" is unreliable; human adjudication is mandatory);
2. **Style drift** — over long production cycles (30+ days), terminology, voice, and formatting gradually drift;
3. **No quality gate** — without an independent check stage, errors reach the final deliverable directly.

Multi-role separates "production" from "checking" so quality problems are caught between stages — **quality comes from process, not from self-discipline**.

> **Key insight**: Multi-role is not "multiple AI instances" — it is "**one AI playing different roles under different rule constraints**". No multi-instance orchestration, no message bus — only files and rules.

## 2. Role definitions (four roles)

| Role | Responsibility | Permission boundary |
|------|----------------|---------------------|
| **Controller** | Overall coordination: set goals, decompose tasks, assign work, approve final drafts, adjudicate inter-role disputes | Highest execution authority · does not replace human adjudication · major disputes must go to the human |
| **Editor** | Content quality: review and revise executor output, unify style and terminology, propose changes | Authority to modify executor output · does not redefine goals |
| **Executor** | Concrete production: draft, research, persist to disk, revise per feedback | Produces only · no self-review or self-adjudication · revisions follow editor/controller feedback |
| **Reviewer** | Final review: cross-check, produce issue lists, verify consistency | **Inspects only, does not adjudicate** · submits issues to controller/human · does not modify directly |

> Roles can be added or removed (e.g. a "data clerk"), but the **four-role loop (produce → check → revise → finalize) is not optional** — drop any stage and multi-role degenerates back to single-role.

## 3. Files as the interface

Roles communicate **not through dialogue but through file flow in agreed directories** — where files exist, the process exists; next launch loads and resumes.

### Directory convention (example, adjustable per project)

```
_Work/               # Work area (intermediate files flowing between roles)
├── controller/      # Outline, task assignment, final drafts
├── executor/        # Drafts, source material
├── editor/          # Revised drafts, feedback
└── reviewer/        # Issue lists, final review conclusions
_Output/             # Final deliverables (approved)
```

### Instruction status protocol (_Directives/ interface)

Roles respond by appending a status line to the instruction file: format `[date time][status tag][role]`

| Tag | Meaning |
|-----|---------|
| `[NEW]` | Controller issues a new task |
| `[ACK_REC]` | Received and understood the instruction |
| `[ACK_DONE]` | Instruction executed; deliverable persisted |
| `[FEED_NEED]` | Requesting additional information |
| `[INFO_ERR]` | Obvious error found; correction requested |
| `[INFO_SUG]` | Optimization suggestion for this instruction |

## 4. Collaboration flow (one standard round)

```
Controller sets outline → assigns to executor → executor drafts (_Work/executor/)
   → editor revises (_Work/editor/ · feedback written back)
   → executor revises per feedback → controller re-checks → reviewer final review (_Work/reviewer/ · issue list)
   → controller approves → persists to _Output/ → session closeout (five memory hooks)
```

**Key points**:
- Every stage's output **must be persisted** — not persisted equals not done (otherwise the next launch forgets it);
- The reviewer's "issue list" contains **facts and candidates, not adjudication** — adjudication belongs to the controller and the human;
- After a round completes, experience (terminology, review findings, rule gaps) enters the distillation layer and is auto-loaded next round.

## 5. Role discipline (positive/negative list)

**Must do**:
- Inter-role handoffs must go through files (traceable);
- On detecting boundary violations/conflicts, surface first, then act — no self-inference;
- Update the distillation layer at each round's closeout (progress, consensus, todos).

**Forbidden**:
- Executor self-review and self-adjudication (self-review blind spot);
- Reviewer directly modifying deliverables (inspect only, don't adjudicate);
- Verbal handoffs between roles (no file means no evidence chain);
- Roles exercising human adjudication (the 100% human decision-rights axiom is non-transferable).

## 6. Integration with core mechanisms

| Mechanism | Integration |
|-----------|-------------|
| Startup sequence | Multi-role rules load with `rules/`; role identity files can live in `templates/identity/` |
| Five closeout hooks | All role outputs settle together per session (dialogue record/distill/log/analects/backup) |
| Ambiguity governance | Inter-role conflict = ambiguity, handled via "surface → locate → analyze → human adjudicate → solidify" |
| Incident handling | Role boundary/conflict incidents become institutional patches via "incidents as assets" (see end-to-end case 3) |
| Reuse mechanism | Role-settled terminology/review checklists/process templates register into the reuse library for cross-project use |

---

## 7. Multi-role verification checklist (pre-enablement self-check)

- [ ] Four roles' responsibilities and permission boundaries written into this workspace's rules
- [ ] File-flow directories established (_Work/ four subdirectories + _Output/)
- [ ] Instruction status protocol defined (six tags)
- [ ] Role discipline positive/negative list confirmed
- [ ] One end-to-end round completed (controller → executor → editor → reviewer → approve) → deliverable persisted
- [ ] Five closeout hooks executed → this round's experience recorded in the distillation layer

---

*GOAA · Multi-Role Collaboration Mechanism · Genericized translation · 2026-08-29 · v0.1.0*
