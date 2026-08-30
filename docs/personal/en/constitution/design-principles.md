# GOSAA Design Principles (Generic · V1.0 EN)
> **Semantics**: Machine (mechanism/translation layer · How)

> **Role**: this file answers two questions — **why** it is designed this way (rationale · Why) and **how** the architecture is built (method · How). Design Philosophy and Design Principles are merged here: both the rationale and the method.
> **Authoritative counterpart**: aligned with the GOAA architecture design principles academic paper (the master draft) — axiom system, file foundation, five-layer architecture, rule governance, normalized adjudication, and generation evolution all follow the paper's wording.
> **Generic translation (single version 1.0)**: open-sourced, sanitized.

---

## I. Governance-oriented vs execution-oriented (why governance)

- **Two orientations**: mainstream agent frameworks solve "how to make AI do more work" (execution-oriented — enhancing task scheduling and execution efficiency); GOAA solves "how to make AI reliably governable" (governance-oriented — long-term controllability, aligned rights and responsibilities, traceability).
- **Governance-oriented** = "long-term controllability" as the first principle: define the governance boundary first, then carry execution capability on top of it — **governance is the foundation, execution is the add-on**.
- **Why governance is necessary**: the disorder of an agent system is not a fixable bug but a structural feature of long-term operation — rules decay with interaction, behavior drifts with running, the system bloats with evolution (technical entropy); rules are written but not agreed upon, decisions execute but are not aligned (cognitive entropy, i.e., Cognitive Lag). Governance counters both kinds of entropy.
- **Four design goals**:
  1. **Sovereignty never lost**: 100% human decision rights, physically enforced
  2. **Cost bounded**: governance cost has a ceiling, does not spiral with system growth
  3. **No stock backlog**: startup carries only distillation + core files; stock entropy handled by version retirement
  4. **Memory continuity**: one resident governed body (continuity + quality baseline)

## II. The four axioms (the four-dimensional governance boundary)

| # | Axiom | In one sentence |
|---|-------|-----------------|
| 1 | **Axiom of decision rights** (who governs) | In single-subject human-machine collaboration, the human retains final decision rights — ownership, decision rights, and responsibility are one; the machine executes only within explicit, unambiguous authorization and never decides autonomously |
| 2 | **Axiom of file ontology** (physical carrier) | Physical files are the authoritative carrier of memory and rules — files exist, the system exists; files lost, the system resets to zero |
| 3 | **Axiom of inherent ambiguity** (the fundamental difficulty) | The human-machine semantic gap is inherent and cannot be fully eliminated — governance aims to reduce and surface ambiguity, not to pursue absolute semantic consistency |
| 4 | **Axiom of entropy increase** (why governance must persist) | Any continuously running human-machine system, without active governance, inevitably tends toward disorder — entropy cannot be eliminated; governance keeps its growth within a bearable range |

> The axiom wording follows the GOAA academic papers (Cognitive Lag / master draft). Terms such as entropy, negative entropy, and entropy sink are used as system-science analogies — describing the change and governance of system disorder, not strict thermodynamic quantities.

## III. File-ontology foundation & workspace anchoring (why files)

**Why files are irreplaceable**: governance needs three physical properties — **sovereignty needs physical enforcement** (permissions are a physical property of the file system, not a software promise), **evidence needs physical persistence** (audit trails persist independently of process termination), **entropy needs physical export** (file persistence externalizes runtime state). The file system's determinism comes from physical properties, not runtime quality — files exist, governance exists; startup is loading, not rebuilding.

- **Permissions are sovereignty**: who may write rules, who may change memory, is enforced by the file system, not by model self-discipline
- **History leaves traces**: audit trails provide traceable evidence for governance rulings
- **Entropy sink**: file persistence provides the physical export channel for entropy — each landing is one runtime-entropy export
- **Workspace anchoring** (first implementation principle of the file-ontology axiom): all long-term rules, memory, and collaboration assets are stored classified by project folder; each startup anchors to the target workspace folder, and all rule loading, memory reading, and consensus writing are strictly confined within that directory boundary

**Layered loading (light startup)**:

```
Distillation = primary load (light, focused, does not pollute context)
Full backup = complete process record (quality fallback)
Index = full navigation entry
Sandbox = physical cold storage
```

Key principle: distillation + full = layered, not alternative; startup carries distillation + design principles; stock entropy handled by version retirement (not cleaned, skipped).

## IV. Five-layer architecture overview (how it is organized)

```
Axiom layer (four axioms · stable kernel)
  → Physical foundation layer (file system · governance anchor)
  → Core mechanism layer (four-layer memory / rule governance / normalized adjudication)
  → Execution add-on layer (models/frameworks · replaceable)
  → Scenario application layer (individual → micro team)
```

- **Governance as foundation, execution as add-on**: contrary to "execution first, governance later", GOAA builds the governance substrate first, with execution capability carried on top as a replaceable add-on — governance mechanisms are not bound to any specific model or framework
- **Bottom-up dependency**: upper layers depend on the lower layers' determinism; lower layers do not depend on upper-layer implementation details — as long as the file system exists, the governance loop runs
- **Rule tiers**: constitutional → mechanism → methodology → instance — generic rules accumulate for reuse, one-off tasks are used and discarded, one-off tasks never pollute generic rules

