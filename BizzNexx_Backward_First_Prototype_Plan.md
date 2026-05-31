# BizzNexx Backward-First Prototype Plan

## Prototype Objective

Build a realistic, clickable and partially functional prototype that shows what BizzNexx feels like as a paid growth and operating service for one narrow customer workflow before committing to a full product build.

The first prototype should answer one question:

Can a small service business owner understand, trust, and want to use BizzNexx within the first 15 minutes because it helps them present their catalogue, generate leads, follow up, collect payments, and see business health in one place?

## First-Principles Business Scope

BizzNexx should not be another accounting tool, CRM, payment app, or generic website builder.

BizzNexx should understand the small service business as a complete operating system:

- What the business sells
- Who the business sells to
- How customers discover the business
- What proof builds trust
- Which inquiries become leads
- Which leads need follow-up
- Which offers or packages were sent
- Which payments are due
- Which business actions should happen today

The paid service should combine three layers:

- Public growth layer: catalogue website, service page, inquiry capture, WhatsApp CTA, trust proof, lead magnets
- Operating layer: lead tracker, follow-ups, quote/fee plan tracker, payment visibility, customer records
- Intelligence layer: AI messages, business health score, next-best-action suggestions, monthly summary

The first prototype should prove the combined value of these three layers. A beautiful website without operations is incomplete. A tracker without lead generation is also incomplete.

## First Use Case

### Tutor / Coach Catalogue-to-Fee Growth System

A tutor or coach offers classes, packages, trial sessions, or batches. Today their catalogue is scattered across WhatsApp messages, Instagram posts, PDF fee charts, old images, and verbal explanations. They receive student/parent inquiries through WhatsApp, Instagram, referrals, or phone calls. They need a professional web page that presents their services, captures leads, helps them respond quickly, schedules trial classes, follows up politely, tracks monthly fees, and shows what needs attention today.

This is the recommended first use case because the workflow is simple, catalogues are easy to model, recurring payments are common, follow-ups matter, and Ria Mukherji can explain the problem clearly through content.

## Backward-First Target Experience

When the user opens BizzNexx, the first screen should immediately show:

- How their public catalogue page is performing
- How many inquiries came from the page
- Who needs follow-up today
- Which trial classes are pending confirmation
- Which students or parents owe money
- How much cash is expected this month
- What message should be sent next
- A simple BizzNexx Health Score

The product should feel like a business assistant, not a spreadsheet.

Example first-screen message:

> Good morning. Your catalogue page generated 4 new inquiries this week. You have 6 follow-ups today, Rs. 18,500 pending, and 3 trial students waiting for confirmation.

## Paid Service Definition

BizzNexx can start as an assisted service before becoming a self-serve platform.

### What the Customer Pays For

- BizzNexx sets up their service catalogue
- BizzNexx creates a clean public web page for the business
- BizzNexx gives them a lead capture and WhatsApp inquiry flow
- BizzNexx organizes their leads, follow-ups, payments, and monthly records
- BizzNexx gives them AI-assisted messages and next actions
- BizzNexx helps them look more professional and respond faster

### Initial Service Packages

#### Starter Setup

For solo tutors/coaches with 3-5 services.

Includes:

- One-page catalogue website
- Lead capture form
- WhatsApp inquiry button
- Basic lead tracker
- Fee/payment tracker
- 10 message templates
- One assisted setup call

#### Growth Setup

For tutors/coaches with batches, testimonials, and multiple packages.

Includes:

- Multi-section catalogue website
- Services, batches, fees, testimonials, FAQ
- Lead capture and source tracking
- Trial class workflow
- Payment tracker
- AI message library
- Monthly business health dashboard

#### Managed Monthly Copilot

For users who need ongoing help.

Includes:

- Monthly dashboard review
- Catalogue updates
- Message/template updates
- Lead and payment hygiene review
- Monthly export preparation

## Prototype Scope

### In Scope

- Public catalogue website for the business
- Catalogue/service management
- Lead capture from the public page
- WhatsApp CTA and pre-filled inquiry messages
- Dashboard for today's actions
- Lead and student tracker
- Trial class tracker
- Fee/payment tracker
- AI-assisted WhatsApp message suggestions
- Business Health Score
- Business profile/service page publishing
- Monthly CA-ready export mock
- Assisted setup flow

### Out of Scope

- Full accounting
- GST filing
- Payment gateway ownership
- WhatsApp Business API automation
- Inventory
- SEO-heavy marketplace features
- Paid ads management
- Complex website themes
- Lending or recovery workflows
- Complex CRM pipeline customization

## Core Ontology

### Business

Represents the tutor, coach, trainer, or small institute.

Fields:

