# BizzNexx Realistic Synthetic Pilot Data and India Sensecheck

## 1. Purpose

This document defines realistic synthetic pilot data for BizzNexx and critically evaluates whether it is operationally believable for Indian service-led microbusinesses.

The goal is not to create pretty demo data. The goal is to create data that exposes real operational complexity:

- Informal WhatsApp-led inquiries
- Regional/local trust signals
- Price sensitivity
- Follow-up gaps
- Advance/balance payments
- Recurring dues
- Instagram/referral-led discovery
- Mobile-first owner behavior
- Messy but structured enough data

## 2. Design Principles for Synthetic Data

Synthetic data must be:

- Specific to business type
- Plausible in Indian cities
- Mobile and WhatsApp-first
- Price-realistic for micro/small businesses
- Operationally messy but not chaotic
- Useful for testing follow-up and payment workflows
- Clear enough for selected-user feedback
- Free from fake exaggerated claims

Synthetic data must not:

- Claim impossible outcomes
- Use premium metro pricing for all markets
- Hide practical constraints
- Assume laptop usage
- Assume users maintain CRM fields manually
- Assume all prospects come from forms
- Ignore local language/Hinglish behavior

## 3. Synthetic Pilot Businesses

The first pilot dataset should include six businesses:

1. Tutor / Coaching: Kolkata
2. Tutor / Skills Trainer: Indore
3. Bridal Makeup Studio: Durgapur
4. Event Photographer: Pune
5. Design Freelancer / Small Agency: Bengaluru
6. Local Home Service / Home Bakery: Lucknow

These six cover:

- Recurring payment use case
- Trial/consultation use case
- Advance/balance use case
- Portfolio/gallery use case
- Proposal/milestone use case
- Local-area service use case

## 4. Business 1: Ananya Learning Studio

### Business Profile

- Persona: Tutor / Coach
- City: Kolkata
- Owner: Ananya Sharma
- Mode: Hybrid
- Language: English + Hinglish
- Monthly revenue range: Rs. 45,000-80,000
- Current acquisition: WhatsApp referrals, parent groups, Instagram, local posters
- Current pain: missed parent follow-ups, late monthly fees, repeated explanation of batches

### Public Page Positioning

Headline:

Maths and Science coaching for Classes 8-12 with trial classes, parent updates, and structured revision.

Subtext:

Hybrid batches for CBSE, ICSE, and WB board students in South Kolkata. Parents receive monthly progress notes and fee reminders.

### Catalogue Items

1. Class 9-10 Maths Foundation
   - Format: Group batch
   - Fee: Rs. 2,500/month
   - Trial: Free 30-minute assessment
   - Timing: Tue/Thu 6 PM, Sat 11 AM

2. Class 11-12 Physics Support
   - Format: Small group
   - Fee: Rs. 3,500/month
   - Trial: Rs. 300 trial session
   - Timing: Mon/Wed 7 PM

3. One-to-One Doubt Class
   - Format: 1:1 session
   - Fee: Rs. 800/session
   - Trial: Not applicable

### Trust Proof

- 8 years teaching experience
- 120+ students taught
- Parent testimonial: "My son's confidence improved before boards because concepts were explained patiently."
- Result proof: "2025 batch: 14 students scored 80+ in Maths/Science"

### Persona-Specific Inquiry Fields

- Parent/student name
- Phone number
- Class
- Board
- Subject
- Preferred timing
- Trial interest
- Message

### Sample Leads

1. Rohit parent
   - Source: Catalogue page
   - Class: 10
   - Board: ICSE
   - Interested service: Class 9-10 Maths Foundation
   - Status: New inquiry
   - Next action: Send trial options
   - Expected value: Rs. 2,500/month
   - Follow-up age: 1 day

2. Meera parent
   - Source: Instagram bio
   - Class: 12
   - Board: CBSE
   - Interested service: Physics Support
   - Status: Trial scheduled
   - Next action: Send reminder before 7 PM session
   - Expected value: Rs. 3,500/month
   - Follow-up age: due today

