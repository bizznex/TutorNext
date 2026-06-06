# Learning Studio Beta Rollout Readiness Plan

## 1. Objective

Roll out the Learning Studio version of BizzNexx to beta users as soon as it is genuinely ready.

The target is not a broad public launch. The target is a polished, trustworthy, selected-user beta where a real tutor can say:

- "I would share this page with parents."
- "This captures inquiries better than WhatsApp alone."
- "This helps me remember trials and follow-ups."
- "This makes fee reminders less awkward."
- "I can understand why I would pay for setup and monthly support."

The standard should be high. "OpenAI, Anthropic, or Microsoft level" does not mean overbuilding a huge platform before beta. It means the beta must feel:

- Clear
- Trustworthy
- Fast
- Safe
- Beautifully simple
- Useful in the first session
- Honest about what it does and does not do

## 2. Current State

### 2.1 What Is Strong

Business and product thinking:

- Learning Studio ontology exists.
- Business strategy plan exists.
- Execution action plan exists.
- Ananya Learning Studio is selected as the validation anchor.
- The product boundary is clear: not LMS, not ERP, not payment gateway, not lead guarantee.
- The core loop is clear: public page -> inquiry -> trial follow-up -> enrollment -> monthly fee tracking.

Technical foundation:

- React frontend exists.
- Django backend exists.
- SQLite persistence exists.
- Core models exist: Business, Catalogue, CatalogueItem, TrustProof, FAQ, Testimonial, Inquiry, Lead, FollowUpTask, Customer, Payment, MessageTemplate, SetupProject, PageEvent, ScoreReason.
- API-backed business records exist.
- Inquiry capture creates Inquiry and Lead.
- Inquiry capture creates follow-up task.
- Lead status updates persist.
- Payment mark-paid actions persist.
- Operator setup stage persists.
- Frontend falls back to sample/local data if API is unavailable.

Product foundation:

- Public catalogue preview exists.
- Owner Today view exists.
- Leads view exists.
- Payments view exists.
- Messages view exists.
- Insights view exists.
- Operator setup view exists.
- Persona packs exist.

### 2.2 What Is Not Yet Beta-Ready

The main remaining gap is not the existence of screens. It is the quality and specificity of the Learning Studio experience.

Current risk:

The product may function, but still feel like a prototype catalogue rather than a share-worthy business system for a real tutor.

Missing or weak:

- Learning Studio-specific public page structure
- Parent-first trust hierarchy
- Rich Ananya seed data
- Tutor-specific inquiry UX
- Trial workflow clarity
- Enrolled student and fee cycle clarity
- Follow-up ageing and urgency
- Message templates that feel natural
- Operator readiness checklist quality
- Privacy, consent, terms, and beta-safe disclaimers
- Authentication/access control for real beta data
- Production deployment
- Regression tests and launch checks
- Mobile polish and visual QA

## 3. Product Quality Bar

### 3.1 What "Top-Tier" Means for This Beta

Top-tier product quality for this beta means:

- The product does one narrow job extremely clearly.
- Every screen has an obvious purpose.
- Every piece of data earns its place.
- The language matches the user's real world.
- No inflated claims are made.
- The user knows what happens next.
- The experience works beautifully on a phone.
- The owner can act without training.
- The parent can trust without reading too much.
- The beta handles privacy and consent responsibly.

### 3.2 What It Does Not Mean Yet

It does not mean:

- Full LMS
- Enterprise ERP
- Advanced AI automation
- Multi-tenant scale architecture
- Marketplace lead generation
- Automated WhatsApp Business API
- Payment gateway
- Complex analytics
- Mobile app store release

Those are later. The beta must earn the right to expand.

## 4. Beta Scope

### 4.1 Included in Beta

One persona:

- Learning Studio / Tutor / Coach

One flagship demo:

- Ananya Learning Studio

Core user journeys:

- Parent views public page
- Parent submits structured inquiry
- Owner receives parent inquiry action
- Owner sends or previews WhatsApp response
- Trial is scheduled or followed up
- Enrollment creates monthly fee expectation
- Fee due/overdue appears in owner dashboard
- Owner sends payment reminder
- Operator verifies setup readiness

