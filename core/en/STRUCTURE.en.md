# GOAA Open-Source Project · Project Structure Guide (Final · External Review Entry)

> **🔴 Role (set by author, 2026-08-19)**: This file is the **whole-project structure guide** — the **first entry for external review**. External reviewers (human/AI) can judge the project structure from this single file, without digging into internals.
> **🔴 Sync rule**: This file MUST always match the actual project structure — every step updates its status column (✅ done / 🟡 pending). The structure landing uses this file as the single comparison baseline.
> **Version**: Single version 1.0 | **Status**: structure finalized, content being written chapter by chapter | **Authority**: same layer as README — README = facade (thin), this file = structural truth (thick).

---

## 1. One-Line Positioning

GOAA is the 2.0 engineering form of the GOAA governance-oriented agent architecture — **it does not solve "how to make AI work", it solves "how to make AI work controllably"**: humans hold 100% decision rights, files = memory & rules carrier, three-semantics disambiguates.

## 2. Complete Structure Tree (one-to-one with actual)

```
GOAA/
├── README.md              # Facade: why/features/quick entry (thin)    ✅
├── README.en.md           # English facade                            ✅
├── LICENSE                # Apache-2.0                                ✅
├── DEPLOY.md              # ★ Self-bootstrap deployment (copy to any AI) ✅
├── AGENTS.md              # AI collaboration guidelines               ✅
├── CONTRIBUTING.md        # Contribution guide                        ✅
├── BENCHMARK.md           # Running benchmarks (architecture = measurable) ✅
├── SECURITY.md            # Security policy (confidential disclosure) ✅
├── CODE_OF_CONDUCT.md     # Community code of conduct                 ✅
├── CITATION.cff           # Citation format (academic entry)          ✅
├── STRUCTURE.md           # This file = external review first entry  ✅
├── STRUCTURE.en.md        # This file (English)                      ✅
│
├── constitution/          # L0 Constitution layer (L0 of five-level)
│   ├── basic_law.md        # Basic Law (mother axiom/survival/operational/generations) ✅
│   └── design-principles.md # Design principles (Why+How merged · axiom rationale + method) ✅
│
├── rules/                 # Rules layer (what to write · rules side of rules-mechanisms separation)
│   ├── classification.md   # Five-level classification                ✅
│   ├── validation.md       # Rule Effect-Gate (written ≠ effective)   ✅
│   └── rules.yaml          # ★ Programming-semantics instance (validator-checkable) ✅
│
├── mechanisms/            # Mechanisms layer (how to verify · mechanisms side of separation)
│   ├── startup.md          # Startup sequence                         ✅
│   ├── shutdown.md         # Wrap-up five-hooks                       ✅
│   ├── onboarding.md       # First activation onboarding              ✅
│   ├── problem-gate.md     # Problem gate (true-problem entry)        ✅
│   ├── ambiguity-governance.md  # Ambiguity governance                ✅
│   ├── memory-loading.md   # Memory loading rules (load/recall/threshold/archive/anti-tamper) ✅
│   ├── reuse.md            # Reuse mechanism                          ✅
│   └── dynamic-rates.md    # Dynamic rates monitoring                 ✅
│
├── methodologies/         # Methodologies (reusable assets · method points + mechanism pointers)
│   ├── methodology-01-true-problem.md        # True-problem judgment (pointer → problem-gate) ✅
│   ├── methodology-02-ambiguity-resolution.md # Ambiguity resolution (pointer → ambiguity-governance) ✅
│   └── methodology-03-dynamic-rates.md       # Dynamic rates design (pointer → dynamic-rates) ✅
│
├── templates/             # ★ Runtime templates (copied at deployment · bootstrap gap)
│   ├── workspace-structure.md   # Workspace directory overview       ✅
│   ├── identity/                # Identity templates (system three files + profile)
│   │   ├── Agent_Profile.md     # Identity profile template           ✅
│   │   ├── SOUL.md              # Behavior baseline (three-file one)  ✅
│   │   ├── IDENTITY.md          # Architecture map (three-file two)   ✅
│   │   └── USER.md              # Owner profile (three-file three)    ✅
│   └── memory/                  # Memory format templates (four-layer contract)
│       ├── distill.md           # Distillation template               ✅
│       ├── 灵魂备份.md           # Soul backup format                  ✅
│       ├── 对话记录.md           # Conversation record (A5 verbatim)   ✅
│       ├── 日志.md               # Log format                          ✅
│       └── 论语.md               # Sayings format                      ✅
│
├── docs/                  # Deep docs (thin facade thick system · L4 reference)
│   ├── concepts/           # Core concepts one by one (mother axiom/QA duality/entropy governance/three-semantics/falsifier/anti-drift)
│   │                       #   (one file per concept · on-demand read) ✅ 6 pieces
│   ├── lightweight-guide.md # Lightweight trimming guide (standard/minimal) ✅
│   ├── applicability.md     # Applicability boundaries (author statement) ✅
│   ├── project-introduction.md # Project intro supplement (external reviews/originality/portrait) ✅
│   ├── comparison.md       # vs LangGraph/AutoGen/dsh (governance-layer uniqueness) ✅
│   ├── internals/          # Core mechanism internals (01-06 · full dual-chain navigation, Core full-open) ✅ 6 pieces
│   ├── research/           # Academic paper entry (DOI · abstract · three-boundary declaration) ✅
│   ├── case-studies/       # Governance case studies (book/paper/open-source · author production history) ✅ 3 cases
│   ├── compatibility.md    # Compatibility proof (substrate thesis · no replacement, coexistence) ✅
│   ├── falsification-log.md # Falsification log (social-validation evidence chain · Core full version) ✅
│   ├── known-limits.md     # Pre-registered disclosure list (five-dimension honest disclosure) ✅
│   ├── version-policy.md   # Version policy (draft · finalized before release) ✅
│   └── adr/                # Architecture decision records           ✅ ADR-0001
│
├── examples/              # Examples
│   ├── project-template.md # Project body four-piece set               ✅
│   ├── activation/         # First-activation tool (README+py+yaml)    ✅
│   └── end-to-end/         # End-to-end cases (book/self-bootstrap/stress test) ✅ 3 cases
│
├── integrations/          # Framework integration examples (LangChain/CrewAI/AutoGen · Core full-open) ✅
│   └── integration-guide.md # General integration guide (rule front-loading/memory back-write/adjudication callback) ✅
│
├── plugins/               # Optional capability plugins
│   └── memory-vector/      # Dual-index memory retrieval (inverted default · vector optional · honest fallback) ✅
│
├── tools/                 # Tools (programming semantics · validation/execution)
│   ├── validator.py        # Consistency validator (deployment self-check · only tool) ✅
│   └── verify-ownership.py # Ownership verification (5 automated + 2 manual checks) ✅
│
└── .github/               # CI/Issue templates
    ├── workflows/validate.yml  # CI validation                        ✅
    └── ISSUE_TEMPLATE/          # Issue templates                     ✅
```

