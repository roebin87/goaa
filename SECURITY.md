# Security Policy
> **语义形态**：人语义（意图锚·概念解释·阅读）

## Supported Versions

| Version | Status |
|---------|:---:|
| 1.0 (current single version) | ✅ Supported |

This project adopts a **core stable + periphery iterative** dual-track strategy: the architecture core (constitution/rules/core mechanisms) maintains major version stability, while the periphery ecosystem iterates rapidly (see README "Version Strategy"). Security fixes are merged into the 1.0 branch as patches.

## Reporting a Vulnerability

This architecture is a **governance-oriented agent architecture template** — it is not an executable program; it does not run code or process data itself. However, its design files (rules/mechanisms/deployment instructions) could be maliciously exploited to induce deployers into unsafe operations (e.g., unauthorized file reads/writes, bypassing decision rights).

If you find such design-level security issues, **do not discuss publicly**. Report via:

1. **Direct message to the author**: GitHub account `roebin87`
2. **Confidential issue**: open an Issue with `[SECURITY]` prefix and note "sensitive" — the author will handle it privately

**Suggested report content**:
- Affected file/mechanism (e.g., a DEPLOY.md step, a rule in rules/)
- What dangerous operation could be induced
- Possible exploitation path and impact

## Response Commitment

- Acknowledge receipt within 48 hours
- Give an assessment (accepted/rejected/needs more info) within 7 days
- After a fix is merged, log it in "Security Update Record" below

## Security Update Record

- None yet

---

*GOAA · Security Policy · Single version 1.0 · 2026-08-19*
