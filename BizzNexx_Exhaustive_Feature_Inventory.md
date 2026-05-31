# BizzNexx Exhaustive Feature Inventory

## 1. Why This Document Exists

The current BizzNexx MVP exposes prototype tabs that reflect internal thinking:

- Mobile Owner
- Public Page
- Operator
- Pilot Readiness

This is not how the product should feel.

For the business owner, BizzNexx should feel like one mobile-first command center with a simple business selector and view switcher. Public page, owner dashboard, and setup/admin controls should not feel like separate products.

This document defines the exhaustive feature inventory before further UI changes.

## 2. Product Architecture Reframe

### Current Problem

Separate tabs make the product feel like a demo:

- "Mobile Owner" and "Public Page" should not be peer-level product tabs.
- "Pilot Readiness" is internal and should not appear in the customer experience.
- The public page should be previewed/published from the business workspace.
- Operator tools should be internal/admin-only.

### Correct Mental Model

One business workspace with mode switchers:

- Business: dropdown
- Persona pack: fixed after setup
- Workspace mode:
  - Today
  - Leads
  - Payments
  - Page
  - Catalogue
  - Messages
  - Insights
  - Setup

Customer-facing public page should be reachable from:

- Preview Page
- Share Link
- Publish Status

Operator-only tools should be reachable from:

- Internal setup checklist
- Notes/blockers
- Data quality
- Go-live readiness

## 3. Navigation Requirements

### Remove As Top-Level User Tabs

- Pilot Readiness
- Public Page as a separate global tab
- Mobile Owner label

### Replace With

#### Header Controls

- Business dropdown
- Persona badge
- Publish status
- Preview public page button
- Copy share link button
- Install app prompt where supported

#### Primary Owner Navigation

- Today
- Leads
- Payments
- Catalogue
- Messages
- Insights

#### Internal Operator Navigation

Visible only in operator mode:

- Setup
- Content Quality
- Data Quality
- Go-Live Checklist
- Support Notes

## 4. Feature Groups

BizzNexx needs features across eight layers:

1. Business Setup
2. Catalogue and Public Page
3. Inquiry Capture
4. Lead and Follow-Up Operations
5. Payment and Receivables
6. Messages and AI Assistance
7. Insights and Scores
8. Operator / Assisted Service Layer

## 5. Layer 1: Business Setup Features

### MVP

- Business profile
- Owner profile
- Persona pack selection
- City/service area
- WhatsApp number
- Preferred language
- Brand tone
- Payment terms
- Setup stage
- Publish status

### Needed Next

- Setup wizard
- Persona-specific intake forms
- Missing content checklist
- Owner input completeness score
- Real/synthetic content label
- Setup package selection
- Support contact owner

### Later

- Multi-user team access
- Staff roles
- Custom domain setup
- Brand asset upload
- Google Business Profile connection guide

## 6. Layer 2: Catalogue and Public Page Features

### MVP

- Public page preview
- Catalogue items
- Pricing labels
- Trust proof
- FAQs
- Testimonials
- Media/gallery placeholders
- Case studies for agency persona
- WhatsApp CTA
- Inquiry form

### Needed Next

- Persona-specific page layouts
- Page section enable/disable
- Page quality score
- Share preview
- Mobile preview
- "What happens next" section
- Stronger proof hierarchy
- Gallery/media consent status
- Price display control:
  - show exact price
  - starting from
  - contact for price
  - hide price
- Availability/date/slot fields where relevant
- Service area block
- Owner profile block
- Booking/process block

### Later

- Custom themes
- Custom domain
- SEO editor
- Google Business Profile link instructions
- Instagram bio preview
- Social share cards
- Public reviews widget

## 7. Layer 3: Inquiry Capture Features

### MVP

- Basic inquiry form
- Persona-specific two-field extension
- Inquiry creates lead
- Source is captured
- Catalogue item selected

### Needed Next

- Full persona-specific inquiry schema:
  - tutor: class, board, subject, timing, trial interest
  - bridal/event: event date, event type, venue, package, budget
  - agency: project type, budget, timeline, company, current link
