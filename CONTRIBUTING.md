# Contributing to GOAA

> **Core stable, periphery iterates** — the architecture core (constitution/rules/core mechanisms) stays stable at the major version to ensure the governance substrate's determinism; the peripheral ecosystem iterates quickly, and community contributions are welcome. Thanks for any contribution that makes GOAA easier to use.

The GOAA repository consists of **three releases** — please identify your target before contributing:

| Release | Position | Note |
|------|------|------|
| 🟢 `lite/` | Beginner | Minimal usable · ownership verification (5-minute start) · for complete non-technical beginners |
| 🟡 `personal/` | Personal productivity | Multi-role collaboration + memory plugin + end-to-end evidence · for creators/small teams |
| 🔴 `core/` | All-outcomes open source | Academic paper entry + case studies + framework integrations + falsification mechanism · for developers/researchers |
| 📄 Root layer | Repository facade | README / CONTRIBUTING / CI / templates / license and other repo-wide public files |

> The three releases are **strict subsets** (Lite ⊂ Personal ⊂ Core): improvements contributed to a lower level naturally benefit higher levels; the reverse requires consistency care.

## Contribution Categories & Acceptance Scope

| Level | Type | Note | Handling |
|------|------|------|---------|
| ✅ **Welcome** | Doc fixes/supplements | typos, wording polish, doc supplements, FAQ updates | merge anytime |
| ✅ **Welcome** | Examples/case studies | scenario examples, end-to-end cases, best practices | merge anytime |
| ✅ **Welcome** | Translations | EN/other-language supplements, translation polish | merge anytime |
| ✅ **Welcome** | Template improvements | identity/memory/workspace template improvements | merge after review |
| ✅ **Welcome** | Tooling scripts | validator, init script, auxiliary tool improvements | merge after review |
| ✅ **Welcome** | Bug fixes | tool scripts, doc links, config errors | merge anytime |
| ⚠️ **Review needed** | Peripheral mechanism improvements | non-core mechanism optimizations under `mechanisms/` | design review + improvement note |
| ⚠️ **Review needed** | Core mechanism changes | changes to `constitution/`, core `mechanisms/` | design review process + design doc |
| ⚠️ **Review needed** | Constitution/axiom changes | changes to `basic_law.md`, `design-principles.md` | author final review + full argumentation |
| ❌ **Not accepted** | Violating core design principles | changes violating "data sovereignty / 100% human decision / governance first" | closed directly |
| ❌ **Not accepted** | Auto-merge rules | any CI auto-merge configuration | closed directly (merges require human final review) |

## Falsification Entry (The Contribution GOAA Values Most)

**We don't ask you to believe; we ask you to falsify.** If you believe GOAA's theory or claims are problematic, submit an Issue using the [falsification/question template](.github/ISSUE_TEMPLATE/falsification.md):

1. First read the [pre-registered disclosure list](core/docs/known-limits.md) — known limitations and unverified claims are already public
2. Submit an Issue describing your objection (**please attach factual evidence**)
3. Your objection will be recorded in the [falsification log](core/docs/falsification-log.md) and publicly responded to

**Every fact-based objection is an opportunity for GOAA's theory to advance.**

## Issues

- Title: `[category] brief summary` (category: concept / bug / doc / question / enhancement / falsification)
- Body should include:
  - Your use scenario (whether you actually ran GOAA)
  - Problem description / concept discussion point
  - Your expectation vs. what actually happened
- **Good first issue**: issues with this label suit new contributors — usually low-barrier tasks like doc fixes, example supplements, small tool improvements.
- Bug reports: use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md).

## Pull Requests

- Branch naming: `fix/` `docs/` `feat/` prefix
- Change description should cover: what changed, why, how it was verified
- Core design changes (`constitution/`, core `mechanisms/`): open an Issue to discuss first, attach a design doc, then submit the PR
- All PRs must pass CI validation (three-release self-check: `verify-ownership.py` + `validator.py`) and the author's human final review before merging — **no auto-merge rules are allowed**

### Open List of Peripheral Contributions (PRs Welcome)

| Category | Content | Examples |
|------|------|------|
| Examples | scenario landing examples | creator/small-team/compliance scenario examples |
| Adaptations | startup scripts for different models/platforms | local-model deployment scripts, framework mounting examples |
| Tutorials | usage guides/best practices | Obsidian/VS Code guides |
| Translations | EN/other-language versions of files | `-en` counterparts |
| Integrations | mounting external execution frameworks | LangChain/AutoGen/CrewAI mounting examples |
| Docs | doc fixes/supplements | typo/example corrections |

> Peripheral contributions don't touch the architecture core and don't violate core design principles — any peripheral that makes GOAA more usable is welcome.

### Contributor Growth Path

1. **Doc contributor** → fixes, doc supplements, translations
2. **Example contributor** → landing examples, best practices
3. **Tooling contributor** → validator optimizations, auxiliary scripts
4. **Mechanism contributor** → peripheral mechanism improvements (review required)
5. **Core maintainer** → core design review (author invitation)

### Contributor Recognition

- All merged PR contributors are listed in the README contributor list
- Significant contributions (new mechanisms, full example series, important tools) get individually noted in the contributor list
- Annual active contributors are acknowledged in the project's yearly summary

## Community Governance Terms

1. **Merges require human final review**: all code and doc merges require the author's human final review — **no auto-merge rules are allowed** (CI only validates; it never auto-merges);
2. **Third-party derivation labeling**: derived projects must be labeled "unofficial" · **must not use official logos/names** (to avoid confusion with the official repo); the "GOAA" name belongs to the author Jianlong Yin — modified versions violating core principles (data sovereignty / 100% human decision / governance first) may not use the GOAA name;
3. **DCO originality declaration**: all contributors confirm their content is original when submitting (Developer Certificate of Origin) · contributions must align with core design principles (not violating the design spirit of the constitution/rule/core-mechanism layers).

## Concept Discussions

- Start them in Discussions with the `concept` label
- The author responds; core design changes require the design-review process

---

*GOAA · Contribution Guide (Root Layer) · 2026-08-30 · aligned with the three-release structure and the falsification orientation*
