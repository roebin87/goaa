# STRUCTURE.md · GOAA Repository Structure

> **One look tells you where things live.** GOAA separates documentation from code, and versions from languages — no `-zh` pseudo-versions, no docs scattered inside code directories.

---

## Top-Level Layout

```
goaa/
├── README.md / README-zh.md      # Entry (EN default · ZH link) — version picker
├── CHANGELOG(.md/-zh.md)          # Version history
├── CONTRIBUTING(.md/-zh.md)       # Contribution guide (falsification-first)
├── RELEASE-NOTES-v0.1.0.md        # v0.1.0 release notes
├── LICENSE · CITATION.cff · VERSION · CODE_OF_CONDUCT.md · SECURITY.md
├── docs/                          # ALL documentation (versions × languages)
│   ├── lite/{en,zh}/              #   Lite release docs (introductory · 15 files)
│   ├── personal/{en,zh}/          #   Personal release docs (standard · full set)
│   └── core/{en,zh}/              #   Core release extensions (paper · case studies · falsification)
├── tools/                         # Verification code (validator · verify-ownership · shutdown · rule-conflict)
├── integrations/                  # Framework integrations (LangChain · CrewAI · AutoGen)
├── examples/                      # End-to-end examples & templates
├── plugins/                       # Optional plugins (memory-vector)
└── assets/                        # Images · logos
```

## The Two Axes

| Axis | How it is expressed |
|---|---|
| **Version** (Lite ⊂ Personal ⊂ Core) | `docs/lite/` → `docs/personal/` → `docs/core/` — each adds documents, never rewrites |
| **Language** (en · zh) | every version has `en/` (English) and `zh/` (Chinese) copies |

**Content lives once.** Documents exist only in their version's area — `personal/` holds the standard full set, `core/` holds only the Core extensions (paper, case studies, falsification, compatibility, known-limits, version-policy, dual-chain nav 06). Shared code (tools/integrations/examples/plugins) lives once at the repo root.

## Release Packaging Map

| Release | Files |
|---|---|
| **Lite** (15) | `docs/lite/en` + `docs/lite/zh` + `tools/verify-ownership.py` + LICENSE/CITATION/README |
| **Personal** (154) | `docs/personal/en` + `docs/personal/zh` + `tools/` + `examples/` + `plugins/` + root meta |
| **Core** (181) | Personal + `docs/core/en` + `docs/core/zh` + `integrations/` |

The strict subset relation (Lite ⊂ Personal ⊂ Core) is preserved at the file-list level; Lite documents are the introductory variants, Personal/Core share identical document content where the same file appears.

## Why This Structure

- **No `-zh` pseudo-versions** — language is a sub-directory, not a version;
- **Documents have one entrance** (`docs/`) — find a document by release, then by language;
- **Code has one home** (root-level `tools/` · `integrations/` · `examples/` · `plugins/`) — no code copies inside each edition;
- **One content, one place** — fixing a term means editing the file once per language, not per version × language.

---

*GOAA · STRUCTURE.md · v0.1.0 · 2026-08-31（目录结构规范化·方案一落地）*
