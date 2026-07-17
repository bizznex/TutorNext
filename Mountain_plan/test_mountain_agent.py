import unittest
from datetime import date

from mountain_agent import (
    CHECK_EVIDENCE,
    CHECK_HANDOFF,
    CHECK_HOUR_1,
    CHECK_HOUR_2,
    DEFAULT_WORKBOOK,
    MARKER_RE,
    build_issue_body,
    calculate_metrics,
    load_plan,
    next_gate,
)


def issue(day: int, checked: list[str]) -> dict:
    boxes = "\n".join(
        f"- [{'x' if item in checked else ' '}] {item}"
        for item in [CHECK_HOUR_1, CHECK_HOUR_2, CHECK_EVIDENCE, CHECK_HANDOFF]
    )
    return {"body": f"<!-- mountain-plan:v1 day={day} date=2026-07-{17 + day:02d} -->\n{boxes}"}


class MountainAgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.plans, cls.gates = load_plan(DEFAULT_WORKBOOK)

    def test_workbook_has_expected_90_day_window(self) -> None:
        self.assertEqual(len(self.plans), 90)
        self.assertEqual(self.plans[0].date, date(2026, 7, 18))
        self.assertEqual(self.plans[-1].date, date(2026, 10, 15))

    def test_metrics_include_missing_days_as_zero(self) -> None:
        issues = [
            issue(1, [CHECK_HOUR_1, CHECK_HOUR_2, CHECK_EVIDENCE, CHECK_HANDOFF]),
            issue(2, [CHECK_HOUR_1]),
        ]
        metrics = calculate_metrics(self.plans, issues, before_day=4)
        self.assertEqual(metrics.elapsed_days, 3)
        self.assertEqual(metrics.completed_hours, 3)
        self.assertEqual(metrics.scheduled_hours, 6)
        self.assertEqual(metrics.evidence_days, 1)
        self.assertEqual(metrics.completed_days, 1)
        self.assertEqual(metrics.signal, "Recovery required")

    def test_issue_body_has_stable_marker_and_checklist(self) -> None:
        metrics = calculate_metrics(self.plans, [], before_day=1)
        body = build_issue_body(self.plans[0], next_gate(self.gates, 1), metrics)
        marker = MARKER_RE.search(body)
        self.assertIsNotNone(marker)
        self.assertEqual(marker.group(1), "1")
        self.assertIn("9:00–10:00", body)
        self.assertIn(CHECK_EVIDENCE, body)
        self.assertIn("G1 Role truth", body)


if __name__ == "__main__":
    unittest.main()
