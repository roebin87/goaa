# GOAA Lite · Beginner Edition

> **Make AI governable. Keep your memory yours.**
> **让 AI 干得可控，让你的记忆属于你。**

[中文版](https://github.com/roebin87/goaa/tree/main/lite-zh)

GOAA is a **governance-oriented AI architecture**: mainstream tools solve "how to make AI work"; GOAA solves "how to make AI reliably governable — and how to keep what's yours always yours."

This folder (`lite/`) is the minimal usable version — **no technical background needed**. In 5 minutes you can have an AI work companion whose memory belongs entirely to you.

---

## Generations (What GOAA Is & Where It's Going · One-Line Version)

```
1.0 Ownership (whose memory) → 2.0 Decision Authority (who decides) → 3.0 Social Validation (verify together) → 4.0 Meta-Order
★ Current: 2.0 · Full theory in the academic paper (DOI at the bottom)
```

## How to Start (Three Steps)

1. **Download**: download this entire `lite/` folder to your computer (anywhere is fine);
2. **Open**: in your AI assistant (e.g. WorkBuddy / Claude / Cursor or other local tool), **set the `lite/` folder as the workspace** — the level that contains this README;
3. **Speak**: say **"hello"** to the AI — it automatically starts the onboarding, creating your dedicated AI companion in ~5 minutes.
   - If the AI doesn't start automatically, tell it: **"Read mechanisms/onboarding-lite.md and follow its instructions."**

> ✅ **Self-check**: the first level of your workspace should show `README.md`, `constitution/`, `templates/` folders. If you see an outer directory name like `goaa-lite`, you anchored at the wrong level — set the workspace to this folder instead.

## What's in This Folder (What Each Piece Does)

| Path | Purpose |
|------|---------|
| `constitution/basic_law.md` | **Core principles** — the highest agreement between you and your AI (readable in 5 minutes) |
| `templates/identity/` | Your dedicated profiles: SOUL (behavior covenant) / IDENTITY (structure map) / USER (your profile) / Agent_Profile (AI portrait) — the AI walks you through them at activation |
| `templates/memory/` | Memory templates: distillation (cross-day essence) / dialogue record (verbatim retention) — **your memory files** |
| `mechanisms/startup.md` | Startup flow: how the AI loads every time you open the workspace |
| `mechanisms/shutdown.md` | Wrap-up flow: the five things the AI must do before closing a conversation (memory persistence) |
| `mechanisms/onboarding-lite.md` | First-activation onboarding script (for the AI) |
| `tools/verify-ownership.py` | **Ownership verification**: one command proving "your memory is 100% yours" (see below) |
| `docs/ownership.md` | Ownership guide: the five checks explained + exit/migration guide |

## Core Proof Action: Verify "Memory Belongs to You" (60 seconds)

```bash
python3 tools/verify-ownership.py
```

You'll see **5 ✅** (local / plain text / no cloud / portable / no lock-in) plus 2 manual verification guides. These 5 conditions all holding means: your AI memory lives in your own folder — plain text, readable offline, copyable, bound to no vendor. No LLM or AI application can withhold it.

> Found any check failing? Tell us — GOAA doesn't ask you to believe, it asks you to falsify (feedback entry at the bottom).

## Freedom to Leave (Come and Go Freely)

Done with it? **Just delete this folder** — all your memory is inside it; copy it to another computer or hand it to another AI assistant anytime. No cloud accounts, no lock-in.

## Verifier's Posture

GOAA was created by a **non-AI-engineer, non-CS designer** — the comprehension threshold of governance-oriented architecture belongs to ordinary people. The project's full theory is published as an academic paper; any claim can be questioned and verified.

- Academic paper DOI: `10.5281/zenodo.22165301` (GOAA Architecture Design Principles)
- License: [Apache-2.0](LICENSE) · Citation: [CITATION.cff](CITATION.cff)
- Feedback/falsification: GitHub Issues (`github.com/roebin87/goaa`)

---

*GOAA Lite v0.1.0 · 2026-08-28 · Generic translation*
