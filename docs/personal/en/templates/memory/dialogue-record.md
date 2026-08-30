# Conversation Record Template (A5 Verbatim Raw Transcript)

> **Purpose**: Conversation records are the **verbatim raw transcript** of each session (top-level survival-grade); never distill, never omit, never condense.
> **Iron rule**: **Verbatim** — no shrinking, no shifting responsibility (expressions like "per the chat platform" are prohibited; responsibility lies with the Agent, not the platform); the file header MUST carry the phrase "Verbatim raw transcript (A5 top-level survival-grade)"; content is presented turn by turn verbatim as "Owner: exact words / Agent: reply"; **write to disk progressively as the conversation happens** — never backfill all at once at wrap-up.
> **Completeness**: Tool calls, command executions, and file changes are core links of the full chain and must be recorded raw (see "Tools & File Operations" block); anomaly scenarios (interruption/error/failure/block) must be fully recorded.
> **Location**: After deployment, place at `_Memory/history/对话记录/YYYY-MM-DD_HHMM-HHMM.md` (one file per session; never merge, never overwrite).
> **Generic template note**: This file is a self-bootstrap initialization template; it contains no runtime instance data; it is populated item by item by the onboarding flow (after deployment it becomes your system's own file).

---

# Verbatim Raw Transcript (A5 Top-Level Survival-Grade)

- **Date**: YYYY-MM-DD
- **Time span**: HH:MM - HH:MM (Session 【N】 of the day)
- **Participants**: 【Owner name】 (human) ／ 【Instance name】 (Agent)
- **Record nature**: Verbatim raw transcript · never modify · never delete
- **Completeness check**: File hash: 【fill SHA-256】 ｜ Entries: 【N】 (paired with validator tamper-proof check)

## Full Conversation

### Turn 1
**Owner**: (verbatim exact words)

**Agent**: (verbatim reply)

### Turn 2
**Owner**: (verbatim exact words)

**Agent**: (verbatim reply)

(…continue appending, written to disk progressively as the conversation happens…)

## Tools & File Operations (full-chain trace)

| Time | Operation | Target | Result |
|------|------|------|------|
| HH:MM | 【command/tool/file change】 | 【path/object】 | 【success/failure/blocked】 |

## Anomaly Record

- 【conversation interruption/model error/execution failure/permission block etc. · time + description】

---

*【Instance name】 · Conversation Record · YYYY-MM-DD Session 【N】 · Verbatim raw transcript (A5 top-level survival-grade) · never to be modified or deleted*
