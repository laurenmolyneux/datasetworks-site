---
title: How to find broken links and SEO issues across a whole website
description: Crawl a site and get every broken link, missing or duplicate title, meta description, H1, canonical and sitemap gap as one spreadsheet, page by page.
tool: website-seo-audit
---
Most SEO problems are boring and fixable: a page with no meta description, two pages with the same title, a link to a product that no longer exists, a page that never made it into the sitemap. The hard part is finding them across hundreds of pages without clicking through each one.

## What you get

The [Website SEO Audit](/tools/website-seo-audit/) reads the site's robots.txt and XML sitemap, crawls up to the number of pages you set, and returns one row per page with:

- `title`, `titleLength`, `metaDescription`, `metaDescriptionLength`, `h1`, `h1Count`
- `canonical`, `metaRobots` and `xRobotsTag` (so you can spot accidental `noindex`)
- `brokenLinks`: every link on the page that returned 404, 410, a server error or no answer, marked internal or external
- `inSitemap`, `redirected`, `responseMs`, `wordCount`, `imagesMissingAlt`, `structuredDataTypes`
- `issues`: a list of fixed codes such as `duplicate_title`, `missing_meta_description`, `multiple_h1`, `not_in_sitemap` and `broken_links`

A per-site summary with issue counts is saved as `SUMMARY` in the run's key-value store.

## Steps

1. Open the tool on Apify and add your site, e.g. `example.com`.
2. Set **Max pages per site**. Start with 50 to see what comes back; raise it for a full audit.
3. Run it, export as CSV or Excel, and sort by `issueCount` or `brokenLinkCount`. Fix the pages at the top first.

## Run it after every release

Save the input as an Apify task and add a weekly schedule, or call it from your deploy pipeline:

```
curl -X POST "https://api.apify.com/v2/acts/datasetworks~website-seo-audit/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"websites": ["example.com"], "maxPagesPerSite": 100}'
```

Set `checkExternalLinks` to `false` if you only care about links inside your own site.

## Why some links show as "unverified"

Some sites refuse automated checks and answer 403 or 429 even when the page exists (review sites and social networks often do). The tool counts these as `unverifiedLinkCount` instead of calling them broken, so the broken list stays worth acting on.

## Cost

$2 per 1,000 pages audited. Link checks and the sitemap read are free. A weekly 200-page audit costs about $1.60 a month.
