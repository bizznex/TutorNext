# BizzNexx Business Case Ontology

## Purpose

This ontology defines what BizzNexx must understand about a small Indian service business before it can credibly create a catalogue website, generate leads, manage follow-ups, and improve payment visibility.

BizzNexx is not an accounting platform, not a generic CRM, and not only a website builder. It is a service-business growth and operating layer.

## Core Thesis

Small Indian service businesses do not only need software. They need a guided operating system that helps them:

- Package what they sell
- Look credible online
- Capture inquiries
- Respond quickly
- Follow up without awkwardness
- Convert leads into customers
- Track fees and outstanding payments
- Keep monthly business records organized

The wedge is catalogue-to-lead-to-cash, not accounting.

## Why This Exists

### Market Reality

India has a very large base of micro and small enterprises. The MSME Annual Report 2025-26 reports 7.61 crore registered MSMEs including informal micro enterprises on UAP as of 31 January 2026, with service and trading businesses forming a major share.

Digital payments are already mainstream. UPI processed 22.64 billion transactions worth Rs. 29.53 lakh crore in March 2026, according to NPCI-reported March 2026 data summarized by payments infrastructure trackers.

The problem is not whether customers can pay digitally. The problem is whether the business has a coherent path from discovery to inquiry to follow-up to payment.

Delayed payments remain structurally painful. The GAME-FISME-C2FO delayed payments report cited Rs. 7.34 lakh crore in delayed MSME payments as of March 2024.

Research on Indian MSMEs also shows that digital adoption is desired but blocked by cost, complexity, skills, trust, and unclear ROI. Zoho's MSME customer operations survey reported high perceived importance for CRM, finance, BI, and AI, but also cited cost, budget constraints, lack of training, and complexity as barriers.

### Customer Reality

Small service businesses often operate across:

- WhatsApp chats
- Instagram pages
- Phone calls
- Referral networks
- Google Forms
- Excel or notebooks
- UPI screenshots
- PDF brochures
- Verbal pricing explanations

This creates an execution gap:

- Catalogue is unclear
- Trust proof is scattered
- Leads are forgotten
- Follow-ups are inconsistent
- Fees are pending or untracked
- Owners cannot see what action matters today

## Primary Customer Segment

### Initial Beachhead

Tutors, coaches, trainers, and small coaching studios.

### Why This Segment First

- Clear service catalogue
- Repeat inquiries
- Trial-class workflow
- Recurring monthly fees
- Parent/student communication happens heavily on WhatsApp
- Trust proof matters
- Follow-up and payment reminders are common but uncomfortable
- Public page can be simple and valuable

### Adjacent Segments

- Makeup artists
- Photographers
- Event service providers
- Freelancers and small agencies
- Fitness trainers
- Consultants
- Home-based professionals
- Creators selling services or workshops

## Jobs To Be Done

### Business Owner Jobs

- Help prospects understand what I offer
- Make my business look professional
- Capture inquiry details without manually asking everything again
- Respond quickly with a good message
- Know whom to follow up with today
- Convert inquiries into trials, consultations, bookings, or customers
- Track advance, balance, and monthly payments
- Avoid rude or awkward payment reminders
- Know whether my business is improving
- Send organized records to my CA or accountant

### End-Customer Jobs

- Understand the service quickly
- Know pricing or next step clearly
- Trust the provider
- Contact without friction
- Book trial/consultation/inquiry easily
- Receive clear communication

### BizzNexx Team Jobs

- Set up the business properly
- Translate messy business details into a clean catalogue
- Create reusable templates
- Monitor whether the owner is using the system
- Improve messages, page copy, and workflow based on real behavior

## Value Proposition

BizzNexx helps service businesses get a professional catalogue page and a simple operating dashboard so they can generate inquiries, follow up faster, collect better, and understand what needs attention today.

## Why Indian Consumers Would Pay

Here "consumer" means the paying customer: the small business owner.

They will pay if BizzNexx produces visible commercial outcomes:

- More credible online presence
- More inquiries from referrals, WhatsApp, Instagram, and search
- Faster response to prospects
- Fewer forgotten follow-ups
- Better conversion from inquiry to trial or booking
- Clearer pending payment visibility
- Less awkward payment communication
- Less month-end chaos
- Less dependence on the owner's memory

They will not pay for:

- A generic website
- A CRM that feels like extra data entry
- Accounting features they already get elsewhere
- AI messages that do not understand their actual offer
- Dashboards that do not lead to action

## Paid Product Boundary

### Must Do

- Create and host a public catalogue page
- Capture inquiries
- Connect inquiry to WhatsApp
- Maintain catalogue items
- Track lead status
- Track follow-up dates
- Suggest next action
- Track fees and payment status
- Generate useful WhatsApp messages
- Show Growth Score and Health Score
- Provide monthly summary/export

