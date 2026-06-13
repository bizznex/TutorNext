# Learning Studio Production Web App Accountable Tasklist

Date: 2026-06-07

Product: BizzNexx Learning Studio

Objective: build a fully functioning, production-ready, mobile and browser web app for tutors, private trainers, coaches, hobby instructors, and corporate trainers, with WhatsApp at the core and integrations across Instagram, YouTube, LinkedIn, Google Forms, and supporting growth channels.

Execution standard: productionized means secure, responsive, observable, deployable, supportable, legally safer, integration-ready, and usable by real tutors with real parent/student/client data.

## 1. Product North Star

BizzNexx Learning Studio should help a tutor or trainer run and grow their business without losing focus on teaching.

The app should own:

- Public trust presence.
- Structured inquiry capture.
- WhatsApp-first follow-up.
- Trial/demo conversion.
- Student/learner/client memory.
- Batch, schedule, and capacity visibility.
- Fee/package/session tracking.
- Proof, testimonials, referrals, and social growth.
- Owner action dashboard.
- Operator-assisted setup and quality control.
- Integration with growth and content channels.

The app should not lead with:

- Full LMS.
- Marketplace lead guarantees.
- Parent/student mobile apps.
- Heavy ERP workflows.
- Payment gateway dependency.
- Automated WhatsApp API before manual flow is validated.

## 2. Production Definition of Done

The product is production-ready only when all of these are true:

- Mobile and desktop web app work reliably across current Chrome, Safari, Edge, and Android/iOS browsers.
- Public pages are shareable, fast, SEO-ready, and trustworthy.
- Owner/operator dashboards are authenticated and not publicly exposed.
- Real inquiry, lead, trial, payment, proof, and message workflows persist in the backend.
- WhatsApp handoff works manually from day one.
- WhatsApp Business Cloud API path is designed and can be enabled after Meta setup and approval.
- Instagram, YouTube, LinkedIn, and Google Forms integrations have clear MVP scopes, OAuth/app-review plans, fallback modes, and data ownership rules.
- Data privacy, consent, deletion, audit, backup, and access control are handled.
- There is a staging environment, production environment, backup process, monitoring, and regression test suite.
- Every feature has an owner, priority, acceptance criteria, and validation signal.

## 3. Accountability Model

### Owner Roles

| Role Code | Role | Accountability |
| --- | --- | --- |
| PROD | Product Owner | Scope, user journeys, priority, acceptance criteria |
| UX | Product Design | Mobile-first UX, visual system, accessibility, copy quality |
| FE | Frontend Engineering | Responsive app, state management, web performance, browser QA |
| BE | Backend Engineering | APIs, models, workflow logic, permissions, integrations |
| DATA | Data/Analytics | Event taxonomy, dashboards, cohort metrics, exports |
| OPS | BizzNexx Operator | Assisted setup workflow, content readiness, pilot operations |
| QA | Quality Engineering | Test planning, manual QA, automated regression, release gates |
| SEC | Security/Privacy | Auth, authorization, privacy, consent, audit, compliance |
| GTM | Growth/Marketing | Positioning, social integrations, content flows, launch support |
| SUPPORT | Customer Support | Help docs, issue handling, onboarding support, feedback loop |

### Status Values

| Status | Meaning |
| --- | --- |
| Not Started | No active work yet |
| Discovery | Requirements or technical research underway |
| Designed | UX/API/data contract is ready |
| In Build | Implementation underway |
| In Review | PR/design/content review underway |
| In QA | Functional, responsive, security, or integration QA underway |
| Blocked | Waiting on dependency, access, approval, or decision |
| Done | Meets acceptance criteria and is deployed or ready to deploy |

### Priority Values

| Priority | Meaning |
| --- | --- |
| P0 | Required for private beta with real users |
| P1 | Required for paid pilot and retention |
| P2 | Required for scale and multi-segment expansion |
| P3 | Later or only if validated by demand |

## 3A. Execution Cursor

This section shows where the team should start. Update it whenever the active slice changes.

Current active phase:

Slice 0: Foundation Cleanup.

Current active objective:

Prepare the current prototype for production work without rewriting blindly.

Current active tasks:

| Task ID | Task | Owner | Priority | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| C-001 | Audit current frontend architecture | FE | P0 | Not Started | Identify routes, state, API usage, design debt, responsive gaps |
| D-001 | Audit current backend models/APIs | BE | P0 | Not Started | Identify model gaps, workflow gaps, auth gaps, migration risks |
| A-004 | Map public visitor journey | PROD/UX | P0 | Not Started | Align public page, inquiry, WhatsApp, trial CTA |
| A-005 | Map owner inquiry-to-fee journey | PROD/UX | P0 | Not Started | Align lead, trial, enrollment, fee, proof, action queue |
| D-002 | Define tenant/account model | BE/SEC | P0 | Not Started | Must be decided before real multi-user production work |
| E-001 | Choose auth approach | SEC/BE | P0 | Not Started | Must be decided before owner/operator dashboard hardening |
| N-001 | Choose production hosting architecture | BE/FE/SEC | P0 | Not Started | Must be decided before staging/production setup |

Do not start large new implementation work until `C-001`, `D-001`, `D-002`, `E-001`, and `N-001` are resolved.

