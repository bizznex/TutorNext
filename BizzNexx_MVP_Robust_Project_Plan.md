# BizzNexx MVP Robust Project Plan

## 1. Executive Decision

BizzNexx should move forward as a catalogue-to-lead-to-cash operating system for Indian service-led microbusinesses.

This MVP must be governed by the persona-first blueprint in `BizzNexx_Persona_First_Operating_Blueprint.md`. That document is the operating source of truth for business types, owner personas, buyer personas, segment-specific fields, workflow statuses, message templates, scoring logic, setup gates, and feature rejection rules.

The existing robust plan is directionally correct on these points:

- Start with service-led microbusinesses.
- Stay WhatsApp-first in user mental model.
- Avoid competing directly with accounting, GST filing, payment gateway, and ERP products.
- Validate willingness to pay before heavy automation.
- Use Ria Mukherji-led content as a core distribution channel.
- Build around leads, follow-ups, payments, AI messages, and business health.

The plan needs one strategic correction:

Catalogue and public web presence must be a core MVP pillar, not an optional portfolio feature. The paid promise is stronger when BizzNexx creates the business's public service catalogue, captures inquiries from it, and then manages the operating workflow behind those inquiries.

## 2. Refined MVP Positioning

### One-Line Promise

BizzNexx helps Indian service businesses create a professional catalogue page, capture inquiries, follow up on WhatsApp, track payments, and know what to do next.

### What BizzNexx Is

- A paid setup-backed growth and operating system
- A simple public catalogue page builder for service businesses
- A lead capture and follow-up workflow
- A payment visibility and receivables discipline layer
- An AI-assisted message and business action assistant
- A CA-ready record organizer, not a tax filing product

### What BizzNexx Is Not

- Not accounting software
- Not GST filing software
- Not a payment gateway
- Not a debt recovery service
- Not a broad CRM
- Not a marketplace
- Not a generic website builder

## 3. Market Context

India's MSME base is massive and mostly micro. The MSME Annual Report 2025-26 reports 7.61 crore registered MSMEs including informal micro enterprises on UAP as of 31 January 2026.

Digital behavior is already mainstream. UPI processed 22.64 billion transactions worth Rs. 29.53 lakh crore in March 2026. This means BizzNexx does not need to teach users to accept digital payments; it needs to help them track, follow up, and organize them.

Customer operations are a real pain. Zoho's Indian MSME survey found CRM, finance, BI, and AI are viewed as important, but adoption is blocked by high software cost, budget constraints, training gaps, complexity, and local-language limitations.

Digital presence remains weak. A 2025 SERP Forge analysis reported by SMEStreet found only 1% of sampled MSME websites were actually working, and many failed basic hygiene like mobile readiness, contact details, SEO title, or accessibility.

Delayed payments are still a major macro problem. The GAME-FISME-C2FO delayed payments report cited Rs. 7.34 lakh crore in delayed MSME payments as of March 2024.

Competitors validate the need but leave room for BizzNexx:

- myBillBook, Vyapar, and Khatabook are strong in billing, accounting, inventory, ledgers, GST, payment reminders, and reports.
- Website builders solve presence but usually do not own lead-to-cash discipline.
- WhatsApp API tools solve messaging automation but are often too technical or expensive for tiny service businesses.
- Generic CRMs are too broad and data-entry-heavy.

BizzNexx should win by being narrower, service-business-specific, setup-assisted, and outcome-oriented.

## 4. MVP Strategy

### MVP Thesis

The MVP must prove that a business owner will pay for a system that:

- Makes their services look professional
- Helps prospects inquire easily
- Captures leads cleanly
- Tells the owner whom to follow up with
- Helps them send better WhatsApp messages
- Tracks money due and overdue
- Creates a basic monthly business summary

### MVP Success Standard

The MVP is ready to scale only if at least:

- 15 businesses complete setup
- 10 publish catalogue pages
- 8 share their page publicly
- 8 capture real inquiries or enter real leads
- 6 use follow-up or payment message templates
- 5 return weekly for 3 weeks
- 5 pay setup fees
- 3 agree to monthly continuation

