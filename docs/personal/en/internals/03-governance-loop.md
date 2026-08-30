# 03 · GOAA Normalized Adjudication Loop Working Principles
> **Semantics**: Machine (mechanism/translation layer · How)

> This document publishes the design principles and workflows of GOAA's normalized adjudication loop.

## 1. Why Normalized Adjudication

In mainstream human-machine collaboration, humans are "exception fallbacks" — only intervene when AI goes wrong. GOAA believes this is wrong: **human adjudication should be a fixed环节 of the governance loop, not a fire brigade.**

**Core insight**: AI execution drift (semantic ambiguity), rule decay/conflict, and cognitive lag (human cognition can't keep up with system evolution) cannot be self-repaired by AI. They must be governed through normalized human adjudication.

## 2. Complete Adjudication Loop Flow

```
① Ambiguity Revelation → ② Localization → ③ Human Adjudication → ④ Consolidation → ⑤ Retirement
     ↑                                                                      │
     └──────────────────────────────────────────────────────────────────────┘
                              (continuous loop)
```

### 2.1 ① Ambiguity Revelation
Make hidden ambiguity, conflict, and lag visible rather than masked.
**Mechanisms**: Instruction dual-check (human intent vs machine execution), rule conflict detection, memory decay detection, cognitive lag revelation.
**Principle**: Revelation precedes resolution — make the problem seen first, then decide how to handle.

### 2.2 ② Localization
Locate the root and layer of ambiguity/conflict/lag.
**Routing**: Vocabulary ambiguity → human semantic layer; syntactic ambiguity → machine semantic layer; pragmatic ambiguity → context layer; execution ambiguity → mechanism layer; rule conflict → rules layer; cognitive lag → governance layer.

### 2.3 ③ Human Adjudication
Final decision made by human (owner); AI only provides analysis and suggestions.
**Principles**: Human holds 100% final decision rights (mother axiom); adjudication targets rules layer (rule effect/consensus consolidation/version iteration), not action layer; adjudication frequency bound to rule change frequency (far below action execution frequency, magnitude difference can be 100x+).

### 2.4 ④ Consolidation
Solidify adjudication results as system assets, ensuring no repeat adjudication.
**Paths**: New rules → rules/ (after effect gate four checks); rule modifications → rules/ (old archived, new validated); decision consensus → _Memory/distill/; important decisions → _Memory/history/analects/; constitution updates → constitution/ (after design review).

**Rule Effect Gate (Four Checks)**: 1) Existence check (file exists, format correct); 2) Semantic sync check (rules consistent with basic law/design principles key concepts); 3) Reference check ([Rxxx] references defined, no dead links); 4) YAML Schema compliance (rules.yaml required sections complete, rule IDs unique).

> **Internal implementation note**: Open-source validator.py provides generic version of above four checks. Internal full version additionally includes directory read-only permission enforcement and deep semantic rule checks, not yet open-sourced.

### 2.5 ⑤ Retirement
Obsolete rules, consensus, and memory need retirement to avoid rule obesity.
**Triggers**: Rule no longer referenced (reference count 0); rule conflicts with new rule, human adjudicates retirement; rule's scenario no longer exists; rule explicitly marked "pending retirement."
**Process**: Detect pending retirement → human confirmation → old rule archived to _Memory/history/rule-archive/ → index updated, marked retired → distill updated, remove retired rules.

**Non-Additive Principle**: More rules isn't better. New rules must prove "problems will occur without adding," otherwise don't add. This is the core principle against rule obesity.

## 3. Governance Intensity Grading (BCG Four-Level Mapping)

GOAA's governance intensity is not one-size-fits-all, but graded by task risk:
- **B (Baseline)**: Daily conversation, info query, low-risk tasks → Light governance (startup loading + shutdown)
- **C (Controlled)**: Document generation, code writing, medium-risk tasks → Medium governance (+ rule check + ambiguity detection)
- **G (Governed)**: Architecture changes, rule modifications, high-risk tasks → Strong governance (+ human adjudication confirmation + effect gate)
- **S (Sovereign)**: Constitution modifications, core principle changes → Strongest governance (+ design review + major version update)

**Dynamic rate design**: Governance intensity dynamically adjusts based on task risk, not fixed.

---

*GOAA · Normalized Adjudication Loop · Based on academic paper DOI:10.5281/zenodo.22165301 · 2026-08-28*