- Business name
- Owner name
- Business type
- City
- Teaching mode: online, offline, hybrid
- Contact number
- WhatsApp number
- Public page slug
- Brand colors
- Logo/photo
- Service categories
- Payment terms
- Preferred language
- Trust proof available: testimonials, certifications, results, portfolio

### Catalogue

Represents the complete public offer structure of the business.

Fields:

- Business
- Catalogue title
- Primary promise
- Target audience
- Service categories
- Featured services
- Testimonials
- FAQs
- Contact CTA
- Active/inactive status

### Catalogue Item / Service

Represents what the tutor sells and what appears on the public web page.

Fields:

- Service name
- Subject or skill
- Format: one-to-one, group, batch, workshop
- Duration
- Monthly fee
- Trial fee
- Advance required
- Display price: visible, hidden, starting from, contact for pricing
- Public description
- Benefits
- Who it is for
- Outcomes promised
- CTA label
- Notes

### Public Web Page

Represents the website BizzNexx creates for the customer.

Fields:

- Business
- Slug
- Page title
- Hero headline
- Hero subtext
- Sections enabled
- Published status
- Last updated date
- Inquiry CTA
- WhatsApp CTA
- SEO title
- SEO description

### Trust Proof

Represents evidence that helps visitors trust the business.

Fields:

- Business
- Type: testimonial, result, certification, before-after, client logo, work sample
- Title
- Description
- Customer name
- Image/document link
- Approved for public use

### Lead Source

Represents where the lead came from.

Fields:

- Source type: catalogue page, WhatsApp, Instagram, referral, call, manual, campaign
- Source detail
- Campaign name
- Landing page
- UTM/source tag

### Lead

Represents a new inquiry.

Fields:

- Lead name
- Parent/student name
- Phone number
- Source: WhatsApp, Instagram, referral, call, website
- Source detail
- Landing page or catalogue item
- Interested service
- Inquiry date
- Status: new, contacted, trial scheduled, trial completed, converted, lost
- Expected monthly value
- Next follow-up date
- Last message sent
- Notes

### Inquiry

Represents a form submission or WhatsApp click before it becomes a qualified lead.

Fields:

- Business
- Name
- Phone number
- Message
- Interested catalogue item
- Source page
- Created date
- Qualified status
- Converted lead

### Trial Class

Represents a scheduled or completed trial.

Fields:

- Lead
- Service
- Trial date
- Trial status: proposed, confirmed, completed, missed, rescheduled
- Feedback
- Next action

### Customer / Student

Represents a converted paying student or client.

Fields:

- Name
- Parent/contact person
- Phone number
- Service enrolled
- Start date
- Monthly fee
- Payment cycle
- Active/inactive status
- Notes

### Quote / Fee Plan

Represents the package or fee communicated.

Fields:

- Lead or student
- Service
- Fee amount
- Billing frequency
- Discount, if any
- Terms
- Sent date
- Status: draft, sent, accepted, rejected, expired

### Payment

Represents fees, advances, balances, and dues.

Fields:

- Student/customer
- Amount due
- Amount paid
- Due date
- Payment date
- Status: unpaid, part-paid, paid, overdue
- Payment mode: UPI, cash, bank transfer
- Reference note

### Follow-Up

Represents the next action BizzNexx asks the owner to take.

Fields:

- Related lead/student/payment
- Follow-up type: inquiry, trial, quote, fee, reactivation
- Due date
- Priority
- Suggested message
- Status: pending, done, snoozed

### AI Message

Represents message suggestions the owner can copy into WhatsApp.

Types:

- First response
- Trial confirmation
- Trial reminder
- Fee quote
- Payment reminder
- Overdue payment reminder
- Reactivation
- Thank-you message
- Catalogue page intro
- Service explanation
- Testimonial request
- Referral request

### BizzNexx Health Score

Represents business operating discipline.

Initial score components:

- Lead response discipline: 20
- Follow-up discipline: 20
- Conversion health: 15
- Payment collection health: 20
- Repeat customer health: 10
- Documentation readiness: 10
- Profile readiness: 5

### BizzNexx Growth Score

Represents whether the business is ready to generate and convert demand.

Initial score components:

- Catalogue completeness: 20
- Trust proof quality: 15
- Lead capture readiness: 15
- Response speed: 15
- Follow-up discipline: 15
- Payment clarity: 10
- Monthly review readiness: 10

## Recommended Real-App Prototype Stack

### Option A: Fastest No-Code Prototype

Use this if the goal is to test with real users within 5-7 days.

- Interface: Glide or Softr
- Database: Google Sheets or Airtable
- Forms: Google Forms or Tally.so
- Dashboard: Glide/Softr built-in charts or Looker Studio
- AI messages: OpenAI API through Make.com/Zapier, or manually generated first
- WhatsApp: Click-to-WhatsApp links with pre-filled messages
- Landing page: Framer, Carrd, or Webflow
- Demo data: 3 fake tutor businesses with realistic leads/payments

