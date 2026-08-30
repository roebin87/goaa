# Lightweight Guide (trimming guide)
> **Semantics**: Human (intent/concept layer · reading)

> **Purpose**: the full structure serves full governance; this guide explains which directories/files can be trimmed on demand, so the architecture can both support full governance and adapt to personal-minimal/small-project scenarios.
> **Principle**: constitutional layer / identity layer / memory chronicle = not trimmable (governance bottom line); everything else trims by scenario.
> **Path view**: this document = **body view** (this workspace IS the body · single-track 2026-08-27) — `constitution/` `_Memory/` etc. are all relative to the body root (EN or ZH folder) · the repo IS the body.
> **Version**: Single version 1.0

---

## 1. Three-tier config

| Tier | Applies to | Keep | Trimmable |
|------|------|------|--------|
| **Full tier** | full governance · long-term running | everything | none |
| **Standard tier** (recommended) | personal primary use | constitution/identity/rules/mechanisms/memory/projects/production | `docs/` deep docs, `examples/`, `_Temp` can be omitted |
| **Minimal tier** | small projects · quick start | constitution (Basic Law) / identity (three files) / memory (distillation + chronicle) | `rules/` mechanism layer merged into IDENTITY notes, `methodologies/` can be added later |

## 2. Minimal-tier minimum set (runnable within ~10 files)

```
workspace/
├── identity/ (SOUL + IDENTITY + USER + Agent_Profile)
├── constitution/basic_law.md
├── _Memory/distill/ + history/
└── mechanisms/ (startup + shutdown is enough)
```

- distillation/chronicle formats follow the templates/memory templates;
- rules and mechanisms are first written into IDENTITY's notes section, then split out as the system grows.

## 3. Trimming discipline

1. **Run it through before trimming**: first deployment uses the standard tier; trim on demand only after it runs smoothly;
2. **Trimming never removes the bottom line**: constitution and the chronicle (append-only) are never trimmed;
3. **Trimming leaves a trace**: record what was trimmed in the change log so it can be restored later.

---

*【System name】 · Lightweight Guide · Single version 1.0*
