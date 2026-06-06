# GitHub Pages Beta Preview

This is the fastest no-new-cloud-account preview path for BizzNexx.

It deploys the React frontend as a static GitHub Pages site. This is useful for UI review and guided beta walkthroughs when Render or another backend host is not available yet.

## What This Preview Can Do

- Show the BizzNexx workspace UI
- Show Ananya Learning Studio
- Show the **Beta Studio** tab
- Use local fallback demo data in the browser
- Let reviewers submit local test inquiries
- Let reviewers update local lead/payment states
- Demonstrate the product concept externally

## What This Preview Cannot Do

- Persist data across users
- Use the Django API
- Store real parent inquiries centrally
- Support owner/operator production access
- Replace the Render private beta deployment

Use this for fast UI validation. Use Render for API-backed private beta.

## Setup

1. Go to the GitHub repo.
2. Open **Settings**.
3. Open **Pages**.
4. Set source to **GitHub Actions**.
5. Push to `main`, or manually run the workflow:
   - **Actions**
   - **Deploy Frontend Preview to GitHub Pages**
   - **Run workflow**

## Expected URL

For this repo, the likely URL is:

```text
https://rickdatascientist.github.io/bizznexx-mvp/
```

If GitHub shows a different Pages URL, use that.

## Review Instructions

1. Open the GitHub Pages URL.
2. Select **Ananya Learning Studio**.
3. Open **Beta Studio**.
4. Review the parent page and trial inquiry flow.
5. Use `BETA_USER_REVIEW_GUIDE.md` during the call.
6. Capture feedback in `BETA_FEEDBACK_FORM.md`.

## Important Note

Because this is a static preview, it is not the place to collect real parent/student data. Treat all entered data as local browser demo data only.

