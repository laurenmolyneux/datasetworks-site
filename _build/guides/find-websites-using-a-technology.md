---
title: Find which companies use Shopify, HubSpot or any other technology
description: Check a list of company websites for their CMS, ecommerce platform, analytics, chat and marketing tools, to build targeted lead lists.
tool: website-tech-stack
---
If you sell a Shopify app, a HubSpot integration or a replacement for Intercom, your best leads are the companies already using those tools. Their websites usually give it away in the page code.

## What you get

The [Website Tech Stack & Company Profile Lookup](/tools/website-tech-stack/) loads each homepage once and returns:

- `technologyNames` and `technologies`: about 100 detectable tools across CMS, ecommerce, analytics, ad pixels, live chat, marketing automation, payments, CDN and frameworks
- `siteName`, `description`, `language` and the company's official `socialProfiles`
- `server`, `https`, `responseMs`

## Steps

1. Paste a list of domains (from a CRM export, a directory or a trade-show list) into **Websites**.
2. Run and export to a spreadsheet.
3. Filter `technologyNames` for the tool you care about, e.g. contains "Shopify" or does not contain "Google Analytics".

## For enrichment and AI agents

Call it from your CRM workflow or agent with one domain at a time, and you get a short company profile plus its stack:

```
curl -X POST "https://api.apify.com/v2/acts/datasetworks~website-tech-stack/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" -d '{"domains": ["allbirds.com"]}'
```

Pair it with the [DNS & email lookup](/tools/domain-dns-ssl-lookup/) to add the company's email provider too.

Cost: $2 per 1,000 websites. The tool follows robots.txt and collects company-level facts only.
