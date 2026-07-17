# Mountain Plan daily coach

This folder turns `Google_90_Day_Bulletproof_Mountain_Plan.xlsx` into a lightweight GitHub accountability system. The workbook remains the source of truth.

## Daily rhythm

At **9:00 AM India time** every day from **18 July through 15 October 2026**, GitHub Actions creates one issue assigned to the repository owner. The issue contains:

- the two focused founder hours from the workbook;
- the required evidence and Codex handoff;
- the next hard gate and its pass condition;
- cumulative completed-hour and evidence rates from prior daily issues.

Work directly in the issue: complete the two hours, add links under **Evidence and learning**, check the boxes, and close it only after the evidence exists. Missing daily issues and unchecked boxes count as zero progress.

GitHub may start scheduled workflows a few minutes after the exact cron time during periods of high load. The schedule is configured as `03:30 UTC`, which is `09:00 Asia/Kolkata` year-round.

## Manual run

Use **Actions → Mountain Plan — Daily Coach → Run workflow** and optionally provide a date in `YYYY-MM-DD`. Duplicate issues are prevented.

For a local preview:

```bash
python -m pip install -r Mountain_plan/requirements.txt
python Mountain_plan/mountain_agent.py --date 2026-07-18 --dry-run
```

## Performance definition

- **Pace:** completed hour checkboxes / scheduled hours.
- **Evidence discipline:** days with the required-evidence checkbox / elapsed days.
- **Fully completed day:** both hours and required evidence checked.
- **On track:** both pace and evidence are at least 90%.
- **Watch:** the lower score is 70–89%.
- **Recovery required:** the lower score is below 70%.

The calculation is intentionally strict: it rewards finished, evidenced work rather than activity alone.