## 5. Core MVP Modules

### Module 1: Business Setup

Purpose: collect enough information to create a working business system.

Required features:

- Business profile
- Owner/contact details
- Segment selection
- Preferred language and tone
- WhatsApp number
- Service area
- Logo/photo upload placeholder
- Setup status

### Module 2: Catalogue Builder

Purpose: structure what the business sells.

Required features:

- Catalogue title and promise
- Service/category list
- Catalogue item details
- Pricing display options
- Trial/consultation policy
- FAQs
- Trust proof/testimonials
- Publish/unpublish status

### Module 3: Public Catalogue Page

Purpose: generate trust and inquiries.

Required features:

- Public route: `/b/{business-slug}`
- Mobile-first design
- Services/catalogue items
- Inquiry form
- Click-to-WhatsApp CTA
- Testimonials/trust proof
- FAQs
- Basic SEO title/meta description

### Module 4: Inquiry Capture

Purpose: turn public interest into structured leads.

Required features:

- Inquiry form submission
- WhatsApp click event logging
- Source tracking
- Interested service
- Auto-create inquiry record
- Convert inquiry to lead

### Module 5: Lead Pipeline

Purpose: prevent lead leakage.

Required statuses:

- New
- Contacted
- Trial/consultation proposed
- Trial/consultation scheduled
- Quote/fee sent
- Converted
- Lost

Required features:

- Next follow-up date
- Lead source
- Interested service
- Expected value
- Notes
- Lost reason

### Module 6: Follow-Up Tasks

Purpose: answer "What should I do today?"

Required features:

- Today's follow-ups
- Overdue follow-ups
- Task priority
- Related lead/customer/payment
- Mark done/snooze
- Suggested message

### Module 7: Payment Visibility

Purpose: track receivables without becoming accounting software.

Required features:

- Amount due
- Amount paid
- Due date
- Paid/part-paid/unpaid/overdue status
- Payment mode
- Reference note
- Payment reminder message

### Module 8: AI Message Assistant

Purpose: help owners communicate better.

MVP message types:

- New inquiry reply
- Service explanation
- Trial/consultation confirmation
- Post-trial follow-up
- Quote/fee message
- Payment reminder
- Overdue payment reminder
- Reactivation
- Testimonial request
- Referral request

Guardrails:

- No legal/tax advice
- No guaranteed results
- No threatening collections language
- User must be able to edit before sending

### Module 9: Growth and Health Dashboard

Purpose: show action, not vanity analytics.

Required cards:

- Page views
- WhatsApp clicks
- New inquiries
- Open leads
- Follow-ups due today
- Pending payments
- Expected cash
- Growth Score
- Health Score

### Module 10: Monthly Summary Export

Purpose: provide CA-ready organization without claiming compliance automation.

Required export fields:

- Business name
- Month
- Leads received
- Converted customers
- Amount due
- Amount collected
- Outstanding amount
- Payment modes
- Customer list
- Notes for CA/accountant

## 6. Shared Platform Data Model

### Required Entities for MVP

- User
- Business
- Business Owner
- Subscription / Package
- Setup Project
- Catalogue
- Catalogue Item
- FAQ
- Trust Proof
- Public Page
- Page Event
- Inquiry
- Lead
- Follow-Up Task
- Trial / Consultation
- Quote / Fee Plan
- Customer
- Payment
- Message Template
- Generated Message
- Score Snapshot
- Monthly Summary
- Support Request

### Entities to Defer

- Inventory
- GST filing return
- Payment gateway settlement
- Loan/credit
- Multi-branch hierarchy
- Staff attendance
- Marketplace matching
- Ad campaign manager

## 7. Business Case Packs

Each use case should share the same core platform but have its own catalogue fields, statuses, message templates, scoring logic, and public page copy.

## 7.1 Tutor / Coach / Trainer Pack

### Customer

Solo tutor, coaching class, music teacher, fitness trainer, language coach, online trainer.

### Core Workflow

Catalogue page -> parent/student inquiry -> trial class -> fee plan -> enrollment -> monthly fee tracking -> parent/student follow-up.

