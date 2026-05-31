# BizzNexx Team UI Review Guide

This guide is for teammates who need to review the BizzNexx prototype UI and product flow.

## What You Need From Rick

You do **not** need Rick's GitHub password, laptop password, or any private credentials.

You only need:

1. A GitHub account.
2. Access to the private repository:

```text
https://github.com/rickdatascientist/bizznexx-mvp
```

Rick must invite your GitHub username from:

```text
Repository > Settings > Collaborators and teams > Add people
```

## Option A: Review The UI From Your Own Laptop

Use this if you want to run the prototype yourself.

### 1. Install Required Tools

Install these free tools:

- Git
- Python 3.11 or later
- Node.js LTS

Check installation:

```powershell
git --version
python --version
node --version
npm --version
```

### 2. Clone The Repository

```powershell
git clone https://github.com/rickdatascientist/bizznexx-mvp.git
cd bizznexx-mvp
```

If GitHub asks you to sign in, use your own GitHub account that Rick invited.

### 3. Start The Backend

Open a terminal:

```powershell
cd prototype/backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver 8000
```

Keep this terminal open.

The backend should be available at:

```text
http://localhost:8000/api/businesses/
```

### 4. Start The Frontend

Open a second terminal:

```powershell
cd prototype/frontend
npm install
npm run dev
```

Open the URL shown in the terminal. Usually:

```text
http://localhost:5173
```

## Option B: Review A Live Link From Rick

Use this if you only need to see the UI and do not want to set up code locally.

Rick can run the app on his laptop and share a temporary Cloudflare Tunnel or similar free tunnel link.

Important limits:

- The link works only while Rick's laptop and tunnel are running.
- The link is temporary.
- This is for selected review only, not public launch.

## Suggested UI Review Script

Review all three demo businesses from the business dropdown:

- Ananya Learning Studio
- Ria Bridal Studio
- Northstar Design Co.

For each business, check:

1. **Today**
   - Does the action queue feel useful?
   - Are open leads, follow-ups, and pending amounts clear?
   - Do score reasons explain what needs attention?

2. **Leads**
   - Can you understand each lead's next action?
   - Try changing a lead status.
   - Open the WhatsApp follow-up preview.

3. **Payments**
   - Are pending payments visible?
   - Try marking one payment as paid.
   - Open the payment reminder preview.

4. **Catalogue**
   - Does the public page preview feel credible for the business type?
   - Are services/packages specific enough?
   - Submit a test inquiry and confirm it appears in the workflow.

5. **Messages**
   - Do the message templates feel specific to the business?
   - Do they sound natural for Indian customers?

6. **Insights**
   - Do Growth Score and Health Score explain useful action?
   - Are the warnings practical?

7. **Operator Mode**
   - Turn on Operator mode from the sidebar.
   - Open Setup.
   - Check whether setup quality, blockers, and readiness are understandable.

## What Feedback We Want

Please give feedback in this structure:

```text
Business reviewed:
Screen:
What felt useful:
What felt confusing:
What felt fake/superficial:
What would make a real business owner pay:
Priority: High / Medium / Low
```

## Important Notes

- This is an MVP prototype for selected feedback.
- Demo data is synthetic.
- Do not enter real customer personal data.
- Do not use this for real payment collection yet.
- Do not push directly to `main` unless Rick asks you to. Developers should create a branch and pull request.

## Developer Contribution Flow

If you are contributing code:

```powershell
git checkout -b your-name/short-change-description
```

Make changes, then:

```powershell
git status
git add .
git commit -m "Describe your change"
git push -u origin your-name/short-change-description
```

Then open a pull request on GitHub.
