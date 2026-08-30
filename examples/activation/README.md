# Example · First Onboarding Tool (Onboarding Tool)

> **Authoritative flow**: The **process spec for first onboarding lives in [mechanisms/onboarding.md](../../docs/personal/en/mechanisms/onboarding.md)** — this directory is only that flow's **executable tool implementation** (CLI executor), not the flow definition.
> This example is for users who want to run onboarding from the command line; for conversational onboarding, just follow the deployment instructions in DEPLOY.md.

## Why first onboarding exists

AI has no persistent memory and does not know who you are. First onboarding = letting the instance "know you well enough":
1. **Knowledge transfer**: understand the system's core mechanisms (startup / wrap-up / distillation / backup / validation)
2. **Info collection**: learn the owner's basics (name / background / goals / collaboration preferences / boundaries)
3. **Profile freeze**: write the "owner profile" — **machine read-only, only the owner may change it**

> First onboarding is knowledge transfer, not form-filling — after it, you should already understand the system skeleton (see the 8-step flow and the machine's honest disclosure in mechanisms/onboarding.md).

## How to use

### Option 1: Conversational onboarding (recommended · no dependencies)

Say the opening line to the instance:

> "I need you to get to know me well enough for us to work together — you can ask me questions until you fully understand me."

The instance follows the 8-step flow in [mechanisms/onboarding.md](../../docs/personal/en/mechanisms/onboarding.md) (welcome → mechanism knowledge transfer → naming → collection → boundaries → recap → save → return initiative).

### Option 2: CLI executor (optional · requires Python)

```bash
pip install pyyaml
python3 first-activation-guide.py            # interactive onboarding (collects the 8 required items)
python3 first-activation-guide.py --dry-run  # preview the flow
```

> ⚠️ The CLI executor covers only the "info collection" segment (steps ③-⑦ of the flow); mechanism knowledge transfer and returning initiative are conversational steps handled by conversational onboarding.

## Files

| File | Purpose |
|------|------|
| `first-activation-guide.yaml` | Collection flow definition (required items) |
| `first-activation-guide.py` | CLI executor (reads yaml → asks item by item → generates the owner profile) |
| `../../docs/personal/en/mechanisms/onboarding.md` | **Authoritative onboarding flow** (full 8-step process) |

## Output

`identity/owner-profile.md` — machine read-only, only the owner may edit (per the non-autonomy axiom: the profile is the owner's self-description; the machine has no right to change it).

---

*GOAA Generic Example · Single version 1.0 · 2026-08-19*
