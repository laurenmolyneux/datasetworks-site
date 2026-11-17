---
title: How to find UK government contracts to bid on (and get alerts every morning)
description: A practical way to monitor UK public sector tenders from Find a Tender and Contracts Finder, filter them to your sector and get a daily list of new opportunities.
tool: public-tenders
---
UK public bodies publish their contract opportunities in two places. **Find a Tender** carries higher-value contracts, and **Contracts Finder** carries smaller ones, from about £12,000 for central government and £30,000 for the wider public sector. Councils, NHS trusts, universities, schools and housing associations all post there, and many contracts suit small suppliers.

The problem is checking both sites every day. Saved searches send long emails, the two sites use different categories, and good opportunities have short deadlines.

## The quick version

Run the [EU & UK Public Tenders](/tools/public-tenders/) tool with this input:

```json
{"keywords": ["cleaning", "facilities management"], "countries": ["GB"], "noticeKind": "open", "publishedWithinDays": 1}
```

You get one row per new opportunity from both UK portals (and nothing from the EU, because only `GB` is in the countries list), with the buyer, value, deadline and a link to the official notice.

## Step by step

1. **Pick your keywords.** Use the words buyers use in titles, not your own marketing terms: `grounds maintenance`, `catering`, `software`, `training`, `translation`, `CCTV`.
2. **Or use CPV codes.** Every notice has a CPV code for what is being bought. The first two digits cover a sector: `72` IT services, `79` business services, `90` cleaning and waste, `80` education and training, `45` construction, `85` health and social care.
3. **Set a minimum value** if small contracts are not worth your time, for example `"minValue": 50000`.
4. **Choose the kind of notice.** `open` gives tenders you can still bid on. `awards` shows who won past contracts and for how much, which is the best way to price your bid and see who you are up against.
5. **Run it daily.** Save the input as a task on Apify, set **Published in the last N days** to 1, and schedule it for 7am. Add the email, Slack or Google Sheets integration to get the new list each morning.

## Example: IT suppliers

```json
{"cpvCodes": ["72", "48"], "countries": ["GB"], "noticeKind": "open", "publishedWithinDays": 1, "minValue": 25000}
```

`48` is software packages, so this catches both software and IT service contracts worth £25k or more.

## Example: see who wins in your market

```json
{"keywords": ["grounds maintenance"], "countries": ["GB"], "noticeKind": "awards", "publishedWithinDays": 90, "maxResults": 500}
```

Sort by `valueAmount` and look at `awardedSuppliers` and `buyerName`. Councils that bought last year will often buy again when the contract ends.

## What it costs

$2 per 1,000 notices. A daily alert for one sector usually returns 5 to 50 notices, so it costs a few cents a day. Set **Max results** as a hard cap.

## Where the data comes from

All notices come from the UK Cabinet Office's official OCDS APIs for Find a Tender and Contracts Finder, published under the Open Government Licence. Contact names, emails and phone numbers are left out of the results; use the `url` to read the full notice and documents on the official site.
