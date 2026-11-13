---
title: How to track competitor hiring from their careers pages
description: Pull every open role at a list of companies from Greenhouse, Lever, Ashby, Personio and Recruitee job boards, and watch what they hire for.
tool: company-jobs
---
A company's open roles say a lot about its plans: a new country, a new product line, an AI team, a sales push. Most fast-growing companies post their jobs on an applicant tracking system (ATS) like Greenhouse, Lever or Ashby, and those boards are public.

## What you get

The [ATS Job Listings tool](/tools/company-jobs/) takes a list of companies and returns every open role, one row per job: `title`, `location`, `department`, `employmentType`, `isRemote`, `compensation` (where posted), `postedAt`, `url`, and optionally the full `description` as plain text.

## Steps

1. Enter company board names, e.g. `stripe`, `lever:palantir`, `ashby:ramp`. The board name is the bit after the ATS domain in the company's careers URL (`boards.greenhouse.io/stripe` → `stripe`).
2. Run. Export to a spreadsheet.
3. Pivot by `company` and `department` to see where each competitor is growing.

## Turn it into a weekly report

Schedule the run weekly in Apify and compare with last week's dataset: new departments, new locations and roles that disappeared are the interesting signals. An AI agent can do the comparison for you via the API:

```
curl -X POST "https://api.apify.com/v2/acts/datasetworks~company-jobs/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["stripe", "ashby:ramp"], "maxJobsPerCompany": 200}'
```

## Other uses

- Recruiters and job boards building a feed of roles at target companies
- Investors watching hiring velocity at portfolio or competitor companies
- Sales teams spotting buying signals ("hiring 5 data engineers" → they may need data tools)

Cost: $1.50 per 1,000 jobs. Only company job data is collected, no personal data.
