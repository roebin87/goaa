# Changelog

All notable changes are recorded in this file. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow Semantic Versioning.

## [Unreleased]

### Changed · Repository Structure Normalized (docs-centric · 2026-08-31)

- **Documentation centralized** under `docs/` — three releases × two languages: `docs/lite/{en,zh}/` · `docs/personal/{en,zh}/` · `docs/core/{en,zh}/` (replaces the six flat `core/`·`core-zh/`·`personal/`·`personal-zh/`·`lite/`·`lite-zh/` directories);
- **Language de-masked**: `-zh` pseudo-versions removed — language is now a sub-directory (`en/` / `zh/`), not a version;
- **Code separated from docs**: `tools/` · `integrations/` · `examples/` · `plugins/` live once at the repo root (no per-edition copies);
- **Deduplicated content**: Personal and Core shared documents now exist once (Core keeps only its extensions: paper · case studies · falsification · known-limits · compatibility · version-policy); repo file count 362 → 212;
- **Root-level meta unified**: single `LICENSE` · `CITATION.cff` · `VERSION` · `CONTRIBUTING` · `CODE_OF_CONDUCT.md` · `SECURITY.md`; new `STRUCTURE.md` describes the layout;
- **Scripts/CI adapted**: `tools/validator.py` and `tools/verify-ownership.py` paths updated (run at repo root) · CI self-check runs both scripts at root.

## [v0.1.0] - 2026-08-29

### First Release · GOAA Three Releases

GOAA (Governance-Oriented Agent Architecture) v0.1.0 official release — governance as the foundation, capabilities as add-ons.

#### Added

- **Three-release architecture** (strict subsets Lite ⊂ Personal ⊂ Core · 0 missing):
  - **Lite (Beginner)** · 15 files — 5-minute verification "your memory belongs to you" · ownership verification 5 ✅
  - **Personal (Productivity)** · 154 files (incl. bilingual) — multi-role collaboration mechanism + memory-vector plugin + 3 end-to-end examples
  - **Core (All-outcomes)** · 181 files (incl. bilingual) — academic paper entry + full dual-chain navigation + framework integration examples (LangChain/CrewAI/AutoGen) + governance case studies + falsification registry + pre-registered disclosure list + compatibility proof + version policy statement
- **EN mirror**: core docs bilingual (concepts/constitution/mechanisms/docs core)
- **Falsification mechanism**: `docs/falsification-log.md` (9-field registry) + `docs/known-limits.md` (5-dimension pre-registered disclosure list)
- **Honesty by design**: verify-ownership.py 5 automated + 2 manual checks · memory-vector plugin zero-dependency dual index · graceful degradation without endpoints

#### Docs

- Root README (repo facade · three-release navigation · decision tree · falsification entry)
- Release notes RELEASE-NOTES (GitHub Release body source)

#### Known Limitations

Full list in [docs/known-limits.md](docs/core/en/known-limits.md). Highlights:

- Core claims (e.g. 100% human decision lowers total cost) are mainly supported by theoretical argument + case studies; strict controlled experiments await the academic line
- Framework integration examples are minimal runnable demos (prove integrability, not production-grade performance comparisons)
- Community ecosystem starts from zero; social validation (3.0 generation) awaits community questioning and validation
