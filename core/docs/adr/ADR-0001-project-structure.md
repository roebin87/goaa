# ADR-0001 · Project Structure Finalized (governance-first · file-driven)

> **Status**: Accepted ｜ **Date**: 2026-08-19 ｜ **Decision-maker**: author adjudicates · AI executes
> **Series**: docs/adr/ architecture decision records (decision trace · audit trail origin)

---

## Background

The GOAA open-source project needed to settle its directory structure. The V1 structure was rejected (curse of knowledge — taking the internal system's structure for granted, forgetting that open-source readers are zero-context people); after cross-checking against the DeepSeek Harness paradigm + 2.0 design principles, a V2 structure was produced and needed finalization.

## Decision options

| Option | Description |
|------|------|
| A · V1 structure | export the internal system structure directly (rejected) |
| B · V2 structure | anchored to the dsh paradigm (thin portal, thick system / ADR / complete templates) + 2.0 principles (five-tier classification / three semantics / rules-mechanisms separation / loading layers / self-bootstrap) — **adopted** |
| C · entirely new design | redesign detached from the existing system (rejected · wastes existing theoretical assets) |

## Decision (adopt B)

Adopt the V2 structure and finalize it. Core points:
1. **Root level**: README (thin facade) + STRUCTURE.md (thick truth · single entry for external review) + DEPLOY (self-bootstrap deployment)
2. **Constitutional layer** constitution/ (Basic Law / Design Principles) — establish the rules first
3. **Rules ↔ mechanisms separation**: rules/ (what is written) + mechanisms/ (how to verify)
4. **templates/** (identity / memory / workspace templates · self-bootstrap gap)
5. **docs/** (concepts one by one + comparison + adr decision trace)
6. **tools/ minimized**: only validator.py (the verifier · no fabricated execution capability)

## Consequences

- ✅ Positive: the structure = the entry point for external review (a reviewer reads one file to judge); every directory has a theoretical basis (no redundancy); self-bootstrappable (templates complete)
- ⚠️ Cost: content must be written file by file (book-style, chapter by chapter); new readers still need time to digest
- 📌 Follow-up: core stable version 1.0 (core design changes require review; periphery iterates with community); to be supplemented before the English version's external release

## Related

- Concepts: three semantics / priority rules / falsifier
- Mechanisms: all (the structure carries the mechanisms)
- Files: STRUCTURE.md (structural truth · the living embodiment of this ADR)

---

*GOAA · ADR-0001 · Single version 1.0 · 2026-08-19*