### Catalogue Needs

- Subjects/classes
- Board/exam/category
- Batch timing
- Online/offline mode
- Trial class policy
- Monthly fee
- Teacher profile
- Testimonials/results

### MVP Fields

- Student name
- Parent/contact person
- Class/grade
- Subject
- Preferred timing
- Trial date
- Monthly fee
- Payment cycle

### AI Messages

- New parent inquiry reply
- Trial class confirmation
- Trial reminder
- Fee plan explanation
- Post-trial follow-up
- Monthly fee reminder
- Testimonial request

### Health/Growth Metrics

- Inquiry-to-trial conversion
- Trial-to-enrollment conversion
- Monthly fee collection health
- Follow-up punctuality
- Catalogue completeness

### Go-Live Readiness

- 3 demo tutor pages
- 20 tutor-specific message templates
- Trial scheduling fields
- Monthly fee tracker
- Parent-friendly public page template

## 7.2 Makeup Artist / Photographer / Event Service Pack

### Customer

Makeup artist, wedding photographer, event decorator, mehendi artist, small event planner.

### Core Workflow

Instagram/WhatsApp/catalogue inquiry -> event date check -> package quote -> advance collection -> booking confirmation -> balance reminder -> testimonial/gallery update.

### Catalogue Needs

- Service packages
- Event types
- Portfolio/gallery
- Location/service area
- Starting price
- Add-ons
- Booking/advance policy
- Testimonials

### MVP Fields

- Event date
- Event type
- Venue/location
- Package interested
- Quote amount
- Advance required
- Balance due
- Booking status

### AI Messages

- Event inquiry reply
- Availability check
- Package explanation
- Quote message
- Advance payment request
- Balance reminder
- Post-event review request

### Health/Growth Metrics

- Inquiry-to-quote conversion
- Quote-to-booking conversion
- Advance collection status
- Event-date follow-up readiness
- Portfolio completeness

### Go-Live Readiness

- Gallery section
- Event date field
- Quote/package template
- Advance/balance payment flow
- Portfolio consent note

## 7.3 Freelancer / Small Agency Pack

### Customer

Designer, developer, marketing freelancer, content agency, small creative studio, consulting freelancer.

### Core Workflow

Service page -> project inquiry -> discovery call -> proposal/quote -> milestone/payment schedule -> delivery tracking -> invoice/payment reminder.

### Catalogue Needs

- Services
- Packages/retainers
- Case studies
- Work samples
- Client testimonials
- Process explanation
- Starting price or quote CTA

### MVP Fields

- Company/client name
- Contact person
- Project type
- Budget range
- Discovery call date
- Proposal status
- Milestone amount
- Payment due date

### AI Messages

- Discovery call confirmation
- Proposal follow-up
- Scope explanation
- Quote message
- Milestone payment reminder
- Project reactivation
- Testimonial request

### Health/Growth Metrics

- Inquiry-to-call conversion
- Proposal-to-win conversion
- Average project value
- Overdue milestone payments
- Case study readiness

### Go-Live Readiness

- Case study block
- Proposal/quote object
- Milestone payment tracker
- B2B tone templates
- Discovery call workflow

## 7.4 Consultant / Professional Service Pack

### Customer

Career coach, business consultant, tax consultant, legal consultant, therapist-like non-regulated coach, home-based professional.

### Core Workflow

Credibility page -> consultation inquiry -> booking -> package pitch -> payment -> repeat session or retainer.

### Catalogue Needs

- Expertise areas
- Consultation format
- Credentials
- Session/package pricing
- Disclaimer
- Testimonials
- Booking CTA

### MVP Fields

- Consultation topic
- Preferred time
- Session type
- Package interested
- Payment status
- Follow-up date
- Disclaimer acceptance

### AI Messages

- Consultation inquiry reply
- Session confirmation
- Package explanation
- Follow-up after session
- Payment reminder
- Referral request

### Health/Growth Metrics

- Inquiry-to-booking conversion
- Booking-to-paid conversion
- Repeat session rate
- Trust proof completeness
- Disclaimer readiness