Current build constraint:

Use the selected MVP heatmap in section `4A`. If a proposed task does not support the selected MVP spine, defer it unless it is required for security, deployment, or data integrity.

## 4. Workstream A: Product Scope and Journey Architecture

Goal: freeze the production product shape before engineering expands.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| A-001 | Define production personas: academic tutor, exam coach, hobby teacher, skill trainer, corporate trainer, fitness/yoga/sports trainer | P0 | PROD | Not Started | Persona definitions and priority order are documented |
| A-002 | Freeze first production persona as P-AST Academic School Tutor | P0 | PROD | Not Started | Product, data, and beta scripts all reference this as first ICP |
| A-003 | Define second persona expansion path: P-HBY or P-CEX | P1 | PROD | Not Started | Decision criteria and trigger metrics are documented |
| A-004 | Map public visitor journey from share link to inquiry | P0 | PROD/UX | Not Started | Journey includes trust, course fit, fee clarity, trial CTA, and confirmation |
| A-005 | Map owner journey from inquiry to trial to enrollment to fee tracking | P0 | PROD/UX | Not Started | Every owner step has status, next action, and message template |
| A-006 | Map operator setup journey from intake to ready-to-share | P0 | PROD/OPS | Not Started | Setup checklist has required, optional, and quality-gate items |
| A-007 | Define out-of-scope list for production beta | P0 | PROD | Not Started | LMS, marketplace leads, heavy ERP, parent app, and gateway dependency are explicitly deferred |
| A-008 | Define success metrics for beta, paid pilot, and production launch | P0 | PROD/DATA | Not Started | Metrics include share rate, inquiry completeness, trial conversion, fee tracking, owner WAU |
| A-009 | Create release naming: Alpha, Private Beta, Paid Pilot, Public Launch | P0 | PROD | Not Started | Each stage has entry and exit criteria |

## 4A. Selected MVP Feature vs Persona Heatmap

This heatmap is the selected MVP feature constraint. It should override the broader feature universe when deciding what enters the first production build.

Legend:

- Critical: build as a first-class workflow for that persona.
- Useful: support the workflow, but do not over-customize for first release.
- Low: do not optimize for this persona in MVP unless needed by another persona.

| MVP Feature | Academic Tutor (P-AST) | Exam Coach (P-CEX) | Hobby Teacher (P-HBY) | Skill Trainer (P-SKL) | Fitness Trainer (P-FIT) | Corporate Trainer (P-COR) |
| --- | --- | --- | --- | --- | --- | --- |
| Public Trust Page | Critical | Critical | Critical | Critical | Useful | Low |
| Structured Inquiry Form | Critical | Critical | Critical | Critical | Critical | Useful |
| WhatsApp Handoff/Template | Critical | Critical | Critical | Critical | Critical | Critical |
| Trial/Demo Workflow | Critical | Critical | Useful | Critical | Useful | Useful |
| Student/Learner Memory | Critical | Useful | Critical | Critical | Critical | Low |
| Monthly Fee Tracker | Critical | Critical | Critical | Useful | Critical | Useful |
| Owner Action Queue | Useful | Critical | Useful | Critical | Useful | Low |
| Testimonials/Proof Section | Critical | Critical | Critical | Critical | Useful | Useful |
| Parent/Client FAQ | Critical | Critical | Critical | Useful | Critical | Low |
| Privacy/Consent Controls | Critical | Useful | Critical | Useful | Useful | Low |

### Heatmap Implications

- P-AST Academic Tutor remains the best first persona because almost every selected MVP feature is Critical.
- P-CEX Exam Coach is the strongest second persona if the product leans toward batch launches, exam urgency, and proof.
- P-HBY Hobby Teacher is also strong, especially where trial/demo, proof, and monthly class fees matter.
- P-SKL Skill Trainer is a strong adjacent fit, but the MVP should avoid overbuilding adult learner/certification workflows early.
- P-FIT Fitness Trainer is usable through the same inquiry, WhatsApp, fee, memory, and FAQ spine, but should not define the first release.
- P-COR Corporate Trainer should remain a later variant because proposal, invoice, certificate, B2B reporting, and decision-maker workflows are different enough to add scope.

### MVP Build Bias

The first production release should bias toward features that are Critical for at least three of the first four personas:

1. WhatsApp Handoff/Template.
2. Structured Inquiry Form.
3. Public Trust Page.
4. Testimonials/Proof Section.
5. Monthly Fee Tracker.
6. Trial/Demo Workflow.
7. Student/Learner Memory.
8. Parent/Client FAQ.
9. Privacy/Consent Controls.
10. Owner Action Queue.

### Persona Expansion Rule

Do not add persona-specific complexity unless the feature is:

- Critical for P-AST and at least one of P-CEX, P-HBY, or P-SKL.
- Reusable across the shared business workflow.
- Useful without requiring the product to become a full LMS, ERP, or social media scheduler.

## 5. Workstream B: UX, Design System, and Responsive Experience

