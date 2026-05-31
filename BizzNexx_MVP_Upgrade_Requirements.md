# BizzNexx MVP Upgrade Requirements

## 1. Objective

Upgrade the current BizzNexx MVP from a functional skeleton into a credible selected-user feedback product.

The next version must feel deep enough that a private tutor, bridal/event business, or design company can understand:

- What BizzNexx will create for them
- Why their prospects would trust the page
- How inquiries are captured
- How follow-ups happen
- How payments are tracked
- What work BizzNexx removes from their day
- Why they might pay for setup and monthly support

## 2. Current State

### What Exists

- React frontend
- Django backend
- SQLite local database
- Seeded demo businesses
- Public page view
- Inquiry form
- Inquiry-to-lead API workflow
- Lead-to-follow-up task workflow
- Payment tracker
- Operator setup stage
- PWA basics

### Current Weakness

The product is operationally real but commercially unconvincing.

It lacks:

- Strong persona-specific public pages
- Real buyer-facing copy
- Proof assets
- Portfolio/case-study depth
- Persona-specific inquiry forms
- Score explanations
- Urgency/ageing in dashboard
- Clear "what happens next" after inquiry
- Owner-facing value proof

## 3. MVP Upgrade Scope

### Included Personas

The next build pass will focus only on:

1. Private Tutor / Coach
2. Bridal Studio / Event Service
3. Design Company / Freelancer / Agency

Other personas remain documented but should not be built until these three feel credible.

## 4. Required User-Provided Inputs

These are required if we want the MVP to feel real rather than synthetic.

### For Tutor Demo

- Tutor name or studio name
- Teacher profile: experience, qualifications, teaching style
- Subjects/classes/boards taught
- Batch/timing examples
- Fee structure
- Trial class policy
- 2-3 testimonials or sample parent feedback
- Any student result/proof examples
- City/location and online/offline mode
- Preferred tone: English, Hindi, Hinglish, formal, friendly

### For Bridal/Event Demo

- Business/studio name
- Service categories
- Package names and starting prices
- Advance and balance rules
- Service area/city
- 5-8 portfolio images, or permission to use placeholders for now
- 2-3 testimonials/reviews
- Event types served
- Availability/booking process
- Preferred tone

### For Design Company / Agency Demo

- Company/studio name
- Service categories
- Package/rate ranges
- 2-3 case studies or sample projects
- Work sample images/screenshots, or permission to use placeholders
- Discovery call process
- Proposal/payment milestone terms
- Client testimonials
- Preferred tone

## 5. If Real Inputs Are Not Available

If the above inputs are not available yet, we can use realistic synthetic demo content for internal testing only.

Synthetic content must be clearly labelled as demo content and should not be used for public pilot claims.

## 6. Product Requirements

### 6.1 Persona-Specific Public Pages

Each persona must have its own page structure.

#### Tutor Page Requirements

Sections:

- Hero with clear parent-facing promise
- Teacher profile
- Subjects/classes/boards
- Trial class CTA
- Batch/timing examples
- Fee cards
- Results/testimonials
- Parent FAQ
- What happens after inquiry
- WhatsApp CTA

#### Bridal/Event Page Requirements

Sections:

- Visual hero
- Portfolio/gallery
- Packages
- Event date and location CTA
- Advance/balance rules
- Service area
- Testimonials
- Booking process
- FAQ
- WhatsApp CTA

#### Design/Agency Page Requirements

Sections:

- Sharp positioning hero
- Services/packages
- Case studies/work samples
- Process
- Starting budget/range
- Discovery call CTA
- Client proof
- Qualification form
- FAQ
- WhatsApp CTA

### 6.2 Persona-Specific Inquiry Forms

#### Tutor Inquiry Fields

- Parent/student name
- Phone number
- Class/grade
- Subject
- Board/exam
- Preferred timing
- Trial interest
- Message

#### Bridal/Event Inquiry Fields

- Name
- Phone number
- Event type
- Event date
- Location/venue
- Package interested
- Budget range
- Message

#### Design/Agency Inquiry Fields

- Name
- Phone/email
- Business/company name
- Project type
- Budget range
- Timeline
- Service interested
- Message

### 6.3 Dashboard Requirements

The owner dashboard must become an action queue, not just metric cards.

Required:

- Today's priority actions
- Lead ageing
- Follow-up ageing
- Payment ageing
- Suggested message preview
- Edit-before-WhatsApp-send
- Why this action matters
- Score explanation
- What changed since last visit

### 6.4 Operator Console Requirements

The BizzNexx operator console must manage assisted setup.

Required:

- Persona pack selected
- Intake completeness
- Catalogue completeness
- Proof completeness
- Page readiness
- Inquiry form readiness
- Message template readiness
- Payment tracker readiness
- Go-live checklist
- Operator notes
- Blockers