### Go-Live Readiness

- Disclaimer component
- Consultation booking workflow
- Professional credibility template
- Sensitive-claims guardrails
- No legal/tax/medical advice overclaiming

## 7.5 Creator / Workshop / Paid Services Pack

### Customer

Creator selling workshops, courses, brand collaborations, consulting calls, digital services, cohort programs.

### Core Workflow

Creator catalogue/rate card -> inquiry -> package/rate discussion -> deliverables -> payment -> repeat collaboration.

### Catalogue Needs

- Offer list
- Workshop/course details
- Audience profile
- Rate card
- Brand collaboration formats
- Proof/social metrics
- Deliverables

### MVP Fields

- Inquiry type
- Brand/client name
- Deliverable type
- Campaign date
- Rate quoted
- Deliverable status
- Payment due

### AI Messages

- Brand inquiry reply
- Rate card explanation
- Deliverables confirmation
- Payment follow-up
- Repeat collaboration pitch
- Testimonial/referral request

### Health/Growth Metrics

- Inquiry-to-deal conversion
- Deliverables completed
- Payment delay
- Repeat collaboration rate
- Rate-card readiness

### Go-Live Readiness

- Rate card block
- Deliverables tracker
- Brand/service inquiry fields
- Social proof section
- Creator-friendly tone templates

## 7.6 Home Service / Local Specialist Pack

### Customer

Repair service, beauty service at home, home bakery, local trainer, small local specialist.

### Core Workflow

Local service page -> inquiry -> availability/location check -> quote -> booking -> payment -> repeat/referral.

### Catalogue Needs

- Service list
- Service area
- Availability
- Price range
- Photos/work samples
- Customer reviews
- WhatsApp booking CTA

### MVP Fields

- Location
- Service needed
- Preferred date/time
- Quote amount
- Booking status
- Payment status
- Repeat/referral note

### AI Messages

- Booking inquiry reply
- Availability confirmation
- Quote explanation
- Booking reminder
- Payment reminder
- Review request
- Referral request

### Health/Growth Metrics

- Inquiry-to-booking conversion
- Area/source performance
- Repeat customers
- Payment collection health
- Review readiness

### Go-Live Readiness

- Service area fields
- Local SEO basics
- Availability workflow
- Review/testimonial capture
- Mobile-first booking CTA

## 8. MVP Technical Plan

## 8A. Practical Operating Model: No-Data-Entry First

The biggest product risk is expecting Indian microbusiness owners to open a laptop and maintain records. The MVP must be designed around capture from the places where work already happens: WhatsApp, Instagram, phone calls, forms, UPI screenshots, and owner memory.

### Practical Principle

Do not ask the owner to "use a CRM." Give them a mobile-first assistant that captures business events with the least possible effort.

### What the Customer Actually Does

The owner should only need to do a few lightweight actions:

- Share their BizzNexx catalogue link in WhatsApp, Instagram bio, status, reels captions, Google Business Profile, and referrals.
- Tap a mobile notification or dashboard card that says "3 leads need follow-up today."
- Copy or send a suggested WhatsApp message.
- Mark simple statuses: contacted, trial booked, quote sent, paid, part-paid, lost.
- Forward screenshots/messages to BizzNexx during the assisted pilot if they do not want to enter data.

The customer should not be expected to:

- Maintain complex CRM fields.
- Open a laptop daily.
- Re-enter every WhatsApp conversation manually.
- Understand accounting or dashboard terminology.
- Configure automations.

### MVP Capture Channels

#### 1. Public Catalogue Page as Primary Capture

This is the cleanest data source.

Flow:

1. Prospect visits `/b/{business-slug}`.
2. Prospect submits inquiry form or clicks WhatsApp CTA.
3. BizzNexx captures service interest, name, phone, source, and message.
4. Inquiry appears in mobile owner dashboard.
5. Owner gets suggested response.

Why this matters:

- The owner does not enter the lead.
- BizzNexx captures structured data at source.
- The page becomes both marketing and operations infrastructure.

#### 2. Click-to-WhatsApp With Pre-Filled Context

