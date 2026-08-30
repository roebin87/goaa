# Workspace Directory Overview (template) — Single-Track Body Structure (V2.0)

> **Purpose**: this file is the directory-structure overview of the body (this workspace) — **single-track principle (2026-08-27 ruling): this workspace IS the body** · `constitution/` `rules/` `mechanisms/` etc. are the body layers; no second deployment copy.
> **vs V1.0**: V1.0 showed the dual-track "create a new second directory + copy components" layout — deprecated; single-track = the repo IS the body, and the onboarding script auto-creates `_Memory/` and `identity/`.
> **How to fill**: items inside `【】` are confirmed at deployment; body layers must not be missing (constitution/identity/memory).

---

# Workspace Directory Overview (single-track body)

> Body root: 【absolute path, e.g. C:/Users/<you>/zh or ~/GOAA/en】

## Directory tree

```
[Body root · this workspace]      # the downloaded en/ (or zh/) folder
├── README.md                     # Facade: why / features / quick start
├── AGENTS.md                     # AI collaboration spec (with wake hooks)
├── constitution/                 # Constitution layer (Basic Law + Design Principles · Why+How) 🔒read-only
├── rules/                        # Rules layer (what to write · classification/gate/rules.yaml) 🔒read-only
├── mechanisms/                   # Mechanisms layer (how to verify · startup/shutdown/onboarding) 🔒read-only
├── methodologies/                # Methodology layer (reusable cross-context methods) 🔒read-only
├── examples/                     # Examples (onboarding guide / project template) ✍️reference
├── tools/                        # Tools (validator) 🔒read-only
├── templates/                    # Templates (identity/ three files · memory/ five items) 🔒read-only
├── docs/                         # Docs (guides/concepts/comparison/exit guide) ✍️reference
├── identity/                     # Identity layer (auto-created at onboarding: three files + owner profile) 🔒read-only (owner-editable)
└── _Memory/                      # Memory layer (auto-created at onboarding · four sublayers)
    ├── distill/                  # Distillation (cross-session continuity core · overwrite) ✍️overwritable (backup first)
    ├── history/                  # Chronicle (soul backups / dialogue records / logs · append-only) 📌append-only
    ├── index/                    # Index (MEMORY index / sayings) ✍️overwritable
    └── snapshot/                 # Snapshot (optional · body-level snapshot) ✍️overwritable
```

> **Identity/Memory auto-initialization**: created automatically at first onboarding by `examples/activation/first-activation-guide.py` (`identity/` three files expanded from `templates/identity/` + `_Memory/` four layers) — no manual creation needed.

### Directory permission mapping (aligned with validator)

| Layer | Permission | Note |
|-------|-----------|------|
| `constitution`/`rules`/`mechanisms`/`methodologies`/`tools`/`templates`/identity | 🔒 read-only | System-level · agent cannot modify (requires owner instruction + trace) |
| `_Memory/history/` | 📌 append-only | Chronicle · never delete or modify |
| `_Memory/distill/`, `index/` | ✍️ overwritable | Backup before overwrite |
| `docs/`, `examples/` | ✍️ reference | Readable · changes recommended via contribution flow |

## Memory four-layer contract

| Layer | Content | Rule |
|-------|---------|------|
| Distillation | Cross-session continuity core | Overwrite at startup main load |
| Chronicle | Soul backups / dialogue records / logs | Append-only · never delete · survival-grade |
| Index | MEMORY / sayings | Index ≠ archive · precise info read source |

## Project workspaces (optional extension)

For multi-project use, create `projects/` under the body root (project four-piece set: full backup/distill/index/execution) — omit for single-instance use.

## Deployment checklist (after onboarding)

- [ ] Body tree complete (constitution/rules/mechanisms/methodologies/examples/tools/templates in place)
- [ ] `identity/` generated (three files + owner profile)
- [ ] `_Memory/` four layers created (distill/history/index/snapshot)
- [ ] `python3 tools/validator.py` → [PASS]
- [ ] `python3 tools/validator.py --memory` → [PASS] (first-time WARN acceptable)

---

*Workspace Directory Overview (Single-Track V2.0) · 2026-08-27 single-track ruling · this workspace IS the body*