Goal: build a professional web app that opens cleanly on mobile and desktop.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| B-001 | Define visual direction: calm, trustworthy, mobile-first, India-local, parent-friendly | P0 | UX | Not Started | Moodboard/design principles approved |
| B-002 | Create responsive layout system for public page, owner dashboard, and operator console | P0 | UX/FE | Not Started | Works at 360px, 390px, 768px, 1024px, 1440px |
| B-003 | Define typography, spacing, button, form, card, table, tag, status, and empty-state components | P0 | UX/FE | Not Started | Components are documented and reused |
| B-004 | Build mobile-first navigation for owner dashboard | P0 | UX/FE | Not Started | Owner can access Today, Leads, Trials, Students, Fees, Messages, Proof |
| B-005 | Build public page trust hierarchy | P0 | UX | Not Started | Parent understands teacher, fit, fee, timing, trial, and next step in 30 seconds |
| B-006 | Design inquiry form for thumb-friendly mobile completion | P0 | UX/FE | Not Started | Form is usable without zooming on mobile |
| B-007 | Design action cards for Today's Actions | P0 | UX/FE | Not Started | Every card has why it matters, suggested action, and status control |
| B-008 | Design fee tracker with polite reminder flow | P0 | UX/FE | Not Started | Owner sees due, overdue, part-paid, paid, deferred clearly |
| B-009 | Design proof/testimonial management UI | P1 | UX/FE | Not Started | Owner/operator can add, approve, hide, and publish proof |
| B-010 | Create accessibility checklist | P0 | UX/QA | Not Started | Contrast, focus states, labels, keyboard navigation, and screen reader basics pass |
| B-011 | Create responsive QA screenshot matrix | P0 | QA/UX | Not Started | All core screens checked across mobile and desktop widths |

## 6. Workstream C: Frontend Application

Goal: build the production web client.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| C-001 | Audit current frontend architecture | P0 | FE | Not Started | Current routes, state, API usage, and technical debt are documented |
| C-002 | Define route map: public page, inquiry, owner app, operator app, auth, settings | P0 | FE/PROD | Not Started | Route map approved |
| C-003 | Implement public studio page route | P0 | FE | Not Started | API-backed page renders with loading, error, and fallback states |
| C-004 | Implement tutor-specific inquiry flow | P0 | FE | Not Started | Inquiry submits successfully and creates backend lead |
| C-005 | Implement owner Today action dashboard | P0 | FE | Not Started | Owner sees actionable inquiry, trial, fee, and proof tasks |
| C-006 | Implement Leads and Trial workflow UI | P0 | FE | Not Started | Owner can update lead/trial statuses |
| C-007 | Implement Students/Learners client memory UI | P0/P1 | FE | Not Started | Owner can view learner context and next action |
| C-008 | Implement Fee Tracker UI | P0 | FE | Not Started | Owner can mark paid/part-paid/deferred and preview reminders |
| C-009 | Implement Message Templates UI | P0 | FE | Not Started | Owner can preview, edit, copy, and open WhatsApp message |
| C-010 | Implement Proof/Testimonial UI | P1 | FE | Not Started | Owner/operator can manage proof items |
| C-011 | Implement Operator Setup Console | P0 | FE | Not Started | Operator can track readiness and missing inputs |
| C-012 | Implement settings for public visibility and contact options | P1 | FE | Not Started | Owner can configure fee visibility, phone, WhatsApp, social links |
| C-013 | Add offline-tolerant UI states for bad network | P1 | FE | Not Started | User sees clear retry and draft-safe messaging |
| C-014 | Optimize bundle size and loading performance | P0 | FE | Not Started | Core public page reaches performance target on mobile |

## 7. Workstream D: Backend, Data Model, and Workflow Engine

Goal: make the product real, persistent, and scalable beyond seeded demos.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| D-001 | Audit current backend models and API endpoints | P0 | BE | Not Started | Existing models, gaps, and migration risks are documented |
| D-002 | Define tenant/account model | P0 | BE/SEC | Not Started | Multiple tutors/businesses can exist without data leakage |
| D-003 | Define Business/Profile model extensions | P0 | BE | Not Started | Supports persona, public slug, mode, languages, locality, social links |
| D-004 | Define Course/Batch/Program model | P0 | BE | Not Started | Supports academic, skill, hobby, fitness, corporate variants |
| D-005 | Define Inquiry model with persona-specific extra context | P0 | BE | Not Started | Academic, skill, corporate, fitness fields can be stored cleanly |
| D-006 | Define Lead and Trial workflow states | P0 | BE/PROD | Not Started | States cover new, contacted, trial proposed, scheduled, attended, enrolled, lost |
| D-007 | Define Student/Learner/Client model | P0 | BE | Not Started | Stores contact, context, enrollment, tags, notes, privacy-safe fields |
| D-008 | Define Enrollment and Fee Cycle model | P0 | BE | Not Started | Supports monthly fees, packages, sessions, part-paid, deferred, paid |
| D-009 | Define Proof/Testimonial model | P0/P1 | BE | Not Started | Supports type, attribution, approval, visibility, media URL |
| D-010 | Define Message Template model | P0 | BE | Not Started | Supports variables, workflow type, tone, language, persona |
| D-011 | Define Follow-up Task model | P0 | BE | Not Started | Generates action queue tasks with due dates and source objects |
| D-012 | Implement action generation rules | P0 | BE | Not Started | Inquiry creates response task; trial creates reminder/follow-up; fee due creates reminder |
| D-013 | Implement payment ageing logic | P0 | BE | Not Started | Due and overdue buckets are generated correctly |
| D-014 | Implement API permission checks | P0 | BE/SEC | Not Started | Owner cannot access another owner's data |
| D-015 | Implement admin/operator APIs | P0 | BE/OPS | Not Started | Operator can set up businesses with controlled access |
| D-016 | Create migration plan for current seed/demo data | P0 | BE | Not Started | Existing demo data survives or is recreated cleanly |

