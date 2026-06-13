# Team Handoff: BizzNexx Learning Studio

Date: 2026-06-13

Use this file as the team entry point. The product direction, MVP feature choices, and production workstreams have already been shaped. Do not restart discovery unless a blocker invalidates the current assumptions.

## 1. Current Mission

Build BizzNexx Learning Studio into a production-ready responsive web app for tutors and private trainers.

The first production wedge is:

P-AST Academic School Tutor.

The product must help the tutor:

- Look credible with one shareable public page.
- Capture structured inquiries instead of scattered WhatsApp messages.
- Follow up on trial/demo interest.
- Track students/learners and monthly fees.
- Send polite WhatsApp messages.
- Collect proof, testimonials, and referrals.
- Know what to do today from an owner action queue.

## 2. Authoritative Documents

Read in this order:

1. `TEAM_HANDOFF_START_HERE.md`
2. `Learning_Studio_Production_Web_App_Accountable_Tasklist.md`
3. `Learning_Studio_Tutor_Growth_Feature_CMD_Tracker.md`
4. `Learning_Studio_Beta_Rollout_Readiness_Plan.md`
5. `Learning_Studio_Execution_Action_Plan.md`
6. `README.md`
7. `PROJECT_LOG.md`

Supporting beta docs:

- `BETA_USER_REVIEW_GUIDE.md`
- `BETA_FEEDBACK_FORM.md`
- `PRIVATE_BETA_QA_CHECKLIST.md`
- `DEPLOYMENT_PRIVATE_BETA.md`

## 3. Locked Product Decisions

These are settled for now:

- The product is not a generic CRM, LMS, coaching ERP, or lead marketplace.
- WhatsApp is the core workflow.
- Manual WhatsApp handoff launches before WhatsApp Business Cloud API automation.
- Public trust page plus structured inquiry is the entry loop.
- Owner dashboard should be an action queue, not a decorative analytics page.
- P-AST Academic Tutor is the first production persona.
- P-CEX Exam Coach, P-HBY Hobby Teacher, and P-SKL Skill Trainer are the strongest adjacent personas.
- P-COR Corporate Trainer is later because it pulls the product toward proposals, invoices, certificates, and B2B reporting.
- Payment gateway, full LMS, parent app, marketplace leads, heavy test engine, and GST/accounting are deferred.

## 4. Selected MVP Feature Spine

Build the first production version around these selected features:

1. Public Trust Page
2. Structured Inquiry Form
3. WhatsApp Handoff/Template
4. Trial/Demo Workflow
5. Student/Learner Memory
6. Monthly Fee Tracker
7. Owner Action Queue
8. Testimonials/Proof Section
9. Parent/Client FAQ
10. Privacy/Consent Controls

Everything else must justify itself against this spine.

## 5. Active Execution Board

The main task board is:

`Learning_Studio_Production_Web_App_Accountable_Tasklist.md`

Use the IDs in that file for all task references. Do not invent parallel task IDs unless adding a new workstream.

Status values:

- Not Started
- Discovery
- Designed
- In Build
- In Review
- In QA
- Blocked
- Done

Priority values:

- P0: required for private beta with real users
- P1: required for paid pilot and retention
- P2: required for scale and expansion
- P3: later or demand-validated

## 6. Immediate Build Slice

Start with Slice 0 and Slice 1 from the production tasklist.

### Slice 0: Foundation Cleanup

Goal: prepare current prototype for production work.

Tasks:

- Audit current frontend architecture.
- Audit current backend models and APIs.
- Define tenant/account model.
- Choose auth approach.
- Choose production hosting architecture.
- Define final data model for Business, Course/Batch, Inquiry, Lead/Trial, Student/Learner, Fee Cycle, Proof, Message Template, Follow-up Task.
- Create staging environment plan.

Exit criteria:

- Product, data, auth, deployment, and UX direction are aligned.

### Slice 1: Share-Ready Public Page

Goal: tutor can share one professional link.

Tasks:

- Public tutor profile.
- Course/batch catalogue.
- Testimonials/proof section.
- FAQ.
- Trial CTA.
- WhatsApp CTA.
- Privacy/consent note.
- Mobile polish.

Exit criteria:

- A real tutor would be willing to share the page with parents.

## 7. First 20 Tasks

Use these as the first practical sprint board:

| Order | Task ID | Task | Owner | Priority |
| --- | --- | --- | --- | --- |
| 1 | A-001 | Define production personas | PROD | P0 |
| 2 | A-004 | Map public visitor journey | PROD/UX | P0 |
| 3 | A-005 | Map owner inquiry-to-fee journey | PROD/UX | P0 |
| 4 | C-001 | Audit current frontend architecture | FE | P0 |
| 5 | D-001 | Audit current backend models/APIs | BE | P0 |
| 6 | B-001 | Define visual direction | UX | P0 |
| 7 | D-002 | Define tenant/account model | BE/SEC | P0 |
| 8 | E-001 | Choose auth approach | SEC/BE | P0 |
| 9 | N-001 | Choose production hosting architecture | BE/FE/SEC | P0 |
| 10 | B-002 | Create responsive layout system | UX/FE | P0 |
| 11 | D-004 | Define Course/Batch/Program model | BE | P0 |
| 12 | D-005 | Define Inquiry model | BE | P0 |
| 13 | D-006 | Define Lead/Trial states | BE/PROD | P0 |
| 14 | C-003 | Implement public studio page route | FE | P0 |
| 15 | C-004 | Implement tutor inquiry flow | FE | P0 |
| 16 | F-001 | Implement manual WhatsApp click-to-chat | FE | P0 |
| 17 | F-003 | Create WhatsApp template library | PROD/OPS | P0 |
| 18 | E-006 | Add inquiry consent timestamp | SEC/FE/BE | P0 |
| 19 | M-001 | Create inquiry-to-lead backend tests | QA/BE | P0 |
| 20 | N-002 | Create staging environment | BE/FE | P0 |

