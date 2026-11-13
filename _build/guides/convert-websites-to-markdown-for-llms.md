---
title: Convert web pages to clean Markdown for LLMs and RAG
description: Turn any list of URLs or a whole site section into clean Markdown text, without menus, ads and cookie banners, ready for an LLM or vector database.
tool: web-to-text
---
Feeding raw HTML to a language model wastes tokens on navigation, scripts and footers, and makes answers worse. What you want is the main text of the page, with headings, lists, tables and links kept.

## What you get

[Web to Text](/tools/web-to-text/) fetches each page and returns `markdown` (the main content), `title`, `description`, `language`, `wordCount` and, if you ask, the page's `links`. It can also follow links within a site to a set depth, so you can grab a whole docs section in one run.

## Steps

1. Add start URLs, e.g. a documentation homepage or a list of articles.
2. Set how deep to follow links (0 = only the pages you listed).
3. Run, then export JSON or pull it from the API straight into your chunking and embedding step.

```
curl -X POST "https://api.apify.com/v2/acts/datasetworks~web-to-text/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"startUrls": [{"url": "https://en.wikipedia.org/wiki/Web_scraping"}]}'
```

## Use it from an AI agent

The tool is available through Apify's MCP server, so an agent in Claude, Cursor or any MCP client can call it to read a page when it needs fresh information.

## Responsible by default

It identifies itself honestly and follows each site's robots.txt, so pages a site has asked crawlers to avoid are skipped and not charged.

Cost: $1 per 1,000 pages.