## 8. Workstream E: Authentication, Authorization, and Privacy

Goal: protect real parent/student/client data.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| E-001 | Choose auth approach for production | P0 | SEC/BE | Not Started | Decision covers email/password, OTP, or managed auth |
| E-002 | Implement owner login | P0 | BE/FE | Not Started | Owner dashboard requires authentication |
| E-003 | Implement operator/admin login | P0 | BE/FE | Not Started | Operator tools are protected |
| E-004 | Implement role-based access control | P0 | SEC/BE | Not Started | Roles include owner, operator, admin, support |
| E-005 | Add public/private visibility controls | P0 | BE/FE | Not Started | Owner can control public fee, testimonials, phone, location |
| E-006 | Add inquiry consent text and consent timestamp | P0 | SEC/FE/BE | Not Started | Every inquiry captures consent version and timestamp |
| E-007 | Create privacy policy | P0 | SEC/PROD | Not Started | Policy covers data collected, purpose, retention, deletion, contact |
| E-008 | Create terms and beta disclaimer | P0 | SEC/PROD | Not Started | Terms clarify no guaranteed leads/results/fee recovery |
| E-009 | Create data deletion workflow | P0 | SEC/BE/OPS | Not Started | Owner/operator can delete or anonymize user data on request |
| E-010 | Add audit trail for sensitive operator changes | P1 | SEC/BE | Not Started | Changes to public page, fees, proof, and contacts are logged |
| E-011 | Define DPDP Act alignment checklist for India | P0 | SEC | Not Started | Consent, purpose limitation, access, deletion, and minor data handling are documented |
| E-012 | Define backup and restore policy | P0 | SEC/BE | Not Started | Recovery point and recovery time targets are documented |

## 9. Workstream F: WhatsApp Core Integration

Goal: make WhatsApp the primary business workflow without making API automation a launch blocker.

### Fallback Strategy

Stage 1: manual WhatsApp handoff using prefilled links and copied templates.

Stage 2: WhatsApp Business Cloud API for approved accounts, templates, webhooks, and message status.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| F-001 | Implement manual WhatsApp click-to-chat links | P0 | FE | Not Started | Owner can open WhatsApp with prefilled message |
| F-002 | Implement copy-to-clipboard for all message templates | P0 | FE | Not Started | Owner can copy message if click-to-chat fails |
| F-003 | Create WhatsApp template library for tutor workflows | P0 | PROD/OPS | Not Started | Includes first response, trial, reminder, fee, progress, testimonial, referral |
| F-004 | Add template variable system | P0 | BE/FE | Not Started | Variables include name, class, subject, batch, fee, due date, slot |
| F-005 | Track prepared/sent status manually | P0 | FE/BE | Not Started | Owner can mark message sent and update next status |
| F-006 | Design WhatsApp Business Cloud API architecture | P1 | BE | Not Started | Includes phone_number_id, access token, webhook verification, message sending, statuses |
| F-007 | Create Meta app and WhatsApp Business setup checklist | P1 | BE/OPS | Not Started | Steps for Business Manager, app, phone number, webhook, permissions are documented |
| F-008 | Implement webhook endpoint for incoming WhatsApp events | P1 | BE | Not Started | Endpoint verifies challenge and routes events to tenant |
| F-009 | Implement outbound message service abstraction | P1 | BE | Not Started | Manual, Cloud API, and future providers can share interface |
| F-010 | Implement message template approval workflow tracking | P1 | OPS/BE | Not Started | Template status is tracked: draft, submitted, approved, rejected |
| F-011 | Implement delivery/read status display | P2 | BE/FE | Not Started | Owner can see status only when API integration is active |
| F-012 | Add opt-in and opt-out handling | P1 | SEC/BE | Not Started | WhatsApp messaging respects consent and opt-out |
| F-013 | Add rate-limit and retry policy | P1 | BE | Not Started | Failed sends retry safely and do not spam |

## 10. Workstream G: Instagram Integration

Goal: help tutors use Instagram for trust, proof, and inquiry capture without overpromising automation.

### MVP Strategy

Stage 1: social link, Instagram profile embed/link, campaign UTM tracking, manual content prompts.