## 8. Repository Structure

Important paths:

- `prototype/frontend`: React + Vite frontend.
- `prototype/backend`: Django + DRF backend.
- `prototype/shared`: shared planning/reference area.
- `render.yaml`: Render deployment blueprint.
- `.github`: GitHub Actions and preview workflows.

Planning docs live in the repo root.

## 9. Local Run Commands

Backend:

```bash
cd prototype/backend
python manage.py migrate
python manage.py seed_demo
python manage.py runserver 8000
```

Frontend:

```bash
cd prototype/frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

## 10. Engineering Rules

Follow these rules unless the product owner explicitly changes them:

- Keep public pages mobile-first.
- Do not expose owner/operator dashboards publicly.
- Do not store unnecessary sensitive student data.
- Do not build WhatsApp API automation before manual WhatsApp handoff is stable.
- Do not build full LMS, parent app, payment gateway, marketplace leads, or GST/accounting in the first production slice.
- Every workflow must have a clear owner action.
- Every P0 feature must have acceptance criteria and QA coverage.
- Every integration must have a fallback mode.
- Every external API key/token must live in environment configuration, never in source.

## 11. UX Rules

The app should feel:

- Calm.
- Trustworthy.
- Mobile-first.
- Parent-friendly.
- Operationally serious.
- India-aware.
- WhatsApp-native.

Avoid:

- Generic SaaS dashboards.
- Heavy CRM vocabulary.
- Decorative analytics.
- Claims of guaranteed leads, marks, admissions, or fee recovery.
- Overbuilding for corporate trainers during tutor MVP.

## 12. Integration Strategy

### WhatsApp

Launch:

- Click-to-chat links.
- Editable templates.
- Copy-to-clipboard.
- Manual "sent" status.

Later:

- WhatsApp Business Cloud API.
- Approved templates.
- Webhooks.
- Delivery/read status.
- Opt-in/opt-out automation.

### Instagram

Launch:

- Profile link.
- Campaign/source tracking.
- Caption prompts.
- Proof reuse.

Later:

- Instagram API OAuth.
- Insights.
- Publishing only after permission/app-review path is clear.

### YouTube

Launch:

- Channel/video/playlist links.
- Teaching proof video section.

Later:

- YouTube Data API metadata and analytics.

### LinkedIn

Launch:

- Profile/company link.
- LinkedIn-ready testimonial/case-study copy.

Later:

- Corporate trainer variant.
- LinkedIn API only after B2B use case is validated.

### Google Forms

Launch:

- Native BizzNexx inquiry form remains primary.
- Allow external Google Form link if needed.

Later:

- Google Forms response import.
- Feedback/testimonial form generation.
- Google Sheets export.

## 13. QA Gates

No private beta release unless:

- Public page works on mobile and desktop.
- Inquiry creates lead and follow-up task.
- Owner dashboard requires auth.
- Owner action queue works.
- Manual WhatsApp handoff works.
- Trial/demo workflow works.
- Fee tracker works.
- Privacy/consent text exists.
- Synthetic/demo data is labeled.
- Backup approach exists.
- Smoke tests pass.

No paid pilot unless:

- Operator setup console works.
- Page readiness checklist works.
- Proof/testimonial workflow works.
- Source tracking works.
- Weekly owner digest works.
- Support docs exist.
- At least one tutor has real data in the app.

## 14. Documentation Maintenance

Update these files after meaningful changes:

- `PROJECT_LOG.md`: current status, done, left, next action.
- `Learning_Studio_Production_Web_App_Accountable_Tasklist.md`: task status and acceptance.
- `TEAM_HANDOFF_START_HERE.md`: only when major direction changes.
- `README.md`: only when setup, run, deployment, or product overview changes.

## 15. Git Hygiene

Before starting a task:

```bash
git status --short
```

During work:

- Keep changes scoped to the task ID.
- Do not mix feature, formatting, and planning changes in one commit.
- Do not commit secrets, `.env`, database files, or local build outputs.
- Mention task IDs in commit messages when possible.

Suggested commit message format:

```text
<area>: <short action> (<task-id>)
```

Examples:

```text
docs: add production handoff guide (A-009)
frontend: build public studio route (C-003)
backend: add inquiry trial states (D-006)
```

## 16. Current Handoff State

Planning state:

- Feature strategy exists.
- Persona mapping exists.
- Selected MVP heatmap exists.
- Production accountable tasklist exists.
- This team handoff guide now exists.

Implementation state:

- Prototype exists.
- Productionization has not yet started from the new tasklist.
- Current implementation should be audited before major rewrites.

Recommended next action:

Start with task `C-001` and `D-001` in parallel:

- Audit frontend architecture.
- Audit backend models/APIs.

Then lock:

- `D-002` tenant/account model.
- `E-001` auth approach.
- `N-001` hosting architecture.

Only after those are clear should the team begin large implementation changes.
