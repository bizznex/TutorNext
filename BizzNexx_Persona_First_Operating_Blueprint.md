# BizzNexx Persona-First Operating Blueprint

## 1. Purpose

This document defines how BizzNexx should understand each customer persona before building features. The goal is to avoid a messy, generic business and instead create a structured, repeatable, segment-aware operating system for Indian service-led microbusinesses.

The rule is simple:

No feature should be built unless it maps to a specific persona, business event, workflow, data object, and measurable outcome.

## 2. Core Operating Philosophy

BizzNexx is persona-first, not feature-first.

The customer does not want another CRM, website builder, accounting tool, or dashboard. The customer wants their business to look professional, get inquiries, respond faster, follow up properly, collect money, and know what matters today.

Therefore BizzNexx must understand:

- Who the business owner is
- What the business sells
- How the business gets inquiries
- What proof builds trust
- How the prospect becomes a paying customer
- Where follow-up usually breaks
- Where money gets stuck
- What the owner can realistically do on mobile
- What BizzNexx must do for them

## 3. Non-Negotiable Design Rules

1. Mobile-first owner experience.
2. Assisted setup before self-serve complexity.
3. Catalogue page is the first structured data capture point.
4. No heavy manual CRM maintenance.
5. Every dashboard card must produce an action.
6. Every business type gets its own vocabulary.
7. Every business type gets its own onboarding schema.
8. Every business type gets its own message templates.
9. Every business type gets its own health and growth scoring logic.
10. Avoid regulated promises: GST filing, legal advice, tax advice, lending, recovery.

## 4. Persona Architecture

Each BizzNexx persona has five layers:

### Layer 1: Owner Persona

Who runs the business and what constraints they have.

### Layer 2: Buyer Persona

Who inquires and pays.

### Layer 3: Offer Ontology

What is being sold and how it should be represented in the catalogue.

### Layer 4: Operating Workflow

How inquiry turns into payment.

### Layer 5: BizzNexx Intervention

What BizzNexx captures, recommends, automates, or assists.

## 5. Universal BizzNexx Objects

These objects are common across business types:

- Business
- Owner
- Public Page
- Catalogue
- Catalogue Item
- Trust Proof
- Inquiry
- Lead
- Follow-Up Task
- Quote / Fee Plan
- Customer
- Payment
- Message Template
- Generated Message
- Page Event
- Growth Score
- Health Score
- Monthly Summary
- Subscription / Package
- Setup Project
- Support Request

Every persona pack extends these objects with business-specific fields.

## 6. Universal Customer Journey

1. Business owner signs up or is onboarded by BizzNexx.
2. BizzNexx collects business details, services, proof, payment terms, and communication style.
3. BizzNexx creates a public catalogue page.
4. Owner shares page through WhatsApp, Instagram, referrals, Google Business Profile, and content.
5. Prospect submits inquiry or opens WhatsApp with pre-filled context.
6. Inquiry becomes lead.
7. Owner receives mobile action card.
8. BizzNexx suggests message.
9. Owner sends message through WhatsApp.
10. Lead moves through segment-specific stages.
11. Payment is tracked.
12. Dashboard shows next actions, pending money, and business health.
13. Monthly summary is generated.

## 7. Persona Pack 1: Tutor / Coach / Trainer

### Owner Persona

Solo tutor, coaching class owner, music teacher, language trainer, fitness coach, or skills trainer.

Typical behavior:

- Runs business from phone.
- Gets leads from parents, students, referrals, WhatsApp groups, Instagram, flyers.
- Explains the same course details repeatedly.
- Tracks trials and monthly fees manually.
- Dislikes awkward payment reminders.

### Buyer Persona

Parent, student, working professional, or learner.

Buyer needs:

- Understand subject/course quickly.
- Trust teacher quality.
- Know batch timing and fee.
- Book trial easily.
- Receive clear WhatsApp communication.

### Catalogue Ontology

Required catalogue fields:

- Subject/course
- Class/grade/skill level
- Board/exam/category
- Delivery mode: online, offline, hybrid
- Batch timing
- Trial class policy
- Monthly fee/session fee
- Teacher profile
- Results/testimonials
- Parent/student FAQ