### Should Do Later

- Custom domains
- Google Business Profile support
- Basic local SEO optimization
- Testimonial collection workflow
- Referral request workflow
- WhatsApp Business API integration
- Payment link integration
- Automated reminders
- Role-based team access

### Should Not Do Initially

- Full accounting
- GST filing
- Aggressive debt recovery
- Payment gateway ownership
- Marketplace matching
- Inventory management
- Lending
- Paid ad management
- Complex website customization

## Ontology Overview

The ontology is organized into nine domains:

1. Business Identity
2. Catalogue and Offer
3. Public Presence
4. Inquiry and Lead Flow
5. Conversion Workflow
6. Customer and Relationship
7. Payment and Receivables
8. Intelligence and Recommendations
9. Service Delivery and Commercial Packaging

## Domain 1: Business Identity

### Business

Represents the service business being enabled.

Attributes:

- business_id
- legal_or_trade_name
- public_display_name
- owner_name
- business_type
- segment
- city
- service_area
- operating_mode: online, offline, hybrid
- phone_number
- whatsapp_number
- email
- preferred_language
- brand_tone: friendly, professional, premium, local, Hinglish
- logo
- owner_photo
- brand_colors
- status: draft, active, paused, archived

Relationships:

- Business has one or more Catalogues
- Business has many Catalogue Items
- Business has many Inquiries
- Business has many Leads
- Business has many Customers
- Business has many Payments
- Business has many Message Templates

### Owner

Represents the human decision-maker.

Attributes:

- owner_id
- name
- role
- phone
- digital_comfort_level: low, medium, high
- preferred_support_channel
- willingness_to_self_serve
- support_notes

Relationships:

- Owner owns Business
- Owner receives Follow-Up Tasks
- Owner approves Catalogue Content

## Domain 2: Catalogue and Offer

### Catalogue

Represents the structured set of offers shown publicly.

Attributes:

- catalogue_id
- business_id
- title
- primary_promise
- target_audience
- positioning_angle
- active_status
- completeness_score
- last_reviewed_at

Relationships:

- Catalogue belongs to Business
- Catalogue contains Catalogue Items
- Catalogue appears on Public Page
- Catalogue has FAQs
- Catalogue has Trust Proof

### Catalogue Item

Represents one sellable service, package, batch, workshop, consultation, or subscription.

Attributes:

- item_id
- catalogue_id
- name
- category
- short_description
- detailed_description
- format: one_to_one, group, batch, workshop, consultation, package
- delivery_mode: online, offline, hybrid
- duration
- frequency
- price_type: fixed, starting_from, hidden, custom_quote
- price_label
- actual_price
- advance_required
- trial_available
- trial_price
- who_it_is_for
- outcomes
- prerequisites
- capacity_limit
- display_order
- active_status

Relationships:

- Catalogue Item belongs to Catalogue
- Catalogue Item generates Inquiries
- Catalogue Item is referenced by Leads
- Catalogue Item can have Fee Plans

### Fee Plan

Represents pricing terms offered to a prospect or customer.

Attributes:

- fee_plan_id
- catalogue_item_id
- name
- billing_frequency: one_time, per_session, monthly, milestone, custom
- amount
- advance_amount
- balance_amount
- due_rule
- discount
- terms
- status: draft, active, retired

Relationships:

- Fee Plan belongs to Catalogue Item
- Fee Plan can be sent as Quote
- Fee Plan can generate Payments

### FAQ

Attributes:

- faq_id
- catalogue_id
- question
- answer
- display_order
- public_status

## Domain 3: Public Presence

### Public Page

Represents the hosted web page created for the business.

Attributes:

- page_id
- business_id
- slug
- custom_domain
- page_title
- meta_description
- hero_headline
- hero_subtext
- primary_cta
- secondary_cta
- published_status
- mobile_ready_status
- https_status
- last_published_at

Relationships:

- Public Page belongs to Business
- Public Page displays Catalogue
- Public Page captures Inquiries
- Public Page records Page Events

### Page Section

Attributes:

- section_id
- page_id
- section_type: hero, services, proof, faq, contact, testimonial, gallery, pricing
- title
- content
- display_order
- enabled

### Trust Proof

Represents credibility evidence.

Attributes:

- proof_id
- business_id
- proof_type: testimonial, result, certification, work_sample, before_after, case_study
- title
- body
- customer_name
- customer_role
- media_url
- consent_status
- approved_for_public_use
- display_order

Relationships:

- Trust Proof belongs to Business
- Trust Proof can be shown on Public Page
- Trust Proof can be requested through AI Message

### Page Event

Represents visitor behavior.

Attributes:

- event_id
- page_id
- event_type: view, whatsapp_click, inquiry_submit, service_view, phone_click
- catalogue_item_id
- source
- campaign
- device_type
- created_at

Relationships:

- Page Event belongs to Public Page
- Page Event may create Inquiry

## Domain 4: Inquiry and Lead Flow

### Inquiry

Represents a prospect action before qualification.

Attributes:

- inquiry_id
- business_id
- page_id
- catalogue_item_id
- name
- phone_number
- email
- message
- preferred_time
- location
- source: public_page, whatsapp, instagram, referral, call, manual, campaign
- source_detail
- urgency
- qualification_status: new, qualified, spam, duplicate, not_relevant
- created_at

Relationships:

- Inquiry belongs to Business
- Inquiry can convert to Lead
- Inquiry references Catalogue Item

### Lead

Represents a qualified sales opportunity.

Attributes:

- lead_id
- business_id
- inquiry_id
- name
- contact_person
- phone_number
- interested_item
- lead_source
- status: new, contacted, trial_proposed, trial_scheduled, trial_completed, quote_sent, converted, lost
- expected_value
- probability
- next_follow_up_date
- last_contacted_at
- lost_reason
- notes

Relationships:

- Lead belongs to Business
- Lead may originate from Inquiry
- Lead has Follow-Up Tasks
- Lead has Quotes
- Lead may become Customer

### Lead Source

Attributes:

- source_id
- business_id
- source_type
- source_name
- campaign_name
- tracking_code
- cost
- active_status

## Domain 5: Conversion Workflow

### Trial / Consultation

Represents the intermediate step before purchase.

Attributes:

- trial_id
- lead_id
- catalogue_item_id
- scheduled_at
- duration
- mode
- location_or_link
- status: proposed, confirmed, completed, missed, rescheduled, cancelled
- feedback
- next_action

Relationships:

- Trial belongs to Lead
- Trial may trigger Follow-Up Task
- Trial may lead to Quote

### Quote

Represents a commercial offer sent to the lead.

Attributes:

- quote_id
- lead_id
- fee_plan_id
- amount
- terms
- sent_at
- status: draft, sent, accepted, rejected, expired
- valid_until
- message_sent

Relationships:

- Quote belongs to Lead
- Quote references Fee Plan
- Accepted Quote creates Customer and Payment Schedule

### Follow-Up Task

Represents a recommended or scheduled action.

Attributes:

- task_id
- business_id
- related_entity_type
- related_entity_id
- task_type: inquiry_reply, trial_confirmation, post_trial, quote_follow_up, payment_reminder, reactivation, testimonial_request
- due_date
- priority
- status: pending, done, snoozed, cancelled
- suggested_message_id
- completed_at

Relationships:

- Follow-Up Task belongs to Business
- Follow-Up Task may reference Lead, Customer, Payment, Trial, or Quote
- Follow-Up Task may use AI Message

## Domain 6: Customer and Relationship

### Customer

Represents a converted buyer.

Attributes:

- customer_id
- business_id
- name
- contact_person
- phone_number
- email
- location
- customer_type: parent, student, client, company, individual
- status: active, inactive, churned
- start_date
- notes

Relationships:

- Customer belongs to Business
- Customer enrolls in Service Enrollment
- Customer has Payments
- Customer can provide Trust Proof

### Service Enrollment

Represents an active relationship between customer and service.

Attributes:

- enrollment_id
- customer_id
- catalogue_item_id
- fee_plan_id
- start_date
- end_date
- status
- billing_cycle
- next_due_date

Relationships:

- Enrollment belongs to Customer
- Enrollment generates Payment Schedule

## Domain 7: Payment and Receivables

### Payment Schedule

Represents expected payments.

Attributes:

- schedule_id
- customer_id
- enrollment_id
- amount_due
- due_date
- recurrence_rule
- status

### Payment

Represents actual or expected payment state.

Attributes:

- payment_id
- business_id
- customer_id
- lead_id
- amount_due
- amount_paid
- due_date
- paid_at
- status: unpaid, part_paid, paid, overdue, waived
- payment_mode: UPI, cash, bank_transfer, card, other
- reference_note
- screenshot_or_receipt_url

Relationships:

- Payment belongs to Business
- Payment may belong to Customer or Lead
- Payment may create Follow-Up Task

### Monthly Summary

Represents CA-ready but non-accounting monthly records.

Attributes:

- summary_id
- business_id
- month
- total_inquiries
- total_converted
- total_amount_due
- total_amount_collected
- total_overdue
- active_customers
- export_status

## Domain 8: Intelligence and Recommendations

### AI Message Template

Represents reusable message structures.

Attributes:

- template_id
- business_id
- message_type
- language
- tone
- body
- variables
- safety_status
- active_status

