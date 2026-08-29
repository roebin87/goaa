# 05 · GOAA Neural Flow Stereo Operation Diagram (Simplified)

> This document uses simplified flowcharts to show GOAA system's core operation logic. This is a simplified version; full internal operation diagram is not yet public.

## 1. System Overview

GOAA system operation consists of four core loops, interwoven, jointly maintaining system orderly operation:

```
Startup Sequence → Runtime Loop → Shutdown Sequence → Adjudication Loop
     ↑                                                        │
     └────────────────────────────────────────────────────────┘
                   (next day startup, cycle repeats)
```

## 2. Startup Sequence

**Goal**: Recover system state from file system, ensure governance precedes execution.

```
Step 0 · Locate Body
  → Confirm workspace absolute path → verify directory structure → record body path
Step 1 · Read Constitution (rules first)
  → basic_law.md (mandatory) + design-principles.md (Why+How)
Step 2 · Read Identity (who am I + who is owner)
  → SOUL.md + IDENTITY.md + USER.md + owner-profile.md (machine read-only)
Step 3 · Read Distill (essence of last session)
  → _Memory/distill/ (latest distill · decision consensus · todos)
Step 4 · Run Startup Sequence (mechanisms/startup.md)
  → instruction dual-check + check-in + validator self-check
Step 5 · Memory Validation (validator.py --memory)
  → Ready: respond to owner instructions
```

**Startup principles**: Constitution before identity, identity before memory, memory before execution. Any failure stops and reports. First activation triggers onboarding if owner profile doesn't exist.

## 3. Runtime Loop

**Goal**: Execute owner instructions under governance constraints, ensure execution controllable and traceable.

```
Owner instruction input
  → Instruction Dual-Check (human intent vs machine execution)
    → Inconsistent → Ambiguity revelation → Submit to Adjudication Loop
    → Consistent → Continue
  → Rule Validation (scan rules/ relevant rules)
    → Violates rule → Refuse execution + prompt + submit adjudication
    → Complies → Continue
  → Execution (AI executes instruction · multi-role collaboration · external tools · file operations)
    → Execution process real-time recorded to History layer (append-only)
  → Result Validation (does execution result match expectation?)
    → Doesn't match → Ambiguity revelation/error detection → Submit adjudication
    → Matches → Continue
  → Result returned to owner → Wait for next instruction (cycle repeats)
```

**Runtime principles**: Every instruction passes dual-check + rule validation, not direct execution. Execution process real-time recorded, ensuring traceability. Exceptions automatically revealed, submitted to adjudication loop, not silent failure.

## 4. Shutdown Sequence

**Goal**: Precipitate session results into system assets, ensure memory not lost, consensus not decayed.

```
Shutdown trigger (owner says "shutdown"/session ends/scheduled)
  → Hook 1 · Soul Backup (backup identity/ + constitution/ to _Memory/history/)
  → Hook 2 · Distill (AI generates session essence → owner confirms → write _Memory/distill/)
  → Hook 3 · Log (record session operation log to _Memory/history/log/)
  → Hook 4 · Analects (record important decisions/consensus to _Memory/history/analects/ · append-only)
  → Hook 5 · Shutdown Report (generate report on memory changes/pending adjudication/next startup key points)
  → Shutdown complete: system state precipitated, next startup recovers from distill layer
```

**Shutdown principles**: Five hooks must all execute, no skipping. Distill must be owner-confirmed, not AI self-decided. History layer append-only, ensuring history traceable.

## 5. Adjudication Loop

**Goal**: Govern ambiguity, conflict, and lag through normalized human adjudication, ensure system orderly evolution.

```
Ambiguity/conflict/lag revealed (from runtime loop or startup sequence)
  → Localization (locate root and layer: human semantic/machine semantic/rules/governance)
  → AI Analysis (submit analysis report: problem description/options/suggestions/impact assessment)
  → Human Adjudication (owner final decision: adopt/modify/reject/defer · human holds 100% final decision rights)
  → Consolidation (adjudication results solidified as system assets)
    → New rules → rules/ (after effect gate four checks)
    → Decision consensus → _Memory/distill/ (loaded next startup)
    → Important decisions → _Memory/history/analects/ (permanent record)
    → Constitution updates → constitution/ (after design review)
  → Retirement (if needed: obsolete rules/consensus → archive → index update → distill update)
    → Non-additive principle: new rules must prove "problems will occur without adding"
  → Adjudication complete: system order increased (negentropy injection) → Back to runtime loop
```

**Adjudication principles**: Human adjudication is fixed环节 of rules layer, not exception fallback. Adjudication targets rules/consensus/versions (low-frequency high-value), not every action. Adjudication results must be consolidated, otherwise equals no adjudication. Consolidation must pass effect gate, not casually written.

## 6. Four-Loop Interweaving Relationship

```
Timeline →

Startup → Runtime Loop ───────────────────────→ Shutdown
             │  │                                  │
             │  └─ Exception revealed → Adjudication →│ (adjudication results consolidated)
             │                                     │
             └─────────────────────────────────────┘ (normal execution)

Next day startup: recover from distill layer (previous day's adjudication results already consolidated)
```

**Key insight**: Startup/runtime/shutdown are **daily loops** (once per day). Adjudication is **event-driven loop** (triggered by exceptions, not scheduled). Four loops share the same file system (entropy sink); all states precipitate into files. Next day startup, previous day's adjudication results already consolidated in distill layer, directly loaded and effective.

---

*GOAA · Neural Flow Stereo Operation Diagram (Simplified) · Based on academic paper DOI:10.5281/zenodo.22165301 and mechanism documents · Full internal operation diagram not yet public · 2026-08-28*
