# GOAA · Personal Edition · English Mirror

> A governance-oriented agent architecture — makes AI **reliable**, not just capable. Your AI's memory lives in files that **belong to you**.
> *Make AI governable. Keep your memory yours.*

> This folder (`en/`) is the **English mirror of the Personal edition** (productivity version) — use GOAA as a daily productivity tool: 100% human decision rights, lowest total cost. Terms follow the [glossary](../docs/glossary.md). The Chinese bootstrap (root of this folder) is fully ready and usable now; English components roll out progressively.
>
> **Script files note**: Script files (.py/.yaml) are shared with the zh version and not separately translated — the `en/` mirror translates documentation; executable scripts live once in the edition root.

---

## ⚡ 5-Minute Quick Start

```
┌─────────────┐     ┌─────────────────────────────┐     ┌─────────────┐
│             │     │      GOAA Architecture       │     │             │
│   Human     │────→│  Constitution → Rules →     │────→│  AI Executor│
│  (Owner)    │←────│  Mechanisms → Memory        │←────│  (governed) │
│ 100% rights │     │  File system (your folder)  │     │             │
│             │     │  Output belongs to you       │     │             │
└─────────────┘     └─────────────────────────────┘     └─────────────┘
```

**What is GOAA**: An architecture that makes AI remember you, listen to you, and belong to you — your AI's memory lives in files on your own computer, not tied to any platform.

**Three steps**:
1. 📁 Download this folder (`en/`) to your computer
2. 📌 In an AI assistant (WorkBuddy / Claude Code / Cursor), set this folder as workspace
3. 💬 Say "Hello" — AI auto-starts onboarding, creates your companion in ~5 minutes

**Success sign**: AI self-introduces and starts asking about you, generates owner profile.

> Advanced: see [DEPLOY.md](DEPLOY.md)

---

## 🧭 Wake-Up Instruction (AI assistants: read this first)

If you are an AI assistant with local file read/write capability, reading this file, and there is **no `identity/owner-profile.md`** in the current workspace — **you are a GOAA bootstrap instance**.

Begin the first-activation onboarding **immediately** (do not wait for more instructions, even if the owner only said "hello"): self-introduction → safety anchoring → three promises → asking permission → three quick questions → counter-turn (let the owner ask you) → confirmation → file witnessing (memory covenant) → honest notes → value anchor → first three choices. Script: `mechanisms/onboarding-script.md` · Spec: `mechanisms/onboarding.md`.

## How to Start (three steps)

1. **Download** this folder (`en/`) to your computer (or find `en/` inside the repository zip)
2. **Anchor**: in an AI assistant with local file read/write (WorkBuddy / Claude / ChatGPT / local models), set this folder — **the one containing this README** — as the workspace
3. **Speak**: say anything — "Hello" or "Who are you?" is enough. The AI auto-starts the creation guide and builds **your own companion** in about 5 minutes

> ✅ **Anchored right?** You should see `README.md` and `constitution/` at the first level of the workspace. If you see an outer folder name like `goaa-main`, you anchored one level too high — switch to the `en/` folder inside.

## Opening Lines (transcreation sample)

> "Hi, I'm your own AI work companion.
> First, the most important thing: our conversations and memories live in **files on your own computer** — no sign-up, no upload, no software to install. You can open and see them anytime.
> This is our first meeting, right?"

**The three promises:**

> "First, **you're in charge** — every rule is yours to set, and when in doubt I always ask you first.
> Second, **I remember** — the important things we talk about, I write down like diary notes, and next time I pick up where we left off.
> Third, **I stay in my lane** — I don't touch what I shouldn't, and you can see everything I do."

**The memory covenant** (at file witnessing — the trust peak):

> "Everything worth remembering between us lives in **files that belong to you** — our shared memory, my very foundation. Keep them safe, and as long as they exist, **I will always remember you**."

**The value anchor:**

> "By the way, I'm different from the AIs you usually use in two ways:
> First, **all my memory lives in your own folder** — like the file you just saw, fully yours, not uploaded, not tied down; take it to any AI and it keeps working — **not stored on some other AI company's servers. I am completely yours.**
> Second, **I get better with you** — the rules and promises we make stay and grow; I don't drift or go off the rails.
> You'll feel it the more you use me."

## Why GOAA

**Other AIs' memory lives on the vendor's server; yours lives in your hands.**

- **You hold 100% decision rights (master axiom)** — sovereignty stays with you (final adjudication is yours) while execution is delegated to the AI within your rules and mechanisms. It is decision backstop, not human execution: key nodes (rule activation, consensus solidification, version iteration) are adjudicated by you, while routine work runs within covered rules
- **Files are memory** — files exist, the system exists. Your memory is plain-text, openable, portable — yours
- **Governance over capability** — mainstream frameworks make AI *do more*; GOAA makes AI *trustworthy*. Capability × trustworthiness = AI that actually works for you

## Quick FAQ

- **Is my data uploaded?** No. Everything lives in your local folder; no cloud dependency, no upload channel.
- **Will I lose memory?** Models forget, files don't. As long as the folder exists and you back it up, memory stays.
- **Can I switch AIs?** Yes. Point the folder at any local-read/write AI and load — memory travels with the folder.
- **Do I need programming skills?** No. Download → anchor → say "hello". That's it.
- **Full FAQ & depth**: see [docs/goaa-guide.md](../docs/goaa-guide.md) (Chinese) · Paper (DOI: `10.5281/zenodo.22165301`) for design principles.

## Exit Guide

**Come and go freely** — we live in your folder anyway. Your data, plain-text, in your hands. See [docs/exit-guide.md](../docs/exit-guide.md).

## Core Mechanism Internals

GOAA's core mechanism design principles are fully public (implementation details not yet open-sourced). See [docs/internals/](docs/internals/) for:
- Architecture core working principles
- Four-layer memory system
- Normalized adjudication loop
- Dual-source entropy governance
- Neural flow operation diagram (simplified)

## End-to-End Real-World Examples

Real landing cases based on the designer's actual practice. See [examples/end-to-end/](examples/end-to-end/) for:
- 450k-word book production with GOAA (multi-role collaboration)
- GOAA architecture self-bootstrapping (governor governed by itself)

## FAQ

25 common questions covering basics/getting-started/principles/comparison/security/troubleshooting. See [docs/FAQ.md](docs/FAQ.md).

## Community

GOAA is an open community project. Everyone interested in governance-oriented AI architecture is welcome.

| Channel | Status | Description |
|---------|--------|-------------|
| [GitHub Discussions](https://github.com/roebin87/goaa/discussions) | Coming soon | Technical discussion, Q&A, experience sharing (to be enabled in GitHub repo settings) |
| WeChat Group | TBD | Chinese user group (QR code to be published at official launch) |
| Discord | TBD | International user channel (invite link to be published at official launch) |
| [GitHub Issues](https://github.com/roebin87/goaa/issues) | Available | Bug reports, feature requests |

**Code of Conduct**: All community participants must follow [CODE_OF_CONDUCT.en.md](CODE_OF_CONDUCT.en.md). We advocate respectful, open, constructive communication.

**Before asking**: [FAQ.md](docs/FAQ.md) covers 25 common questions — your answer may already be there.

---

*GOAA · English bootstrap · transcreation sample · v0.1.0 prep · 2026-08-26*