## 3. Structure-Principle Mapping (why structured this way)

| Structure | 2.0 principle basis | Problem solved |
|-----------|--------------------|----------------|
| `constitution/` | Five-level L0 · mandatory read layer | Rules before work |
| `rules/`+`mechanisms/` | Rules↔mechanisms separation (what to write vs how to verify) | Rules data-driven, checkable |
| `rules.yaml` | Programming semantics of three-semantics | Rules checkable (not pure docs) |
| `templates/identity/` | L1 identity · self-bootstrap | System three-file templates (fatal bootstrap gap) |
| `templates/memory/` | Layered loading · four-layer contract | Distillation/wrap-up formats (fatal bootstrap gap) |
| `docs/adr/` | Decision traces · anti-doc-mode self-congratulation | ADR ritual (aligned with dsh) |
| `BENCHMARK.md` | Verification-effective principle (written≠effective) | Architecture standing = measurable |
| `docs/concepts/` | Human semantics of three-semantics | Solves "others cannot understand" |
| `SECURITY.md` | Non-autonomy axiom · anti-exploitation | Confidential design-defect reporting channel |
| `CITATION.cff` | Academic hit | Standard paper-citation entry |

## 4. External Review Guide (how reviewers use this file)

1. **See structure**: read Section 2 tree — judge whether layers are clear, responsibilities separated, essentials missing;
2. **See status**: read status column (✅/🟡) — judge maturity (🟡 = structure defined, content pending);
3. **See rationale**: read Section 3 mapping — judge whether each structure has a theoretical basis (no basis = redundancy);
4. **Dig on demand**: to go deep into a structure, read the corresponding file per Section 2 paths — no whole-library read needed;
5. **Review output**: give "structure reasonable/which redundant/which missing" — no implementation details needed.

## 5. Writing Order (book-style · chapter by chapter · each step reviewable)

1. ✅ Root-level ritual files (SECURITY/CODE_OF_CONDUCT/CITATION · 2026-08-19)
2. ✅ templates/identity (Agent_Profile + system three files · 4 pieces · 2026-08-19)
3. ✅ templates/workspace-structure + memory (6 pieces · 2026-08-19)
4. ✅ docs/concepts (6 core concepts) + lightweight-guide (2026-08-19)
5. ✅ rules.yaml (programming-semantics instance · YAML check PASS · 2026-08-19)
6. ✅ docs/comparison.md (governance-layer uniqueness · 2026-08-19)
7. ✅ docs/adr/ADR-0001 (project structure finalized · 2026-08-19)
8. ✅ AGENTS.md + BENCHMARK.md (2026-08-19)
9. 🟡 English versions (README/DEPLOY/AGENTS/others in progress — publish gate)

> **Root-level files all ready** (README/LICENSE/DEPLOY/CONTRIBUTING/AGENTS/BENCHMARK/SECURITY/CODE_OF_CONDUCT/CITATION/Project Structure Guide) — English batch 1 done, remaining to complete before release.

---

*GOAA Open-Source Project · Project Structure Guide · Single version 1.0 · 2026-08-19 · This file = external review first entry · single baseline for structure landing*
