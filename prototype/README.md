# BizzNexx Prototype

BizzNexx is a persona-first operating layer for Indian service-led microbusinesses.

This prototype proves the first product loop: a business presents a credible page, captures structured inquiries, follows up through WhatsApp, tracks pending payments, and knows what needs attention today.

The current beta focus is **Learning Studio**: tutors and small coaching businesses that need parent trust, trial follow-up, and monthly fee discipline without becoming CRM users.

The goal is to show the product feel before building the full platform:

- Public catalogue pages for persona-specific demo businesses
- Inquiry capture that creates leads in local storage
- Click-to-WhatsApp handoff
- Mobile-first owner dashboard
- BizzNexx operator console
- Lead pipeline
- Payment visibility
- Segment-specific message suggestions
- BizzNexx Growth Score and Health Score
- PWA install basics

## Product Essence

BizzNexx is not a generic website builder, CRM, accounting app, or LMS.

It is a paid service and software layer that helps small businesses:

- Look trustworthy to prospects
- Reduce repeated WhatsApp explanations
- Capture better lead context
- Act on today's follow-ups
- Track fee/payment status without owning payment settlement
- Improve operational discipline through assisted setup

For Learning Studio, that means:

- A parent-ready page
- Trial inquiry capture
- Teacher credibility and proof
- Parent-friendly message templates
- Trial and post-trial action queue
- Monthly fee reminders

## Structure

- `frontend/`: React prototype UI with sample data
- `backend/`: Django backend shape and first-pass models
- `shared/`: shared ontology notes and sample records

## Recommended First Run

Run the backend first so the MVP uses real persisted records.

```bash
cd prototype/backend
python manage.py migrate
python manage.py seed_demo
python manage.py runserver 8000
```

Then run the frontend.

```bash
cd prototype/frontend
npm install
npm run dev
```

The frontend reads from `http://localhost:8000/api` by default and falls back to browser-local demo data if the API is not running.

## Real Workflow Now Implemented

- Businesses are stored in SQLite through Django.
- Catalogue pages, services, trust proof, leads, payments, setup stages, messages, and page events are real models.
- Public inquiry capture creates both an `Inquiry` and a `Lead`.
- Inquiry capture also creates a follow-up task.
- Lead status changes persist through the API.
- Payment mark-paid actions persist through the API.
- Operator setup stage changes persist through the API.

## Guided Feedback Flow

Use this sequence during feedback calls:

1. Open the app.
2. Choose a demo business from the sidebar.
3. Start with `Today` to show open leads, payment actions, and score reasons.
4. Open `Leads`, update a lead status, and preview the WhatsApp follow-up.
5. Open `Payments`, mark one payment paid, and preview a payment reminder.
6. Open `Catalogue` to review the public page preview and submit a sample inquiry.
7. Open `Messages` to check persona-specific templates.
8. Open `Insights` to explain why the scores changed.
9. Turn on `Operator mode` only when showing internal setup quality control.

## Important Pilot Boundary

This MVP is ready for guided feedback demos with selected users on a local or private deployment. Before public real-data collection, complete:

- Consent and privacy policy
- Terms and safe collections disclaimer
- Production domain and HTTPS
- Admin access control
- Data deletion process

## Private Beta Controls

The prototype now includes lightweight private-beta controls. They are not a replacement for production authentication, but they reduce accidental exposure during selected-user validation.

Backend:

- Copy `backend/.env.example` to `backend/.env`.
- Set `DJANGO_DEBUG=False` for deployment.
- Set `DJANGO_ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`, and `CSRF_TRUSTED_ORIGINS`.
- Set `BIZZNEXX_BETA_API_KEY` to require `X-BizzNexx-Beta-Key` on API calls.

Frontend:

- Copy `frontend/.env.example` to `frontend/.env`.
- Set `VITE_API_BASE` to the deployed API URL.
- Set `VITE_BETA_API_KEY` to match the backend key.
- Set `VITE_BETA_ACCESS_CODE` to show an access-code gate for invited reviewers.

Local development remains open if these env vars are not set.

For hosted deployment, use the root `render.yaml` and follow `../DEPLOYMENT_PRIVATE_BETA.md`.

## First Prototype Principle

BizzNexx is not an accounting platform. It is a paid service and software layer that helps small service businesses present what they sell, capture inquiries, follow up, collect better, and understand what needs attention today.