3. Ayan parent
   - Source: WhatsApp referral
   - Class: 9
   - Board: WB
   - Interested service: Maths Foundation
   - Status: Contacted
   - Next action: Follow up after parent asked for fee details
   - Expected value: Rs. 2,500/month
   - Follow-up age: 3 days

### Sample Payments

1. Aarav
   - Service: Class 9 Maths
   - Amount due: Rs. 2,500
   - Status: Overdue
   - Age: 6 days overdue
   - Payment mode expected: UPI

2. Sohini
   - Service: One-to-One Doubt Class
   - Amount due: Rs. 1,600
   - Amount paid: Rs. 800
   - Status: Part paid
   - Age: 2 days pending

### Operational Sensecheck

High plausibility.

This is a strong first use case because:

- Parents already use WhatsApp.
- Trial and fee follow-up are real workflows.
- Monthly recurring fees create repeated need.
- Tutor can share the page in parent groups and referrals.
- Data capture fields are practical.

Risks:

- Some tutors may not want to publicly show fees.
- Parents may still prefer calling directly.
- Manual fee marking may be skipped unless reminders are useful.

Mitigation:

- Allow "Contact for fee" display.
- Keep click-to-call and WhatsApp CTAs.
- Add one-tap "paid" and "remind later."

## 5. Business 2: SpeakEasy English and Interview Coaching

### Business Profile

- Persona: Skills Trainer / Coach
- City: Indore
- Owner: Neha Jain
- Mode: Online
- Language: Hindi + English + Hinglish
- Monthly revenue range: Rs. 35,000-70,000
- Current acquisition: Instagram reels, WhatsApp referrals, local college groups
- Current pain: too many DMs asking same questions, trial call scheduling, payment before batch

### Public Page Positioning

Headline:

Spoken English and interview confidence coaching for students and first-job professionals.

Subtext:

Practical online batches with mock interviews, speaking practice, and simple weekly assignments.

### Catalogue Items

1. Spoken English Confidence Batch
   - Fee: Rs. 2,999/month
   - Format: Online group
   - Timing: Mon/Wed/Fri 8 PM

2. Interview Preparation Sprint
   - Fee: Rs. 4,999 for 3 weeks
   - Format: Small group
   - Includes: resume discussion, mock interview, HR questions

3. One-to-One Speaking Practice
   - Fee: Rs. 999/session
   - Format: 1:1 online

### Trust Proof

- 6 years training experience
- 300+ learners trained
- Testimonial: "I was scared to speak in interviews. The mock rounds helped a lot."
- Proof: "Placed learners from Indore, Bhopal, Jaipur, and Nagpur"

### Sample Leads

1. Kunal
   - Source: Instagram reel
   - Interested service: Interview Preparation Sprint
   - Status: New inquiry
   - Next action: Send batch start date and payment details
   - Expected value: Rs. 4,999

2. Radhika
   - Source: WhatsApp group
   - Interested service: Spoken English Batch
   - Status: Fee sent
   - Next action: Follow up before batch closes
   - Expected value: Rs. 2,999/month

### Operational Sensecheck

High plausibility.

This use case tests:

- Instagram lead source
- Batch deadline pressure
- Payment before joining
- Hinglish messaging
- Digital-only delivery

Risks:

- Learners may be price-sensitive.
- Many leads may be low-intent from reels.

Mitigation:

- Add lead quality fields: budget, urgency, batch interest.
- Add automated qualification questions.

## 6. Business 3: Ria Bridal Studio

### Business Profile

- Persona: Bridal / Event Service
- City: Durgapur
- Owner: Ria Das
- Mode: Venue service
- Language: Bengali + Hindi + English
- Monthly revenue range: seasonal, Rs. 40,000-2,00,000
- Current acquisition: Instagram, referrals, wedding groups
- Current pain: date availability, repeated package sharing, advance/balance tracking

### Public Page Positioning

Headline:

Bridal, engagement, and party makeup with clear packages, venue service, and date booking support.

