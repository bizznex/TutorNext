# BizzNexx Free Review Sharing Guide

This guide keeps the review setup free. Do not share GitHub passwords, personal access tokens, or cloud credentials in chat or documents.

## What We Are Sharing

There are two separate review needs:

1. **Code review**: teammates can inspect, comment, and run the project.
2. **UI/product review**: teammates can open the live BizzNexx prototype in a browser.

For code review, use a free private GitHub repository. For live UI review, use temporary Cloudflare Quick Tunnel links from your laptop.

## Recommended Free Setup

### Step 1: Create A Free Private GitHub Repo

Create the repo yourself from your GitHub account.

Suggested repo name:

```text
bizznexx-mvp
```

Use:

- Visibility: Private
- README: unchecked, because this project already has files
- `.gitignore`: none, because this repo now has a project `.gitignore`

After creating it, GitHub will show commands similar to:

```powershell
git init
git add .
git commit -m "Initial BizzNexx MVP prototype"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bizznexx-mvp.git
git push -u origin main
```

Run those locally from:

```powershell
D:\BizSaarthi_AI
```

If GitHub asks you to sign in, use the browser/device login flow or Git Credential Manager. Do not paste credentials into project files.

### Step 2: Invite Teammates

In GitHub:

```text
Repo > Settings > Collaborators and teams > Add people
```

Give teammates access based on role:

- Read: product reviewers who only need to inspect.
- Triage/Write: developers who need to comment deeply or push branches.

### Step 3: Run Backend Locally

From a terminal:

```powershell
cd D:\BizSaarthi_AI\prototype\backend
python manage.py migrate
python manage.py seed_demo
python manage.py runserver 0.0.0.0:8000
```

Keep this terminal open.

### Step 4: Run Frontend Locally

From a second terminal:

```powershell
cd D:\BizSaarthi_AI\prototype\frontend
npm install
npm run dev
```

Keep this terminal open.

### Step 5: Create Public Review Links

Use Cloudflare Quick Tunnel or another free localhost tunnel.

You need two public links:

- One tunnel for backend port `8000`
- One tunnel for frontend port `5173`

Example shape:

```text
Backend tunnel:  https://backend-random.trycloudflare.com
Frontend tunnel: https://frontend-random.trycloudflare.com
```

The frontend must know the backend URL. Start Vite with `VITE_API_BASE` set to the backend tunnel plus `/api`.

PowerShell example:

```powershell
cd D:\BizSaarthi_AI\prototype\frontend
$env:VITE_API_BASE="https://backend-random.trycloudflare.com/api"
npm run dev
```

Then share the frontend tunnel link with reviewers:

```text
https://frontend-random.trycloudflare.com
```

## What Reviewers Should Test

Ask teammates to review this sequence:

1. Pick each business from the business dropdown.
2. Open Today and check whether the action queue feels useful.
3. Open Leads and change one lead status.
4. Open Payments and generate a reminder.
5. Open Catalogue and review the public page preview.
6. Submit a test inquiry from Catalogue.
7. Open Messages and check whether templates feel business-specific.
8. Toggle Operator mode and inspect setup quality.

## Important Limits

- The Cloudflare Quick Tunnel link is temporary. If you stop the tunnel, the link dies.
- Your laptop must stay on and connected.
- This setup is for selected review only, not public launch.
- Current Django settings are permissive for development review. Tighten `ALLOWED_HOSTS`, CORS, secrets, and permissions before production.
- The local SQLite database is ignored by Git. Teammates should run migrations and `seed_demo` to recreate demo data.

## No-Cost Rule

Do not add paid hosting, paid database, paid email, paid SMS, or paid automation yet. The next stage should still run on:

- Local laptop
- Free private GitHub repo
- Free temporary tunnel
- Synthetic demo data
