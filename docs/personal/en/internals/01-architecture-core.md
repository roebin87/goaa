# 01 · GOAA Architecture Core Working Principles
> **Semantics**: Machine (mechanism/translation layer · How)

> This document publishes the design principles and workflows of GOAA's architecture core. Full implementation details are not yet open-sourced.

## 1. Five-Layer Architecture and Dependencies

GOAA uses a bottom-up five-layer architecture. Each layer depends on the layer below. Governance is not bound to specific models or execution frameworks.

```
Layer 5 · Application Layer (book production/self-bootstrapping/knowledge management...)
Layer 4 · Execution Add-on Layer (multi-role collaboration/external tools/execution frameworks)
Layer 3 · Core Mechanism Layer (startup/shutdown/ambiguity governance/memory loading/reuse)
Layer 2 · Rules & Memory Layer (rule classification/effect gate/four-layer memory/distillation)
Layer 1 · Constitution & Physical Base Layer (basic law/design principles/file system/permission isolation)
```

**Dependency principles**: Bottom-up dependency; upper layers must not bypass lower layers. Governance logic concentrated in layers 1-3; layer 4+ are execution add-ons. Models and execution frameworks are replaceable at layer 4.

## 2. Loading Sequence: Constitution→Rules→Mechanisms→Execution

GOAA startup follows a strict sequence, ensuring governance precedes execution:

1. **Step 0**: Locate body (workspace anchoring)
2. **Step 1**: Read constitution (basic_law.md + design-principles.md)
3. **Step 2**: Read identity (SOUL + IDENTITY + USER + owner profile)
4. **Step 3**: Read distillation (_Memory/distill/, create empty if first time)
5. **Step 4**: Run startup sequence (instruction dual-check + check-in + validator self-check)
6. **Step 5**: Memory validation (validator.py --memory)
7. **Ready**: Respond to owner instructions

**Loading principles**: Constitution before identity, identity before memory, memory before execution. Any failure stops and reports. First activation triggers onboarding if owner profile doesn't exist.

## 3. Governance-Execution Separation (Physical Implementation)

GOAA's "governance-execution separation" is implemented through file system physical isolation.

**Governance files (read-only/human-controlled)**: constitution/ (machine read-only), rules/ (machine read-only, effect-gated), _Memory/history/ (append-only), identity/owner-profile.md (machine read-only).

**Execution files (writable/machine-controlled)**: _Memory/snapshot/ (writable), _Memory/index/ (writable), _Memory/distill/ (writable at shutdown, human-confirmed), workspace temp files.

**Physical hooks (HOOKS)**: Startup hook (must read constitution), shutdown hook (must execute five hooks), rule effect hook (must pass four checks), permission hook (governance files marked machine read-only).

> **Internal implementation note**: Directory read-only permission enforcement and deep semantic rule checks are internal custom capabilities not yet open-sourced. Open-source validator.py provides generic structural validation.

## 4. Model-Agnostic Design

GOAA's core governance layer is independent of specific AI models:
- Models at layer 4 (execution body, replaceable)
- Governance logic in files (pure text, no model-specific API dependency)
- DEPLOY.md instructions work with any AI assistant with local file read/write capability
- Four-layer memory is pure text files, portable to any AI platform

## 5. Design Principles and Academic Correspondence

| Architecture design | Academic paper correspondence | Core axiom |
|---------------------|-------------------------------|------------|
| Constitution precedes execution | Decision rights axiom (Axiom 1) | Human holds 100% final decision rights |
| File system physical base | File ontology axiom (Axiom 2) | Files are authoritative carriers of memory and rules |
| Governance-execution physical isolation | Governance-execution separation principle | Governance rights belong to human, execution rights delegable to machine |
| Model-agnostic design | Sovereignty-execution rights separation | Mechanisms/authorization/adjudication belong to human, execution replaceable |

---

*GOAA · Architecture Core Working Principles · Based on academic paper DOI:10.5281/zenodo.22165301 · 2026-08-28*