Stage 2: Instagram Graph API for Business/Creator accounts where app review and permissions allow.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| G-001 | Add Instagram profile link to public page | P0 | FE/BE | Not Started | Public page displays Instagram when configured |
| G-002 | Add inquiry source value for Instagram | P0 | BE/FE | Not Started | Leads from Instagram links are tagged correctly |
| G-003 | Generate Instagram bio link and caption suggestions | P1 | GTM/FE | Not Started | Owner gets shareable copy for bio and posts |
| G-004 | Add campaign UTM builder for Instagram posts/stories | P1 | FE/BE/DATA | Not Started | Campaign source is tracked |
| G-005 | Create proof-to-Instagram content prompt | P1 | GTM/OPS | Not Started | Testimonial/result can become caption draft |
| G-006 | Research Instagram API permissions and app review needs | P1 | BE/SEC | Not Started | Required scopes, limitations, and fallback are documented |
| G-007 | Implement OAuth connection for Instagram Business/Creator accounts | P2 | BE/FE | Not Started | Owner can connect account in staging |
| G-008 | Pull basic profile/media insights where permitted | P2 | BE/DATA | Not Started | Connected account metrics appear in growth dashboard |
| G-009 | Publish/schedule content only after permission validation | P3 | BE/FE | Not Started | No production publish feature until app review and policy path are clear |
| G-010 | Add integration health status | P2 | BE/FE | Not Started | Owner sees connected, expired, permission missing, or action required |

## 11. Workstream H: YouTube Integration

Goal: let tutors showcase teaching videos, playlists, testimonials, and workshop recordings.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| H-001 | Add YouTube channel/video/playlist links to public page | P0/P1 | FE/BE | Not Started | Owner can add links and public page renders them safely |
| H-002 | Add course-specific YouTube resource links | P1 | FE/BE | Not Started | Course cards can show relevant demo/resource videos |
| H-003 | Add YouTube source tracking for inquiries | P1 | DATA/BE | Not Started | Leads from YouTube links are tagged |
| H-004 | Research YouTube Data API quota, OAuth, and API key requirements | P1 | BE | Not Started | API usage, quota risks, and fallback are documented |
| H-005 | Pull channel/video metadata using YouTube Data API | P2 | BE | Not Started | Title, thumbnail, playlist, and video metadata are cached |
| H-006 | Create "teaching proof video" section | P1 | UX/FE | Not Started | Public page can show selected videos without clutter |
| H-007 | Add video content quality checklist for operators | P1 | OPS/GTM | Not Started | Operator knows what videos are safe and useful to feature |
| H-008 | Add YouTube performance metrics later | P2 | DATA/BE | Not Started | Views/engagement shown only after proper API integration |

## 12. Workstream I: LinkedIn Integration

Goal: support corporate trainers, higher-education tutors, and professional skill trainers.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| I-001 | Add LinkedIn profile/company page link to public page | P1 | FE/BE | Not Started | Public page displays LinkedIn when configured |
| I-002 | Add LinkedIn source tracking for inquiries | P1 | DATA/BE | Not Started | Leads from LinkedIn campaign links are tagged |
| I-003 | Create LinkedIn-ready testimonial/case-study copy generator | P1 | GTM/FE | Not Started | Owner can produce professional proof copy |
| I-004 | Create corporate trainer landing page variant | P2 | UX/FE/PROD | Not Started | Page includes topics, outcomes, case studies, inquiry form |
| I-005 | Research LinkedIn Marketing API versioning and access tier requirements | P2 | BE/SEC | Not Started | Version header, app review, and access requirements are documented |
| I-006 | Implement LinkedIn OAuth only after clear use case | P3 | BE/FE | Not Started | OAuth is not built before reporting/publishing needs are validated |
| I-007 | Pull campaign/reporting metrics only after approval | P3 | BE/DATA | Not Started | Metrics respect LinkedIn API access and data storage requirements |

## 13. Workstream J: Google Forms and Google Workspace Integration

Goal: integrate with tutor workflows that already use Google Forms, Sheets, and simple feedback forms.

### MVP Strategy

Stage 1: native BizzNexx inquiry forms remain primary.

Stage 2: import/sync Google Forms responses for users who already have forms.

Stage 3: generate Google Forms for feedback, testimonials, or quizzes where useful.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| J-001 | Decide when to use native forms vs Google Forms | P0 | PROD/BE | Not Started | Native inquiry is primary; Google Forms is import/feedback integration |
| J-002 | Add external Google Form link support | P1 | FE/BE | Not Started | Owner can link existing form from public page if needed |
| J-003 | Add Google Forms source tracking | P1 | DATA/BE | Not Started | Imported or linked responses retain source |
| J-004 | Research Google Forms API OAuth and watches | P1 | BE | Not Started | Create/update/retrieve responses and push notification options documented |
| J-005 | Implement Google OAuth connection for Workspace | P2 | BE/FE/SEC | Not Started | Owner can connect Google account in staging |
| J-006 | Import Google Forms responses into inquiries | P2 | BE | Not Started | Responses map to inquiry fields with review step |
| J-007 | Generate testimonial/feedback Google Form | P2 | BE/FE | Not Started | Owner can create a feedback form from BizzNexx |
| J-008 | Sync selected data to Google Sheets | P2 | BE/DATA | Not Started | Owner can export leads/fees to Sheet with least-privilege scope |
| J-009 | Implement Google API retry/backoff and quota handling | P2 | BE | Not Started | 429/5xx errors handled safely |

## 14. Workstream K: Growth, Campaigns, and Content Operating Layer