For MVP, use WhatsApp deep links instead of full WhatsApp API dependency.

Example:

`https://wa.me/{number}?text=Hi,%20I%20am%20interested%20in%20Class%2010%20Maths%20trial%20from%20your%20BizzNexx%20page`

Benefits:

- No API approval needed.
- Works immediately.
- Customer stays inside familiar WhatsApp behavior.
- The message carries service context.

Limitation:

- BizzNexx cannot automatically read the resulting chat unless the business uses the WhatsApp Business Platform/Cloud API or forwards data back.

#### 3. Assisted Intake Through BizzNexx Ops

For paid pilot users, BizzNexx should offer concierge data setup.

The owner can send:

- Existing services/packages
- Old brochures/PDFs
- Instagram profile
- UPI/payment screenshots
- List of pending leads
- WhatsApp screenshots where consent and privacy are acceptable

BizzNexx team converts this into:

- Catalogue page
- Lead list
- Payment list
- Message templates
- Dashboard

This is important because the paid service is not only software. It is "done-with-you business setup."

#### 4. Mobile Quick Add

For anything not captured automatically, the mobile dashboard should support ultra-fast entry:

- Add lead in under 20 seconds
- Add payment due in under 15 seconds
- Mark paid in one tap
- Snooze follow-up in one tap
- Copy message in one tap

Fields must be minimal and progressive. Ask only what is needed now; enrich later.

#### 5. Instagram Capture

MVP path:

- Put BizzNexx catalogue link in Instagram bio.
- Use reel captions and story CTAs pointing to the catalogue page.
- Add "DM/WhatsApp for booking" CTA.
- Manually log Instagram leads through mobile quick add or assisted BizzNexx Ops.

Later path:

- Use Instagram Messaging API and webhooks for professional accounts.
- This requires Meta app setup, permissions, account eligibility, and app review.

#### 6. WhatsApp API Capture Later

Do not make WhatsApp API mandatory for MVP.

Reason:

- WhatsApp Business App itself does not expose simple CRM-style webhooks.
- Official automation requires WhatsApp Business Platform/Cloud API.
- Cloud API requires Meta setup, webhooks, templates, phone number configuration, and pricing discipline.
- Some users may resist migrating their number or paying messaging/API costs.

Use WhatsApp API only after the workflow is proven.

API-enabled future flow:

1. Business connects WhatsApp Business Platform.
2. Inbound messages hit BizzNexx webhook.
3. BizzNexx classifies inquiry/service/payment intent.
4. BizzNexx creates or updates lead.
5. Owner approves suggested response.
6. Templates handle follow-up and payment reminders where allowed.

### Mobile Application Strategy

Indian microbusiness owners need mobile access first.

MVP approach:

- Build a mobile-first responsive web app.
- Installable PWA, so it appears like an app on Android home screen.
- Push notifications can be added after the first pilot.
- Keep desktop as admin/operator tool, not owner requirement.

Why PWA first:

- Faster than native app.
- No Play Store dependency at pilot stage.
- Same React codebase can serve public pages and owner dashboard.
- Easier iteration during validation.

Native app later:

- Only after weekly usage is proven.
- Use React Native or Flutter if mobile engagement justifies it.
- Native app should focus on notifications, quick actions, camera/screenshot upload, and WhatsApp handoff.

### How Customers Benefit Without Data Entry

Customers benefit because BizzNexx moves data capture upstream and makes the rest assisted:

- Lead data comes from catalogue inquiry forms.
- Service context comes from the catalogue item clicked.
- WhatsApp messages carry pre-filled context.
- BizzNexx Ops helps convert messy existing information into structured setup.
- Owner only confirms status and sends messages.
- Dashboard is action-first, not reporting-first.

The practical value is not "please maintain another app."

The practical value is:

"Share this page. Leads come in organized. We tell you whom to follow up with. We give you the message. You tap and send. You mark paid when money comes."

### Automation Maturity Ladder

#### Level 0: Concierge MVP

- BizzNexx team sets up page and dashboard.
- Leads captured through form.
- Owner forwards missed WhatsApp/Instagram leads if needed.
- BizzNexx team cleans data weekly for pilot users.

