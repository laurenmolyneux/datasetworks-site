---
title: How to get a daily feed of new EU and UK public tenders
description: Pull new government tenders and contract awards from TED, UK Find a Tender and Contracts Finder into one spreadsheet or alert, filtered by keyword, CPV code, country and value.
tool: public-tenders
---
Public bodies in Europe publish billions in contracts every week, but they publish them on different portals: TED for the EU, Find a Tender for higher-value UK work and Contracts Finder for smaller UK contracts. Checking all three by hand every morning is slow, and their search pages all work differently.

## What you get

The [EU & UK Public Tenders](/tools/public-tenders/) tool searches all three official open-data APIs and returns one row per notice with the same fields every time:

- `title`, `titleEnglish` and `description`: what is being bought
- `buyerName`, `buyerCountry`, `buyerCity`: the public body buying it
- `cpvCodes` and `contractType`: the official category (works, supplies, services)
- `valueAmount` and `valueCurrency`: estimated or awarded value, when published
- `publishedDate` and `deadline`: when it opened and when bids are due
- `awardedSuppliers`: the winning companies, for award notices
- `url`: the official notice page to read the full documents

## Steps

1. Open the tool on Apify and add a few **Keywords** for your sector, such as `cybersecurity` or `facilities management`.
2. Choose **Open opportunities** to see tenders you can bid on, or **Contract awards** to see who won.
3. Narrow it down with **Buyer countries** (for example `DE`, `NL`, `GB`), **CPV codes** (`72` is IT services, `45` is construction) and a **Minimum value**.
4. Run it and export to CSV, Excel or JSON.

## Turn it into a daily tender alert

Save the input as a task, set **Published in the last N days** to 1 and add a daily schedule. Connect the run to email, Slack or a webhook, or pull the results from the API:

```
curl -X POST "https://api.apify.com/v2/acts/datasetworks~public-tenders/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["software"], "countries": ["DE", "FR", "GB"], "publishedWithinDays": 1}'
```

## Track competitors with contract awards

Set **Notice kind** to **Contract awards** and use your market's CPV codes. The `awardedSuppliers` column shows which companies are winning, from which buyers, and at what value.

## Cost

$2 per 1,000 notices. A daily alert for one sector usually returns a few dozen notices, so it costs cents a day. Use **Max results** to set a hard cap.

## Where the data comes from

Every notice comes from an official open-data API: the EU Publications Office's TED search API and the UK Cabinet Office's OCDS APIs (Open Government Licence). Contact names, emails and phone numbers are left out.
