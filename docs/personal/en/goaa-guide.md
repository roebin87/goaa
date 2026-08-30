# GOAA Guide & FAQ (user-facing · must-read after download)
> **Semantics**: Human (intent/concept layer · reading)

> **Purpose**: for users who just downloaded this repo — what GOAA is, how it differs from other AIs, how memory works, and common questions, answered in one place.
> **Version**: Single version 1.0 · 2026-08-26
> **For the AI**: when users ask GOAA-related questions (differences/memory/safety/usage), this document is the authoritative answer source.

---

## 1. What GOAA Is

**In one line**: GOAA is a governance-oriented AI architecture — it doesn't chase "what AI can do," it chases "**AI you can rely on**."

**In one paragraph**: Mainstream agent frameworks (e.g. various enhancement-oriented assistants) solve "how to make AI work" — the more capability the better; GOAA solves "**how to make AI reliably governable**" — clear boundaries, dependable memory, decision rights in human hands. The two multiply: enhancement raises the capability baseline, governance raises the deployment coefficient — capability × trustworthiness = AI that actually works for you.

**Three core beliefs**:
1. **Sovereignty stays with the human**: you hold 100% decision rights; AI holds only execution and recommendation rights (the Mother Axiom);
2. **Memory lives in files**: AI has no memory; files exist, the system exists — memory is your asset, not the vendor's resource;
3. **Evolution through governance**: rules/mechanisms/memory keep sedimenting, fitting you better over time.

**The designer**: a non-AI-engineer, non-CS author — the understanding threshold of governance-oriented architecture belongs to ordinary people.

## 2. The Fundamental Difference from Other Agents

**It comes down to one thing: who holds sovereignty.**

| Comparison | GOAA | Other Agents |
|--------|------|-----------|
| **Where memory lives** | your local folder, plain-text MD, viewable and editable anytime | vendor servers, invisible and non-portable |
| **Who decides** | you hold 100% decision rights; AI has only execution and recommendation rights | opaque AI decisions, non-transparent rules |
| **Switching AIs** | copy the folder; any AI can continue where you left off | platform-bound; switching resets everything |
| **Investigating problems** | everything is traced; logs/change records live in files | customer support only; no evidence trail |

**In one line: other AIs are services you borrow; GOAA is an AI that belongs to you.**

## 3. How Memory Is Solved (three-layer mechanism)

**Core idea: don't rely on model memory — store in files.**

| Layer | Mechanism | What it does |
|----|------|------|
| **Startup loading** | every new conversation first reads `identity/owner-profile.md` and the recent log | restores "who you are, what we discussed" |
| **Wrap-up archiving** | say "wrap up" when the conversation ends | the day's important content is distilled into a digest and written to the log — nothing lost |
| **Files are memory** | all rules, agreements, and history live in MD files in your folder | plain text, viewable and editable, independent of any cloud |

**Models naturally forget, but files don't** — as long as the folder exists, no matter how many conversations you switch or which AI you use, the memory stays.

## 4. Memory Management vs. Other Agent Architectures

| Comparison | GOAA | Other Agent Architectures |
|--------|------|----------------|
| Where stored | your local MD files, plain text readable | vendor cloud vector DB / model context |
| Whose it is | yours — copy, delete, modify anytime | the vendor's — you only have usage rights |
| How it remembers | startup reads files + wrap-up distills and archives | automatic vectorization + retrieval, black box |
| Can you see it | open the file and see, even edit | invisible; you don't know what it recorded |
| Can it be lost | files exist → always there | platform data purge, model changes, expiry → gone |
| Switching AIs | hand the folder to any AI and continue | platform-bound; start from zero |

**In one line: other architectures lend you memory as a feature; GOAA hands you memory as property.**

## 5. FAQ (15 questions)

**Q1: Is the data safe? Will it be uploaded?**
A: All memory, rules, and conversation records live in local files on your own computer (plain-text MD), independent of any cloud service, with no channel for uploading. You can open, back up, or delete the folder anytime.

**Q2: Can memory be lost?**
A: The model naturally forgets, but files don't. Every wrap-up archives important content into files; as long as the folder exists, the memory exists. We recommend backing up regularly as the wrap-up reminds you (just copy the folder).

**Q3: Can I continue with a different AI assistant?**
A: Yes. Memory lives in files, not in the model — point any locally read-write AI assistant (WorkBuddy / Claude / ChatGPT / local models) at the folder, load per the startup sequence, and memory carries over seamlessly.

