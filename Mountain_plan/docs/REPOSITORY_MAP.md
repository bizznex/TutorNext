# Mountain Plan repository map

The Mountain Plan workbook and daily coach are the private orchestration layer. Product implementation, public evidence, decisions, tests, and releases remain isolated in four public repositories.

| Product | Public repository | Owned scope | 90-day target |
|---|---|---|---|
| Decision360 CPG | https://github.com/rickdatascientist/decision360-cpg | Supply-chain decision workflows, deterministic decision logic, governed agent layer, product evaluation | Public beta |
| Decision Agent Benchmark | https://github.com/rickdatascientist/decision-agent-benchmark | Decision/economic metrics, benchmark tasks, runner, scorecards, findings | Public alpha |
| Transformation Mapper | https://github.com/rickdatascientist/transformation-mapper | Evidence ingestion, opportunity generation, transparent scoring, no-build decisions | Demonstrable prototype |
| Commerce Growth | https://github.com/rickdatascientist/commerce-growth | Catalog readiness and category opportunity; strictly non-medical | Vertical demonstration |

## Boundary rules

1. Each product owns its README, charter, roadmap, decisions, evidence, implementation, tests, issues, and releases.
2. The private orchestration repository may link to public artifacts but does not become the implementation home for a product.
3. Shared schemas or libraries must become versioned dependencies with an explicit owner. Do not copy them silently across repositories.
4. Public repositories contain only public sources, independently created material, synthetic data, and sanitized validation summaries.
5. Interview notes, personal data, employer/customer material, compensation details, private role calibration, and the Mountain Plan workbook stay private.
6. A public claim is a hypothesis until a reproducible or reviewable evidence artifact is linked.

## Public release gate

Before any product release, confirm product-specific acceptance tests, evidence, security, privacy, IP/clean-room review, known limitations, and a named human approval decision in that product's repository.
