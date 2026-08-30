# GOAA Framework Integration Examples
> **语义形态**：人语义（意图锚·概念解释·阅读）

> Integration examples showing GOAA as a governance substrate coexisting with mainstream enhanced-agent frameworks.

---

## Integration Overview

GOAA does not replace any enhanced framework — it coexists with them as a governance substrate:

| Framework | Position | Integration Pattern | Governance Strength | Example Path |
|------|---------|---------|---------|---------|
| **LangChain** | The most mainstream Python Agent framework | Rules-first + memory-last | **L1–L2** (prompt-injection + decision callback) | [`langchain/`](langchain/) |
| **CrewAI** | Multi-role collaboration framework | Multi-role rules foundation | **L2** (rules-first + callback) | [`crewai/`](crewai/) |
| **AutoGen** | Microsoft multi-agent dialogue framework | Governance + memory substrate | **L1–L2** (prompt-injection + callback) | [`autogen/`](autogen/) |

> **Governance strength is labeled to avoid misinterpretation**: all current integrations are **file-level governance** (rules read into the prompt + key-node callbacks) — enforcement relies on the model following the rules. A runtime-level interception (L3, planned) will provide stronger enforcement; see [governance strength levels](#governance-strength-levels) below.

---

## Governance Strength Levels

GOAA integrates at different enforcement strengths depending on the adapter. The level tells you **how strongly governance is enforced** — not how capable the framework is:

| Level | Mechanism | Enforcement | Status |
|-------|-----------|-------------|--------|
| **L1 · Prompt-injection** | GOAA rules/identity injected as system prompt | Relies on the model following the rules (soft) | ✅ Available (LangChain/AutoGen patterns) |
| **L2 · Rules-first + Decision callback** | Rules loaded before task; key nodes pause and submit to human adjudication | Rule coverage enforced by design; adjudication is human-closed-loop | ✅ Available (CrewAI + all three patterns) |
| **L3 · Runtime interception** | Seam-level interception at the execution substrate (planned runtime-governance adapter) | Physical enforcement independent of model compliance | 🚧 **Planned** (next exploration line · announced in README "Exploring") |

> **What this means for you**: L1–L2 integration is enough for governance-as-contract use (rules + memory + human adjudication). L3 runtime interception targets stronger enforcement scenarios and is part of GOAA's "runnable governance substrate" direction — progress will be announced via the paper and future releases.

---

## Common Integration Patterns

All framework integrations follow three patterns (usable alone or combined):

### Pattern 1: Rules-First
Before executing a task, the Agent reads GOAA's `constitution/basic_law.md` and `rules/rules.yaml`, then executes under rule constraints.

### Pattern 2: Memory-Last
After completing a task, the Agent writes outputs and processes into GOAA's `_Memory/` directory, incorporating them into GOAA's memory system.

### Pattern 3: Decision Callback
When the Agent hits a key node not covered by rules, it pauses execution and submits the options to the GOAA governance layer; it continues after the human side decides.

---

## What Each Example Contains

- `README.md`: integration guide, architecture diagram, minimal runnable example
- `minimal-example.py`: minimal runnable code
- `integration-guide.md`: integration steps, interface notes, FAQ

---

## Prerequisites

All integration examples require:
- Python 3.8+
- A GOAA workspace initialized (`python tools/init.py`)
- The corresponding framework Python SDK (`pip install langchain` / `pip install crewai` / `pip install pyautogen`)

---

## One-Line Summary

**GOAA provides the governance substrate for all enhanced frameworks — governance as the foundation + capabilities as add-ons = the optimal agent architecture direction.**

---

*GOAA Framework Integration Examples · Core Edition · 2026-08-28*