#### Level 1: Mobile Self-Serve MVP

- Owner can edit catalogue.
- Owner can quick-add leads/payments.
- Owner sees mobile dashboard.
- Owner copies messages.

#### Level 2: Light Integrations

- WhatsApp click tracking.
- Google Sheets import/export.
- Google Business Profile link placement.
- Calendar link for consultations/trials.
- Payment link field, not payment gateway ownership.

#### Level 3: Official Messaging Integrations

- WhatsApp Cloud API for eligible users.
- Instagram Messaging API for professional accounts.
- Webhooks for inbound inquiries.
- Approved templates for notifications.

#### Level 4: Semi-Automated Copilot

- AI classifies messages.
- AI drafts replies.
- Owner approves sending.
- System creates follow-up tasks automatically.

### MVP Design Consequence

The first build should prioritize:

- Public page that captures leads.
- Mobile dashboard.
- One-tap actions.
- BizzNexx operator admin.
- Assisted setup workflow.
- Import/forward-friendly data cleanup.

It should not prioritize:

- Heavy CRM forms.
- Desktop-first dashboards.
- Mandatory WhatsApp API connection.
- Native mobile app before validation.
- Fully automated AI chatbot.

### Frontend

- React
- Mobile-first responsive UI
- PWA-ready owner dashboard
- Public catalogue page
- Owner dashboard
- Setup wizard
- Catalogue editor
- Lead pipeline
- Payment tracker
- Message assistant

### Backend

- Django
- Django REST Framework
- PostgreSQL
- Django admin for BizzNexx internal operations
- Role model: admin, BizzNexx operator, business owner
- API endpoints for public page, inquiries, leads, payments, messages, scores
- Webhook-ready architecture for future WhatsApp/Instagram integrations

### AI

- Prompt templates by business pack
- Guardrail layer for unsafe claims
- Editable output
- Logging of generated and copied messages

### Hosting

- React: Vercel/Netlify or same VPS behind Nginx
- Django API: Render/Fly.io/Railway/VPS
- PostgreSQL: managed database
- Media: S3-compatible object storage later; local/media placeholder for MVP
- Domain: `bizznexx.com` or selected domain
- Public pages: `bizznexx.com/b/{slug}` initially

## 9. MVP Build Roadmap

### Phase 0: Alignment and Assets, 3-5 Days

Deliverables:

- Final MVP scope
- Segment pack order
- Updated ontology
- Demo data for 6 packs
- Go-live checklist
- Initial pricing hypothesis

Decision gate:

- Founders agree the first sellable offer is catalogue page + lead capture + operating dashboard.

### Phase 1: Functional MVP Foundation, 2 Weeks

Deliverables:

- Django project
- PostgreSQL schema
- Auth and roles
- Business setup
- Catalogue and catalogue item APIs
- Public page route
- Inquiry form
- Lead pipeline
- Payment tracker
- Basic dashboard

Decision gate:

- A real business can be set up internally and share a public page that captures inquiries.

### Phase 2: Vertical Pack MVP, 1 Week

Deliverables:

- Tutor pack complete
- Event/makeup/photo pack complete
- Freelancer/agency pack complete
- Segment-specific fields
- Segment-specific messages
- Segment-specific public page templates

Decision gate:

- 3 demo businesses look meaningfully different by segment, not like the same template with labels changed.

### Phase 3: AI and Scoring, 1 Week

Deliverables:

- AI message assistant
- Message template library
- Growth Score v0
- Health Score v0
- Recommendation cards
- Safety disclaimers

Decision gate:

- User can generate/copy useful messages and understand the score-based next action.

### Phase 4: Pilot Readiness, 1 Week

Deliverables:

- Privacy policy
- Terms and scope disclaimer
- Intake form
- Onboarding SOP
- Support SOP
- Internal admin dashboard
- Analytics/event tracking
- Backup process
- Pilot landing page

Decision gate:

- Team can onboard 5 paid pilot users without engineering intervention for every small change.

