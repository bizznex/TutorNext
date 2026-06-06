# Private Beta QA Checklist

Run this after deployment and after any beta-facing change.

## Deployment Info

- Frontend URL:
- API URL:
- Deployment date:
- Build/commit:
- QA owner:

## Environment

- `DJANGO_DEBUG=False`
- `DJANGO_SECRET_KEY` set
- `DJANGO_ALLOWED_HOSTS` restricted
- `CORS_ALLOW_ALL_ORIGINS=False`
- `CORS_ALLOWED_ORIGINS` set to frontend URL
- `CSRF_TRUSTED_ORIGINS` set to frontend URL
- `BIZZNEXX_BETA_API_KEY` set
- `VITE_API_BASE` set to API URL
- `VITE_BETA_API_KEY` matches backend key
- `VITE_BETA_ACCESS_CODE` set

## Backend QA

- API service deploy succeeded
- API health check `/healthz` returns `{"status":"ok"}`
- Database service exists
- `python manage.py migrate` completed
- `python manage.py seed_demo` completed
- `/api/businesses/` rejects missing/wrong beta key
- `/api/businesses/` works with correct beta key
- Admin URL loads

## Frontend QA

- Frontend opens over HTTPS
- Access code gate appears
- Wrong access code is rejected
- Correct access code opens workspace
- Ananya Learning Studio appears
- Beta Studio tab appears for Ananya
- Beta Studio tab does not appear for non-tutor personas
- Beta terms page appears

## Learning Studio Flow

- Parent page content renders
- Teacher profile renders
- Trust proof renders
- Course cards render
- FAQ renders
- Trial inquiry form submits
- Submitted inquiry creates a new lead
- Today dashboard updates after inquiry
- Message preview opens
- WhatsApp handoff link opens
- Lead status can be changed
- Payment reminder preview opens
- Payment can be marked paid

## Mobile QA

- Sidebar/navigation usable on mobile
- Beta Studio hero text fits
- Course cards stack correctly
- Inquiry fields are usable
- Message modal fits viewport
- Buttons do not overflow
- No text overlaps

## Safety QA

- Beta disclaimer visible
- Inquiry data-use copy visible
- Beta terms explain no guaranteed leads/results/payment recovery
- No copy guarantees marks, admissions, ranks, or fee recovery
- Synthetic/demo nature is clear enough for beta

## Result

Status:

- Pass
- Pass with P1 issues
- Blocked

P0 issues:

1.
2.
3.

P1 issues:

1.
2.
3.

Decision:

- Ready for 3-5 guided beta users
- Fix issues first