Goal: help tutors grow without becoming full-time marketers.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| K-001 | Create batch launch campaign workflow | P1 | PROD/GTM/FE | Not Started | Owner can create campaign page/copy for new batch |
| K-002 | Create exam-season campaign workflow | P1 | PROD/GTM | Not Started | Academic/exam tutors get timely campaign templates |
| K-003 | Create workshop/demo week workflow | P1 | PROD/GTM | Not Started | Hobby/skill trainers can launch short campaigns |
| K-004 | Create referral request workflow | P1 | PROD/FE/BE | Not Started | Owner can request referrals after positive milestone |
| K-005 | Create testimonial request workflow | P1 | PROD/FE/BE | Not Started | Owner can request, approve, and publish testimonials |
| K-006 | Create content calendar prompts | P2 | GTM/FE | Not Started | Owner sees weekly suggestions for Instagram, YouTube, LinkedIn |
| K-007 | Create local SEO checklist | P1 | GTM/OPS | Not Started | Page has locality, service keywords, schema-ready content |
| K-008 | Add UTM builder for all social campaigns | P1 | DATA/FE/BE | Not Started | Campaign links are generated and tracked |
| K-009 | Add lead source dashboard | P1 | DATA/FE | Not Started | Owner sees which channel creates inquiries |

## 15. Workstream L: Analytics and Business Intelligence

Goal: measure whether the product actually helps the tutor grow.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| L-001 | Define event taxonomy | P0 | DATA/PROD | Not Started | Events cover page view, CTA click, inquiry, trial, fee, message, proof |
| L-002 | Implement page view tracking | P0 | DATA/FE/BE | Not Started | Public page views are recorded by business and source |
| L-003 | Implement CTA click tracking | P0 | DATA/FE | Not Started | WhatsApp, inquiry, social, video clicks are tracked |
| L-004 | Implement inquiry conversion tracking | P0 | DATA/BE | Not Started | Page view to inquiry rate is measurable |
| L-005 | Implement trial funnel metrics | P1 | DATA/BE | Not Started | Inquiry to trial to enrolled is measurable |
| L-006 | Implement fee discipline metrics | P1 | DATA/BE | Not Started | Expected, collected, overdue, and ageing are measurable |
| L-007 | Implement source performance dashboard | P1 | DATA/FE | Not Started | Owner sees source-wise lead volume and quality |
| L-008 | Implement weekly owner digest | P1 | DATA/BE/FE | Not Started | Owner sees actions, inquiries, trials, fees, and proof prompts |
| L-009 | Implement operator portfolio dashboard | P1 | OPS/DATA/FE | Not Started | Operator sees readiness, active accounts, risk accounts |
| L-010 | Define privacy-safe analytics retention policy | P0 | DATA/SEC | Not Started | Personal data is minimized in analytics events |

## 16. Workstream M: QA, Testing, and Release Gates

Goal: avoid launching a beautiful but brittle product.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| M-001 | Create backend unit tests for inquiry-to-lead-to-task | P0 | QA/BE | Not Started | Tests pass in CI |
| M-002 | Create backend tests for trial status transitions | P0 | QA/BE | Not Started | Invalid transitions are blocked |
| M-003 | Create backend tests for fee ageing and payment states | P0 | QA/BE | Not Started | Due/overdue/paid/part-paid logic passes |
| M-004 | Create backend tests for tenant isolation | P0 | QA/SEC/BE | Not Started | Cross-tenant access attempts fail |
| M-005 | Create frontend smoke tests for public page | P0 | QA/FE | Not Started | Page loads and CTA works |
| M-006 | Create frontend smoke tests for inquiry submission | P0 | QA/FE | Not Started | Inquiry creates lead and confirmation |
| M-007 | Create frontend smoke tests for owner dashboard | P0 | QA/FE | Not Started | Owner can see and update actions |
| M-008 | Create responsive visual QA checklist | P0 | QA/UX | Not Started | Mobile and desktop layouts pass |
| M-009 | Create accessibility QA checklist | P0 | QA/UX | Not Started | Keyboard, labels, focus, contrast pass |
| M-010 | Create integration mock tests | P1 | QA/BE | Not Started | WhatsApp/Google/YouTube failures do not break core app |
| M-011 | Create release blocker checklist | P0 | QA/PROD | Not Started | No release without auth, privacy, backup, tests, mobile QA |
| M-012 | Create regression suite in CI | P0 | QA/BE/FE | Not Started | Tests run on every PR/main build |

## 17. Workstream N: Infrastructure, Deployment, and Operations

Goal: make the app deployable, monitorable, and recoverable.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| N-001 | Choose production hosting architecture | P0 | BE/FE/SEC | Not Started | Frontend, backend, database, static assets, and domain plan approved |
| N-002 | Create staging environment | P0 | BE/FE | Not Started | Staging mirrors production configuration |
| N-003 | Create production environment | P0 | BE/FE | Not Started | HTTPS, env vars, database, and domain configured |
| N-004 | Configure database backups | P0 | BE/SEC | Not Started | Automated backups and restore test exist |
| N-005 | Configure logs and error monitoring | P0 | BE/FE | Not Started | Backend and frontend errors are visible |
| N-006 | Configure uptime monitoring | P0 | BE/OPS | Not Started | Downtime alerts are sent |
| N-007 | Configure CI/CD pipeline | P0 | BE/FE/QA | Not Started | Tests run and deploys are repeatable |
| N-008 | Configure secrets management | P0 | SEC/BE | Not Started | API keys and tokens are not stored in code |
| N-009 | Configure custom domain and HTTPS | P0 | BE/OPS | Not Started | Production URL is stable and secure |
| N-010 | Create rollback plan | P0 | BE/QA | Not Started | Failed deploy can be reverted |
| N-011 | Create database migration plan | P0 | BE | Not Started | Migrations are tested before production |