### Phase 5: Paid Pilot, 3-4 Weeks

Deliverables:

- 10-15 pilot users
- 5+ paid setup users
- Weekly usage report
- Objection log
- Testimonial library
- Pricing feedback
- Go/no-go SaaS decision

Decision gate:

- Build deeper product only if real businesses share pages, capture leads, use follow-ups, and pay.

## 10. Go-Live Requirements

### Product Requirements

- Public business pages work on mobile
- Inquiry form creates records
- WhatsApp CTA works
- Dashboard shows real open tasks
- Catalogue editor works for BizzNexx operators
- Lead pipeline supports each pack
- Payment tracker supports unpaid, part-paid, paid, overdue
- Message assistant has safe templates
- Monthly summary export exists
- Admin can create/edit/publish business pages

### Business Requirements

- Pricing page or offer sheet
- Starter/Growth/Managed package definitions
- Pilot terms
- Refund/cancellation policy
- Sales script
- Intake form
- 6 demo businesses
- 10 content scripts
- Founder outreach list
- Support process

### Legal and Trust Requirements

- Privacy policy
- Terms of use
- Consent for collecting customer phone/payment details
- Consent for testimonials/photos
- Disclaimer: not accounting/GST/legal/tax advice
- Safe collections policy
- Data deletion process
- Internal access control

### Technical Requirements

- Production environment
- Domain and HTTPS
- Environment variables
- Database backups
- Error logging
- Basic analytics
- Admin access controls
- CORS/security settings
- Form spam protection
- Media upload limit
- Deployment runbook

### Operations Requirements

- Setup SOP
- Catalogue content checklist
- Pilot onboarding checklist
- Support SLA
- Issue tracker
- User feedback log
- Weekly metrics review
- Data correction process

## 11. Launch Offer

### Recommended Pilot Offer

BizzNexx Starter Pilot for service businesses.

Includes:

- Public catalogue page
- 3-5 services/packages
- Inquiry form
- WhatsApp CTA
- Basic lead dashboard
- Payment tracker
- 10 WhatsApp message templates
- One setup call
- 14-day support

Pilot pricing hypothesis:

- Setup: Rs. 1,999-4,999
- Monthly continuation: Rs. 499-999

Do not advertise as cheap website building. Advertise as "your service page plus lead and payment system."

## 12. Immediate Build Priorities

1. Use the persona-first blueprint to lock the first three persona packs: Tutor, Event Provider, Freelancer/Agency.
2. Expand backend models to match the MVP ontology.
3. Create Django project and API.
4. Add React routing for public pages and owner dashboard.
5. Build inquiry form that creates real records.
6. Build BizzNexx operator console for assisted setup.
7. Build admin-assisted catalogue editor.
8. Add 3 segment demo businesses.
9. Add message template library by segment.
10. Add Growth Score and Health Score calculations.
11. Create pilot landing page and setup intake.
12. Prepare go-live legal/disclaimer pages.

## 13. Research Sources

- Ministry of MSME Annual Report 2025-26: https://msme.gov.in/ministry-msme-annual-report-2025-26-english
- MSME Annual Report PDF: https://msme.gov.in/sites/default/files/MSMEANNUALREPORT2025-26ENGLISH_0.pdf
- Zoho State of Digital and Customer Operations in Indian MSMEs: https://oweb.zohowebstatic.com/sites/oweb/images/zohobigin/state-of-digital-and-customer-operations-in-india-msme.pdf
- India SME Forum / Meta State of Digitalisation in Indian MSMEs: https://indiasmeforum.org/digishaastra/assets/docs/Final-META-Report-Card-2025.pdf
- SMEStreet on MSME digital presence: https://smestreet.in/msme-opportunities/msme-digital-presence-remains-low-despite-indias-online-push-10917024
- FISME delayed payments summary: https://fisme.org.in/study/delayed-payments-to-msmes-decline-from-rs-10-lakh-cr-to-rs-7-lakh-cr-but-challenges-persist-game-fisme-report/
- myBillBook feature positioning: https://mybillbook.in/
- Khatabook feature positioning: https://khatabook.com/en/
