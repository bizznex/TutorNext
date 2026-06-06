# Learning Studio Execution Action Plan

## 1. Recommendation

Yes, build the UI first.

But do not build a decorative UI first. Build a clickable, persona-specific UI that proves the business loop:

Parent sees trust -> parent sends structured inquiry -> owner gets next action -> trial is followed up -> enrolled student creates monthly fee cycle -> owner sees what to do today.

The UI is the right first move because this persona will be validated through perceived usefulness and share-worthiness. A tutor will not care that the backend is elegant if the parent-facing page feels generic. A parent will not submit an inquiry if the page does not create trust. The owner dashboard must feel like immediate relief, not another admin surface.

The caveat:

Before UI implementation, define a thin Learning Studio data contract so every screen is grounded in real objects. This prevents the first build from becoming a static mockup that later needs to be rebuilt.

## 2. Execution Principle

Build in this order:

1. Validation UI
2. Thin data model/API alignment
3. Workflow logic
4. Owner/operator tooling
5. Paid pilot instrumentation

The first release should feel real even if some logic is still seeded or manually assisted.

## 3. Target Outcome

At the end of this workstream, Ananya Learning Studio should have:

- A parent-ready public page
- A tutor-specific inquiry form
- A realistic inquiry-to-trial journey
- A simple owner action dashboard
- A monthly fee tracker
- Persona-specific message templates
- Operator setup readiness checklist
- Demo data deep enough for selected-user validation

Primary validation question:

Would a real tutor share this page with parents and use the dashboard weekly?

Secondary validation question:

Would the tutor pay for setup and continue paying for monthly operating support?

## 4. Workstream Overview

### Workstream A: Product Definition

Goal:

Convert the strategy into precise screens, fields, states, and acceptance criteria.

Tasks:

- Define Learning Studio MVP scope.
- Freeze Ananya as the first validation persona.
- Define user journeys for parent, owner, and BizzNexx operator.
- Define the minimum data contract.
- Define screen acceptance criteria.
- Define what is explicitly out of scope.

Deliverables:

- Learning Studio MVP scope checklist
- Screen list
- Data object list
- Acceptance criteria

Owner:

Product/business strategy.

Priority:

P0.

### Workstream B: Public Page UI

Goal:

Make the Ananya page credible enough for a tutor to proudly share.

Tasks:

- Create parent-facing hero section.
- Add teacher credibility section.
- Add class/subject/board coverage section.
- Add course cards with fee/timing/trial policy.
- Add trial CTA.
- Add parent testimonials and result proof.
- Add "what happens after inquiry" section.
- Add parent FAQ.
- Add WhatsApp CTA with contextual message.
- Ensure mobile-first layout.
- Add empty/missing-proof fallback states.

Acceptance Criteria:

- Parent can understand fit within 30 seconds.
- Page answers class, board, subject, fee, timing, trial, and trust questions.
- CTA is visible without feeling pushy.
- Page does not make exaggerated result claims.
- Tutor would not feel embarrassed sharing the page in a WhatsApp group.

Priority:

P0.

### Workstream C: Tutor Inquiry Flow UI

Goal:

Capture enough context so the owner does not repeat basic questions.

Tasks:

- Build tutor-specific inquiry form.
- Include parent/student name.
- Include phone number.
- Include class.
- Include board.
- Include subject.
- Include preferred timing.
- Include trial interest.
- Include message/concern.
- Add confirmation state after inquiry.
- Add WhatsApp handoff with prefilled context.
- Add validation for required fields.

Acceptance Criteria:

- Inquiry creates a lead with class/board/subject context.
- Parent knows what happens next.
- Owner receives enough detail to respond directly.
- Form works on mobile comfortably.

Priority:

P0.

### Workstream D: Owner Dashboard UI

Goal:

Turn the dashboard into today's action queue.

Tasks:

- Create "Today's Actions" panel.
- Show new parent inquiries.
- Show trials to schedule.
- Show trials due today.
- Show post-trial follow-ups.
- Show fees due today.
- Show overdue fees.
- Add suggested message preview for each action.
- Add WhatsApp send/edit action.
- Add status update controls.
- Add compact business health summary.

Acceptance Criteria:

- Owner can understand what needs attention in under 30 seconds.
- Every dashboard card leads to a concrete action.
- Dashboard language uses tutor vocabulary, not generic CRM vocabulary.
- Payment reminders feel polite and relationship-safe.

Priority:

P0.

### Workstream E: Payment and Fee Cycle UI

Goal:

Make recurring fee tracking visible without becoming accounting software.

Tasks:

- Add enrolled student fee list.
- Show monthly fee amount.
- Show due date.
- Show paid, part-paid, due, overdue states.
- Show overdue ageing: 3, 7, 14 days.
- Add one-tap paid marking.
- Add reminder message template.
- Add part-payment state.
- Add payment mode note: UPI, cash, bank transfer.

Acceptance Criteria:

