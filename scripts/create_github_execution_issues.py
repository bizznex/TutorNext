from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass


REPO = "bizznex/TutorNext"


@dataclass(frozen=True)
class Issue:
    task_id: str
    title: str
    priority: str
    phase: str
    workstream: str
    description: str
    acceptance: str
    validation: str
    dependencies: str
    vision: str
    labels: list[str]


ISSUES = [
    Issue(
        "C-001",
        "Audit current frontend architecture",
        "P0",
        "P0 Foundation & Product Definition",
        "Frontend Engineering",
        "Identify routes, state, API usage, design debt, responsive gaps, and what can be reused for ContexureEarth Tutor.",
        "Frontend audit is documented with files, risks, reusable components, rewrite boundaries, and next decisions.",
        "Large implementation changes have a clear base.",
        "Existing prototype UI and README context.",
        "V7",
        ["priority:P0", "phase:foundation", "workstream:frontend"],
    ),
    Issue(
        "D-001",
        "Audit backend models and APIs",
        "P0",
        "P0 Foundation & Product Definition",
        "Backend & Data Model",
        "Identify model gaps, workflow gaps, auth gaps, migration risks, and generic-to-education naming pressure.",
        "Backend audit documents current models, endpoints, tenant/auth/model gaps, and safe production changes.",
        "Tenant/account and auth decisions can be made confidently.",
        "Existing Django/DRF backend.",
        "V7/V8",
        ["priority:P0", "phase:foundation", "workstream:backend"],
    ),
    Issue(
        "A-001",
        "Define production personas",
        "P0",
        "P0 Foundation & Product Definition",
        "Strategy & Product Definition",
        "Document academic tutor, exam coach, hobby teacher, skill trainer, fitness trainer, corporate trainer, and priority order.",
        "Persona definitions and priority order are approved; P-AST remains first ICP unless evidence changes.",
        "No MVP task optimizes for non-ICP without explicit exception.",
        "Feature heatmap and roadmap.",
        "V1",
        ["priority:P0", "phase:foundation", "workstream:strategy"],
    ),
    Issue(
        "A-004",
        "Map public visitor journey",
        "P0",
        "P0 Foundation & Product Definition",
        "Strategy & Product Definition",
        "Map parent path from shared link to inquiry, trial CTA, confirmation, and WhatsApp handoff.",
        "Journey includes trust, course fit, fee clarity, trial, confirmation, and privacy note.",
        "Parent can understand next step in 30 seconds.",
        "A-001",
        "V1/V2",
        ["priority:P0", "phase:foundation", "workstream:strategy", "workstream:ux"],
    ),
    Issue(
        "A-005",
        "Map owner inquiry-to-fee journey",
        "P0",
        "P0 Foundation & Product Definition",
        "Strategy & Product Definition",
        "Map owner path from inquiry to trial to enrollment to fee tracking and proof/referral prompt.",
        "Every owner step has status, next action, and message template.",
        "Owner knows what to do today without reading a manual.",
        "A-001",
        "V2/V4/V5/V6/V7",
        ["priority:P0", "phase:foundation", "workstream:strategy", "workstream:ux"],
    ),
    Issue(
        "D-002",
        "Define tenant/account model",
        "P0",
        "P0 Foundation & Product Definition",
        "Backend & Data Model",
        "Decide account, owner, operator, support, tutor studio boundaries and data isolation rules.",
        "Multi-tutor data isolation design is documented and ready for implementation.",
        "No real beta user data enters the system without a tenant boundary.",
        "D-001",
        "V7",
        ["priority:P0", "phase:foundation", "workstream:backend", "workstream:security"],
    ),
    Issue(
        "E-001",
        "Choose production auth approach",
        "P0",
        "P0 Foundation & Product Definition",
        "Auth, Privacy & Trust",
        "Choose email/password, OTP, managed auth, or phased auth approach for owner/operator dashboard.",
        "Auth decision covers roles, account recovery, beta path, and production migration.",
        "Owner/operator dashboards cannot be public.",
        "D-002",
        "V7",
        ["priority:P0", "phase:foundation", "workstream:security", "workstream:backend"],
    ),
    Issue(
        "N-001",
        "Choose production hosting architecture",
        "P0",
        "P0 Foundation & Product Definition",
        "Infrastructure & Deployment",
        "Decide staging/production deployment, database, static assets, backups, monitoring, domain, and rollback.",
        "Hosting architecture is approved and can support private beta safely.",
        "Staging can be created confidently.",
        "D-001,E-001",
        "V7",
        ["priority:P0", "phase:foundation", "workstream:infra"],
    ),
    Issue(
        "B-001",
        "Define ContexureEarth Tutor visual direction",
        "P0",
        "P0 Foundation & Product Definition",
        "UX, Design & Copy",
        "Set calm, credible, parent-friendly, mobile-first, education-native design principles.",
        "Moodboard/design principles are approved and mapped to public page, forms, dashboard, and operator console.",
        "Tutor would not be embarrassed to share the public page.",
        "IMD-006",
        "V1",
        ["priority:P0", "phase:foundation", "workstream:ux"],
    ),
    Issue(
        "IMD-006",
        "Founder decision: brand architecture",
        "P0",
        "P0 Foundation & Product Definition",
        "Strategy & Product Definition",
        "Confirm public product naming and relationship between ContexureEarth Tutor and BizzNexx operating layer.",
        "Decision is recorded in roadmap, handoff docs, README, and issue labels if needed.",
        "No confusion in UI/demo language.",
        "Critical evaluation document.",
        "V1-V10",
        ["priority:P0", "phase:foundation", "workstream:strategy"],
    ),
    Issue(
        "IMD-007",
        "UI copy pass for ContexureEarth Tutor",
        "P0",
        "P0 Foundation & Product Definition",
        "UX, Design & Copy",
        "Replace generic microbusiness language in the tutor path with learner, parent, course, batch, fee cycle, and operating rhythm language.",
        "Tutor demo uses education-native language while preserving the current working flow.",
        "Reviewers do not perceive the product as a generic CRM.",
        "IMD-006,C-001",
        "V1/V8",
        ["priority:P0", "phase:foundation", "workstream:ux", "workstream:frontend"],
    ),
    Issue(
        "DATA-000",
        "Define event taxonomy",
        "P0",
        "P0 Foundation & Product Definition",
        "Analytics & Metrics",
        "Define page view, CTA click, inquiry, trial, fee, message, proof, setup, and owner action events.",
        "Events have trigger, properties, privacy level, and owner.",
        "Activation funnel and weekly completed tutor actions can be measured.",
        "A-004,A-005",
        "V7",
        ["priority:P0", "phase:foundation", "workstream:data"],
    ),
]


