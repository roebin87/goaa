# Contributing Guide

> **Core stable, periphery iterative** — the architecture core (constitution/rules/core mechanisms) maintains major version stability to ensure deterministic governance; the periphery ecosystem iterates rapidly and welcomes community contribution. Any contribution that makes GOAA easier to use is welcome.

## Contribution Categories & Acceptance

| Level | Type | Description | Handling |
|-------|------|-------------|----------|
| ✅ **Welcome** | Doc fixes/additions | Typos, wording improvements, doc additions, FAQ updates | Merge anytime |
| ✅ **Welcome** | Examples/cases | Scenario landing examples, end-to-end cases, best practices | Merge anytime |
| ✅ **Welcome** | Translations | English/other language version additions, translation improvements | Merge anytime |
| ✅ **Welcome** | Template improvements | Identity/memory/workspace template improvements | Merge after review |
| ✅ **Welcome** | Tool scripts | Validator, init scripts, auxiliary tool improvements | Merge after review |
| ✅ **Welcome** | Bug fixes | Tool script, doc link, config error fixes | Merge anytime |
| ⚠️ **Review required** | Peripheral mechanism improvements | Non-core mechanism optimizations under mechanisms/ | Design review required, with improvement notes |
| ⚠️ **Review required** | Core mechanism changes | Changes to constitution/, core mechanisms/ | Design review process required, with design doc |
| ⚠️ **Review required** | Constitution/axiom changes | Changes to basic_law.md, design-principles.md | Author final review required, with full argumentation |
| ❌ **Not accepted** | Violates core design principles | Changes violating "100% human decision rights", "file ontology", "governance-oriented" | Closed directly |
| ❌ **Not accepted** | Auto-merge rules | Any CI auto-merge configuration | Closed directly (merges require human final review) |

## Issues

- Title: `[category] short description` (category: concept / bug / doc / question / enhancement)
- Body should include:
  - Your usage scenario (have you actually run GOAA?)
  - Problem description / concept discussion point
  - Expected vs actual behavior
- **Good first issue**: Issues tagged with this label are suitable for new contributors, typically low-barrier tasks like doc fixes, example additions, small tool optimizations.

## Pull Requests

- Branch naming: `fix/` `docs/` `feat/` prefix
- Change description: what changed, why, how it was verified
- Core design changes (constitution/, core mechanisms/) please open an Issue for discussion first, with design doc, before submitting PR
- All PRs must pass CI checks (validator.py) and be merged after author's manual final review — **no auto-merge rules**

### Open Peripheral Contribution List (PRs welcome)

| Category | Content | Examples |
|----------|---------|----------|
| Examples | Scenario landing examples | Personal creator / small team / compliance scenarios |
| Adapters | Startup scripts for different models/platforms | Claude/ChatGPT/local-model deployment scripts |
| Tutorials | Usage tutorials / best practices | Obsidian/VS Code guides |
| Translations | File English/other-language versions | `.en.md` additions |
| Integrations | Mounting external execution frameworks | LangGraph/dsh mounting examples |
| Docs | Documentation fixes/additions | Typos/example corrections |

> Peripheral contributions do not touch the architecture core and do not violate core design principles — any peripheral artifact that makes GOAA more usable is welcome.

### Contributor Growth Path

1. **Doc contributor** → Fixes, adds docs, translates
2. **Example contributor** → Submits landing examples, best practices
3. **Tool contributor** → Optimizes validator, develops auxiliary scripts
4. **Mechanism contributor** → Participates in peripheral mechanism improvements (review required)
5. **Core maintainer** → Participates in core design reviews (author invitation only)

### Contributor Recognition

- All merged PR contributors will be listed in the README contributors section
- Major contributions (new mechanisms, complete example series, important tools) will be noted separately with contribution details
- Annual active contributors will be acknowledged in the project annual summary

### Community Governance Terms (added 2026-08-26, updated 2026-08-28)

1. **Merges require human final review**: all code and documentation merges require the author's manual final review — **no auto-merge rules** (CI runs checks only; never auto-merges);
2. **Third-party derivative labeling**: derivative projects based on this repository must be labeled "unofficial version" and **must not use the official branding/name** (to avoid confusion with the official repo);
3. **DCO (Developer Certificate of Origin)**: all contributors confirm their content is original when submitting · contributions must stay consistent with core design principles (not violating the design spirit of constitution layer / rules layer / core mechanisms).

## Concept Discussions

- Open in Discussions with the `concept` tag
- The author replies; core design changes require the design review process

---

*GOAA · Contributing Guide · Core stable version 1.0 · Created 2026-08-19 · Updated 2026-08-28 to core stable + periphery iterative*
