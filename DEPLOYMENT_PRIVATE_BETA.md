# BizzNexx Private Beta Deployment

## Target

Deploy the Learning Studio beta as a private HTTPS deployment:

- Frontend: `bizznexx-beta`
- Backend API: `bizznexx-beta-api`
- Database: `bizznexx-beta-db`

The repository includes a Render blueprint in `render.yaml`.

## Deploy Steps

1. Push the latest `main` branch to GitHub.
2. Open Render and create a new Blueprint from the GitHub repo.
3. Use the root `render.yaml`.
4. Let Render create:
   - Postgres database
   - Django API web service
   - Vite static frontend
5. After the API service is created, open its environment variables.
6. Copy the generated `BIZZNEXX_BETA_API_KEY`.
7. Add the same value to the frontend service as `VITE_BETA_API_KEY`.
8. Set `VITE_BETA_ACCESS_CODE` on the frontend service to the code you want to share with beta reviewers.
9. Redeploy the frontend after setting those values.

## First Data Seed

After the API deploy succeeds, open the Render shell for `bizznexx-beta-api` and run:

```bash
python manage.py seed_demo
```

This creates the Ananya Learning Studio, Ria Bridal Studio, and Northstar Design Co. demo records in the production beta database.

## Expected URLs

If the Render service names are unchanged:

- Frontend: `https://bizznexx-beta.onrender.com`
- API: `https://bizznexx-beta-api.onrender.com/api`

If Render changes the domains, update:

- Backend `DJANGO_ALLOWED_HOSTS`
- Backend `CORS_ALLOWED_ORIGINS`
- Backend `CSRF_TRUSTED_ORIGINS`
- Frontend `VITE_API_BASE`

## Before Inviting Beta Users

Verify:

- Frontend opens on HTTPS.
- API health check returns OK at `/healthz`.
- Access code gate appears if `VITE_BETA_ACCESS_CODE` is set.
- API responds through the frontend.
- Ananya Learning Studio appears.
- Beta Studio tab opens.
- Trial inquiry creates a lead.
- Message preview opens.
- Payment status update works.
- Beta terms page is visible.
- GitHub Actions CI is passing on `main`.

## Current Limitations

This is private-beta safety, not production-grade auth.

Still needed before public launch:

- Real user authentication
- Reviewed privacy policy and terms
- Formal data deletion workflow
- Error monitoring
- Backup/restore procedure
- Staging/production separation
- End-to-end tests
