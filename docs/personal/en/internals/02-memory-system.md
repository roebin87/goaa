# 02 · GOAA Four-Layer Memory System Working Principles
> **Semantics**: Machine (mechanism/translation layer · How)

> This document publishes the design principles and workflows of GOAA's four-layer memory system.

## 1. Why Four-Layer Memory

AI models have no persistent memory — context is lost when each conversation ends. GOAA builds a four-layer memory system through the file system to solve "AI can't remember."

**Memory is not just storage; it's a governance tool.** GOAA's memory system serves three governance functions (see Section 3).

## 2. Four-Layer Division and Data Flow

```
Layer 1 · History (append-only) — _Memory/history/ — full conversation records + logs + analects
Layer 2 · Snapshot (auto-generated per session) — _Memory/snapshot/ — complete state at session end
Layer 3 · Index (auto-maintained) — _Memory/index/ — keyword/topic/time/rule reference indexes
Layer 4 · Distill (AI-generated, human-confirmed) — _Memory/distill/ — essence/decision consensus/todos/rule changes
```

**Data flow**: During conversation → History appends in real-time. At shutdown → Snapshot generated + Index updated + Distill generated (AI) → confirmed by human → saved. Next startup → Light load distill (essence) + Deep load on demand (via index → history/snapshot).

## 3. Three Memory Governance Functions

### 3.1 Anchoring Against Decay
**Problem**: AI model context decays — longer conversations, earlier rules/agreements more likely forgotten.
**Solution**: Distill layer light-loaded at every startup, re-injecting core rules, decision consensus, key memories into context.
**Effect**: Cured rules show no cross-session decay (contrasting Liu 2026's reported 94%→61% decay without governance).

### 3.2 Cognitive Gatekeeping
**Problem**: Not all memory worth loading — irrelevant info consumes context, distracts judgment.
**Solution**: Distill layer is human-confirmed "essence"; only distill loaded at startup. Details retrieved on demand via index.
**Effect**: Context space occupied by high-value info; low-value info doesn't distract.

### 3.3 Compute Focusing
**Problem**: Loading full memory every startup consumes massive tokens (compute = cost).
**Solution**: Startup only loads distill (essence, usually few thousand tokens). Details retrieved on demand (may be tens of thousands).
**Effect**: Daily running cost extremely low (startup only few thousand tokens); more only when回溯 needed.

## 4. Memory Loading Strategy

**Startup light load**: Constitution → Identity → Distill (latest) → Index summary. Does NOT load full history or snapshots.

**On-demand deep load**: When owner or AI needs historical details → search index by keyword/topic/time → locate specific files in history/snapshot → read relevant segments (not all).

## 5. Shutdown Five Hooks

Every session end (shutdown) must execute five hooks:
1. **Soul backup**: Backup identity/ and constitution/ to _Memory/history/
2. **Distill**: AI generates session essence → human confirms → write to _Memory/distill/
3. **Log**: Record session operation log to _Memory/history/
4. **Analects**: Record important decisions and consensus to _Memory/history/analects/
5. **Shutdown report**: Generate report on memory changes this session

---

*GOAA · Four-Layer Memory System · Based on academic paper DOI:10.5281/zenodo.22165301 · 2026-08-28*
