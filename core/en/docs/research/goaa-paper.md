# The GOAA Academic Paper (Formal Verification Vehicle)

> This document is the **academic theory entry point** of the GOAA architecture — the full paper is archived open-access on Zenodo. This page provides the paper's identity, core claims, and the three-boundary declaration. This document is the theoretical anchor within this repository; design rationale and implementation details live in `docs/internals/` and the mechanism documents.

---

## Paper Information

| Field | Value |
|---|---|
| **Title** | Governance-Oriented Agent Architecture (GOAA): A File-System-Level Entropy Governance Paradigm Centered on Natural-Person Decision Authority, with Full-Hierarchy Deployment Paths |
| **Author** | Jianlong Yin |
| **Series** | GOAA master paper (sister paper to *Cognitive Lag*: the former presents the full architecture, the latter focuses on the cognitive-lag dimension and entropy-sink design) |
| **Version DOI** | `10.5281/zenodo.22165301` |
| **Concept DOI** | `10.5281/zenodo.22025298` (series-level identifier) |
| **Archive** | Zenodo, open access |

---

## Abstract

As large-language-model-driven agents move from prototype to production, systemic disorder becomes the core bottleneck: rules decay with interaction, behavior drifts with operation, and the system expands with evolution. Existing governance research either fragments by attaching to execution frameworks, or stands as a deterministic control plane but with machines as the governance subject, excluding humans from the routine governance loop.

This paper proposes the Governance-Oriented Agent Architecture (GOAA) — an entropy-governance paradigm centered on natural-person final decision authority, carried physically by file-system-level control:

- **Four axioms frame the governance boundary**: Decision Authority (AI is not a legal subject; responsibility rests with the natural person), File Ontology (the file system is the authoritative carrier of memory and rules), Inherent Ambiguity (human-machine semantic divergence cannot be eliminated, only surfaced and governed), Entropy Increase (disorder is a structural feature of long-running operation);
- **Physical files replace the logical control plane** as the governance substrate, carrying authority, history, and entropy export (authority-as-sovereignty, trace-as-evidence, persistence-as-entropy-sink);
- **Routine human adjudication + file-based four-layer memory** form the governance loop for cognitive entropy — human adjudication is not exception fallback but a fixed stage of the rule layer and consensus layer;
- **Full-hierarchy deployment path**: from individual to enterprise, the governance paradigm adapts smoothly (GOAA Lite → Personal → Core corresponding to increasing governance intensity).

To our knowledge, as of August 2026, no published research systematically demonstrates natural-person adjudication as a routine core stage of the rule and consensus layers, the physical file system as the governance carrier, and single-sovereignty authority-responsibility-unified governance.

---

## Core Claims (Four Axioms)

| Axiom | Content | Governance Implication |
|---|---|---|
| **Axiom 1 · Decision Authority** | Final decision authority rests with the natural person and is non-transferable | Human adjudication is a routine stage (not exception fallback); legal basis of authority-responsibility equivalence |
| **Axiom 2 · File Ontology** | The file system is the authoritative carrier of memory and rules | Rules are anchored in files (reloadable, auditable), independent of model-memory retention |
| **Axiom 3 · Inherent Ambiguity** | Human-machine semantic divergence cannot be eliminated, only surfaced and governed | Surface ambiguity → human adjudication, no self-assumption; three-layer semantics (human/machine/programming) |
| **Axiom 4 · Entropy Increase** | Disorder is a structural feature of long-running operation, not a fixable bug | Sustained governance response; entropy-sink + negative-entropy injection form a closed dual-source loop |

---

## Three-Boundary Declaration (Paper / Design Principles / Implementation)

| Carrier | Authority Level | Description |
|---|---|---|
| **Academic paper** (Zenodo) | **Theoretical authority** | Axiom system, theoretical delimitation, empirical method — **in conflict, the paper prevails** |
| **Design principles** (`constitution/design-principles.md`) | Design rationale | Expanded explanation of architecture design, consistent with the paper's chapters |
| **Implementation** (this repository's code/templates/mechanisms) | Engineering realization | Engineering examples of the theory, evolving with practice |

> **Boundary discipline**: each carrier serves its role — theory questions → paper, design questions → design principles, engineering questions → implementation; no change may create conflict among the three (if conflict arises, the paper prevails and the rest are revised in sync).

---

## Falsification Mechanism

GOAA's academic claims welcome falsification rather than blind belief:

- Objection to any claim in the paper → register it in the [falsification log](../falsification-log.md) (format specified there);
- Known limits and unverified claims → see the [pre-registered disclosure list](../known-limits.md) (limits disclosed before publication, no post-hoc excuses);
- Community objections are graded: fact-based objections are prioritized; malformed ones are guided to be completed.

> Further reading: GOAA's Popperian falsification stance and the verifier's posture of "we don't ask you to believe, we ask you to falsify" — see `../README.md`.

---

## Series Position

- ***Cognitive Lag*** (Yin, 2026): sister paper, focusing on the cognitive-lag dimension and entropy-sink design;
- **This paper**: master paper, presenting the full GOAA picture (axiom system → architecture design → entropy governance → full-hierarchy deployment).

---

*GOAA · Academic Paper Entry · All-Outcomes Open Source Edition (Core) · 2026-08-28*
