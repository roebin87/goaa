# Pre-Registered Disclosure List
> **Semantics**: Human (intent/concept layer · reading)

> **Position**: GOAA's **known limits and unverified claims** — proactively disclosed before release (pre-registered), no post-hoc excuses. Five-dimension honest disclosure, forming the complete two-piece social-validation evidence chain with the [falsification log](falsification-log.md).
>
> This file is the **Core full version** (Lite/Personal only provide an entry).

---

## ① Theoretical Premise Assumptions

GOAA's theory rests on a set of **first-order assumptions** (detailed in paper §3.2; not absolute axioms in the mathematical/logical sense):

| Assumption | Content | Impact if False |
|---|---|---|
| H1 Decision authority | AI is not a legal subject; responsibility rests with the natural person | If law/ethics develop AI responsibility subjects, Axiom 1 needs revision |
| H2 File determinism | File-system determinism (persistence/permissions/audit) exceeds model memory | If future storage layers become non-deterministic (distributed/soft-state), the physical-gate advantage weakens |
| H3 Human adjudication availability | Natural-person participation in rule-layer adjudication is feasible | If a single subject cannot bear the adjudication load, multi-subject governance is needed (=3.0 direction) |
| H4 Entropy axiom | Disorder is a structural feature of long-running operation (S(t)=S₀·e^(αt)) | The rate constant α depends on empirical calibration; may differ across scenarios |

## ② Applicability Boundary

GOAA **applies to**:

- Single-sovereignty scenarios (one natural person / one team leading long-running agent collaboration);
- Text/file-centric production work (books / reports / code / research / operations);
- Long-running operation requiring rule constraints, memory persistence, and decision traceability.

GOAA **does not apply to** (or needs evolution):

- Multi-subject distributed governance (participatory / group decision-making → 3.0 direction, delimited in the paper);
- Low-latency real-time decisions (file I/O has physical overhead; not designed for action-layer high-frequency approvals);
- Non-file carriers (pure runtime / in-model governance is not in current scope).

## ③ Known Limitations

| Limitation | Description | Mitigation |
|---|---|---|
| File-scale ceiling | Retrieval cost rises as memory grows (overweight lookup = self-defeating) | Memory slimming (distill/archive/clean) · optional vector index |
| Human-adjudication dependence | Governance intensity depends on human participation frequency and quality | Adjustable governance intensity (five-level classification) · low-frequency high-value design |
| Single-writer constraint | Collaboration limited to a single writer (workspace anchoring) | Multi-writer scenarios reuse version control/CRDT (paper §4 addresses) |
| Chinese-first | Corpus and examples primarily Chinese (Lite zh-only) | Personal/Core provide en mirrors (from v0.2.0) |
| Setup threshold | Initialization depends on Python and file-operation basics | init script + onboarding docs + fallback phrase |

## ④ Unverified Claims

The following claims have **not yet been independently validated by third parties**; falsification is welcome (register in the [falsification log](falsification-log.md)):

- The causal strength between governance intensity and output quality (case evidence is the author's production history, not controlled comparison);
- The magnitude of file-based memory's suppression of long-run decay (paper evidence is the author's system, sample n=1);
- Quantified improvement of system maintenance efficiency from dual-chain navigation (currently qualitative argumentation);
- The universality of "governance substrate + capability plugin = optimal agent architecture direction" (integration examples are minimal integrations, not benchmark evaluations);
- **Whether the two-mechanism loop (generate/check/adjudicate) genuinely outperforms "AI autonomy + post-hoc audit"** (currently architectural argumentation, no controlled-experiment data);
- **The zero-coordination-cost claim of "not multi-agent, one system across workspaces"** (currently design argumentation, not stress-validated at scale);
- **Whether the 100% human decision "sovereignty/execution separation" indeed does not reduce output efficiency** (benefits of execution delegation are qualitative, not quantified);
- **Cross-scenario universality of the cost advantage** (cache-hit 98.6% / zero orchestration overhead measured on the author's system, n=1; advantage magnitude under different usage patterns (short tasks / low-reuse scenarios) awaits third-party reproduction).

## ⑤ Technical Dependencies

| Dependency | Purpose | Alternative |
|---|---|---|
| Python 3.8+ | Validator / init scripts / plugins | None (current toolchain) |
| File system (local) | Governance substrate (rules/memory/adjudication persistence) | None (architectural core, non-replaceable) |
| LLM API | Agent execution layer | Any compatible API (GOAA governance layer is vendor-agnostic) |
| LangChain/CrewAI/AutoGen (optional) | Integration examples | Example-only dependencies; the governance layer is zero-dependency |
| Local embedding endpoint (optional) | Vector memory index | Honest fallback to keyword search when no endpoint (no silent cloud use) |

---

## Disclosure Commitment

- The above limits and assumptions are **public before release**, not rewritten as stars/reputation change (principle freezing);
- Newly discovered limits are **continuously appended** to this list (augmentative, old entries never deleted);
- Every unverified claim is an **open invitation** to the falsification log.

---

*GOAA · Pre-Registered Disclosure List · All-Outcomes Open Source Edition (Core) · 2026-08-28*