### Workflow

Inquiry -> first response -> trial proposed -> trial scheduled -> trial completed -> fee plan sent -> enrollment -> monthly fee due -> repeat payment reminders -> progress/testimonial request.

### Segment-Specific Lead Statuses

- New inquiry
- Parent/student contacted
- Trial proposed
- Trial scheduled
- Trial completed
- Fee sent
- Enrolled
- Not joined

### Minimum Data Required

- Student name
- Parent/contact person
- Phone number
- Class/grade
- Subject/course
- Preferred timing
- Trial date
- Fee plan
- Payment cycle

### AI Message Templates

- Parent inquiry reply
- Trial class confirmation
- Trial reminder
- Post-trial follow-up
- Fee plan explanation
- Monthly fee reminder
- Progress update
- Testimonial request

### Growth Score Logic

- Catalogue completeness
- Trial CTA readiness
- Testimonials/results availability
- Inquiry response speed
- Trial conversion rate
- Follow-up completion

### Health Score Logic

- Leads with next action
- Trials pending
- Enrollments active
- Monthly fees collected
- Overdue fees
- Parent communication discipline

### BizzNexx Must Do

- Create parent-friendly catalogue page.
- Capture inquiries by subject/class.
- Keep trial and fee workflow visible.
- Generate polite parent-facing messages.
- Track recurring monthly fee cycle.

### Do Not Build Initially

- Attendance management
- Learning management system
- Homework tracking
- Class video hosting
- Full fee accounting

## 8. Persona Pack 2: Makeup Artist / Photographer / Event Service Provider

### Owner Persona

Makeup artist, wedding photographer, mehendi artist, decorator, small event planner, or event service provider.

Typical behavior:

- Gets inquiries through Instagram, WhatsApp, referrals.
- Sends portfolio repeatedly.
- Quotes by event type and date.
- Needs advance to block booking.
- Tracks balance manually.

### Buyer Persona

Bride, family member, event organizer, couple, or small business hosting an event.

Buyer needs:

- See portfolio.
- Check availability.
- Understand packages.
- Trust style and reliability.
- Confirm booking and payment terms.

### Catalogue Ontology

Required catalogue fields:

- Event type
- Service package
- Portfolio/gallery
- Starting price
- Location/service area
- Add-ons
- Booking date availability
- Advance policy
- Balance due policy
- Testimonials

### Workflow

Inquiry -> event date check -> package explanation -> quote sent -> advance requested -> booking confirmed -> pre-event reminder -> balance reminder -> post-event testimonial/gallery update.

### Segment-Specific Lead Statuses

- New event inquiry
- Availability checked
- Package shared
- Quote sent
- Advance pending
- Booking confirmed
- Balance pending
- Completed
- Lost

### Minimum Data Required

- Customer name
- Phone number
- Event date
- Event type
- Venue/location
- Package interested
- Quote amount
- Advance amount
- Balance amount

### AI Message Templates

- Event inquiry reply
- Availability confirmation
- Package explanation
- Quote message
- Advance request
- Booking confirmation
- Balance reminder
- Review/testimonial request

### Growth Score Logic

- Portfolio completeness
- Package clarity
- Inquiry capture readiness
- Instagram/catalogue link readiness
- Quote-to-booking conversion

### Health Score Logic

- Quotes pending
- Advances pending
- Confirmed bookings
- Balance payments due
- Event follow-up readiness

### BizzNexx Must Do

- Make portfolio page visually trustworthy.
- Capture event date and event type.
- Track advance and balance.
- Make quote and booking communication clean.

### Do Not Build Initially

- Full calendar booking marketplace
- Vendor coordination
- Inventory/costing
- Paid ads management
- Automated contract signing

## 9. Persona Pack 3: Freelancer / Small Agency

### Owner Persona

Designer, developer, content writer, marketer, consultant, or small agency founder.

Typical behavior:

- Gets leads from LinkedIn, WhatsApp, Instagram, referrals, communities.
- Sends services, deck, portfolio, or rate card repeatedly.
- Struggles with proposal follow-up.
- Tracks milestone payments manually.

