# Comparison: GOAA vs. LangGraph / AutoGen / dsh (governance-layer uniqueness)

> **Position**: GOAA versus mainstream agent engineering frameworks — **same form, different object layer**: they manage "engineering correctness," GOAA manages "ownership / decision rights / entropy growth."
> **Evidence source**: 2026-08-19 GitHub source-file-level verification (LangGraph/AutoGen/dsh) + live star counts.
> **Boundary**: the 019 iron rule — external material serves only as reference/comparison evidence; it does not alter this system's own statements.

---

## 1. One-line comparison

| Framework | Solves | Object layer |
|------|---------|--------|
| LangGraph / AutoGen / dsh | **how to make AI run smoothly** (state/sandbox/orchestration) | engineering correctness (enhancement-oriented) |
| **GOAA** | **how to make AI reliably governable** (ownership/decision rights/order) | governance (governance-oriented) |

> The relationship is not competition but division of labor: the outside provides "strength," GOAA provides "the order of strength" — the falsifier does not build strength, borrow strength, or govern strength.

## 2. Side-by-side comparison (source-file-level evidence)

### 1. LangGraph (langchain ecosystem · 144k stars)
| Dimension | LangGraph | GOAA counterpart |
|------|-----------|-----------|
| State persistence | checkpointer (Checkpoint snapshots + thread_id isolation + pending-writes incremental fault tolerance) | memory physicalized (files = memory carriers · distillation/chronicle/index) |
| Flow structure | declarative state graphs | mechanism layer (startup/wrap-up/problem-gate/ambiguity…) |
| Incremental fault tolerance | failed nodes do not re-run successful nodes | back up before distillation overwrite (preventing memory gaps) |
| Missing | no ownership/decision-rights concept | Mother Axiom (100% human decision rights) |

### 2. AutoGen (Microsoft · moved to maintenance mode)
| Dimension | AutoGen | GOAA counterpart |
|------|---------|-----------|
| Status | Maintenance Mode (community-maintained · moving to Microsoft Agent Framework) | verification-through-running (this system self-evidenced) |
| Multi-agent dialogue | composable termination conditions (`\|` OR / `&` AND) | normalization (single actor + asset reuse, no multi-agent needed) |
| Human in the loop | human-in-the-loop capability | two-domain division (yes/no domain machine-adjudicated / middle-ground domain human-monopolized) |
| Missing | no sovereignty/order governance | priority rules + single source of truth (the two anti-drift laws) |

### 3. dsh (DeepSeek Harness)
| Dimension | dsh | GOAA counterpart |
|------|-----|-----------|
| Sandbox | bwrap+Landlock three-tier SandboxMode + fail-closed (no backend → no bare pass-through) | directory permission mapping (🔒read-only/📌append-only/✍️overwritable) + validator hard block |
| Sessions | append-only event sourcing + deriveMessages derivation | verbatim conversation records + append-only + hash verification (chronicle layer) |
| Decision trace | AGENTS.md + `.agents/notes/` (implemented/rejected) | change-record blocks + ADR (decision trace) |
| Governance | manages engineering correctness (file-specified AI) | **manages ownership/decision rights/entropy growth (constitutional governance) — same form, different object layer** |

## 3. Governance-layer uniqueness anchors (unique to GOAA · absent in all three)

| # | GOAA-unique | The three counterparts |
|---|-----------|---------|
| 1 | **Mother Axiom: 100% human decision rights** (ownership/decision rights/accountability united) | no such concept (tools have no personified sovereignty) |
| 2 | **Constitutional layer** (Basic Law / Design Principles · immutable) | AGENTS.md is an engineering spec, not a constitution |
| 3 | **Entropy governance** (negative entropy against entropy growth · rule bloat / distillation residue / cognitive drift) | no entropy perspective (config drift ≈ entropy, but no governance-layer counteraction) |
| 4 | **The falsifier** (order gate for strength: checkable + judgeable) | validators check format correctness, not "whether it does well" |
| 5 | **The genuine-problem gate** (non-genuine problems are not approved = no resource consumption) | no problem-quality governance |
| 6 | **Ambiguity judgment belongs to the human** (machine only surfaces · human judges) | machine acts autonomously (no decision-rights division) |

## 4. Conclusion

- **Complementary, not competing**: the 100k-star track is all enhancement-oriented (how to be strong); governance-oriented is a blank — GOAA's unique value = adding the "order" layer to any enhancement-oriented framework;
- **Mountable**: LangGraph/dsh execution capability can serve as GOAA's "tools" (borrowing strength); GOAA's constitution/rules/mechanisms layer on top as "the order of strength" (governing strength);
- **Not a replacement**: GOAA does not replace enhancement-oriented frameworks; it defines what sits above frameworks — "who decides, how falsification works, where entropy comes from."

---

*GOAA · Comparison doc · Single version 1.0 · 2026-08-19 · evidence = GitHub source-file-level verification + live star counts*