Subtext:

Share your event date, venue, and preferred look. We confirm availability and package options before booking.

### Catalogue Items

1. Bridal Makeup Package
   - Starting price: Rs. 12,000
   - Advance: Rs. 4,000 to block date
   - Includes: HD makeup, hair, draping, consultation

2. Engagement Look
   - Starting price: Rs. 7,000
   - Advance: Rs. 2,500
   - Includes: makeup, hair styling, saree/dupatta setting

3. Party Makeup
   - Starting price: Rs. 3,500
   - Advance: Rs. 1,000

### Trust Proof

- 45+ bridal looks
- Portfolio gallery required
- Client testimonial: "Makeup stayed fresh through the full ceremony."
- Venue service available in Durgapur, Asansol, Bardhaman

### Persona-Specific Inquiry Fields

- Name
- Phone number
- Event type
- Event date
- Venue/location
- Preferred look
- Package interested
- Budget range
- Message

### Sample Leads

1. Priyanka
   - Source: Instagram
   - Event date: 14 Feb 2027
   - Location: Durgapur
   - Interested service: Bridal Makeup Package
   - Status: Package shared
   - Next action: Ask for advance to block date
   - Expected value: Rs. 12,000

2. Sanchita
   - Source: Catalogue page
   - Event date: 20 Dec 2026
   - Location: Asansol
   - Interested service: Engagement Look
   - Status: Availability checked
   - Next action: Send package comparison
   - Expected value: Rs. 7,000

### Sample Payments

1. Priyanka
   - Service: Bridal Package Advance
   - Amount due: Rs. 4,000
   - Status: Unpaid
   - Age: due today

2. Mitali
   - Service: Party Makeup Balance
   - Amount due: Rs. 2,500
   - Status: Overdue
   - Age: 2 days overdue

### Operational Sensecheck

High plausibility, but only if gallery exists.

This business will not convert without visuals.

Risks:

- Synthetic page without images will fail feedback.
- Event businesses have seasonal spikes.
- Availability/date conflicts are central.

Mitigation:

- Add gallery placeholders immediately.
- Add event date field as P0.
- Add advance/balance workflow as P0.

## 7. Business 4: FrameCraft Wedding Photography

### Business Profile

- Persona: Event Photographer
- City: Pune
- Owner: Nikhil Pawar
- Mode: On-site event service
- Language: Marathi + Hindi + English
- Monthly revenue range: Rs. 60,000-3,00,000 seasonal
- Current acquisition: Instagram, referrals, venue contacts
- Current pain: package negotiation, dates, advance, deliverable timelines, balance payment

### Public Page Positioning

Headline:

Wedding, engagement, and pre-wedding photography packages with clear deliverables and booking terms.

Subtext:

Check date availability, compare packages, and get a quote for your event.

### Catalogue Items

1. Engagement Photography
   - Starting price: Rs. 18,000
   - Advance: 30%
   - Deliverables: edited photos, online gallery

2. Wedding Day Coverage
   - Starting price: Rs. 45,000
   - Advance: 30%
   - Deliverables: candid + traditional photography

3. Pre-Wedding Shoot
   - Starting price: Rs. 25,000
   - Advance: 40%
   - Deliverables: edited photos and reel

### Trust Proof

- 80+ events covered
- Sample galleries required
- Testimonial: "Delivery timeline was clear and the photos were beautiful."

### Operational Sensecheck

High plausibility.

This tests a different event workflow:

- Deliverables matter
- Milestone/balance payments matter
- Gallery is non-negotiable

Risks:

- Photography packages vary too much for simple cards.
- Delivery disputes can occur.

Mitigation:

- Add deliverables and terms field.
- Add quote customization later, not first.

## 8. Business 5: Northstar Design Co.

### Business Profile

- Persona: Freelancer / Small Agency
- City: Bengaluru
- Owner: Arjun Mehta
- Mode: Remote-first
- Language: English
- Monthly revenue range: Rs. 80,000-2,50,000
- Current acquisition: LinkedIn, referrals, founder WhatsApp groups
- Current pain: vague inquiries, proposal follow-up, milestone payment tracking