- Owner can identify who owes money this month.
- Owner can send a polite reminder.
- Owner can mark payment status quickly.
- No payment gateway or settlement logic is implied.

Priority:

P0.

### Workstream F: Message Templates

Goal:

Make communication easier without pretending to fully automate WhatsApp.

Tasks:

- Draft first response template.
- Draft trial slot proposal.
- Draft trial confirmation.
- Draft trial reminder.
- Draft post-trial follow-up.
- Draft fee plan message.
- Draft monthly fee reminder.
- Draft overdue fee reminder.
- Draft parent progress note.
- Draft testimonial request.
- Support English and Hinglish-friendly tone.

Acceptance Criteria:

- Every template is editable before sending.
- Templates are polite, specific, and parent-facing.
- No message sounds like aggressive sales automation.
- Templates use inquiry context where available.

Priority:

P0/P1.

### Workstream G: Backend/Data Contract Alignment

Goal:

Ensure the UI can become real without major rebuild.

Tasks:

- Define Learning Studio fields on business/profile.
- Define course/batch fields.
- Define tutor-specific inquiry fields.
- Define lead statuses.
- Define trial fields.
- Define enrollment fields.
- Define payment cycle fields.
- Define proof/testimonial/result objects.
- Define message template objects.
- Seed Ananya data.
- Add API shape required by UI.

Acceptance Criteria:

- UI screens can be driven from API-backed data.
- Ananya data includes realistic proof, FAQs, leads, trials, and payments.
- Data model supports at least one other tutor without hardcoding.

Priority:

P0, started in parallel after UI contract is defined.

### Workstream H: Operator Setup Console

Goal:

Make assisted setup repeatable.

Tasks:

- Add Learning Studio persona selection.
- Add intake completeness checklist.
- Add teacher profile completeness.
- Add course completeness.
- Add proof completeness.
- Add trial policy completeness.
- Add inquiry form readiness.
- Add message template readiness.
- Add payment setup readiness.
- Add "ready to share" status.

Acceptance Criteria:

- Operator can see what is missing before launch.
- Operator can set up Ananya-like tutor in a repeatable way.
- Readiness checklist maps to public-page quality, not generic admin fields.

Priority:

P1.

### Workstream I: Validation and Instrumentation

Goal:

Measure whether the offer is commercially believable.

Tasks:

- Track page views.
- Track WhatsApp CTA clicks.
- Track inquiry submissions.
- Track inquiry completeness.
- Track trial scheduled status.
- Track post-trial follow-up completion.
- Track fee reminders sent.
- Track payment status changes.
- Track owner dashboard visits.
- Capture owner feedback after demo.
- Capture parent feedback if possible.

Acceptance Criteria:

- We can tell whether the page is being shared.
- We can tell whether inquiries are better structured.
- We can tell whether follow-ups are happening.
- We can discuss payment willingness with evidence.

Priority:

P1.

## 5. Suggested Build Sequence

### Phase 0: Pre-Build Alignment

Duration:

0.5-1 day.

Tasks:

- Confirm Ananya as the only first UI persona.
- Convert strategy into screen requirements.
- Define data needed by each screen.
- Decide visual tone: credible, warm, parent-first, not flashy.
- Confirm out-of-scope list.

Output:

- Final screen checklist.
- Final data checklist.

### Phase 1: UI Prototype

Duration:

2-4 days.

Tasks:

- Build public page.
- Build inquiry flow.
- Build owner dashboard.
- Build payment list.
- Build message preview components.
- Use seeded/static data where needed.

Output:

- Clickable Learning Studio experience.
- Mobile-first screens.

Why first:

This is the fastest way to test whether the business offer feels real.

### Phase 2: Data/API Integration

Duration:

2-4 days.

Tasks:

- Align backend models/API with screen data.
- Seed Ananya deeply.
- Wire public page to real data.
- Wire inquiry submission to lead creation.
- Wire lead statuses to dashboard.
- Wire payments to dashboard.

Output:

- API-backed Ananya demo.

Parallelizable With:

- Message template writing.
- Operator checklist design.

### Phase 3: Workflow Logic

Duration:

2-3 days.

Tasks:

- Inquiry creates owner action.
- Trial scheduled creates reminder action.
- Trial completed creates post-trial follow-up action.
- Enrollment creates monthly fee cycle.
- Overdue payment creates fee reminder action.
- Status updates change dashboard state.

Output:

- End-to-end parent inquiry to fee follow-up flow.

### Phase 4: Operator and Validation Layer

Duration:

2-3 days.

Tasks:

- Add readiness checklist.
- Add proof completeness.
- Add page quality status.
- Add basic analytics hooks.
- Add selected-user review checklist.

Output:

- Repeatable assisted setup flow.
- Validation-ready pilot.

### Phase 5: Selected-User Review

Duration:

1-2 weeks calendar time.

Tasks:

- Show to 3-5 tutors.
- Ask whether they would share the page.
- Ask whether parent inquiry fields feel right.
- Ask whether they would use fee/follow-up actions.
- Ask what they would pay.
- Observe confusion and resistance.
- Revise offer and UI.

Output:

- Validated or invalidated Learning Studio wedge.

## 6. Parallel Work Plan

After Phase 0, run these in parallel:

Track 1: UI Build

- Public page
- Inquiry form
- Dashboard
- Payment view

Track 2: Data and Backend

- Ananya seed data
- Tutor-specific inquiry schema
- Lead statuses
- Payment cycle fields

Track 3: Business Content

- Copy
- FAQs
- Testimonials
- Message templates
- Offer language

Track 4: Operator/Validation

- Setup checklist
- Demo script
- User interview script
- Feedback capture form

This is better than fully sequential execution because the UI will reveal data gaps, while the data work prevents the UI from floating away from implementation reality.

## 7. Screen Inventory

### Parent-Facing

- Public Learning Studio page
- Course detail section/card
- Tutor inquiry form
- Inquiry confirmation state
- WhatsApp handoff state

### Owner-Facing

- Owner dashboard
- Today's actions
- Parent inquiry detail
- Trial follow-up detail
- Enrolled student/payment list
- Message preview/edit state

### Operator-Facing

- Learning Studio setup checklist
- Business profile intake
- Course/catalogue setup
- Proof/testimonial setup
- Message template setup
- Readiness review

## 8. Minimum Data Contract

Business:

- Name
- City/locality
- Mode
- Languages
- Public headline
- Public subtext

Teacher:

- Name
- Experience
- Qualifications
- Teaching style
- Profile photo, optional

Course:

- Name
- Class range
- Subject
- Board
- Fee
- Timing
- Mode
- Trial policy
- Capacity, optional

Proof:

- Type
- Text
- Attribution
- Year/result context

Inquiry:

- Parent/student name
- Phone
- Class
- Board
- Subject
- Preferred timing
- Trial interest
- Message
- Source

Lead:

- Status
- Next action
- Expected value
- Follow-up age
- Linked inquiry

Trial:

- Proposed slot
- Confirmed slot
- Status
- Reminder state
- Outcome

Enrollment:

- Student
- Course
- Monthly fee
- Start date
- Payment cycle
- Status

Payment:

- Student
- Amount due
- Amount paid
- Due date
- Status
- Ageing
- Mode

Message Template:

- Type
- Tone
- Body
- Variables

## 9. Acceptance Tests

### Public Page Test

A parent should be able to answer:

- Who is the teacher?
- What classes and subjects are taught?
- Is my child's board supported?
- What are the timings?
- What is the fee or fee policy?
- Is a trial available?
- Why should I trust this teacher?
- What happens after I inquire?

### Owner Dashboard Test

The owner should be able to answer:

- Who needs a reply today?
- Which trial is coming up?
- Who needs post-trial follow-up?
- Who has fees due?
- Who is overdue?
- What message should I send?

### Business Validation Test

A tutor should say:

- "I would share this page."
- "This inquiry form saves me questions."
- "This dashboard reminds me of things I currently forget."
- "This fee reminder flow would reduce awkwardness."
- "I can see why this is worth paying for."

## 10. Out of Scope for First Build

Do not build yet:

- Attendance management
- Homework submission
- LMS/video/content library
- Test analytics
- Parent mobile app
- Student portal
- Payment gateway
- Invoice/GST module
- WhatsApp Business API automation
- Multi-branch institute ERP

These can be reconsidered after the first paid pilot signal.

## 11. Immediate Next Tasks

### Task 1: Convert Ananya Into Final Seed Data

Add:

- Rich teacher profile
- Board-specific FAQs
- Trial slots
- Parent concerns
- Better testimonials
- Result proof
- Payment cycles
- Message templates

### Task 2: Build Public Page UI

Start with:

- Hero
- Teacher profile
- Course cards
- Trust proof
- Trial CTA
- FAQ
- Inquiry form

### Task 3: Build Owner Action Dashboard

Start with:

- New inquiries
- Trial actions
- Fee actions
- Message previews

### Task 4: Wire Inquiry Flow

Ensure:

- Inquiry creates lead
- Lead creates next action
- Owner can update status

### Task 5: Create Validation Demo Script

Demo:

1. Parent opens page.
2. Parent submits inquiry.
3. Owner receives action.
4. Owner sends trial message.
5. Trial follow-up appears.
6. Enrollment creates fee cycle.
7. Fee reminder appears.

## 12. Final Build Stance

The right move is UI-first, but not UI-only.

Build the screens first because share-worthiness and perceived usefulness are the core validation points. In parallel, define the data and workflow spine so the UI becomes the actual product rather than a polished brochure.

The first build should make one thing unmistakable:

BizzNexx helps a learning studio turn parent interest into trial, enrollment, fee discipline, and referral-ready trust.