- Lead quality classification
- Duplicate detection by phone
- Spam/manual invalid marker
- Required vs optional fields by persona
- Post-submit confirmation screen
- Owner notification indicator
- Source tracking:
  - public page
  - WhatsApp click
  - Instagram bio
  - referral
  - manual
  - Google profile
- WhatsApp pre-filled message with selected service context

### Later

- Instagram lead form import
- WhatsApp Cloud API webhook
- Google form import
- CSV/import from spreadsheet
- Voice note/manual operator entry

## 8. Layer 4: Lead and Follow-Up Operations

### MVP

- Leads list
- Persona-specific statuses
- Status update
- Next action
- Follow-up age
- Urgency reason
- WhatsApp handoff

### Needed Next

- Today action queue
- Hot/warm/cold lead quality
- Follow-up due date
- Follow-up overdue ageing
- Snooze
- Mark contacted
- Mark lost with reason
- Convert to customer
- Create payment from lead
- Interaction notes
- Last contacted timestamp
- Message history log
- Call attempted marker
- "Why this lead matters" explanation
- Lead source performance

### Later

- Calendar reminders
- Automated nurture sequence
- Team assignment
- Call logging
- WhatsApp message sync

## 9. Layer 5: Payment and Receivables Features

### MVP

- Payment list
- Amount due
- Status
- Mark paid
- Payment reminder
- Ageing reason

### Needed Next

- Due today
- Overdue buckets:
  - 1-3 days
  - 4-7 days
  - 8+ days
- Part-payment support in UI
- Payment mode
- Payment proof/reference note
- Create payment from enrollment/booking/project
- Advance/balance logic
- Monthly recurring fee logic
- Milestone payment logic
- Payment reminder preview/edit
- Promise-to-pay date
- Payment dispute/note
- Monthly collection summary

### Later

- Payment links
- Razorpay/Cashfree/UPI deep link
- Auto reconciliation
- GST invoice integration
- Accounting export integrations

## 10. Layer 6: Messages and AI Assistance

### MVP

- Persona template messages
- WhatsApp handoff

### Needed Next

- Message preview modal
- Edit before send
- Tone selector:
  - polite
  - friendly
  - firm
  - professional
  - Hinglish
- Persona-specific message categories
- Copy text button
- Open WhatsApp button
- Message history log
- Safety guardrails
- Variable filling check
- "Why this message" context

### Later

- OpenAI generation
- WhatsApp Cloud API template approval
- Multi-language variants
- Voice-to-message draft
- A/B testing message variants

## 11. Layer 7: Insights and Scores

### MVP

- Growth Score
- Health Score
- Score reasons
- Basic open lead and pending amount metrics

### Needed Next

- Score breakdown
- Score trend
- Action-linked score reasons
- Page funnel:
  - views
  - WhatsApp clicks
  - inquiries
  - qualified leads
  - conversions
- Follow-up completion rate
- Lead ageing
- Payment ageing
- Source performance
- Persona-specific health metrics
- Weekly summary
- What changed since last visit

### Later

- Benchmarking by persona
- Revenue forecast
- Conversion probability
- Cohort analysis
- Monthly CA-ready export

## 12. Layer 8: Operator / Assisted Service Layer

### MVP

- Setup stage
- Operator checklist
- Notes/blockers

### Needed Next

- Intake completeness
- Catalogue completeness
- Proof completeness
- Page readiness
- Inquiry readiness
- Message readiness
- Payment tracker readiness
- Data quality flags
- Synthetic vs real proof label
- Go-live checklist
- Support notes
- Owner blocker list
- Assigned operator
- Next operator action
- Internal-only user view

### Later

- Support SLA tracking
- Internal task assignment
- Onboarding pipeline
- Billing/subscription management
- Customer success dashboard

## 13. Persona-Specific Features

## 13.1 Tutor / Coach

### Public Page Features

- Teacher profile
- Subjects/classes/boards
- Trial class CTA
- Batch timings
- Online/offline mode
- Fee structure
- Parent testimonials
- Results/proof
- Progress update promise
- Parent FAQ

### Inquiry Features

- Parent/student name
- Class/grade
- Board
- Subject
- Preferred timing
- Trial interest

### Operations Features

- Trial scheduled
- Trial reminder
- Enrolled student
- Monthly fee due
- Parent follow-up
- Progress update template

### Payment Features

