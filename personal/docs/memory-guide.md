# Memory Management Guide (user-facing · files are memory)

> **Core**: GOAA's memory = files in your own folder — managing memory = managing files. This guide teaches you: what to record, where it lives, how to back up, how to migrate, and how to recover when lost.
> **Version**: Single version 1.0 · 2026-08-26

---

## 1. Memory File Map (which file stores what)

| File/directory | What it stores | When written | Can it be changed? |
|-----------|--------|--------|--------|
| `identity/owner-profile.md` | your name/preferences/boundaries (your personal profile) | generated at first onboarding · supplemented continuously | 🔒 machine read-only · only you may edit |
| `_Memory/distill/蒸馏_当前.md` | the most important recent things (cross-conversation continuity core) | overwritten at every wrap-up | append-style; overwrite is executed by the wrap-up mechanism |
| `_Memory/history/日志/` | daily running chronicle (append-only) | end of every session | never delete/modify |
| `_Memory/history/对话记录/` | verbatim raw transcript (A5 survival-grade) | written to disk in real time | never delete/modify |
| `_Memory/history/灵魂备份/` | organized day-end version | daily wrap-up | never delete/modify |
| `_Memory/index/论语/` | your thoughts/quotes (topic-indexed) | captured during use | never delete/modify |
| `_Memory/index/` | memory index (navigation) | updated at wrap-up | updatable |

## 2. Backups (the most important thing)

**Memory = files · files can be lost · so backup = your guardian action.**

1. **Manual backup**: copy the whole workspace folder to a safe place (USB/cloud/another computer) — plain-text files, openable on any device;
2. **Wrap-up reminder**: at every wrap-up the AI reminds you ("our memory lives in these files") — build the habit;
3. **Suggested rhythm**: back up immediately after important conversations · once a week routinely.

## 3. Migration (new device / new AI assistant)

**Memory lives in files, not in the model — so migration = moving a folder:**

1. **Switch AI assistant**: point any locally read-write AI (WorkBuddy / Claude / ChatGPT / local models) at the workspace folder → say "load my system per the startup sequence" → memory carries over seamlessly;
2. **Switch computers**: copy the whole workspace folder to the new computer → anchor → load → memory follows;
3. **Multiple devices**: put the folder into a cloud-sync directory (e.g. OneDrive / Nutstore) — two devices stay in sync.

## 4. Recovery (new conversation / "lost" memory)

1. **New conversation**: at startup the AI automatically reads the distillation + profile and restores "who you are, what we discussed" — no manual action needed;
2. **Feeling the memory is gone**: check first — ① is the workspace still anchored to **the same folder** (changing the folder = changing the "body") ② does the distillation file exist (`_Memory/distill/蒸馏_当前.md`) ③ is the backup still there;
3. **Restore from backup**: copy the backup folder back to the workspace location → re-anchor → load → memory is back;
4. **Last line of defense**: conversation records (verbatim) always live in `_Memory/history/对话记录/` — even if the distillation is lost, the verbatim record remains and can be rebuilt.

## 5. Cleanup & Archiving (preventing "memory bloat")

Files grow heavier over time? Normal — but manageable:

1. **Auto-archive**: the system periodically moves old logs/conversations to a cold-archive directory (`_Memory/history/archive/`) — move only, never delete;
2. **Conclusion sedimentation**: recurring conclusions rise from the memory layer to the rules layer (rules/ is the single data source) — freeing memory-layer space;
3. **Manual trimming**: delete temporary files no longer needed (never delete: logs / conversation records / soul backups — survival-grade);
4. **Size compliance**: when memory files exceed the red line the AI warns (red-flag block) — archive first, then continue.

## 6. Memory Health Check (verifiable)

Run in the deployment area:

```bash
python3 tools/validator.py --memory
```

It outputs the status of each memory layer/core file ([OK] ✓ / [WARN] notice) — **"files are memory" is measurable and verifiable** (the architecture holds = the measurability principle).

## 7. Memory FAQ

**Q: Can memory be lost?**
A: As long as the files exist, it is always there. Models forget, but files don't — provided you: anchor the same folder + keep backups.

**Q: Will the AI secretly modify my memory?**
A: No. The owner profile is machine read-only (filesystem read-only permission); logs/records are survival-grade append-only, never deleted or modified; any new preference is written only after your confirmation (silent supplement is forbidden).

**Q: Can other people see my memory files?**
A: The files are on your computer; unless you share them, no one else can see them; the machine has no upload permission.

**Q: What is distillation? Why does it matter?**
A: Distillation = compressing the most important things of the day into a few lines stored in `_Memory/distill/` — it is the core of cross-conversation continuity ("I still remember when we continue next time" relies on it).

**Q: Can I open and view the memory files directly?**
A: Yes, anytime. All files are plain-text MD — open and see. This is the fundamental difference between GOAA and black-box memory.

---

*GOAA · Memory Management Guide · Single version 1.0 · 2026-08-26*
