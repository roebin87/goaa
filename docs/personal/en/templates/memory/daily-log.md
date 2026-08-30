# Daily Log Template

> **Purpose**: The daily log is the complete chronicle of system operation (one file per day · append-only, never delete). Distinction from soul backup: soul backup = organized day-end version (first & last of the day), log = continuous stream (appended every session).
> **Iron rule**: **Append-only, never delete**; every entry is knowledge capital; do not record transient information (search records / temporary paths), only content of lasting value.
> **Generation timing**: Append a log entry automatically at the end of every session; generate the soul backup at day-end wrap-up — in clear correspondence with the wrap-up five hooks; the two do not overlap in responsibility.
> **Location**: After deployment, place at `_Memory/history/日志/[实例名]/YYYY-MM-DD.md`
> **Generic template note**: This file is a self-bootstrap initialization template; it contains no runtime instance data; it is populated item by item by the onboarding flow (after deployment it becomes your system's own file).

---

# YYYY-MM-DD Log

## Session 1 (HH:MM-HH:MM)

| Time | Type | Content | Related path |
|------|------|------|---------|
| HH:MM | 【decision/execution/discussion/anomaly】 | 【key points】 | 【conversation record / soul backup / project file path】 |
| HH:MM | 【type】 | 【key points】 | 【path】 |

## Session 2 (HH:MM-HH:MM)

| Time | Type | Content | Related path |
|------|------|------|---------|
| HH:MM | 【type】 | 【key points】 | 【path】 |

(…continue appending for each session of the day…)

---

*【Instance name】 · Log · YYYY-MM-DD · append-only, never delete*
