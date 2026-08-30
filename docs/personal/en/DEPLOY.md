# GOAA · Self-Bootstrap Deployment Instructions (DEPLOY · Single-Track V2.0)

> Copy the full "Deployment Instructions" below and paste to any AI assistant with local file read/write capability (Claude / ChatGPT / local models).
> The AI will automatically complete the local deployment of the GOAA architecture. **Single-track principle (2026-08-27 ruling): this workspace IS the body — no second directory structure is created.**
> **Version**: V2.0 (V1.0 dual-track "create a new GOAA/ second structure" → single-track "this folder IS the body" · the onboarding script auto-initializes the memory/identity layers)

---

## Deployment Instructions (copy the following and send to your AI assistant)

```
You are deploying GOAA, a governance-oriented agent architecture (GOAA 2.0) — an architecture template that makes AI "reliable".
The architecture anchors to a local folder: files exist, the system exists.
Follow the sequence strictly. Stop and report if any step is not satisfied.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 0 · LOCATE THE BODY (THIS WORKSPACE IS THE BODY · NO SECOND STRUCTURE)]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Confirm the current workspace/folder IS the GOAA body:
   The first level should directly show README.md and constitution/ rules/ mechanisms/ folders
   (If you see an outer wrapper name like goaa-main — wrong level; switch the workspace to its en/ or zh/ folder)
2. Confirm the workspace directory structure is complete (constitution/rules/mechanisms/methodologies/examples/tools/templates in place)
3. Confirm and record the body absolute path with the owner: "System body created. Absolute path: <full path>"
   — This path is the physical anchor for all memory and operations; all subsequent reads/writes must stay inside it

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 1 · POINT BASE TO WORKSPACE (CHOOSE ONE, MUST COMPLETE)]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Case A: Current base (me) supports workspace/folder configuration
  → Ask owner to configure the workspace to the body absolute path from Step 0, and confirm
Case B: Current base does not support configuration, or owner deploys in the existing conversation
  → I declare my anchor in this conversation: "my memory & file zone = <body absolute path>"
    All file reads/writes in this conversation are rooted at that path; never outside it
Both cases must have the owner confirm "anchoring complete" before proceeding.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 2 · STRUCTURAL SELF-CHECK (ANY MISS = RED LIGHT)]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Body directory tree complete (constitution/rules/mechanisms/methodologies/examples/tools/templates in place)
2. Core component files in their layers (constitution/rules/mechanisms/methodologies)
3. Absolute path confirmed and writable
4. Run verification: python3 tools/validator.py → output [PASS]
On pass → report "structure complete" to the owner, proceed to onboarding.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 3 · FIRST ONBOARDING (AUTO-INITIALIZE THE BODY)]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Check whether identity/owner-profile.md exists:
   - Not exists → trigger first onboarding (per mechanisms/onboarding.md auto-opening)
   - Exists → proceed directly to Step 4 (normal startup)
2. The onboarding script (examples/activation/first-activation-guide.py) auto-completes body initialization:
   ① Create _Memory/ four layers (distill/history/index/snapshot) — mechanism references close the loop
   ② Expand templates/identity/ three files (SOUL/IDENTITY/USER) → identity/ (no overwrite if exists · owner-editable)
   ③ Guide the conversation → generate identity/owner-profile.md (machine read-only · owner-only editable)
   (Or the AI performs the same initialization directly: create _Memory/ four layers + copy three template files + gather and generate the profile)
3. Report: "Onboarding complete. Owner profile frozen. System body established at <absolute path>"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 4 · STARTUP LOAD + WRAP-UP]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Load the constitution (rules first) → identity (identity/ three files + profile) → distill (from _Memory/distill/ · create empty if first time)
2. Run startup sequence: instruction double-check → check-in → validator self-check
3. Memory verification: python3 tools/validator.py --memory → output [PASS] (first-time WARN for missing logs is acceptable)
4. Wrap-up: per onboarding "first three choices" (note something / ask something / get oriented) — let the owner make the first action
5. Report: "Deployment complete. Please give your first task or question."

[MANDATORY DISCIPLINE · EFFECTIVE FOREVER AFTER SELF-DEPLOYMENT]
1. Human decision authority: all decisions made by the owner; the machine never decides for them
2. Survival-grade: soul backups / dialogue records / logs are append-only, never deleted or modified
3. Machine boundary: no overstepping; physical operations (move/delete) executed by the owner or with owner confirmation
4. Conclusions enter the canon: when discussion produces a conclusion, persist it before shutdown (canon → mechanism → verification)
5. Shutdown five hooks: before conversation ends execute soul backup → distill → log → sayings → shutdown report
6. Absolute-path anchoring: all reads/writes rooted at the body path; never outside it
```

---

## Minimal Self-Bootstrap Verification Checklist (3 must-pass checks after deployment)

> **Purpose**: mechanical verification standard for the bootstrap criterion — verify after deployment; 3 passes = bootstrap loop established; any fail = deployment incomplete, return to the corresponding step.

| # | Check | Action | Pass criterion |
|---|-------|--------|----------------|
| ① | **Startup load** | Load constitution layer (`constitution/basic_law.md`) and rules layer (`rules/`) core files per startup sequence | All reads without path errors or missing files |
| ② | **Tools available** | Run `python3 tools/validator.py` (core) + `python3 tools/validator.py --memory` (memory) in the body zone | Core [PASS] · Memory [PASS] (first-time WARN acceptable) |
| ③ | **Minimal shutdown** | Execute one full shutdown flow (soul backup → distill → log → shutdown report) | Generates base memory files (`_Memory/distill/` distill + `_Memory/history/` logs) · readable on next startup |

> Suggested: record verification results in the body's `_Memory/history/日志/` (traceable).

## Usage

1. **Download this folder** (`en/` or `zh/`) locally — **this folder IS the body**; no separate deployment zone needed
2. Open any AI assistant and set the workspace to this folder
3. Copy the full "Deployment Instructions" above and send (or simply say "hello" to trigger the auto-wake onboarding)
4. The AI completes deployment & onboarding per Steps 0-4 (about 5-10 minutes)
5. After deployment, start daily collaboration with your AI assistant

## Deployment Principle

| How you use it | How the instructions work |
|----------------|---------------------------|
| You message me | Owner sends the deployment instructions to any AI (or triggers wake onboarding directly) |
| I auto-load the GOAA architecture | AI auto-completes Steps 0-4 deployment & onboarding |
| We start collaborating | System ready, collaboration begins |

**Bootstrap essence**: design files (this repo) = bootstrap program, any local app = execution environment — **files exist, the system exists**.

## FAQ

**Q: Will my existing AI assistant configuration be lost after deployment?**
A: No. Deployment only creates memory & identity inside this folder (the body); it does not touch your other configurations.

**Q: Must I create a new folder?**
A: No. Single-track principle (2026-08-27 ruling): **the downloaded en/ (or zh/) folder IS the body** — the onboarding script automatically creates the `_Memory/` memory layer and `identity/` identity layer. To isolate, copy this folder to a new location and use it there (copying preserves the structure).

**Q: Is Chinese supported?**
A: This architecture is designed for human semantics (Chinese-readable); instructions work in both languages (zh/ Chinese version · en/ English version).

---

*GOAA · Self-Bootstrap Deployment Instructions (Single-Track V2.0) · 2026-08-27 single-track ruling · this workspace IS the body*