### Generated Message

Represents a specific output for a specific context.

Attributes:

- message_id
- template_id
- related_entity_type
- related_entity_id
- generated_text
- edited_text
- copied_at
- sent_status
- feedback

### Growth Score

Measures demand-generation readiness.

Components:

- Catalogue completeness
- Trust proof quality
- Public page hygiene
- Lead capture readiness
- Response speed
- Follow-up discipline
- Conversion clarity

### Health Score

Measures operating discipline.

Components:

- Lead response discipline
- Follow-up discipline
- Conversion health
- Payment collection health
- Repeat customer health
- Documentation readiness
- Profile readiness

### Recommendation

Represents a next-best action.

Attributes:

- recommendation_id
- business_id
- recommendation_type
- title
- reason
- expected_impact
- priority
- related_entity_type
- related_entity_id
- status

## Domain 9: Service Delivery and Commercial Packaging

### BizzNexx Package

Represents what BizzNexx sells.

Attributes:

- package_id
- name
- setup_fee
- monthly_fee
- included_pages
- included_catalogue_items
- included_templates
- support_level
- export_included
- active_status

### Subscription

Represents a customer's commercial relationship with BizzNexx.

Attributes:

- subscription_id
- business_id
- package_id
- start_date
- renewal_date
- status
- payment_status
- assigned_success_owner

### Setup Project

Represents the assisted onboarding job.

Attributes:

- setup_id
- business_id
- package_id
- status: intake, content_collection, catalogue_draft, page_review, published, handover
- owner_inputs_complete
- assigned_team_member
- target_publish_date
- blockers

### Support Request

Represents help required from BizzNexx.

Attributes:

- support_id
- business_id
- issue_type
- description
- priority
- status
- created_at
- resolved_at

## Critical Product Gaps in Current Prototype

The current prototype shows the idea, but it is still missing several important pieces:

- No real public route per business, such as `/b/ananya-learning-studio`
- No inquiry form connected to lead creation
- No owner setup wizard
- No catalogue item editor
- No quote or fee-plan object in backend models
- No trial/consultation model in backend models
- No customer/enrollment model in backend models
- No payment schedule model
- No page analytics/event model
- No trust-proof consent workflow
- No source attribution or campaign tracking
- No real AI prompt inputs or message generation boundary
- No user roles: BizzNexx admin, business owner, viewer
- No subscription/package object for the paid-service model
- No privacy, consent, or data retention model
- No validation metrics dashboard for the BizzNexx team

## Minimum Viable Business System

The first real version should include only:

- Business profile
- Catalogue and catalogue items
- Public page
- Inquiry capture
- Lead pipeline
- Follow-up tasks
- Payment tracker
- AI message templates
- Growth Score
- Health Score
- BizzNexx package/subscription

Everything else should be deferred until usage proves demand.

## First Pricing Hypothesis

This must be tested, not assumed.

### Starter

- Setup fee: Rs. 1,999-4,999
- Monthly fee: Rs. 299-799
- For solo tutors/coaches

### Growth

- Setup fee: Rs. 5,999-14,999
- Monthly fee: Rs. 999-2,499
- For service businesses with multiple offerings and recurring leads

### Managed Copilot

- Setup fee: Rs. 9,999+
- Monthly fee: Rs. 2,999-7,999
- For businesses that want BizzNexx to actively maintain catalogue, messaging, and monthly review

## Validation Questions

- Would you share this catalogue page with a prospect?
- Would this page make your business look more trustworthy?
- Would you pay to have this set up for you?
- What do you currently use instead?
- How many inquiries did you miss or forget last month?
- How many payment reminders felt awkward last month?
- How much money is pending right now?
- What would make this worth paying for every month?
- Would you pay for setup only, monthly support only, or both?

## Success Metrics

### User Outcome Metrics

- Catalogue page approved
- Catalogue page shared
- Inquiries captured
- Follow-ups completed
- Payments marked paid
- Pending amount reduced
- Messages copied or sent
- User returns after 3 days and 7 days

### Business Metrics

- Setup conversion rate
- Assisted onboarding completion rate
- Paid setup fee conversion
- Monthly subscription attach rate
- Support load per customer
- Churn after first month

## Sources Used For Market Context

- Ministry of MSME, Annual Report 2025-26.
- NPCI March 2026 UPI statistics as summarized by payment infrastructure reporting.
- FISME summary of GAME-FISME-C2FO Delayed Payments Report 3.0.
- Zoho, State of Digital and Customer Operations in Indian MSMEs.
- India SME Forum / Meta, The State of Digitalisation in Indian MSMEs, December 2025.
- CHI 2024/2025 research on WhatsApp for Business use and challenges in India.