### 6.5 Backend Requirements

New or expanded models needed:

- MediaAsset
- Testimonial
- CaseStudy
- FAQ
- PersonaSpecificInquiryDetail
- ScoreReason
- OperatorNote
- SupportRequest
- MonthlySummary
- Package / Subscription

Existing models to improve:

- Business
- Catalogue
- CatalogueItem
- Inquiry
- Lead
- Payment
- SetupProject
- MessageTemplate

### 6.6 AI / Message Requirements

For this upgrade, use template-driven messages first.

Required message types:

Tutor:

- First parent reply
- Trial confirmation
- Trial reminder
- Fee explanation
- Monthly fee reminder

Bridal/Event:

- Event inquiry reply
- Availability check
- Package explanation
- Advance payment request
- Balance reminder

Design/Agency:

- Discovery call reply
- Proposal follow-up
- Scope clarification
- Milestone payment reminder
- Testimonial request

## 7. Content Quality Requirements

All demo content must satisfy:

- Specific, not generic
- Persona vocabulary used correctly
- Buyer objections answered
- Pricing/terms not hidden unless intentional
- Trust proof visible
- CTA is obvious
- Mobile reading is easy
- No exaggerated claims
- No legal/tax/GST/collections overclaim

## 8. Visual Requirements

### Overall

- Mobile-first
- More polished page hierarchy
- Stronger typography
- Less dashboard-demo feel on public pages
- More trust and proof sections
- No decorative clutter

### Tutor

- Calm, credible, parent-friendly
- Focus on outcomes, structure, and reassurance

### Bridal/Event

- Visual-first
- Portfolio/gallery prominent
- Package clarity
- Booking confidence

### Design/Agency

- Sharp, professional, proof-led
- Case studies and process visible

## 9. Acceptance Criteria

### Tutor Acceptance

A parent can understand teacher credibility, subject fit, trial process, fee range, and next step in under 60 seconds.

### Bridal/Event Acceptance

A bride/family can understand style, packages, event-date process, advance rule, and next step in under 60 seconds.

### Design/Agency Acceptance

A business owner can understand services, proof, process, budget range, and discovery call path in under 60 seconds.

### Owner Dashboard Acceptance

The business owner can answer:

- Who should I reply to?
- Who needs follow-up?
- Who owes money?
- What message should I send?
- Why is this urgent?

### Operator Acceptance

BizzNexx team can answer:

- Is this business ready to publish?
- What proof is missing?
- What setup step is blocked?
- What needs follow-up this week?
- Is the user ready for paid pilot?

## 10. Build Order

### Step 1: Backend Model Expansion

- Add proof/media/case study/FAQ/operator models
- Add migrations
- Expand seed data

### Step 2: Content System

- Create persona-specific page content schema
- Create richer seeded content
- Add message templates by persona

### Step 3: Public Page Upgrade

- Build persona-specific page sections
- Add proof/gallery/case study areas
- Add "what happens next"
- Add persona-specific inquiry form

### Step 4: Dashboard Upgrade

- Add action queue
- Add ageing
- Add message preview/edit
- Add score reasons

### Step 5: Operator Console Upgrade

- Add checklist
- Add notes/blockers
- Add go-live readiness

### Step 6: Validation Pass

- Build test
- API workflow test
- Mobile viewport review
- Persona acceptance review

## 11. Out of Scope For This Upgrade

- Native mobile app
- WhatsApp Cloud API
- Instagram DM automation
- Payment gateway integration
- GST filing
- Full accounting
- Marketplace
- Advanced SEO
- Custom domains

## 12. Open Questions For Rick / Team

1. Should the first real demo use synthetic businesses or actual known businesses from the founder network?
2. Can we use real testimonials/images for at least one persona?
3. Which persona should be polished first: tutor, bridal/event, or agency?
4. Should pilot pricing be shown inside the MVP or kept separate for sales conversations?
5. Should BizzNexx branding be visible on customer pages or kept subtle?

## 13. Recommended Assumption If No Answer Yet

Proceed with realistic synthetic demo content for all three personas, but structure the system so real content can replace it easily.

Use `BizzNexx_Realistic_Synthetic_Pilot_Data_and_India_Sensecheck.md` as the source dataset for the next build pass. That document defines the first realistic synthetic businesses, operational constraints, India sensecheck, and the data quality checklist.

Use `BizzNexx_Exhaustive_Feature_Inventory.md` as the product feature source of truth before changing the UI. It defines what to remove, merge, prioritize, hide, and build across the owner workspace, public page preview, and internal operator mode.

Polish in this order:

1. Tutor
2. Bridal/Event
3. Design/Agency

Reason:

Tutor has the clearest repeat workflow, bridal/event has the strongest visual trust gap, and agency has the highest need for proof/case-study depth.
