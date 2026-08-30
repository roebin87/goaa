# Exit Guide · Come and Go Freely
> **Semantics**: Human (intent/concept layer · reading)

> **We already live in your folder** — this is the most fundamental difference between GOAA and cloud/proprietary products: all your memories, rules, and profiles are plain-text files on your own computer — viewable, portable, and migratable anytime.

---

## 1. Where Your Data Lives

| Content | Location (within the deployment area) | Format |
|------|-----------------|------|
| Owner profile | `identity/owner-profile.md` | Markdown plain text |
| Distillation (memory digest) | `_Memory/distill/` | Markdown plain text |
| Conversation records | `_Memory/history/对话记录/` | Markdown plain text |
| Daily log | `_Memory/history/日志/` | Markdown plain text |
| Soul backups | `_Memory/history/灵魂备份/` | Markdown plain text |
| Rules & mechanisms | `constitution/` `rules/` `mechanisms/` | Markdown/YAML plain text |

> **All files are plain-text Markdown — openable, readable, and migratable without any proprietary tool. Your data is fully in your hands.**

## 2. How to Switch AI Foundations

Memory lives in files, not in the model — switching to any AI assistant (WorkBuddy / Claude / ChatGPT / local models) migrates seamlessly:

1. Point the new AI assistant at the deployment folder (as its workspace);
2. Tell the new AI: "Load my system per the startup sequence" (see `mechanisms/startup.md`);
3. The new instance reads the distillation + profile and continues collaborating from memory — **memory carries over seamlessly; nothing is lost by switching foundations.**

## 3. How to Pause / Delete

- **Pause**: just stop talking — the system rests quietly; you can come back anytime;
- **Back up then delete**: copy the deployment folder to a safe location → delete the deployment folder → done;
- **Migrate only, no deletion**: switch foundations per Section 2.

## 4. The One-Line Promise

> **Software that dares to let you leave is software worth staying for.** Our memory is your files — the files are in your hands, and you keep full initiative forever.

---

*GOAA · Exit Guide · Single version 1.0 · 2026-08-26*