Recommended choice: Glide + Google Sheets + OpenAI API later. Start without automation first.

### Option B: Code Prototype

Use this if the goal is to turn the prototype into the first product foundation.

- Customer-facing web app: React
- Admin/backend: Django
- API: Django REST Framework
- Database: PostgreSQL
- UI: Tailwind CSS or shadcn-style component system
- Auth: Django auth or django-allauth
- AI: OpenAI API
- Charts: Recharts
- Deployment: Vercel/Netlify for React and Render/Fly.io/Railway for Django, or one VPS later
- WhatsApp: Click-to-WhatsApp links first

Recommended choice after validation: React + Django + PostgreSQL.

### Option C: Design-First Prototype

Use this if the team first wants look and feel without live data.

- UI design: Figma
- Clickable prototype: Figma prototype links
- Sample data: manual
- Validation: user walkthroughs over Zoom or in-person

Recommended choice for immediate visual alignment: Figma plus a Google Sheet data model.

## Prototype Screens

### 1. Assisted Setup

Purpose: configure the business in less than 15 minutes.

Inputs:

- Business name
- Type of coaching
- Subjects/services
- Catalogue items/packages
- Public page content
- Testimonials/trust proof
- Photos or work samples
- Fee plans
- Trial class policy
- Lead sources
- Payment terms
- Preferred message tone: polite, friendly, professional, Hinglish

Output:

- Workspace created
- Default services created
- Public catalogue page drafted
- Default message templates created
- Dashboard initialized

### 2. Public Catalogue Page

Purpose: help the business look credible and generate inquiries.

Sections:

- Hero: who the business helps and what they offer
- Services/catalogue items
- Trial class or consultation CTA
- Testimonials/trust proof
- FAQs
- Contact and WhatsApp CTA
- Inquiry form

Primary actions:

- Submit inquiry
- Click WhatsApp
- View service details
- Request trial/consultation

### 3. Catalogue Manager

Purpose: help the owner and BizzNexx team maintain what the business sells.

Sections:

- Services/packages
- Prices/fee plans
- Trial policy
- Photos/work samples
- Testimonials
- FAQs
- Publish status

### 4. Home Dashboard

Purpose: show what needs action today.

Sections:

- Catalogue page views/clicks
- New inquiries from catalogue page
- BizzNexx Health Score
- BizzNexx Growth Score
- Today's follow-ups
- Trial classes pending
- Pending payments
- Expected cash this month
- Suggested next best actions
- Quick actions: Add Lead, Add Payment, Send Reminder, Create Quote, Edit Catalogue

### 5. Lead Pipeline

Purpose: track inquiries from first message to conversion.

Statuses:

- New
- Contacted
- Trial Scheduled
- Trial Completed
- Fee Sent
- Converted
- Lost

Primary actions:

- Add note
- Schedule trial
- Generate WhatsApp reply
- Mark as converted
- Mark as lost

### 6. Lead Detail

Purpose: provide context and next action for one lead.

Shows:

- Contact details
- Interested service
- Conversation notes
- Trial status
- Fee plan
- Next follow-up
- Suggested WhatsApp message

### 7. Payments

Purpose: make money visibility obvious.

Views:

- Due this week
- Overdue
- Part-paid
- Paid
- Expected monthly cash

Primary actions:

- Mark paid
- Mark part-paid
- Copy reminder
- Add reference note

### 8. AI Message Assistant

Purpose: make the product feel useful immediately.

Message categories:

- Reply to new inquiry
- Confirm trial class
- Follow up after trial
- Send fee plan
- Payment reminder
- Overdue reminder
- Reactivate old lead
- Explain service/catalogue item
- Ask for testimonial
- Ask for referral

Each message should support:

- English
- Hindi
- Hinglish
- Friendly/professional tone

### 9. Monthly Export

Purpose: prove CA-ready value without becoming accounting software.

Export includes:

- Student/customer list
- Fees due
- Fees paid
- Outstanding payments
- Payment mode
- Month summary

## Sample User Journey

1. Ria's content offers a BizzNexx setup for tutors who want a professional catalogue page and lead tracker.
2. Tutor signs up through a simple form.
3. Tutor enters services, fees, trial policy, testimonials, photos, and five current leads.
4. BizzNexx generates a public catalogue page.
5. A parent submits an inquiry from the catalogue page or clicks WhatsApp.
6. The inquiry appears in the BizzNexx dashboard.
7. Tutor copies a suggested WhatsApp response.
8. Tutor marks the lead as trial scheduled.
9. Tutor marks one fee as part-paid.
10. Health Score and Growth Score update.
11. At month-end, tutor exports a summary.

## Prototype Data Model

