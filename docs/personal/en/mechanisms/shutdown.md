# Mechanism · Wrap-Up Five Hooks (Generic · V1.1 EN)
> **Semantics**: Machine (mechanism/translation layer · How)

> The five save-actions that must complete before closing a conversation — AI has no persistent memory; without saving to files, it's gone.
> **V1.1 EN** (2026-08-26 · includes memory-accumulation visualization).

## The five hooks
> **Semantics**: Machine (mechanism/translation layer · How)

| # | Action | Where | Note |
|---|--------|-------|------|
| 1 | Soul backup + conversation records | `_Memory/history/` | Day's key points (organized) + verbatim transcript (survival-level · never delete/modify) |
| 2 | Distillation update | `_Memory/distill/` | Overwrite — the core for cross-conversation continuity |
| 3 | Daily log | `_Memory/history/` | Append-only — the full chronicle |
| 4 | Sayings collection | `_Memory/index/` | The human's thoughts / quotes, filed by topic |
| 5 | Wrap-up report | `_Memory/index/` | Session summary / todos / health status / memory accumulation |

## Memory-accumulation visualization (V1.1 · the "memory line" in the wrap-up report)

The "health status" section of the wrap-up report **must include the memory line** (making "files are memory" visible):

> Memory today: +N entries · total M (counted across files under `_Memory/`)

- Counting: distillation (1) / log (today's entries) / conversation records (today's) / soul backup (today's) / sayings (topics)
- Effect: at every wrap-up the owner *sees* memory accumulating — the felt experience of memory continuity
- The first wrap-up also plays the "first wrap-up reinforcement" line (see onboarding)

## Mandatory hooks (deployed instances must land them with platform hooks/scripts)

- **Index update**: refresh the memory index at the end of wrap-up
- **Size compliance**: memory file over the red line = red light, blocked
- **Transcript check**: verbatim records not saved = red light, no wrap-up
- **Constitution sync final check**: validator drift red light = no wrap-up

> 🔴 Declaration calibration (2026-08-26): the mandatory hooks above only constitute runtime blocking after a **deployed instance configures platform hooks/scripts** — this repository is a generic open-source mother template and contains no platform-specific enforcement (`validator.py --memory` provides append-only hash baseline detection; see `tools/README.md`).

## Conclusion persistence (pre-wrap-up hook)

When a discussion reaches a conclusion (owner rules "land / accept / confirm"), before wrap-up:
1. Land the conclusion entry (axiom + physical rule + mechanism)
2. Sync subsidiary authoritative files (design principles)
3. Sync downstream (mechanisms / rules files)
4. Validator all green

> Not landed = red light, no wrap-up — enforced physically, not by memory.

## Continuity verification

Wrap up → open a new conversation → startup loads distillation → continuity confirmed = the body loop is closed.

---

*GOAA mechanism · Generic V1.1 EN · Single version · 2026-08-26*
