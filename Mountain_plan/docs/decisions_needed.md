# Mountain Plan decisions needed

Updated: 2026-07-17

| ID | Decision | Owner | Due | Current position | Evidence required | If unresolved |
|---|---|---|---|---|---|---|
| DN-001 | Which Google team and role family owns the proposed contribution? | Rick | Day 10 | Pursuit/AI Transformation is the lead hypothesis | Two independent insider answers plus one recruiter/HM view | Do not apply or optimize the portfolio for a guessed role |
| DN-002 | What India/APAC level is credible without resetting scope? | Rick | Day 10 | Unknown | Insider and recruiter calibration against actual scope and gaps | Keep role positioning provisional |
| DN-003 | What architecture and delivery depth is mandatory? | Rick + technical reviewer | Day 10 | Working fluency is assumed; required depth is unverified | Named-role interview loop expectations and architect review | Convert gaps into the daily fluency syllabus |
| DN-004 | Can the calibrated role plausibly meet the private compensation condition? | Rick | Day 14 | Unverified | Private recruiter/advisor calibration; no public claims | Reject structurally under-level routes |
| DN-005 | Which product is the flagship? | Rick | Day 7 | Decision360 CPG | Six buyer conversations and evidence-quality comparison | Keep 80% of build effort off non-flagship products |
| DN-006 | What is excluded by the clean-room rule? | Rick + legal reviewer if needed | Day 12 | No employer/customer material, personal data, confidential interviews, or copied code | Written provenance and exclusion review | Block public product claims or releases |
| DN-007 | What reuse license should each public repository use? | Rick | Before external code contribution | No license selected; public review only | Licensing intent and any employer/legal constraints | Do not accept external code or imply open-source rights |
| DN-008 | Should shared contracts be a separate repository/package? | Rick + architect | Day 25 | Undecided; no copying between product repos | Two approved product PRDs and a stable cross-product contract | Keep contracts product-local until ownership is clear |
| DN-009 | Should the already-public Decision360 repository remain public before the simulation UI is polished? | Rick | Resolved 2026-07-18 | **Keep public.** The simulation UI is merged, tested, and preserves synthetic/unvalidated claim boundaries | Public repository, merged UI PR, green CI | Closed |

## Immediate Rick actions

1. Select the first Google insider and send or schedule the Day 1 calibration conversation.
2. Answer DN-006 with an initial list of employers, customers, documents, datasets, and product details that must never enter public repositories.
3. Decide whether the public repository names should remain descriptive or later sit under a GroundAI organization/brand.
4. Keep product claims within the synthetic/conformance boundaries recorded in each public repository.

## Codex actions after Rick input

1. Convert insider answers into a role dossier without exposing private notes.
2. Rewrite the contribution thesis where the two independent answers agree or disagree.
3. Translate clean-room exclusions into automated repository checks where feasible.
4. Keep all implementation work inside the owning public product repository.
