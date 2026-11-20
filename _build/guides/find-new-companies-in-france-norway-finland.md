---
title: How to find newly registered companies in France, Norway and Finland
description: Build a list of new companies by industry and area from the official French, Norwegian and Finnish company registers, or check a list of company IDs, with no API keys.
tool: european-company-registry
---
A company that registered last week is a company that needs a bank, an accountant, software, an office and a website. National company registers publish that data openly, but each country has its own API, its own codes and its own field names.

## What you get

The [Company Registry Search](/tools/european-company-registry/) tool queries three official registers at once and returns one row per company with the same fields every time:

- `registryId` and `vatId`: the SIREN, Norwegian organisation number or Finnish Y-tunnus, plus the VAT number
- `name`, `otherNames`, `legalForm` and `status` (active, closed, bankrupt, in liquidation)
- `industryCode` and `industryDescription`, `incorporationDate`
- `street`, `postalCode`, `city`, `employees` band and `website` where the register has them
- `registryUrl`: the company's official register page

It returns company-level data only. Directors, owners, emails and phone numbers are never included, and sole traders are skipped.

## Recipe 1: new software companies this month

```json
{"countries": ["NO", "FI"], "industryCodes": ["62.100", "62100"], "registeredAfter": "2026-11-01", "maxResults": 500}
```

Each register uses its own industry codes: Norway SN2025 with a dot (`62.100`), Finland TOL (`62100`), France NAF (`62.01Z`). Mix them in one run and each code goes only to the register it belongs to.

## Recipe 2: check a list of company IDs

Paste SIRENs, Norwegian organisation numbers or Finnish Y-tunnus codes into **Registry IDs**:

```json
{"registryIds": ["306138900", "923609016", "0112038-9"]}
```

The country is detected from the format. Use it to confirm a supplier exists and is active, or to fill in VAT numbers and legal forms in a CRM.

## Recipe 3: companies in one sector and postcode

```json
{"countries": ["FR"], "industryCodes": ["62.02A"], "postalCode": "69002", "maxResults": 200}
```

## Make it a weekly lead list

Save your input as an Apify task, schedule it weekly with **Registered on or after** set to last week, and add the Google Sheets or Slack integration. New companies land in your sheet automatically.

## Cost

$1.50 per 1,000 companies. A weekly list of 200 new companies costs about $0.30.