### Buyer Persona

Startup founder, small business owner, marketing manager, creator, or individual professional.

Buyer needs:

- Understand service capability.
- See proof/case studies.
- Know process and pricing range.
- Book discovery call.
- Receive proposal and follow-up clearly.

### Catalogue Ontology

Required catalogue fields:

- Service category
- Package/retainer
- Case study
- Work sample
- Starting price/range
- Delivery timeline
- Process
- Client proof
- Discovery call CTA

### Workflow

Inquiry -> discovery call -> requirement note -> proposal/quote -> follow-up -> project won/lost -> milestone payment -> delivery -> final payment -> testimonial/referral.

### Segment-Specific Lead Statuses

- New inquiry
- Discovery call booked
- Requirement captured
- Proposal sent
- Follow-up due
- Project won
- Project lost
- Milestone payment pending
- Completed

### Minimum Data Required

- Client/business name
- Contact person
- Phone/email
- Project type
- Budget range
- Discovery call date
- Proposal status
- Quote amount
- Milestone dates

### AI Message Templates

- Discovery call reply
- Requirement summary
- Proposal follow-up
- Scope explanation
- Milestone payment reminder
- Final payment reminder
- Testimonial request
- Repeat project pitch

### Growth Score Logic

- Case study readiness
- Offer clarity
- Discovery CTA readiness
- Proposal follow-up discipline
- Lead source performance

### Health Score Logic

- Open proposals
- Follow-ups due
- Milestone payments pending
- Win/loss rate
- Repeat client activity

### BizzNexx Must Do

- Package services clearly.
- Track proposals and follow-ups.
- Track milestone payments.
- Generate professional B2B messages.

### Do Not Build Initially

- Project management boards
- Time tracking
- Expense accounting
- Contract automation
- Team productivity tracking

## 10. Persona Pack 4: Consultant / Professional Service Provider

### Owner Persona

Career coach, business consultant, tax consultant, legal consultant, wellness coach, admissions consultant, or other professional service provider.

Typical behavior:

- Sells trust before service.
- Needs credibility and disclaimers.
- Gets inquiries through referrals, social content, WhatsApp, LinkedIn.
- Converts through consultation.

### Buyer Persona

Individual or business seeking expert advice.

Buyer needs:

- Trust credentials.
- Understand scope.
- Know session/package structure.
- Book consultation.
- Receive clear next steps.

### Catalogue Ontology

Required catalogue fields:

- Expertise area
- Credentials
- Consultation type
- Session/package structure
- Price or starting range
- Disclaimer
- Case examples/testimonials
- Booking CTA

### Workflow

Inquiry -> consultation topic captured -> session proposed -> booking confirmed -> payment -> session completed -> follow-up/package pitch -> repeat/retainer.

### Segment-Specific Lead Statuses

- New consultation inquiry
- Topic captured
- Session proposed
- Session booked
- Payment pending
- Session completed
- Package proposed
- Retainer/converted
- Closed

### Minimum Data Required

- Prospect name
- Phone/email
- Consultation topic
- Preferred time
- Session type
- Payment status
- Disclaimer acceptance
- Follow-up date

### AI Message Templates

- Consultation inquiry reply
- Scope clarification
- Session confirmation
- Payment reminder
- Post-session follow-up
- Package proposal
- Referral request

### Growth Score Logic

- Credential completeness
- Disclaimer readiness
- Consultation CTA readiness
- Trust proof availability
- Booking conversion

### Health Score Logic

- Open consultations
- Follow-ups due
- Package proposals pending
- Payment status
- Repeat/retainer conversion

### BizzNexx Must Do

- Create credibility-first public page.
- Handle disclaimers carefully.
- Track consultation and package flow.
- Avoid regulated overclaims.

### Do Not Build Initially

- Legal/tax/medical advice engine
- Document drafting
- Appointment marketplace
- Paid ads
- Full client case management

## 11. Persona Pack 5: Creator / Workshop / Paid Services

### Owner Persona

Creator, influencer, educator, community builder, or expert selling workshops, courses, brand collaborations, paid calls, or services.

Typical behavior:

