<p align="center">
  <img src="assets/logos/GOAA.png" alt="GOAA" width="260">
</p>

# GOAA v0.1.0 — Governance-Oriented Agent Architecture, First Open-Source Release
> **语义形态**：人语义（意图锚·概念解释·阅读）

**Make AI governable. Keep memory yours. Order in collaboration.**

GOAA (Governance-Oriented Agent Architecture) is a governance-oriented agent architecture — not about making AI *smarter*, but about making AI *more governable, more controllable, and more yours*. Mainstream agent frameworks solve "how to make AI work"; GOAA solves "how to make AI reliably governable": governance is the foundation, execution is the add-on.

This release is the **generic open-source master copy v0.1.0** of GOAA 2.0 (GOSAA), shipping three releases simultaneously — from beginner to research.

## Three Releases (Strict Subset: Lite ⊂ Personal ⊂ Core)

| Release | Position | Files | For whom | Core proof action |
|---|---|---|---|---|
| 🟢 Lite | Beginner (15 files) | 15 | Complete non-technical beginners | 5-minute verification "your memory belongs to you" |
| 🟡 Personal | Personal productivity (154 files · incl. bilingual) | 154 | AI-experienced creators/small teams | Multi-role collaboration + memory plugin + end-to-end evidence |
| 🔴 Core | All-outcomes open source (181 files · incl. bilingual) | 181 | Developers/architecture researchers/industry | Academic paper + case studies + framework integrations + falsification mechanism |

All three releases include Chinese-English bilingual content (`en/` mirrors); upgrading means enabling more functional layers, not starting over.

## Core Mechanisms

- **Governance-oriented architecture**: define the governance boundary first, then carry execution capabilities;
- **100% human decision authority (decision backstop)**: sovereignty stays with the human, execution is delegable — key nodes (rule activation/consensus solidification/version iteration) are adjudicated by the human, routine matters are authorized for AI to execute within mechanisms; the human-machine collaboration iterates itself, continuously lowering human-side decision cost;
- **File-system-level governance carrier**: rules and memory are anchored to physical file properties (permissions/traces/persistence), carried in Markdown — human-readable, machine-parseable, broadly accessible;
- **Regular human-adjudication loop**: fixed adjudication stages in the rule layer and consensus layer (not exception fallback);
- **Dual-source entropy governance**: a unified governance framework for technical entropy and cognitive entropy;
- **Structural cost advantage** (token × request dual benchmark): full-window cache hit rate 98.26% (Aug-period/peak-day 98.5-98.6%; industry typical 60-80%) · zero orchestration overhead · context bloat banned by design · lowest-tier model works. Methodology: 39 days of production (2026-07-16 to 08-29), WorkBuddy platform · deepseek models · consumer-grade PC (no GPU) — see paper §8.2 (DOI: 10.5281/zenodo.22165301).

## Quick Start

1. Download the `lite/` (or `personal/` / `core/`) folder
2. Set it as the workspace in your AI assistant (WorkBuddy / Claude Code / Cursor or other local substrate)
3. Say "hello" — the AI enters activation onboarding automatically, creating your dedicated AI companion in ~5 minutes
4. Run `python3 tools/verify-ownership.py` and see 5 ✅ — your memory belongs to you, verifiable

## Falsification Entry

**We don't ask you to believe; we ask you to falsify.** A pre-registered disclosure list (known limitations and unverified claims) is public; any fact-based objection will be recorded and publicly responded to.

## Citation

Use `CITATION.cff` (DOI: `10.5281/zenodo.22165301`) · License Apache-2.0.

## Version Commitment

- **Open & principled (finalized 2026-08-29 · Option 3)**: the code is fully open and evolves with social verification; the three core principles (data sovereignty / 100% human decision / governance first) are prudently upheld — any future change requires a change proposal + the author's final adjudication with full argumentation. See [version policy](docs/core/en/version-policy.md).
- **Core mechanisms stay undisclosed** (this repo = generic open-source master copy · no personal config / runtime memory / project assets).
- **Peripheral ecosystem open for contribution** (see CONTRIBUTING).

---

*GOAA v0.1.0 · Released 2026-08-30*  
*Make AI governable. Keep memory yours. Order in collaboration.*