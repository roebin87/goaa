# Mechanism · Memory Loading & Recovery (Generic · V1.1 EN)

> The complete rules for layered memory loading — "what to load at startup, how to recall during work, what happens when context fills up".
> **V1.1 EN** (2026-08-26 · includes memory recovery flow & layered management).

## 1. Default loading at startup (resident)

| # | Content | Source |
|---|---------|--------|
| 1 | Constitution (three documents) | `constitution/` |
| 2 | Identity (three files + profile) | `identity/` |
| 3 | Global distillation | `_Memory/distill/蒸馏_当前.md` |
| 4 | Core mechanisms (startup/wrap-up/onboarding/problem-gate/ambiguity) | `mechanisms/` |
| 5 | Project distillation (if working inside a project) | `projects/项目名/_蒸馏/` |

## 2. Memory recovery flow (new conversation / new device)

Recovery chain for **any new conversation** (or switching AI / device) — the AI restores "who you are, what we've been doing":

1. **Owner profile** (`identity/owner-profile.md`) → who the owner is / preferences / boundaries
2. **Distillation** (`_Memory/distill/蒸馏_当前.md`) → what we've been doing / most important recent things
3. **Recent log** (`_Memory/history/日志/` latest day) → where we left off
4. **Memory index** (`_Memory/index/`) → locate deeper topic files if needed
5. Detail only when needed → **conversation records / soul backup** (verbatim / organized — heaviest, read last)

> Recovery complete = the AI can say "who you are + what we've been doing + where we left off" — continuity confirmed.

## 3. Layered memory management (five file types)

| File | Written when | Queried how | Nature |
|------|-------------|-------------|--------|
| Distillation (`distill/`) | Every wrap-up, overwrite | Always read at startup | Continuity core |
| Log (`history/日志/`) | Every session, append | Latest day at recovery; history for tracing | Chronicle · append-only |
| Conversation records (`history/对话记录/`) | Realtime during conversation | Only for verbatim detail | Survival-level · append-only |
| Soul backup (`history/灵魂备份/`) | Daily wrap-up | Day review | Survival-level · append-only |
| Sayings (`index/论语/`) | During conversation, with owner confirmation | Topic index | Thought sediment |

## 4. Triggered recall during work

**When information is insufficient, read in order (concentrated → complete)**:
```
index first (_Memory/index/) → locate
then soul backup (that day) → key points
finally conversation records (verbatim, heaviest) → full detail
```
Light-first: index over backup, backup over transcript.

## 5. Context threshold control

- When total tokens hit the warning line (suggest ~70% of context):
  1. Keep: constitution + identity + distillation (high-priority memory)
  2. Unload: low-priority content (old conversations / logs / examples)
  3. Ensure everything is on disk before unloading — unloading = dropping context, never deleting files
- Unloaded content is on file and recallable anytime — files exist, the system exists.

## 6. Archiving & decay (fighting memory entropy)

- **Cold archive**: history older than N months moves to `_Memory/history/archive/` (move, never delete);
- **Conclusion sedimentation**: conclusions that recur across sessions and get cited repeatedly → trigger human confirmation → promote to the rules layer (rules/ is the single source of truth);
- **Index pruning**: `_Memory/index/` updated periodically (drop dead pointers, merge duplicates).

## 7. Exception fallbacks (auto-fallback · no silent failure)

| Exception | Fallback |
|-----------|----------|
| File write fails (disk full / permission) | Stop immediately + red-light report to owner |
| Integrity check fails (memory file tampered) | Alarm at startup, mark the file, refuse to load it |
| Distillation overwrite fails | Auto-rollback to previous backup (`蒸馏_当前.md.bak-*`) |

## 8. Tamper resistance (validated via validator)

- Survival-level files (records/backup/log) record hash + count markers on generation;
- `tools/validator.py --memory` periodically verifies memory structure & file presence; changes = red-light alarm (audit iron rule).

## 9. Global vs project memory priority

- **Global memory = baseline** (constitution/rules/distillation);
- **Project memory may be stricter, never looser** (cannot break global baseline);
- Conflicts resolve to global; if undecidable, ask the owner.

---

*GOAA mechanism · Generic V1.1 EN · Single version · 2026-08-26*
