# GOAA Framework Integration Examples
> **语义形态**：人语义（意图锚·概念解释·阅读）

> Integration examples showing GOAA as a governance substrate coexisting with mainstream enhanced-agent frameworks.

---

## Integration Overview

GOAA does not replace any enhanced framework — it coexists with them as a governance substrate:

| Framework | Position | Integration Pattern | Example Path |
|------|------|---------|---------|
| **LangChain** | The most mainstream Python Agent framework | Rules-first + memory-last | [`langchain/`](langchain/) |
| **CrewAI** | Multi-role collaboration framework | Multi-role rules foundation | [`crewai/`](crewai/) |
| **AutoGen** | Microsoft multi-agent dialogue framework | Governance + memory substrate | [`autogen/`](autogen/) |

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