### 4.2 Excluded From Beta

Do not include:

- Bridal studio rollout
- Design agency rollout
- Attendance
- Homework
- Live class links
- Student portal
- Parent portal
- Payment gateway
- GST or invoice module
- Full WhatsApp automation
- AI-generated claims about student outcomes
- Self-serve onboarding for unknown public users

## 5. What Is Left To Be Done

### 5.1 Product and Content

P0 tasks:

- Rewrite Ananya page copy to be parent-first.
- Add richer teacher profile: experience, qualification, teaching style, parent reassurance.
- Add class/board/subject proof of fit.
- Add 3 strong course cards with timings, fee policy, trial policy, and parent outcome.
- Add "what happens after inquiry" section.
- Add tutor-specific FAQ.
- Add safe testimonials and result proof.
- Add trial slot options.
- Add parent concern examples in seeded leads.
- Add clear beta/demo label where synthetic data is used.

P1 tasks:

- Add progress update examples.
- Add parent referral prompt.
- Add exam-season messaging.
- Add optional fee visibility settings: exact fee, starting fee, range, contact for fee.

### 5.2 UI and Interaction

P0 tasks:

- Redesign public page for Learning Studio specifically.
- Improve mobile layout and spacing.
- Make CTA hierarchy clear: inquire, WhatsApp, trial.
- Build tutor-specific inquiry form, not generic form.
- Add inquiry confirmation state.
- Rework Today dashboard into an action queue.
- Add trial-specific action cards.
- Add fee due/overdue action cards.
- Add editable WhatsApp message previews.
- Add enrolled-student/payment list.
- Add empty states that guide the owner.
- Add loading and API-fallback states that feel intentional.

P1 tasks:

- Add subtle trust indicators: privacy note, response expectation, demo/synthetic label.
- Add score explanations in human language.
- Add "what changed since last visit" summary.
- Add operator preview of public page readiness.

### 5.3 Backend and Data

P0 tasks:

- Extend or normalize Ananya seed data for Learning Studio depth.
- Ensure tutor inquiry fields are saved in `extra_context` consistently.
- Add trial-related status values and next actions.
- Add payment ageing logic.
- Add message templates for tutor workflows.
- Ensure public page data can be fully API-driven.
- Add setup readiness fields or derive readiness from existing objects.

P1 tasks:

- Add explicit Trial object if current Lead/Task model becomes too cramped.
- Add Enrollment object if Customer + Payment is not enough.
- Add lightweight analytics summaries.
- Add export of beta feedback data.

### 5.4 Safety, Privacy, and Trust

P0 tasks before real beta data:

- Add privacy policy.
- Add terms/beta disclaimer.
- Add consent copy near inquiry form.
- Add data deletion process.
- Add admin-only access for owner/operator views.
- Prevent public exposure of internal owner dashboard.
- Avoid storing unnecessary student-sensitive details.
- Make synthetic/demo data visibly separate from real beta data.
- Add safe copy defaults: no guaranteed marks, ranks, admissions, or fee recovery.

P1 tasks:

- Add simple audit trail for operator changes.
- Add consent timestamp to inquiry.
- Add beta participant agreement.
- Add data retention policy.

### 5.5 Deployment and Operations

P0 tasks:

- Choose deployment target.
- Configure production domain.
- Enable HTTPS.
- Configure environment variables.
- Disable Django debug in production.
- Set allowed hosts and CORS safely.
- Set up production database.
- Create backup process.
- Create admin credentials.
- Create beta user access path.
- Create error monitoring or minimum logging.

P1 tasks:

- Add staging environment.
- Add automated deploy.
- Add database backup restore drill.
- Add uptime check.

### 5.6 QA and Testing

P0 tasks:

- Add backend tests for inquiry -> lead -> task.
- Add backend tests for payment status updates.
- Add backend tests for message template retrieval.
- Add frontend smoke test for public page rendering.
- Add frontend smoke test for inquiry submission.
- Add frontend smoke test for owner action dashboard.
- Manually test on mobile viewport.
- Manually test API-down fallback.
- Test with long names, long messages, missing optional fields, and small screens.