## 18. Workstream O: Operator Console and Assisted Setup

Goal: make BizzNexx setup repeatable and quality-controlled.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| O-001 | Build operator intake checklist | P0 | OPS/FE/BE | Not Started | Captures teacher profile, courses, proof, fees, trial policy, FAQs |
| O-002 | Build page readiness score | P0/P1 | OPS/BE/FE | Not Started | Score reflects missing trust-critical content |
| O-003 | Build launch blocker checklist | P0 | OPS/PROD | Not Started | Operator cannot mark ready if key fields are missing |
| O-004 | Build synthetic vs real data indicator | P0 | OPS/FE/BE | Not Started | Demo data is visibly labeled |
| O-005 | Build operator notes and internal status | P1 | OPS/BE/FE | Not Started | Internal notes do not appear publicly |
| O-006 | Build second-account setup workflow | P1 | OPS/PROD | Not Started | Operator can set up a second tutor in under 90 minutes |
| O-007 | Create setup scripts/templates | P1 | OPS | Not Started | Intake forms, message scripts, proof prompts are reusable |

## 19. Workstream P: Support, Documentation, and Training

Goal: make users successful without constant founder intervention.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| P-001 | Create owner onboarding guide | P0 | SUPPORT/OPS | Not Started | Tutor can understand first 5 actions |
| P-002 | Create operator setup guide | P0 | OPS/SUPPORT | Not Started | Operator can set up a tutor step-by-step |
| P-003 | Create WhatsApp message tone guide | P0 | PROD/SUPPORT | Not Started | Templates stay polite, clear, and relationship-safe |
| P-004 | Create FAQ for privacy and parent data | P0 | SEC/SUPPORT | Not Started | User can answer common trust questions |
| P-005 | Create issue reporting channel | P0 | SUPPORT/OPS | Not Started | Beta users can report bugs and feedback |
| P-006 | Create release notes template | P1 | SUPPORT/PROD | Not Started | Users know what changed |
| P-007 | Create integration troubleshooting docs | P2 | SUPPORT/BE | Not Started | WhatsApp, Google, Instagram, YouTube, LinkedIn issues have runbooks |

## 20. Workstream Q: Commercial Packaging and Go-To-Market Readiness

Goal: package the app so tutors understand why they should pay.

| ID | Task | Priority | Owner | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| Q-001 | Define Launch Pack offer | P0 | GTM/PROD | Not Started | Setup scope and price range are clear |
| Q-002 | Define Monthly Assist Pack | P0/P1 | GTM/PROD | Not Started | Monthly value includes updates, dashboard, fee/follow-up support |
| Q-003 | Define Higher-Touch Pack | P1 | GTM/PROD | Not Started | Operator-assisted proof/campaign/review support is priced |
| Q-004 | Create sales demo script | P0 | GTM/PROD | Not Started | Demo shows page, inquiry, trial, fee, proof, dashboard |
| Q-005 | Create beta pricing test questions | P0 | GTM | Not Started | Questions test setup and monthly willingness to pay |
| Q-006 | Create pilot contract or agreement | P0 | SEC/GTM | Not Started | Scope, data, support, payment, and disclaimers are documented |
| Q-007 | Create case study template | P1 | GTM/OPS | Not Started | Pilot results can become proof |
| Q-008 | Create referral offer for tutors | P1 | GTM | Not Started | Referral economics are clear and not overpromised |

## 21. Workstream R: Security Review and Risk Register

Goal: identify what can hurt users, the business, or product trust.

| ID | Risk | Priority | Owner | Mitigation |
| --- | --- | --- | --- | --- |
| R-001 | Parent/student data leakage | P0 | SEC/BE | Tenant isolation, auth, access control, audit logs |
| R-002 | Public dashboard exposure | P0 | SEC/FE/BE | Auth gates and route protection |
| R-003 | WhatsApp spam perception | P0 | PROD/SEC | Manual send, opt-in, opt-out, polite templates |
| R-004 | Tutors expect guaranteed leads | P0 | GTM/PROD | Position as conversion/operations layer, not lead guarantee |
| R-005 | Meta app review delays | P1 | BE/OPS | Manual WhatsApp fallback and staged integration |
| R-006 | Google/LinkedIn OAuth complexity | P2 | BE/SEC | Build only after clear value and least-privilege scopes |
| R-007 | Scope drift into LMS | P0 | PROD | Product decision rules and release gate |
| R-008 | Payment compliance confusion | P1 | SEC/PROD | Track payment status first; gateway later |
| R-009 | Poor mobile performance | P0 | FE/QA | Performance budgets and mobile QA |
| R-010 | Synthetic data mistaken as real | P0 | OPS/FE | Demo labels and production data separation |

## 22. MVP Release Slices

### Slice 0: Foundation Cleanup

Goal: prepare current prototype for production work.

- Audit frontend/backend.
- Define final models and routes.
- Create auth plan.
- Create staging environment.
- Create design system baseline.

Exit criteria:

