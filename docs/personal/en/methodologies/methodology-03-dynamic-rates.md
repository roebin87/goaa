# Methodology 03 · Dynamic Rates Design (Method Points)
> **Semantics**: Machine (mechanism/translation layer · How)

> **Role**: this methodology provides the reusable **method points** for dynamic-rates design; the **authoritative mechanism detail is in `mechanisms/dynamic-rates.md`** — same source, mechanism is authoritative, this file offers method points and use cases.

## Method points (when to use / how to think)

- **When**: judging whether the system is running healthily — use "rates" to make the unobservable health state visible
- **Five principles (quick recall)**: anchor to the immovable layer · single function · early trigger · anti-decay · dual-sided observation
- **Core loop**: rate collection → rate trend → anomaly intervention (human final ruling) → re-collection
- **Boundary**: rates are information, not judgments (human final ruling); thresholds are to be calibrated (validation through operation)

## Use cases

- Wrap-up health-state check · monthly governance review · version-retirement criteria (stock pollution index)

> Full definition (rate-tier breakdown / collection mechanisms / intervention flow / double anchor) see `mechanisms/dynamic-rates.md` — the mechanism file is authoritative.