**Q4: How is this different from ChatGPT / Claude?**
A: They are capability-oriented assistants (how to make AI work); GOAA is a governance-oriented architecture (how to make AI reliably governable). And your memory/rules stay in your hands — you carry them to any AI, no lock-in.

**Q5: Do I need programming knowledge?**
A: Not at all. Download the folder → anchor the workspace → say one line, and the AI guides you through setup automatically (see the three steps in the root README).

**Q6: Does it cost money? Do I need to register?**
A: Neither. This repo is open-source and free (Apache-2.0); deployment requires zero registration, zero accounts, zero cloud dependency.

**Q7: Why is it called "wrap-up"?**
A: It's the author's everyday language — like closing up a stall: put today's things back in place, keep the books, lock the door. Say "wrap up" at the end of each day's conversation and the AI archives the day's memory.

**Q8: What is "distillation"? "Owner profile"?**
A: Distillation = compressing the most important things of the day into a few stored lines (like a diary digest); owner profile = your personal profile (name/preferences/boundaries), machine read-only, only you may edit.

**Q9: Can other people see my data?**
A: The files are on your computer; unless you share them, no one else can see them; and the machine has no upload permission.

**Q10: Will the architecture be updated?**
A: Adopts a "core stable + periphery iterative" dual-track strategy — the architecture core (constitution/rules/core mechanisms) maintains major version stability to ensure deterministic governance; the periphery ecosystem (examples/tutorials/translations/adaptations/tools) iterates rapidly and welcomes community contribution. Core design changes require design review; periphery improvements merge anytime.

**Q11: How do I back up?**
A: Copy the whole workspace folder to a safe location (plain-text files, openable on any device). The AI also reminds you at wrap-up.

**Q12: Can multiple people / teams use it?**
A: Currently positioned for individuals/small teams (the 100% human decision-rights axiom naturally fits individuals and small teams); hundred-person complex collaboration is outside the current applicability boundary.

**Q13: Where is the academic paper?**
A: The GOAA Architecture Design Principles paper (Zenodo DOI: `10.5281/zenodo.22165301`) — read the paper for in-depth design rationale.

**Q14: Who is it for?**
A: Independent creators, small teams, compliance-sensitive roles, and architecture researchers — people who use AI as a production tool and value controllability, auditability, and traceability.

**Q15: How do I start?**
A: Three steps — ① download the `en/` (or `zh/`) folder ② have a locally read-write AI assistant anchor it as the workspace ③ say "hi," and the AI automatically starts the onboarding flow.

## 6. Deep Rationale (academic paper distillation)

**Want to understand why GOAA is designed this way?**

- The complete design rationale is published as an **academic paper** (keeping this repo lightweight — lean, credible files):
  - GOAA Architecture Design Principles paper (Zenodo version DOI): `10.5281/zenodo.22165301`
- **Ask your AI deep questions** (e.g. "why is it structured this way" / "how does it relate to some theory") — the AI proactively mentions the paper and, **after you authorize**, distills it and explains in plain language (one point at a time · no pasted original text).
- Your AI never fetches paper content without your consent — the authorization is yours.

## 7. Applicability Boundary & Limitations (official honest position)

**GOAA is well designed, but not magic. The truth:**

**Where the design excels:**
- **Sovereignty to the user**: memory is handed to you as property, not kept as vendor resource;
- **Files are memory**: simple, transparent, auditable — when something goes wrong you can check and fix;
- **Governance rules in plain text**: AI behavior is controllable and doesn't drift off course mid-conversation.

**Explicit limitations:**
- **Maintenance cost** — files need to be managed and backed up by yourself (no cloud auto-sync; lazy users will find it tiring);
- **Multi-device friction** — purely local; switching devices means copying the folder yourself (a cloud-synced folder helps);
- **Memory retrieval is not smart** — context is restored by reading files; at scale it's less efficient than vector databases;
- **A learning curve** — concepts like rules/mechanisms/wrap-up take getting used to (this repo already tries hard to lower the bar);
- **Early version** — mechanisms are still being polished; some flows may feel heavy.

**Who it fits**: users who value data sovereignty, accept a bit of maintenance cost, and plan long-term use. If you want out-of-the-box, multi-device sync, zero maintenance — cloud agents are more convenient.

**Conclusion**: it's not "better than everyone" — it's that **on the dimension of "sovereign controllability," it goes further than most architectures.**

---

*GOAA · Guide & FAQ · Single version 1.0 · 2026-08-26*