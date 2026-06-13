# First Execution Batch

These are the first issues that should be created in `bizznex/TutorNext`.

The script `scripts/create_github_execution_issues.py` creates labels and issues automatically when GitHub CLI is installed and authenticated.

## Setup Command

```powershell
gh auth login
python scripts\create_github_execution_issues.py
```

## Issues

1. `C-001`: Audit current frontend architecture
2. `D-001`: Audit backend models and APIs
3. `A-001`: Define production personas
4. `A-004`: Map public visitor journey
5. `A-005`: Map owner inquiry-to-fee journey
6. `D-002`: Define tenant/account model
7. `E-001`: Choose production auth approach
8. `N-001`: Choose production hosting architecture
9. `B-001`: Define ContexureEarth Tutor visual direction
10. `IMD-006`: Founder decision: brand architecture
11. `IMD-007`: UI copy pass for ContexureEarth Tutor
12. `DATA-000`: Define event taxonomy

This batch keeps development focused on making the product coherent, safe, and production-ready before broad feature work.

