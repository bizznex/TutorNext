# Public product portfolio status

Updated: 2026-07-18

| Product | Main commit | Verification | Claim boundary |
|---|---|---|---|
| Decision360 CPG | `48c9bc4` | 26 tests; 60/60 qualification cases; 45/45 critical; seven hosted CI jobs | Technical reference and synthetic workflow simulation, not validated planning policy |
| Decision Agent Benchmark | `f88bbc6` | 24 tests; 12/12 executable validation checks; hosted CI | Metric/scorer conformance, not real-agent performance |
| Transformation Mapper | `bd389a6` | 14 tests; 8/8 executable validation checks; hosted CI | Synthetic scoring conformance, not buyer demand or realized transformation value |
| Commerce Growth | `101956e` | 19 tests; 10/10 executable validation checks; hosted CI | Aggregate non-medical catalog conformance, not demand uplift or individual suitability |

All four repositories are public, isolated, and implemented on their `main` branches. Each owns its contracts, synthetic corpus, deterministic analysis, tests, validation evidence, documentation, and CI.

## Portfolio-level work that remains human-owned

- role and level calibration for the Google pursuit;
- clean-room exclusion confirmation and any legal review;
- public reuse-license selection;
- buyer evidence and sealed real-world evaluations before product-value claims;
- the private compensation decision.

These are evidence or authority decisions, not unfinished public-alpha engineering tasks.