Minimum tables:

- Businesses
- Catalogues
- Catalogue Items
- Public Pages
- Trust Proof
- Inquiries
- Lead Sources
- Services
- Leads
- Trial Classes
- Students
- Fee Plans
- Payments
- Follow Ups
- Message Templates
- Health Score Snapshots

## AI Prompt Categories

### First Response Prompt

Generate a polite WhatsApp reply to a new inquiry based on service, location, mode, and tone.

### Catalogue Page Prompt

Generate homepage copy, service descriptions, FAQs, and CTA text from the business profile and services.

### Service Explanation Prompt

Explain one catalogue item in a parent/customer-friendly way.

### Trial Confirmation Prompt

Confirm class time, duration, joining details, and next step.

### Post-Trial Follow-Up Prompt

Ask whether the parent/student wants to continue and offer a simple fee plan.

### Payment Reminder Prompt

Send a polite fee reminder without sounding aggressive.

### Overdue Payment Prompt

Send a firmer but respectful reminder for overdue payment.

### Reactivation Prompt

Restart conversation with an old lead without sounding pushy.

### Testimonial Request Prompt

Ask a satisfied customer for a short testimonial and permission to display it.

## Validation Test

### Users

Start with 10-15 users:

- 8 tutors/coaches/trainers
- 3 freelancers/small agencies
- 2 makeup/event/photo providers

### What to Measure

- Can they understand the dashboard in 2 minutes?
- Does the catalogue page make the business look more professional?
- Would they share the catalogue page with prospects?
- Does the page capture the right inquiry details?
- Can they add a lead without help?
- Do they like the suggested WhatsApp messages?
- Do they know who to follow up with today?
- Do they understand pending payments better than before?
- Would they continue using it for one week?
- Would they pay for assisted setup?
- Would they pay a monthly amount after setup?

## Success Criteria

The prototype is successful if:

- 10 users complete onboarding
- 7 users publish or approve a catalogue page
- 7 users add real leads or payments
- 5 users share their catalogue page or WhatsApp link
- 5 users use suggested messages
- 5 users return after 3 days
- 3 users ask for help setting it up for their actual business
- At least 2 users show willingness to pay for setup or monthly use

## Suggested Timeline

### Days 1-2: Design the Experience

- Finalize tutor use case
- Confirm ontology and fields
- Create sample data
- Create public catalogue page wireframe
- Create dashboard wireframe
- Draft message templates

### Days 3-5: Build the First React + Django Prototype

- Set up Django project and PostgreSQL models
- Set up React app
- Build public catalogue page route
- Build business admin dashboard
- Add lead tracker and payment tracker
- Add click-to-WhatsApp message buttons
- Add sample catalogue data

### Day 6: Content and Landing

- Create BizzNexx landing page
- Create lead capture form
- Draft Ria's first 3 content scripts
- Prepare demo business data

### Day 7: User Testing

- Test with 5 users first
- Observe setup friction
- Capture objections
- Revise UI and wording

### Week 2: Validation Sprint

- Expand to 10-15 users
- Track usage manually
- Collect willingness-to-pay signals
- Decide whether to move to code prototype
- Decide whether the paid setup package is clear enough to sell

## Team Ownership

### Rick

- Product logic
- User journey
- Interview guide
- Health Score definition
- Paid service packaging
- Prototype acceptance criteria

### Ria Mukherji

- User empathy
- Content scripts
- Customer discovery
- Tone and message testing
- Lead magnet distribution
- Catalogue story and trust-building angle

### Subhajit Sen

- Technical architecture
- Tool selection
- Data privacy review
- Prototype scalability path
- Future system architecture
- React + Django structure

### Abhishek Bhattacharya

- Data model
- Django/PostgreSQL model structure
- Dashboard metrics
- Health Score calculations
- Export logic

## Immediate Next Actions

1. Confirm tutor/coaching as the first use case.
2. Confirm that the first paid promise is catalogue page + lead capture + operating dashboard.
3. Create sample data for 3 demo tutor businesses.
4. Define the catalogue page template and fields.
5. Build the first React + Django prototype with one public page and one admin dashboard.
6. Draft 20 WhatsApp message templates.
7. Create the lead magnet: BizzNexx Tutor Catalogue & Lead System.
7. Test with 5 real users before polishing further.

## Recommended Starting Decision

Start with a thin React + Django prototype:

- Django + PostgreSQL for the business, catalogue, inquiry, lead, and payment models
- React for the public catalogue page and owner dashboard
- Click-to-WhatsApp buttons
- Manually prepared AI message templates
- Simple admin-assisted setup by the BizzNexx team
- Figma only for visual polish if needed

This gives the team something real enough to show users and sell as a paid setup service, while keeping the first version narrow enough to build quickly with Codex.
