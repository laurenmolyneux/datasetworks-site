---
title: How to find sales leads from hiring signals
description: Use companies' public job postings to spot who is about to buy what you sell, with a repeatable list you can refresh every week.
tool: company-jobs
---
A company that posts a job for a "Head of Data Engineering" is probably about to buy data tools. One hiring five SDRs needs sales software and training. A first "Compliance Manager" means compliance spend is coming. Job postings are one of the clearest public buying signals there is, and they appear weeks before a purchase.

## The idea

1. Keep a list of companies that fit your customer profile.
2. Every week, pull their open roles.
3. Flag the companies hiring for roles that use, buy or manage what you sell.
4. Reach out while the need is fresh, mentioning the team they are building.

## Pull the jobs

The [ATS Job Listings](/tools/company-jobs/) tool reads companies' public job boards on Greenhouse, Lever, Ashby, Personio and Recruitee, and returns every open role with the same columns. Use the `keyword` filter to keep only the roles that signal a need:

```json
{"companies": ["greenhouse:datadog", "ashby:notion", "greenhouse:figma", "ashby:ramp"], "keyword": "data engineer, analytics, data platform"}
```

Each row has `company`, `title`, `department`, `location`, `postedAt` and the `url` of the posting, so the evidence for every lead is one click away.

## Signals that work well

| You sell | Look for roles like |
| --- | --- |
| Sales tools, sales training | `account executive`, `SDR`, `BDR`, `sales enablement` |
| Data and analytics tools | `data engineer`, `analytics engineer`, `head of data` |
| Security and compliance | `security engineer`, `compliance`, `GRC`, `SOC 2` |
| Recruiting services | many open roles at once, or a first `talent acquisition` hire |
| Cloud and DevOps tooling | `platform engineer`, `SRE`, `DevOps` |
| Expansion services (legal, payroll, office) | the first roles in a new country |

## Make it weekly

Save your input as a task on Apify and schedule it weekly. Send the results to Google Sheets with the built-in integration. Because each job has a stable `jobId`, a new row that wasn't there last week is a new signal.

## Use it with an AI agent

Connect the tool to Claude, ChatGPT or Cursor through MCP (see [how to use Dataset Works tools in AI assistants](/guides/use-data-tools-in-claude-chatgpt-and-cursor-with-mcp/)) and ask: "Which of these 20 companies are hiring data engineers, and what do the postings say about their stack?"

## Cost

$1.50 per 1,000 jobs. A weekly check of 50 companies with a keyword filter usually costs well under a dollar.

## Good practice

Job postings are public business information about companies, not people. Use them to understand what a company needs. Don't use them to identify or contact individual candidates.
