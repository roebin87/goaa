# Applicability Boundary (author's statement)
> **Semantics**: Human (intent/concept layer · reading)

> **Position**: this file is the author's **responsible boundary statement** to users — GOAA cannot do everything, and the author is obliged to tell users "what it fits and what it does not."
> **Version**: Single version 1.0 ｜ **Date**: 2026-08-19

---

## 1. The one-line boundary

**GOAA is "broad-spectrum adaptation of a governance base," not "all-scenario coverage of an all-capable framework."** It does not solve "AI execution efficiency" — it solves "AI you can rely on": whoever uses AI as a production tool and values controllability, auditability, and traceability gets high adaptation value; whoever wants full automation and zero constraints gets low adaptation value.

## 2. Who it fits (author's judgment)

| Audience | Suggested tier | Why it fits |
|------|---------|---------|
| **Independent creators / solo developers** | standard / minimal tier | solving AI memory gaps + overreach — the most precise direct audience |
| **Small teams / studios within 10 people** | standard tier | unified rule base + knowledge-asset sedimentation + accountability-audit loop |
| **SMEs / compliance-sensitive roles** | full tier | clear rights & responsibilities + full-chain audit + zero cost + customizable |
| **Architecture researchers / open-source enthusiasts** | full tier + docs | reference paradigm and material for governance-oriented agent research |

## 3. What it does not fit (author's explicit boundary)

1. **Execution-efficiency-first scenarios** (large-scale automation / high concurrency / unattended operation) — governance processes add operational cost; use execution frameworks like LangGraph/dsh directly;
2. **Fully autonomous multi-agent collaboration scenarios** — GOAA's core principle = 100% human decision rights; it does not support fully autonomous multi-agent auto-running (an inherent philosophical conflict);
3. **Entertainment / chat / light-creativity scenarios** — the rule system feels heavy; the experience is worse than an ordinary chatbot;
4. **Very large enterprise-grade complex collaboration** (hundred-person cross-department / complex permission mapping / multi-level approval) — the current version adapts to single-actor/small-team governance; multi-organization, multi-level complex governance awaits expansion.

## 4. Commitments (author to users)

- **No exaggeration**: does not promise "fully automated, hands-free labor" — only "reliably governable, auditable, traceable";
- **No lock-in**: pure file specification, not bound to any model/language/platform — migratable and exitable anytime;
- **Growable**: start from the minimal tier and upgrade as scale grows (see the three-tier config in `docs/lightweight-guide.md`);
- **Auditable**: all rules, decisions, and changes are traced; users can go back at any time.

---

*GOAA · Applicability Boundary (author's statement) · Single version 1.0 · 2026-08-19 · boundaries = responsibility*