### Public Page Positioning

Headline:

Brand and landing page design for founders who need to launch clearly and look credible.

Subtext:

We help early-stage businesses turn rough ideas into clean brand systems, landing pages, and campaign assets.

### Catalogue Items

1. Starter Brand Kit
   - Starting price: Rs. 18,000
   - Timeline: 7-10 days
   - Includes: logo direction, colors, fonts, usage basics

2. Landing Page Design
   - Starting price: Rs. 25,000
   - Timeline: 10-14 days
   - Includes: page structure, wireframe, UI design

3. Content Design Retainer
   - Starting price: Rs. 15,000/month
   - Includes: 10-12 creatives/month

### Trust Proof

- 12 launch projects
- Case study: D2C snack brand landing page
- Case study: SaaS waitlist page
- Client testimonial: "They helped us explain our product clearly before launch."

### Persona-Specific Inquiry Fields

- Name
- Company name
- Phone/email
- Project type
- Budget range
- Timeline
- Current website/social link
- Message

### Sample Leads

1. Kavya Foods
   - Source: Referral
   - Project type: Landing page
   - Budget: Rs. 25,000-40,000
   - Timeline: 3 weeks
   - Status: Proposal sent
   - Next action: Follow up on scope and timeline
   - Expected value: Rs. 30,000

2. FinPilot
   - Source: LinkedIn
   - Project type: Brand kit
   - Budget: Rs. 15,000-25,000
   - Timeline: 2 weeks
   - Status: Discovery booked
   - Next action: Send pre-call questions
   - Expected value: Rs. 18,000

### Sample Payments

1. Kavya Foods
   - Service: Landing Page Milestone 1
   - Amount due: Rs. 10,000
   - Status: Part paid
   - Age: 5 days pending

### Operational Sensecheck

Medium-high plausibility.

This works if the page includes case studies and qualification fields.

Risks:

- Agencies may already use Notion, Wix, Webflow, Trello, or invoices.
- They may not want a generic BizzNexx page if brand perception matters.

Mitigation:

- Position as lightweight lead and proposal operating layer, not website replacement.
- Allow subtle BizzNexx branding.
- Case studies are P0.

## 9. Business 6: Mishra Home Bakes

### Business Profile

- Persona: Home Service / Home Bakery
- City: Lucknow
- Owner: Pooja Mishra
- Mode: Local delivery/pickup
- Language: Hindi + Hinglish
- Monthly revenue range: Rs. 25,000-65,000
- Current acquisition: WhatsApp status, local referrals, Instagram
- Current pain: order details, advance for custom cakes, delivery location, repeat orders

### Public Page Positioning

Headline:

Custom cakes, brownies, and dessert boxes for birthdays, anniversaries, and small celebrations in Lucknow.

Subtext:

Share your date, flavour, size, and delivery area. We confirm availability, price, and advance before baking.

### Catalogue Items

1. Custom Birthday Cake
   - Starting price: Rs. 1,200/kg
   - Advance: 50%
   - Lead time: 2 days

2. Brownie Box
   - Price: Rs. 499 onwards
   - Lead time: 1 day

3. Dessert Hamper
   - Starting price: Rs. 999
   - Lead time: 2-3 days

### Trust Proof

- 300+ cakes delivered locally
- Hygiene-focused home kitchen
- Customer review: "Cake was fresh, beautiful, and delivered on time."

### Operational Sensecheck

High plausibility, but different from service professionals.

This tests:

- Local area
- Order details
- Advance
- Date/time delivery
- Repeat/referral behavior

Risks:

- Starts moving toward product/order commerce.
- Inventory and delivery can creep in.

Mitigation:

- Keep as local service/order inquiry, not ecommerce cart.
- No inventory.
- No logistics.

## 10. India Operational Sensecheck

### 10.1 Works Across India If

BizzNexx remains:

- Mobile-first
- WhatsApp-led
- Assisted setup
- Low data-entry
- Local language friendly
- Clear about payment tracking, not payment ownership
- Clear about CA-ready records, not tax filing
- Flexible on whether prices are public

### 10.2 Will Break If

- We force owners to maintain CRM fields.
- We require WhatsApp API setup at sign-up.
- We require laptop usage.
- We make every business use the same inquiry form.
- We ignore images for visual businesses.
- We show scores without explanations.
- We overpromise leads or payment recovery.
- We use metro-premium pricing everywhere.
- We ignore regional language behavior.

### 10.3 Regional Sensitivity

Metro markets:

- Higher willingness for design polish
- More competition
- More brand sensitivity
- More existing tools

Tier 2 / Tier 3 markets:

- Higher assisted-setup need
- More WhatsApp/referral dependence
- More Hinglish/regional language requirement
- Price sensitivity but stronger need for basic digital presence

### 10.4 Payment Behavior

Plausible modes:

- UPI
- Cash
- Bank transfer for larger service businesses
- Partial advance for events/custom orders
- Monthly recurring UPI for tutors

Do not build:

- Settlement logic
- Payment gateway ownership
- Lending
- Recovery workflows

### 10.5 Language Behavior

MVP must support:

- English
- Hinglish
- Hindi-oriented simple messaging

Later:

- Bengali
- Marathi
- Tamil
- Telugu
- Kannada
- Malayalam

### 10.6 Trust Signals By Persona

Tutor:

- Experience
- Results
- Parent feedback
- Batch structure
- Trial policy

Bridal/Event:

- Portfolio photos
- Reviews
- Date availability
- Advance rules
- Service area

Agency:

- Case studies
- Work samples
- Process
- Timeline
- Starting budget

Home service:

- Reviews
- Locality
- Photos
- Hygiene/reliability
- Delivery/pickup clarity

## 11. Robust Sensecheck Verdict

### Tutor / Coach

Operationally strongest first persona.

Why:

- Repeated monthly workflow
- Recurring fee tracking
- Clear trial flow
- Parent trust matters
- Easy to demonstrate page-to-lead-to-fee

Recommended as first polished pack.

### Bridal/Event

Commercially strong but visual-heavy.

Why:

- High-value leads
- Advance/balance is natural
- Instagram-led discovery fits
- Clear pain in quote and availability

Condition:

- Must include gallery and event-date capture.

### Design/Agency

Strategically useful but harder to convince.

Why:

- They may already be digitally mature
- Need high-quality proof/case studies
- Generic page may feel weak

Condition:

- Must position as lead/proposal/payment workflow, not website builder.

### Home Bakery / Local Service

Useful later but scope-risky.

Why:

- Can drift toward ecommerce/order management
- Still valuable for local inquiry and advance tracking

Condition:

- Keep as inquiry/booking workflow, not cart/inventory.

## 12. Recommended Implementation Dataset

For the next build, implement only:

1. Ananya Learning Studio
2. Ria Bridal Studio
3. Northstar Design Co.

Use Mishra Home Bakes and FrameCraft as later expansion data after the first three pass acceptance tests.

## 13. Data Quality Checklist Before Coding

Each demo business must include:

- Business profile
- Owner profile
- Buyer persona
- Catalogue items
- Pricing or pricing policy
- CTA
- Persona-specific inquiry fields
- Trust proof
- FAQs
- Sample leads
- Sample payments
- Sample message templates
- Score reasons
- Next-action logic
- Payment ageing
- Follow-up ageing

If any of these are missing, the demo will feel superficial again.

## 14. Final Recommendation

Use this synthetic dataset, but do not treat it as final product truth.

It is strong enough to:

- Upgrade UI depth
- Test operational workflows
- Demonstrate persona understanding
- Run internal acceptance reviews

It is not enough to:

- Claim market validation
- Make public success claims
- Replace interviews
- Set final pricing

The next build should polish the first three personas using this data and enforce the acceptance tests in the persona critique document.