## V. Three semantic layers & the rule effect gate (how rules take effect)

| Semantic layer | Duty | Ambiguity removed |
|----------------|------|-------------------|
| Human semantics | Intent expression (human reads/writes) | Intent ambiguity |
| Machine semantics | Intermediate execution description (machine reads/writes) | Translation ambiguity |
| Programming semantics | High-enforcement layer (YAML/JSON/scripts · verifiable) | Execution ambiguity |

- **Rules ↔ mechanisms separation**: rules = what to write (YAML + Schema + CI · data-driven, checkable); mechanisms = how to verify (process-driven, executable) — every rule must have a corresponding mechanism verifying its operation (writing without verification = idle spinning)
- **Written ≠ effective**: a rule written down is not yet effective — it must pass four checks: platform hard constraints (no conflict with upper mechanisms) · system self-consistency (no conflict with the constitution) · practical executability (feasible within resources and boundaries) · enforcement support (has hooks to land, not dependent on self-discipline); rules that fail the gate have no binding force (see `rules/validation.md`)
- **Three-semantic sync validation**: all three layers must stay consistent — the validator performs normalized comparison (expression difference ≠ drift)
- **Reuse mechanism**: methodologies/rules "produced" are inventory; only when loaded and invoked again are they assets — production side · asset registration → consumption side · reuse retrieval → value side · reuse-rate monitoring; three-in-one verification (internal verification + external calibration + anchored comparison); three exits: reusable → asset library / needs revision → problem gate / abandoned → version retirement

## VI. Normalized adjudication & QA duality (how humans participate)

- **QA duality**: the human-machine question-answer loop is the basic unit of order production — the human's question injects cognition (the question), AI's response surfaces material and gaps (the answer), the human's ruling closes the loop; every effective round of Q&A produces order. Its design draws on traditional yin-yang philosophy as inspiration, originating from the question-answer duality of the human-machine production model
- **Ambiguity surfacing**: AI has no ruling qualification but has surfacing qualification — as the "mirror" of Cognitive Lag, it surfaces rule conflicts, factual contradictions, and pending ruling backlogs into processable problems (surfacing turns ambiguity from "silent accumulation" into "explicit ruling")
- **Normalized adjudication**: human ruling is not an exception fallback but a **fixed step** in the rule and consensus layers — every rule taking effect, every conclusion settling, every consensus solidifying requires human approval; the ruling objects are limited to rule effect / consensus solidification / version iteration (low-frequency, high-value), not single action executions
- **The loop closes on human judgment**: ask → answer → judge → solidify or ask again — Q&A without "judge" is idle spinning
- **Separation of sovereignty and execution**: mechanism design, authorization, and ruling belong to the human (I decide); execution can be mechanized under human-built mechanisms (I execute) — authorization is the legitimate bridge between sovereignty and execution

## VII. Generation evolution (GOAA's overall evolution generations)

| Generation | Abbreviation | Full English name | Essence |
|------------|--------------|-------------------|---------|
| 1.0 | SCA | Soul Contract Architecture | static × static · ownership · frozen |
| 2.0 | GOSAA | Governance-Oriented Solutions Architecture | dynamic × dynamic · machine-side engineering · **current main version** |
| 3.0 | CSA | Constellation of Sovereign Agents | peer multi-subject · collective peak |
| 4.0 | MOA | Meta-Order Architecture | ordered iteration of governance rules · nearing the origin |

- **Overall architecture name**: GOAA = Governance-Oriented **Agent** Architecture; GOSAA = the 2.0 generation codename (Governance-Oriented **Solutions** Architecture) — the two full names differ; formal usage follows the table
- **Generations = shifting main contradiction**: 1.0 ownership → 2.0 machine-side engineering → 3.0 inter-subject governance → 4.0 nearing the origin
- **Generations are compatible forms, not upgrades/replacements**: 1.0 can participate in 3.0 inter-subject fusion

## VIII. Self-bootstrap & verification (how to confirm it is built right)

- **Design files** (constitution + design principles + distillation + index) = the only non-regenerable asset; posts / tools / dashboards = regenerable products
- **Files exist, the system exists**: any computer + any local-file application = system rebuild; copyability is proven (an instance is born = the design files carry enough expression, no designer cognition present)
- **Verification**:
  - Criterion ①: shell + loading runs (startup self-check passes)
  - Criterion ②: wrap-up → new conversation → distillation continuity succeeds (cross-conversation memory continuity)
  - Criterion ③: validator all green = consistency passed
- **Applicability boundary**: this architecture targets **individual and micro-team use cases** — the degree of engineering sophistication is constrained by the scenario, by design (scenarios pursuing full automation / zero constraints / large-scale multi-agent are not applicable; see `docs/applicability.md`)

---

*GOSAA Design Principles · Generic translation V1.0 EN · Single version · 2026-08-19 (Design Philosophy merged 2026-08-26 · aligned with academic paper wording)*
