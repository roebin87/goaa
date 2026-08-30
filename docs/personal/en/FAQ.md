# GOAA Frequently Asked Questions (FAQ)
> **Semantics**: Human (intent/concept layer · reading)

> This document covers the most common questions about GOAA architecture. If your question isn't here, ask in GitHub Discussions.

## Table of Contents

- [1. Basic Concepts](#1-basic-concepts)
- [2. Getting Started](#2-getting-started)
- [3. Architecture Principles](#3-architecture-principles)
- [4. Comparison & Selection](#4-comparison--selection)
- [5. Data & Security](#5-data--security)
- [6. Contribution & Community](#6-contribution--community)
- [7. Troubleshooting](#7-troubleshooting)

---

## 1. Basic Concepts

### Q1: What exactly is GOAA?

GOAA (Governance-Oriented Agent Architecture) is an architecture template that makes AI "work controllably." Its core problem isn't "how to make AI do things" (that's enhancement frameworks), but "how to make AI do things controllably, traceably, and belonging to you."

GOAA's core carrier is the **file system** — your AI's memory, rules, and identity live in your own folder, not tied to any platform.

### Q2: What's the difference between GOAA and mainstream Agent frameworks (LangChain/AutoGPT/CrewAI)?

| Dimension | Mainstream enhancement frameworks | GOAA governance architecture |
|-----------|----------------------------------|------------------------------|
| Core goal | Make AI more capable (do things) | Make AI controllable (governance) |
| Memory carrier | Cloud/vector database/platform-bound | Local plain-text files (your folder) |
| Decision rights | AI autonomous decision-making | Human holds 100% final decision rights |
| For | Developers/engineers | Ordinary people (zero coding ability) |
| Relationship | Base (capability) | Coefficient (controllability) — multiply |

In short: enhancement frameworks make AI "able to do more," GOAA makes AI "trustworthy in what it does." They're complementary, not competitive.

### Q3: Why "governance-oriented" instead of "enhancement-oriented"?

Because GOAA's core design philosophy is **governance before execution**. In human-AI collaboration, AI's execution capability is already strong enough (large models keep improving). The real bottleneck is "can we trust, control, and trace what AI does."

GOAA brings AI's execution behavior into a human-governable framework through constitution layer, rule system, adjudication loop, and memory governance. That's what "governance-oriented" means.

### Q4: Is GOAA a software? Do I need to install it?

GOAA is **NOT software to install**. It's a **file system + operation specification**. You download a folder, set it as workspace in an AI assistant, and you're ready.

No coding ability, no server deployment, no dependency installation. The only requirement is an AI assistant with local file read/write capability (WorkBuddy, Claude Code, Cursor, etc.).

### Q5: Which AI assistants/models does GOAA support?

GOAA's core governance layer is **model-agnostic** — it doesn't depend on any specific AI model or platform. Any AI assistant with local file read/write capability can use GOAA.

Currently recommended: WorkBuddy, Claude Code, Cursor, ChatGPT (with code interpreter). Theoretically, any AI that can read/write local files works.

---

## 2. Getting Started

### Q6: How do I start using GOAA?

Three steps:
1. **Download**: Download `zh/` (Chinese) or `en/` (English) folder to your computer
2. **Anchor**: Set the folder as workspace in your AI assistant (the layer containing README.md)
3. **Speak**: Say "Hello" — AI auto-starts first-activation onboarding, creates your companion in ~5 minutes

See "5-Minute Quick Start" in [README.md](README.md).

### Q7: I have no technical background at all. Can I use GOAA?

**Yes.** GOAA's designer himself has zero coding ability and is not a computer science professional. One of GOAA's design goals is "the understanding threshold of governance architecture belongs to ordinary people."

First-activation onboarding is jargon-free — AI talks to you in natural language, no technical concepts needed. Just answer AI's questions about your preferences and habits. Takes 5-10 minutes.

### Q8: What can GOAA be used for?

GOAA is a general governance foundation for any scenario requiring long-term AI collaboration:
- **Personal knowledge management**: organize notes, build knowledge base, accumulate continuously
- **Content creation**: write books/articles, multi-role collaborative production
- **Project management**: track progress, manage todos, precipitate experience
- **Learning assistant**: study plans, progress tracking, review and consolidation
- **Personal assistant**: schedule management, information organization, decision support

GOAA doesn't limit specific use cases — it's a foundation that "makes AI belong to you, remember you, and listen to you."

### Q9: How is GOAA different from regular AI chat?

Regular AI chat: **each conversation is new, AI doesn't remember you, memory ends when conversation ends.**

GOAA:
- **AI remembers you**: your preferences, habits, conversation history live in files, auto-loaded each startup
- **AI listens to you**: rules you make stay effective, AI doesn't "say and forget"
- **AI belongs to you**: all data in your own folder, not tied to any platform, portable anytime
- **AI evolves**: collaboration experience continuously precipitates, AI understands you better over time

In short: regular AI chat is "one-time," GOAA is "continuous and yours."

---

## 3. Architecture Principles

### Q10: Why "files are memory"?

AI models have no persistent memory — context is lost when each conversation ends. GOAA solves this through the **file system**: write AI's memory, rules, identity, and history into plain-text files in your folder.

Each startup, AI reads these files to restore "memory." Files exist, system exists — as long as your folder is there, your AI companion is there.

That's "files are memory": **files are the authoritative carrier of AI memory**, not dependent on model context or cloud services.

### Q11: What does "human holds 100% decision rights" mean?

This is GOAA's **mother axiom** (most core principle): in human-AI collaboration, humans hold 100% final decision rights; AI only has execution and advisory rights.

Specifically:
- **Rules made by humans**: AI can suggest rules, but rules must be human-confirmed to take effect
- **Key decisions by humans**: decisions on direction, boundaries, important choices must be human-final
- **AI cannot modify governance files**: constitution, rules, identity — AI can only read, not modify
- **Humans can override AI anytime**: AI's suggestions are not binding

This isn't "AI is dumb so humans must manage" — it's the **sovereignty principle**: AI is your tool, not your master. Decision rights of tools always belong to the user.

### Q12: How does GOAA's memory work?

GOAA uses a **four-layer memory system**:

1. **History layer**: complete conversation records and operation logs, append-only, "original archives"
2. **Snapshot layer**: complete state snapshot at each session end, "time capsules"
3. **Index layer**: indexes by keyword/topic/time, "table of contents"
4. **Distill layer**: AI-generated, human-confirmed essence summaries, "core memory"

At startup, only distill layer is loaded (light load, a few thousand tokens). When details needed, retrieve history/snapshot via index (deep load, on-demand). This ensures memory continuity while controlling token cost.

### Q13: How do rules take effect? Why doesn't AI "say and forget"?

GOAA's rule effect has a **four-gate effect gate**:

1. **Existence check**: rule file exists, format correct
2. **Semantic sync check**: rule consistent with constitution/design principles core concepts
3. **Reference check**: referenced rules/concepts defined, no dead links
4. **Schema compliance**: rule file符合 YAML Schema, required fields complete

Only rules passing all four gates take effect. Effective rules are loaded every startup, AI must comply. Rules aren't verbal agreements that "say and forget" — they're **institutions** written to files, validated, and continuously effective.

### Q14: What is the "adjudication loop"?

The adjudication loop is GOAA's core mechanism for governing ambiguity, conflict, and lag, with five steps:

1. **Revelation**: expose hidden ambiguity/conflict/lag (not mask it)
2. **Localization**: locate root cause and layer (human semantic/machine semantic/rules/governance)
3. **Human adjudication**: final decision by human (owner), AI only provides analysis
4. **Consolidation**: write adjudication results to files (new rules/consensus/version updates)
5. **Retirement**: clean obsolete rules/consensus timely, avoid rule bloat

Key: **human adjudication is a fixed环节 of the rules layer, not exception fallback**. AI cannot resolve ambiguity on its own, must submit to human adjudication. This ensures governance rights always in human hands.

---

## 4. Comparison & Selection

### Q15: What's the difference between GOAA and RAG (Retrieval-Augmented Generation)?

RAG solves "how AI gets external knowledge" — inject relevant documents into context via vector retrieval for more accurate answers.

GOAA solves "how AI is governed and belongs to you" — through file system, rule system, adjudication loop, make AI's behavior controllable, traceable, and yours.

Different layers:
- RAG is **knowledge acquisition layer** technology (enhancement)
- GOAA is **governance foundation layer** architecture (governance)

GOAA can work with RAG: use GOAA as governance foundation, RAG for knowledge retrieval. No conflict.

### Q16: What's the difference between GOAA and AI memory plugins (Mem0, Zep)?

| Dimension | Memory plugins (Mem0/Zep) | GOAA |
|-----------|---------------------------|------|
| Core function | Add memory to AI | Add governance to AI (memory is one part) |
| Memory carrier | Cloud database/vector DB | Local plain-text files |
| Data ownership | On plugin provider's servers | In your own folder |
| Portability | Tied to plugin service | Plain-text, portable anytime, works with any AI |
| Governance | None (only memory) | Complete constitution/rules/adjudication/memory system |
| For | Developers | Ordinary people |

In short: memory plugins only solve "does AI remember," GOAA solves the complete problem of "does AI remember + listen + belong to you."

### Q17: I'm already using LangChain/AutoGPT. Do I still need GOAA?

Depends on your needs:
- If you only need AI to "do things" without long-term governance and data ownership, LangChain/AutoGPT is enough
- If you need AI for "long-term collaboration, remembers you, listens to you, data belongs to you," GOAA can serve as governance foundation, working with LangChain/AutoGPT

GOAA and enhancement frameworks are **complementary**, not competitive. Enhancement frameworks provide capability (base), GOAA provides controllability (coefficient). Base × coefficient = truly usable AI collaboration.

---

## 5. Data & Security

### Q18: Is my data safe? Will it be uploaded to cloud?

All GOAA data (memory, rules, identity, conversation records) lives in **your local folder**, not auto-uploaded to any cloud.

The only "external" involvement: your conversation with AI assistant is sent to AI model provider (OpenAI, Anthropic, etc.) — unavoidable with any AI assistant. But GOAA's **file data** isn't auto-uploaded — AI only reads files in your workspace when needed, files themselves stay on your computer.

For extreme privacy requirements, use locally-deployed AI models (e.g., Ollama) — all data stays on your computer.

### Q19: I want to switch AI assistants. Can my GOAA data still be used?

**Yes.** This is one of GOAA's core advantages — **data portability**.

All GOAA data is plain-text files, not tied to any specific AI model or platform. Switch to a new AI assistant, set the same folder as workspace, new AI reads your memory/rules/identity, continues collaboration.

Your AI companion isn't "an account bound to a platform" — it's "a file system in your folder." Folder exists, companion exists.

---

## 6. Contribution & Community

### Q20: Can I contribute to GOAA? How?

**Welcome!** GOAA is open source, Apache-2.0 license.

Contribution ways include (not limited to):
- **Documentation**: improve docs, translate, write tutorials/examples
- **Mechanisms**: propose new mechanism designs, improve existing ones
- **Tools**: develop auxiliary tools (validator, init scripts, migration tools)
- **Templates**: contribute templates for different scenarios (book writing, project management)
- **Adaptation**: adapt for different AI assistants/platforms

See [CONTRIBUTING](../../../CONTRIBUTING.md) for process. GOAA uses "core stable + peripheral iteration" dual-track: core design changes require design review, peripheral improvements merged anytime.

### Q21: What is GOAA's license? Can I use it commercially?

GOAA uses **Apache-2.0** license. This means:
- ✅ Free use (personal and commercial)
- ✅ Modify and distribute
- ✅ Use in closed-source projects
- ✅ Apply for patents
- ⚠️ Must retain copyright and license notices
- ⚠️ Modified files must state modifications
- ⚠️ Cannot use project name for trademark promotion

In short: Apache-2.0 is very permissive, you can do almost anything, just retain notices.

---

## 7. Troubleshooting

### Q22: AI didn't auto-start first-activation onboarding. What to do?

Say to AI: **"Read README.md and follow its instructions to start"** — this forces onboarding.

If still not working, check:
1. Workspace anchored correctly (should be layer containing README.md, not outer)
2. AI assistant has local file read/write capability (some don't support local files)
3. `identity/owner-profile.md` already exists (if exists, AI follows regular startup, won't onboard again)

### Q23: AI seems to have "forgotten" previous rules/agreements. What to do?

Usually because **memory not loaded correctly**. Check:

1. **Shutdown executed**: Did last session end with shutdown five hooks? If not, experience may not have precipitated to distill layer
2. **Distill layer updated**: Check `_Memory/distill/` for latest distill files
3. **Startup loaded**: Did AI read distill layer at startup? Ask AI "what startup files did you read?"
4. **Rules effective**: Check rule files passed effect gate four checks

If all normal but AI still "forgets," manually remind AI "please re-read distill layer and rule files," or re-execute shutdown to update distill layer.

### Q24: Rules conflict. What to do?

GOAA has **rule conflict detection** — scans rule files for same trigger conditions, mutually exclusive instructions, etc.

If conflict found:
1. AI reveals conflict (won't自行 choose which to follow)
2. Submit to adjudication loop, human (owner) final decision
3. Result consolidated: keep one, modify one, or retire both
4. Retired rules archived to `_Memory/history/rule-archive/`

Rule conflict isn't a "bug" — it's normal operation of governance system. Through adjudication loop, rule system continuously optimizes.

### Q25: I want to reset GOAA and start over. How?

To completely reset:
1. **Backup**: backup current workspace first (in case of regret)
2. **Delete instance files**: delete `identity/owner-profile.md`, all content in `_Memory/`, `_Work/`, `_Output/`
3. **Keep template files**: keep `constitution/`, `rules/`, `mechanisms/`, `methodologies/`, `templates/`, `tools/`
4. **Re-activate**: re-anchor workspace in AI assistant, say "Hello," start new onboarding

If you want to reset template files too (e.g., use latest version), just re-download GOAA repository.

---

*GOAA · FAQ · Core stable version 1.0 · 2026-08-28*
*If your question isn't here, ask in GitHub Discussions (repo entry point in the root README)*
