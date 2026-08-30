# Framework Integration Guide

> This guide explains how to use GOAA as a **governance base layer** alongside mainstream enhancement agent frameworks. The integration examples (`integrations/`) are **minimal runnable** demos — proving that "governance base + capability plugin" can coexist and run together.

---

## 1. Generic integration in three steps

All framework integrations follow the same pattern (usable individually or in combination):

| Step | Action | Pattern |
|------|--------|---------|
| **1. Rules first** | Before executing a task, the agent reads GOAA's `constitution/basic_law.md` and `rules/rules.yaml`, and executes under rule constraints | Pattern 1 |
| **2. Memory after** | After completing a task, the agent writes outputs and process into GOAA's `_Memory/` directory, incorporating them into the memory system | Pattern 2 |
| **3. Decision callback** | When the agent hits a critical node not covered by rules, it pauses, presents options to the GOAA governance layer, and continues after human adjudication | Pattern 3 |

---

## 2. Interface reference

| Interface | Path (relative to workspace root) | Description |
|-----------|----------------------------------|-------------|
| Core principles | `constitution/basic_law.md` | Rule base for the agent's system prompt |
| Rule configuration | `rules/rules.yaml` | Machine-readable rule list (checkable by the validator) |
| Role rules | `mechanisms/multi-role.md` | Multi-role division definitions (controller/editor/executor/reviewer) |
| Memory write | `_Memory/history/` | Task outputs and process persisted to disk |
| Pending decisions | `_Memory/unresolved/` | Items awaiting human adjudication (decision callback landing point) |

---

## 3. Running and verifying

```bash
# 1. Initialize the GOAA workspace (first time)
python tools/init.py

# 2. Run an integration example (langchain as example)
cd integrations/langchain
python minimal-example.py

# 3. Verify the governance chain
#    - Rules loaded (agent output complies with basic law/rules)
#    - Memory persisted (task records generated under _Memory/history/)
#    - Decision callback works (pauses at points not covered by rules, waits for human adjudication)
```

> **Minimal integration = argument**: a successfully running example proves the GOAA governance layer can coexist with the framework — deep coupling is not required. The governance base's value lies in **constraint, traceability, and adjudication** — not in replacing execution capability.

---

## 4. FAQ

| Question | Answer |
|----------|--------|
| **Will GOAA replace my framework?** | No. GOAA is a governance base layer; it does not replace any enhancement framework (see [compatibility proof](../docs/core/en/compatibility.md)) |
| **Do I need to modify framework code?** | No. Integration happens only at three interface points: "read rules + write memory + callback for adjudication" |
| **Why are the examples so small?** | Minimal integration focuses on proving "it runs"; business capability comes from the framework itself |
| **How do roles map?** | GOAA's four roles (controller/editor/executor/reviewer) can map to a framework's multi-agent definitions (e.g. CrewAI agent roles) |

---

*GOAA · Framework Integration Guide · Genericized translation · 2026-08-29 · v0.1.0*
