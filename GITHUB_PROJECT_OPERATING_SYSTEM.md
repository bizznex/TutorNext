# GitHub Project Operating System

This repo uses GitHub as the execution monitor for **ContexureEarth Tutor**.

## Repo Roles

- `origin` is the development remote: `rickdatascientist/bizznexx-mvp`
- `production` is the production/main project remote: `bizznex/TutorNext`

## Source Of Truth

- Strategy and complete planning live in `product vision/`.
- Live execution lives in GitHub Issues and pull requests.
- The workbook `product vision/ContexureEarth_Tutor_Professional_Project_Planner.xlsx` remains the master planning tracker.

## Issue Rules

Every active issue should include:

- Task ID
- Phase
- Workstream
- Priority
- Description
- Acceptance criteria
- Validation signal
- Dependencies
- Vision link

## Recommended Board Columns

- Backlog
- Ready
- In Progress
- In Review
- Blocked
- Done

## Labels

Core labels:

- `contexureearth`
- `tutor`
- `priority:P0`
- `priority:P1`
- `priority:P2`
- `priority:P3`
- `phase:foundation`
- `phase:concierge-prototype`
- `phase:private-beta`
- `phase:paid-pilot`
- `phase:public-launch`
- `workstream:strategy`
- `workstream:research`
- `workstream:ux`
- `workstream:frontend`
- `workstream:backend`
- `workstream:security`
- `workstream:whatsapp`
- `workstream:data`
- `workstream:ops`
- `workstream:gtm`
- `workstream:qa`
- `workstream:infra`
- `workstream:ai`
- `status:blocked`

## Branch Naming

Use:

```text
task/<task-id>-short-name
```

Examples:

```text
task/c-001-frontend-architecture-audit
task/d-001-backend-api-audit
task/imd-007-contexureearth-copy-pass
```

## Commit Naming

Use:

```text
<area>: <short action> (<task-id>)
```

Examples:

```text
docs: add frontend architecture audit (C-001)
backend: define tenant model options (D-002)
frontend: update tutor product language (IMD-007)
```

## Pull Request Rules

Open a PR when a task is ready for review.

PR title:

```text
<TASK-ID>: <task title>
```

PR body should include:

- linked issue
- what changed
- acceptance criteria
- verification
- product notes

## First Execution Batch

The first GitHub issue batch should cover the production foundation:

1. `C-001` Audit current frontend architecture
2. `D-001` Audit current backend models/APIs
3. `A-001` Define production personas
4. `A-004` Map public visitor journey
5. `A-005` Map owner inquiry-to-fee journey
6. `D-002` Define tenant/account model
7. `E-001` Choose production auth approach
8. `N-001` Choose production hosting architecture
9. `B-001` Define ContexureEarth Tutor visual direction
10. `IMD-006` Founder decision: brand architecture
11. `IMD-007` UI copy pass for ContexureEarth Tutor
12. `DATA-000` Define event taxonomy

This batch keeps the team focused on making the product safe, coherent, and production-ready before broad feature work.