BASE_LABELS = ["contexureearth", "tutor"]


def run(args: list[str], input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, input=input_text, text=True, capture_output=True, check=False)


def label_exists(name: str) -> bool:
    result = run(["gh", "label", "list", "--repo", REPO, "--json", "name", "--limit", "200"])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    labels = {item["name"] for item in json.loads(result.stdout)}
    return name in labels


def ensure_label(name: str, color: str = "0E8A16", description: str = "") -> None:
    if label_exists(name):
        return
    result = run(["gh", "label", "create", name, "--repo", REPO, "--color", color, "--description", description])
    if result.returncode != 0 and "already exists" not in result.stderr:
        raise RuntimeError(result.stderr.strip())


def issue_exists(task_id: str) -> bool:
    result = run(
        [
            "gh",
            "issue",
            "list",
            "--repo",
            REPO,
            "--state",
            "all",
            "--search",
            f"{task_id} in:title",
            "--json",
            "title",
            "--limit",
            "20",
        ]
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return any(task_id in item["title"] for item in json.loads(result.stdout))


def issue_body(issue: Issue) -> str:
    return f"""## Task

**Task ID:** {issue.task_id}
**Priority:** {issue.priority}
**Phase:** {issue.phase}
**Workstream:** {issue.workstream}
**Vision Link:** {issue.vision}

## Description

{issue.description}

## Acceptance Criteria

{issue.acceptance}

## Validation Signal

{issue.validation}

## Dependencies

{issue.dependencies or "None"}

## Source

Created from the ContexureEarth Tutor project planner and accountable tasklist.
"""


def create_issue(issue: Issue) -> None:
    if issue_exists(issue.task_id):
        print(f"skip existing {issue.task_id}")
        return
    labels = BASE_LABELS + issue.labels
    args = [
        "gh",
        "issue",
        "create",
        "--repo",
        REPO,
        "--title",
        f"{issue.task_id}: {issue.title}",
        "--body",
        issue_body(issue),
    ]
    for label in labels:
        args.extend(["--label", label])
    result = run(args)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    print(result.stdout.strip())


def main() -> None:
    labels = {
        "contexureearth": ("0E8A16", "ContexureEarth product work"),
        "tutor": ("1D76DB", "Tutor product wedge"),
        "priority:P0": ("B60205", "Required before private beta"),
        "priority:P1": ("D93F0B", "Required for paid pilot or retention"),
        "priority:P2": ("FBCA04", "Scale or expansion"),
        "priority:P3": ("C5DEF5", "Deferred or demand-validated"),
        "phase:foundation": ("5319E7", "Foundation and product definition"),
        "phase:concierge-prototype": ("7057FF", "Concierge prototype"),
        "phase:private-beta": ("0052CC", "Private beta"),
        "phase:paid-pilot": ("008672", "Paid pilot"),
        "phase:public-launch": ("0E8A16", "Public launch"),
        "workstream:strategy": ("BFD4F2", "Strategy and product definition"),
        "workstream:research": ("BFDADC", "Research and customer discovery"),
        "workstream:ux": ("D4C5F9", "UX design and copy"),
        "workstream:frontend": ("C2E0C6", "Frontend engineering"),
        "workstream:backend": ("C5DEF5", "Backend and data model"),
        "workstream:security": ("F9D0C4", "Auth privacy and trust"),
        "workstream:whatsapp": ("FEF2C0", "WhatsApp and messaging"),
        "workstream:data": ("D1F2A5", "Analytics and metrics"),
        "workstream:ops": ("FAD8C7", "Operator setup and support"),
        "workstream:gtm": ("FDEBD0", "Marketing sales and launch"),
        "workstream:qa": ("E6E6FA", "QA and release gates"),
        "workstream:infra": ("DDEBFF", "Infrastructure and deployment"),
        "status:blocked": ("000000", "Blocked task"),
    }
    for name, (color, desc) in labels.items():
        ensure_label(name, color, desc)
    for issue in ISSUES:
        create_issue(issue)


if __name__ == "__main__":
    main()