- Monthly fee cycle
- Part-payment
- Overdue fee reminder
- Student-wise dues

## 13.2 Bridal / Event Service

### Public Page Features

- Visual portfolio/gallery
- Event types
- Packages
- Starting price
- Advance/balance rules
- Venue travel/service area
- Availability CTA
- Reviews
- Booking process

### Inquiry Features

- Event date
- Event type
- Venue/location
- Preferred look/package
- Budget range

### Operations Features

- Availability checked
- Package shared
- Advance pending
- Booking confirmed
- Balance pending
- Event completed

### Payment Features

- Advance amount
- Balance amount
- Due before/on event
- Completed-event balance reminder

## 13.3 Design Company / Freelancer / Agency

### Public Page Features

- Sharp positioning
- Services/packages
- Case studies
- Work samples
- Process
- Starting budget
- Timeline expectations
- Discovery call CTA
- Client proof

### Inquiry Features

- Company name
- Project type
- Budget range
- Timeline
- Current website/social link
- Scope note

### Operations Features

- Discovery booked
- Requirements captured
- Proposal sent
- Follow-up due
- Won/lost
- Milestone pending

### Payment Features

- Advance
- Milestone
- Final handover payment
- Retainer renewal

## 14. Feature Priority

### P0: Must Build Before Showing Again

- Replace top-level tabs with business workspace + view dropdown/nav.
- Remove Pilot Readiness from user navigation.
- Public page preview/share inside workspace.
- Persona-specific public page layouts.
- Persona-specific inquiry forms.
- Action queue as the default home view.
- Message preview/edit before WhatsApp.
- Lead and payment ageing.
- Score explanation tied to actions.
- Operator checklist moved to internal mode.

### P1: Must Build Before Paid Pilot

- Full proof/media/case-study management.
- Page quality score.
- Lead quality classification.
- Payment buckets.
- Interaction notes.
- Source performance.
- Monthly summary.
- Support notes and blocker tracking.

### P2: Later

- WhatsApp API
- Instagram DM automation
- Native app
- Payment gateway
- Custom domains
- Advanced SEO
- Team roles

## 15. Required UI Structure

### Owner Workspace

Header:

- Business dropdown
- Persona badge
- Publish status
- Preview page
- Share link

Primary sections:

- Today
- Leads
- Payments
- Catalogue
- Messages
- Insights

### Today View

Must include:

- Top 3 urgent actions
- New inquiries
- Overdue follow-ups
- Payment reminders
- Message previews
- What changed since last visit

### Public Page Preview

Should open as:

- Preview mode inside workspace
- Full page preview option
- Shareable public URL

### Operator Mode

Hidden from owner by default.

Includes:

- Setup checklist
- Content quality
- Data quality
- Blockers
- Go-live readiness
- Support notes

## 16. What To Delete Or Hide

- Delete "Pilot Readiness" from visible app navigation.
- Rename "Mobile Owner" to "Today."
- Move "Public Page" into Preview Page / Catalogue.
- Move "Operator" into internal mode.
- Hide prototype language from customer-facing UI.
- Hide "Feedback MVP" from customer-facing pages.

## 17. Research Notes

Comparable workflow signals:

- WhatsApp Business already provides catalogues, quick replies, labels, and links to catalogue items.
- Instagram business profiles support action buttons, and lead forms are available in some business contexts.
- Google Business Profile supports business links and booking/service links, but these can be sensitive to validity and page quality.
- India-focused CRMs compete on mobile access, follow-up reminders, WhatsApp handoff, and payment reminders.

BizzNexx must therefore not look like a thin clone of WhatsApp Business catalogue or a generic CRM. Its advantage must be:

- Assisted setup
- Persona-specific page depth
- Inquiry-to-follow-up workflow
- Payment ageing
- Action-first mobile dashboard
- BizzNexx operator layer

## 18. Sources

- WhatsApp Business App features: https://whatsappbusiness.com/products/business-app-features/
- Instagram action buttons: https://www.facebook.com/help/instagram/122793804938499
- Google Business Profile links: https://support.google.com/business/answer/6218037
- India mobile CRM/follow-up competitors reviewed through public positioning: HelloLeads, Zopo CRM, ClientPulses, SBS CRM, CRMprocs.
