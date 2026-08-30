# GOAA Core Mechanism Internals

> This directory publishes the **design principles and workflows** of GOAA's core mechanisms. Full implementation details are not yet open-sourced, but design principles are fully public. Independent implementations based on these principles are welcome.

## Document Index

| # | Document | Content |
|---|----------|---------|
| 01 | [Architecture Core](01-architecture-core.md) | Five-layer architecture, loading sequence, governance-execution separation |
| 02 | [Four-Layer Memory System](02-memory-system.md) | History/snapshot/index/distill layers, memory loading, three governance functions |
| 03 | [Normalized Adjudication Loop](03-governance-loop.md) | Ambiguity revelation→localization→adjudication→consolidation→retirement |
| 04 | [Dual-Source Entropy Governance](04-entropy-management.md) | Technical vs cognitive entropy, entropy sink, negentropy injection, alignment capitalization |
| 05 | [Neural Flow Overview (Simplified)](05-neural-flow-overview.md) | Startup sequence, runtime loop, shutdown sequence, adjudication loop flowcharts |

## Reading Guide

- **First read**: 01→02→03→04→05 for overall understanding
- **Architecture researchers**: Focus on 01 and 04 for design philosophy and entropy framework
- **Practitioners**: Focus on 02 and 03 for memory system and adjudication loop implementation
- **Developers**: Focus on 05 for complete system operation flow

## Notes

- Documents based on GOAA academic paper (DOI: 10.5281/zenodo.22165301) and open-source mechanism documents
- Some internal implementation details (directory read-only permission enforcement, deep semantic rule checks) are not yet open-sourced, explicitly noted in documents
- Independent implementations based on these design principles are welcome; discuss in GitHub Discussions

---

*GOAA · Core Mechanism Internals · Core stable version 1.0 · 2026-08-28*
