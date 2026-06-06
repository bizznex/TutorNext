# BizzNexx

BizzNexx is a persona-first business operating layer for Indian service-led microbusinesses.

It helps a small business do four practical things better:

- Look credible when a prospect opens the business page
- Capture useful inquiry details instead of scattered WhatsApp messages
- Follow up on the right lead, trial, booking, or payment at the right time
- Understand what needs attention today without maintaining a heavy CRM

The first focused beta wedge is **Learning Studio**: tutors, coaching classes, and small academic learning businesses.

## Why This Exists

Small service businesses in India often run on WhatsApp, referrals, Instagram, UPI, memory, and owner discipline.

That works until the owner starts losing value through:

- Repeated explanations
- Missed follow-ups
- Unclear inquiries
- Awkward payment reminders
- Weak trust proof
- No simple action queue

BizzNexx is not trying to replace WhatsApp. It is trying to make WhatsApp-led businesses more structured, credible, and easier to operate.

## Current Product Shape

The prototype supports:

- Public catalogue/business pages
- Persona-specific demo businesses
- Inquiry capture
- Inquiry-to-lead workflow
- Follow-up task creation
- Lead status updates
- Payment visibility and mark-paid actions
- Message preview before WhatsApp handoff
- Owner dashboard
- Operator setup view
- Growth and health score explanations
- Private beta access controls
- Render deployment blueprint

## Learning Studio Beta

The Learning Studio beta uses **Ananya Learning Studio** as the validation anchor.

The intended loop:

1. Parent opens a credible learning studio page.
2. Parent submits class, board, subject, timing, and trial interest.
3. Owner gets a parent inquiry action.
4. Owner sends or edits a WhatsApp reply.
5. Trial follow-up is tracked.
6. Enrollment creates monthly fee visibility.
7. Fee reminders are handled politely.

This beta is deliberately narrow. The goal is to prove whether a real tutor would pay for a professional parent-facing page plus a lightweight operating system for inquiries, trials, follow-ups, and monthly fees.

## What BizzNexx Is Not

BizzNexx is not:

- A learning management system
- A coaching ERP
- A payment gateway
- A tax or GST filing product
- A lead-generation guarantee
- A legal compliance tool
- A generic CRM with tutor labels

The product promise is smaller and sharper: help a service business present, capture, follow up, and collect with less chaos.

## Repository Structure

- `prototype/frontend`: React + Vite owner/operator UI
- `prototype/backend`: Django + DRF API
- `render.yaml`: Render private beta deployment blueprint
- `DEPLOYMENT_PRIVATE_BETA.md`: deployment instructions
- `PROJECT_LOG.md`: living record of what is done, what is left, and what is next
- `Learning_Studio_*.md`: research, strategy, execution, and rollout planning for the Learning Studio wedge

## Run Locally

Run the backend:

```bash
cd prototype/backend
python manage.py migrate
python manage.py seed_demo
python manage.py runserver 8000
```

Run the frontend:

```bash
cd prototype/frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

Select **Ananya Learning Studio** and open **Beta Studio**.

## Private Beta Deployment

Use the root `render.yaml` with Render Blueprint deployment.

See:

[DEPLOYMENT_PRIVATE_BETA.md](DEPLOYMENT_PRIVATE_BETA.md)

## Current Status

The product is ready for private deployment setup and guided beta preparation.

It is not yet ready for broad public launch. Remaining work includes real authentication, reviewed legal documents, formal data deletion workflow, monitoring, backups, staging/production separation, and end-to-end tests.