P1 tasks:

- Add Playwright end-to-end tests.
- Add accessibility checks.
- Add visual regression screenshots.
- Add performance budget.

### 5.7 Beta Research and Commercial Validation

P0 tasks:

- Create beta tutor interview script.
- Create parent-facing feedback script.
- Create demo script.
- Create pricing/willingness-to-pay questions.
- Define beta success criteria.
- Recruit 3-5 tutors for guided beta.
- Record friction points.
- Track whether they would share the page.
- Track whether they understand the offer.
- Track whether they would pay setup and monthly support.

P1 tasks:

- Recruit parent reviewers.
- Run before/after comparison against current WhatsApp workflow.
- Capture testimonials if beta experience is positive.

## 6. Critical Path

The fastest responsible path to beta:

1. Freeze Learning Studio scope.
2. Polish Ananya public page.
3. Build tutor-specific inquiry and trial flow.
4. Rework owner Today view into action queue.
5. Add fee cycle clarity.
6. Add safety/privacy basics.
7. Deploy privately.
8. Run guided beta with 3-5 tutors.

Do not wait for:

- Multi-persona support
- Perfect analytics
- Advanced AI
- Full automation
- Full self-serve onboarding

Do not skip:

- Mobile polish
- Privacy/consent
- Access control
- Inquiry-to-lead workflow reliability
- Payment action reliability
- Guided beta script

## 7. Proposed Sprint Plan

### Sprint 0: Beta Scope Lock

Duration:

0.5-1 day.

Tasks:

- Confirm only Learning Studio for beta.
- Confirm Ananya as flagship demo.
- Freeze out-of-scope list.
- Convert this plan into a task board.
- Define launch blocker checklist.

Exit criteria:

- Everyone agrees what beta includes and excludes.

### Sprint 1: Learning Studio UI Polish

Duration:

2-4 days.

Tasks:

- Redesign Ananya public page.
- Add parent-first sections.
- Add tutor inquiry form.
- Improve mobile responsiveness.
- Add inquiry confirmation.
- Add safe trust and consent microcopy.

Exit criteria:

- Page passes parent trust test.
- Tutor would plausibly share it.

### Sprint 2: Owner Action System

Duration:

2-4 days.

Tasks:

- Rework Today view into action queue.
- Add new inquiry actions.
- Add trial actions.
- Add post-trial follow-up actions.
- Add fee due and overdue actions.
- Add editable WhatsApp message previews.
- Add enrolled student/payment list polish.

Exit criteria:

- Owner understands what to do today within 30 seconds.

### Sprint 3: Data and Workflow Hardening

Duration:

2-4 days.

Tasks:

- Deepen Ananya seed data.
- Ensure inquiry extra context is consistent.
- Add/adjust lead statuses for tutor journey.
- Add payment ageing logic.
- Add tutor message templates.
- Ensure dashboard actions persist correctly.

Exit criteria:

- Parent inquiry to fee reminder demo works end to end from backend data.

### Sprint 4: Beta Safety and Deployment

Duration:

2-5 days.

Tasks:

- Add privacy policy.
- Add terms/beta disclaimer.
- Add inquiry consent copy.
- Add access control for owner/operator views.
- Configure production environment.
- Deploy private beta.
- Add backup process.
- Add minimum logs/error visibility.

Exit criteria:

- Real beta users can access safely on HTTPS.
- Internal dashboards are not publicly exposed.

### Sprint 5: QA and Beta Launch

Duration:

1-3 days before launch, then 1-2 weeks beta cycle.

Tasks:

- Run smoke tests.
- Run mobile QA.
- Run guided demo script.
- Launch to 3-5 tutors.
- Collect feedback.
- Record pricing reactions.
- Fix P0 issues quickly.

Exit criteria:

- At least 3 serious user conversations completed.
- Clear decision on whether Learning Studio wedge is commercially promising.

## 8. Launch Blocker Checklist

Do not launch beta with real users if any of these are false:

- Public page is mobile-polished.
- Tutor-specific inquiry form works.
- Inquiry creates lead.
- Lead creates visible owner action.
- Message preview works.
- Payment status can be updated.
- Fee reminders are understandable and polite.
- Synthetic/demo data is labelled when relevant.
- Privacy and beta disclaimer exist.
- Owner/operator views are access-controlled.
- Production site uses HTTPS.
- There is a way to delete beta user data.
- There is a feedback capture process.

## 9. Quality Principles for the Build

### 9.1 Product Clarity

Every screen must answer:

- Who is this for?
- What should the user do now?
- Why does it matter?
- What happens next?

### 9.2 Language Quality

Use tutor vocabulary:

- Parent inquiry
- Trial class
- Batch timing
- Monthly fee
- Follow-up
- Parent update

Avoid generic SaaS vocabulary:

- Pipeline
- Deal velocity
- Close rate
- Funnel optimization
- Collections recovery

### 9.3 Visual Quality

The UI should feel:

- Calm
- Clear
- Trustworthy
- Mobile-first
- Parent-friendly
- Operationally serious

Avoid:

- Decorative dashboards
- Generic cards
- Thin copy
- Overly colorful demo styling
- Marketing fluff

### 9.4 Safety Quality

Never imply:

- Guaranteed marks
- Guaranteed admissions
- Guaranteed fee recovery
- Legal compliance
- Payment ownership
- Tax filing

## 10. Beta Success Metrics

### 10.1 Product Success

Minimum beta success:

- 3-5 tutors complete guided review.
- At least 3 say they would share the public page.
- At least 2 say the action dashboard solves a real problem.
- At least 2 express willingness to pay some setup fee.
- No major confusion about what BizzNexx does.

Strong beta success:

- One tutor agrees to pilot with real parent inquiries.
- One tutor asks for page customization.
- One tutor says fee/follow-up reminders are worth paying for.
- A parent reviewer says the page increases trust.

### 10.2 Operational Success

Minimum:

- Operator can set up Ananya-like profile repeatably.
- Demo flow runs end to end without manual database edits.
- Support issues are understandable and fixable.

Strong:

- Operator can set up a second Learning Studio within 90 minutes.
- Most missing inputs are caught by readiness checklist.

### 10.3 Commercial Success

Minimum:

- Tutors understand setup plus monthly support pricing.
- Pricing objections are specific, not total rejection.

Strong:

- At least one tutor is willing to pay INR 1,499-2,999 setup.
- At least one tutor is willing to consider INR 499-999 monthly support.

## 11. Product Maturity Model

### Level 1: Demo Prototype

Works in guided walkthrough.

Current product is approximately here.

### Level 2: Selected Beta

Safe, polished, private, and useful for 3-5 guided users.

This is the immediate target.

### Level 3: Paid Pilot

Real data, real tutor, real parent inquiries, paid setup or committed payment.

Target after selected beta.

### Level 4: Repeatable Persona Pack

Multiple tutors can be onboarded with predictable setup time and quality.

Target after paid pilot.

### Level 5: Scalable Product

Self-serve or semi-assisted onboarding, stronger security, production observability, richer analytics, repeatable GTM.

Not the immediate target.

## 12. Recommended Immediate Next Move

Start implementation with Sprint 1 and Sprint 2 together:

Track A:

- Redesign Learning Studio public page.
- Build tutor-specific inquiry flow.

Track B:

- Rework owner dashboard into action queue.
- Add trial and fee action cards.

Track C:

- Deepen Ananya data and message templates.

This creates the first beta-worthy product surface fastest.

The backend already has enough structure to support this if we are disciplined. We should only add backend fields when a screen or workflow truly needs them.

## 13. Final Verdict

You are not far from a beta, but you are not ready to invite beta users yet.

The documents are now strong. The prototype foundation is real. The remaining work is a focused beta hardening push:

- Make Learning Studio feel specific.
- Make Ananya share-worthy.
- Make the owner dashboard action-oriented.
- Make inquiry, trial, and fee flows reliable.
- Add privacy/access/deployment basics.
- Test the full journey on mobile.

The fastest serious beta path is not to add more personas. It is to make one persona excellent enough that a real tutor feels seen.