- Gets DMs from brands and followers.
- Has informal rate card.
- Tracks deliverables and payments manually.
- Needs fast response and proof of reach.

### Buyer Persona

Brand, agency, follower, learner, community member, or small business.

Buyer needs:

- Understand available offers.
- See social proof.
- Know pricing/rate card or inquiry path.
- Confirm deliverables.
- Pay and receive output.

### Catalogue Ontology

Required catalogue fields:

- Offer type
- Rate card/package
- Audience profile
- Social proof
- Deliverables
- Timeline
- Past collaborations
- Booking/inquiry CTA

### Workflow

Inquiry -> offer/rate card shared -> deliverables confirmed -> quote sent -> payment/advance -> delivery -> final payment -> testimonial/repeat collaboration.

### Segment-Specific Lead Statuses

- New inquiry
- Rate card shared
- Deliverables discussed
- Quote sent
- Deal confirmed
- Delivery pending
- Payment pending
- Completed
- Repeat opportunity

### Minimum Data Required

- Brand/client name
- Contact person
- Inquiry type
- Deliverable type
- Campaign date
- Rate quoted
- Deliverable status
- Payment status

### AI Message Templates

- Brand inquiry reply
- Rate card explanation
- Deliverable confirmation
- Quote follow-up
- Payment reminder
- Collaboration closure
- Repeat collaboration pitch

### Growth Score Logic

- Rate card readiness
- Social proof completeness
- Offer clarity
- Inquiry-to-deal conversion
- Repeat collaboration readiness

### Health Score Logic

- Open deals
- Deliverables pending
- Payment pending
- Follow-ups due
- Repeat opportunities

### BizzNexx Must Do

- Turn scattered creator offerings into a clear catalogue.
- Track deliverables and payments.
- Help with brand-safe communication.

### Do Not Build Initially

- Social media analytics platform
- Creator marketplace
- Content scheduling
- Contract automation
- Payout splitting

## 12. Persona Pack 6: Home Service / Local Specialist

### Owner Persona

Home bakery, repair service, beauty service at home, yoga teacher, local specialist, pet groomer, or small neighborhood provider.

Typical behavior:

- Gets leads from WhatsApp, referrals, Instagram, Google search.
- Needs location/service area clarity.
- Quotes by service/date/location.
- Relies on reviews and repeat customers.

### Buyer Persona

Local household, individual, parent, resident, or neighborhood customer.

Buyer needs:

- Know service area.
- See services/pricing.
- Check availability.
- Trust reviews.
- Book quickly.

### Catalogue Ontology

Required catalogue fields:

- Service list
- Service area
- Availability window
- Price range
- Photos/work samples
- Customer reviews
- Booking CTA
- Payment terms

### Workflow

Inquiry -> location/service check -> availability confirmation -> quote -> booking -> service completed -> payment -> review/referral.

### Segment-Specific Lead Statuses

- New local inquiry
- Location checked
- Availability shared
- Quote sent
- Booking confirmed
- Service completed
- Payment pending
- Review requested

### Minimum Data Required

- Customer name
- Phone number
- Location
- Service needed
- Preferred date/time
- Quote amount
- Booking status
- Payment status

### AI Message Templates

- Local inquiry reply
- Service area confirmation
- Availability message
- Quote explanation
- Booking reminder
- Payment reminder
- Review request
- Referral request

### Growth Score Logic

- Local service page completeness
- Review readiness
- WhatsApp CTA readiness
- Location clarity
- Booking conversion

### Health Score Logic

- Booking follow-ups
- Payments pending
- Repeat customers
- Reviews collected
- Lost inquiry reasons

### BizzNexx Must Do

- Make local service page clear and mobile-first.
- Capture location and availability needs.
- Track bookings, payments, and reviews.

### Do Not Build Initially

- Route planning
- Marketplace bidding
- Staff scheduling
- Delivery logistics
- Inventory management

## 13. Persona-First Setup Intake

### Universal Intake

- Business name
- Owner name
- WhatsApp number
- City/service area
- Business type
- Preferred language
- Preferred tone
- Existing Instagram/website/link
- Current services
- Current pricing
- Proof/testimonials/photos
- Payment terms
- Current pain: leads, follow-up, payments, catalogue, CA records