- Product, technical, and deployment plans are aligned.

### Slice 1: Share-Ready Public Page

Goal: tutor can share one professional link.

- Public profile.
- Course/batch catalogue.
- Proof/testimonial section.
- FAQ.
- Trial CTA.
- WhatsApp CTA.
- Mobile polish.

Exit criteria:

- A tutor says they would share the page with parents/learners.

### Slice 2: Inquiry and WhatsApp Follow-Up

Goal: parent/client inquiry becomes a real owner action.

- Structured inquiry.
- Lead creation.
- Suggested WhatsApp response.
- Status update.
- Inquiry confirmation.
- Source tracking.

Exit criteria:

- Owner can respond without asking basic repeated questions.

### Slice 3: Trial and Enrollment Workflow

Goal: reduce missed trial/demo conversions.

- Trial proposed/scheduled/reminder/attended/no-show.
- Post-trial follow-up.
- Enrolled/lost/follow later statuses.
- Lost reason tracking.

Exit criteria:

- Owner can see every trial needing action.

### Slice 4: Fee and Business Memory

Goal: protect recurring revenue.

- Student/learner memory.
- Enrollment.
- Monthly fee/package/session tracker.
- Due/overdue actions.
- Polite reminders.

Exit criteria:

- Owner knows who owes fees and what message to send.

### Slice 5: Proof, Referral, and Growth

Goal: convert good teaching into growth assets.

- Testimonial request.
- Referral request.
- Proof approval.
- Campaign links.
- Source dashboard.

Exit criteria:

- Owner has a repeatable proof and referral loop.

### Slice 6: Integrations

Goal: connect external channels safely.

- WhatsApp manual handoff.
- WhatsApp Cloud API readiness.
- Instagram link and source tracking.
- YouTube showcase.
- LinkedIn link and corporate variant.
- Google Forms import/export path.

Exit criteria:

- Integrations improve workflow without breaking core product.

## 23. Launch Gates

### Private Beta Gate

Required:

- Public page mobile-ready.
- Inquiry creates lead and task.
- Owner auth exists.
- Owner Today dashboard works.
- WhatsApp manual handoff works.
- Trial workflow works.
- Fee tracker works.
- Privacy, consent, and beta disclaimer exist.
- Dashboard is not public.
- Backups exist.
- Smoke tests pass.

### Paid Pilot Gate

Required:

- Operator setup console works.
- Page readiness score works.
- Proof/testimonial workflow works.
- Source tracking works.
- Weekly owner digest works.
- Support docs exist.
- Payment/fee tracking is stable.
- At least one tutor has real data in the app.

### Public Launch Gate

Required:

- Multi-tenant isolation verified.
- Production monitoring and rollback verified.
- Security review complete.
- Data deletion flow tested.
- Integration fallbacks documented.
- Pricing and onboarding are clear.
- Repeatable setup time under 90 minutes for target persona.

## 24. External Platform Notes

### WhatsApp

Manual WhatsApp handoff should launch first. WhatsApp Business Cloud API should be staged because it needs Meta setup, phone number configuration, access tokens, webhooks, templates, status handling, opt-in/opt-out, and operational monitoring.

### Instagram

Start with profile links, UTM tracking, content prompts, and proof reuse. API-based publishing or insights should come later because Instagram API access depends on account type, permissions, and app review.

### YouTube

Start by displaying selected videos/playlists and tracking clicks. API-based metadata and analytics can come later with API key/OAuth and quota controls.

### LinkedIn

Start with LinkedIn profile/company links and corporate trainer copy. API-based reporting or campaign features should be deferred until a corporate trainer persona is commercially validated.

### Google Forms

Native BizzNexx forms should remain primary. Google Forms should support import/sync for existing tutor workflows and feedback/testimonial forms later. Google Forms API supports creating/updating forms, retrieving responses, and push notifications, so it is useful for feedback and legacy form migration.

## 25. Official Documentation References

- WhatsApp Cloud API overview: https://developers.facebook.com/docs/whatsapp/cloud-api/
- Instagram Platform / Instagram API: https://developers.facebook.com/docs/instagram-platform/
- YouTube Data API reference: https://developers.google.com/youtube/v3/docs/
- Google Forms API overview: https://developers.google.com/workspace/forms/api/guides
- Google Forms API reference: https://developers.google.com/forms/api/reference/rest
- Google Sheets API documentation: https://developers.google.com/workspace/sheets/api
- LinkedIn Marketing API Program: https://learn.microsoft.com/en-us/linkedin/marketing/
- LinkedIn Marketing API versioning: https://learn.microsoft.com/en-us/linkedin/marketing/versioning

## 26. Immediate Next 20 Tasks

These should become the first active execution board.

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

## 27. Strategic Verdict

The production app should be built in layers:

1. First, make one tutor share-worthy and operationally organized.
2. Then make inquiry, WhatsApp follow-up, trial, fee, and proof workflows reliable.
3. Then add source tracking and growth loops.
4. Then add external integrations carefully, with fallbacks and permissions.
5. Then scale to more personas and stronger automation.

The deepest product moat is not a long feature list. It is a trusted, India-aware operating rhythm that turns a tutor's existing demand into structured follow-up, enrollment, fee discipline, proof, and referrals.
