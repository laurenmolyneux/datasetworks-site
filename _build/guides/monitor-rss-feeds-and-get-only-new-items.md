---
title: Monitor RSS feeds and get only the new items, as JSON
description: Watch competitor blogs, news sites and release notes for new posts on a schedule, with one clean JSON format for RSS, Atom and JSON Feed.
tool: rss-feed-to-json
---
Most company blogs, news sites, changelogs and podcasts still publish a feed. Feeds are the politest, most reliable way to follow a site: they are made to be read by machines, and they change format far less than web pages. The catch is that there are four formats (RSS 2.0, RSS 1.0, Atom and JSON Feed), dates come in a dozen styles, and you usually only want what is new since you last looked.

## Common uses

**Competitor and market monitoring.** Follow competitors' blogs, product changelogs and press pages, and get a daily list of what they published.

**Content and newsletter pipelines.** Pull the week's posts from a list of sources into a sheet or database, ready to curate.

**Fresh sources for AI agents.** Give an agent a stable feed of recent articles to summarise, classify or answer questions from, without a parser for each site.

## What you get

The [RSS & Atom Feed Reader to JSON](/tools/rss-feed-to-json/) returns one row per item with the same fields whatever the format:

| field | example |
| --- | --- |
| `feedTitle` / `feedUrl` | The GitHub Blog / https://github.blog/feed/ |
| `title` / `link` | the item's headline and URL |
| `publishedAt` | always ISO 8601 in UTC |
| `summary` | plain text, HTML removed, up to 1,000 characters |
| `categories` | tags the publisher gave the item |
| `imageUrl` / `enclosures` | thumbnail, podcast audio or attachments |
| `itemId` | a stable ID, handy for de-duplicating in your own database |

You don't need to know a site's feed address: give it `github.blog` and the tool finds the feed the site advertises.

## Steps

1. Paste feed URLs or website addresses into the tool.
2. Tick **Only new items since the last run** and give it a **State key**, e.g. `competitors`.
3. Run it once (you get the latest items), then schedule it hourly or daily. Each later run returns only items published since the previous one, and you're only charged for those.
4. Send results to a spreadsheet, Slack, or a webhook with an Apify integration, or read them from the API.

Add **Keywords** (e.g. `pricing, launch, acquisition`) to get only the items that matter, or **Only items from the last N days** for a one-off digest.

## Cost

$0.80 per 1,000 items returned. A schedule that checks 20 blogs every hour and finds 30 new posts a day costs about $0.75 a month in item fees.
