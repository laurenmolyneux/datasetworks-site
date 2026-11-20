---
title: Monitor news mentions and trending topics for any company or keyword
description: Get recent worldwide news articles, in 100+ languages, for a list of keywords, plus a simple trend score showing whether coverage is rising or falling.
tool: news-trend-monitor
---
Media monitoring services are expensive and mostly built for PR teams. If you just need to know what's being written about a few companies, products or topics, and whether that coverage is growing, a scheduled data run does the job.

## What you get

The [News & Trend Monitor](/tools/news-trend-monitor/) searches worldwide online news (via the open GDELT project) for each term, and returns one row per article: `title`, `url`, `domain`, `publishedAt`, `sourceCountry` and `language`.

A summary per term gives article counts, a volume timeline and `changePercent`: how much coverage grew or shrank between the first and second half of the time window.

## Steps

1. Enter search terms, e.g. your company, competitors or a topic ("AI agents", "Nvidia").
2. Pick a time window (1 hour to 90 days) and a maximum number of articles per term.
3. Run, and sort by `publishedAt` or look at `changePercent` in the summary.

## Daily briefing for an AI agent

Schedule it each morning and hand the results to an AI agent to summarise:

```
curl -X POST "https://api.apify.com/v2/acts/datasetworks~news-trend-monitor/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries": ["Nvidia"], "timespan": "24h", "maxArticlesPerQuery": 20}'
```

Cost: $0.01 per search term plus $1 per 1,000 articles.