### Segment Intake Add-ons

Tutor:

- Subjects/classes
- Board/exam
- Trial class rules
- Batch timings
- Monthly fee cycle

Event provider:

- Event types
- Package names
- Portfolio photos
- Advance/balance terms
- Service area

Freelancer/agency:

- Services
- Case studies
- Budget ranges
- Discovery call process
- Milestone terms

Consultant:

- Expertise areas
- Credentials
- Disclaimers
- Session/package types
- Booking process

Creator:

- Offer types
- Rate card
- Audience proof
- Deliverables
- Collaboration terms

Home service:

- Service area
- Availability
- Price ranges
- Service photos
- Review proof

## 14. Structured Delivery SOP

### Stage 1: Intake

Output:

- Completed persona-specific intake
- Segment selected
- Missing information list
- Setup package confirmed

Exit gate:

- Enough information exists to draft catalogue page.

### Stage 2: Catalogue Structuring

Output:

- Catalogue title
- Service categories
- Catalogue items
- Pricing display rules
- FAQs
- Trust proof list

Exit gate:

- Owner approves what the business sells and how it is described.

### Stage 3: Public Page Build

Output:

- Public page draft
- WhatsApp CTA
- Inquiry form
- Mobile preview

Exit gate:

- Owner says they would share the page with a real prospect.

### Stage 4: Operating Dashboard Setup

Output:

- Lead pipeline
- Follow-up tasks
- Payment tracker
- Segment-specific message templates
- Growth and Health Score v0

Exit gate:

- Owner can understand what to do today in under 2 minutes.

### Stage 5: Pilot Handover

Output:

- Page link
- Mobile app/PWA install instruction
- First 10 leads/payments entered or imported
- Support channel opened
- Weekly check-in scheduled

Exit gate:

- Owner can share page, capture inquiry, send message, and mark status.

### Stage 6: Weekly Review

Output:

- Leads captured
- Follow-ups completed
- Payments pending
- Messages used
- Owner blockers
- Improvement actions

Exit gate:

- Owner sees practical value and agrees to continue or pay.

## 15. Build Governance

### Feature Acceptance Checklist

Before building a feature, answer:

- Which persona needs this?
- Which business event triggers it?
- Which data object stores it?
- Which mobile action uses it?
- Which dashboard card reflects it?
- Which success metric improves?
- Can BizzNexx Ops do it manually first?

If these cannot be answered, reject or defer the feature.

### Data Field Acceptance Checklist

Before adding a field, answer:

- Is it required to capture inquiry, follow up, quote, collect, or summarize?
- Can it be inferred from catalogue/page context?
- Can it be optional or progressive?
- Does the owner understand the label?
- Is it segment-specific?

If not required, defer it.

## 16. MVP Implementation Order

1. Build universal Business, Catalogue, Public Page, Inquiry, Lead, Task, Payment, Message objects.
2. Build mobile-first owner dashboard.
3. Build BizzNexx operator console.
4. Build Tutor persona pack first.
5. Add Event Provider pack.
6. Add Freelancer/Agency pack.
7. Add Consultant pack.
8. Add Creator pack.
9. Add Home Service pack.
10. Add Growth and Health Scores per pack.
11. Add PWA install support.
12. Add pilot reporting dashboard for BizzNexx team.

## 17. What To Reject Now

- Generic CRM customization.
- Native mobile app before PWA validation.
- Full WhatsApp API integration before pilot proof.
- Instagram DM automation before manual capture proves value.
- Payment gateway integration before payment tracking proves value.
- GST filing or accounting automation.
- Marketplace model.
- Complex themes and design customization.
- Features not attached to a specific persona workflow.

## 18. Definition of a Structured Business

BizzNexx is structured only if:

- Each customer belongs to a persona pack.
- Each persona pack has defined fields, statuses, messages, scores, and page sections.
- Each setup project has stage gates.
- Each user has a clear package and scope limit.
- Each support request is logged.
- Each feature maps to a workflow.
- Each pilot user produces measurable behavior.

This is how BizzNexx avoids becoming messy.
