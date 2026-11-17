---
title: How to use Dataset Works tools in Claude, ChatGPT and Cursor (MCP)
description: Connect all eight Dataset Works data tools to your AI assistant through the Model Context Protocol, so it can look up tenders, jobs, websites and domains for you.
---
Every Dataset Works tool can be called by an AI assistant through the **Model Context Protocol (MCP)**. You connect once, and then you can ask in plain English: "find open UK tenders for school catering this week", "what is Ramp hiring for?", or "check SPF and DMARC for these 30 domains". The assistant picks the right tool, runs it and reads the results.

The tools run on Apify, which hosts the MCP server and handles billing, so you pay per result and nothing else.

## The MCP server address

Use this URL to get all eight tools:

```
https://mcp.apify.com/?tools=datasetworks/public-tenders,datasetworks/company-jobs,datasetworks/web-to-text,datasetworks/website-tech-stack,datasetworks/domain-dns-ssl-lookup,datasetworks/website-seo-audit,datasetworks/shopify-store-products,datasetworks/news-trend-monitor
```

Or load just one, for example `https://mcp.apify.com/?tools=datasetworks/public-tenders`.

## Claude (claude.ai and Claude Desktop)

1. Open **Settings**, then **Connectors**, then **Add custom connector**.
2. Paste the URL above and give it a name, such as "Dataset Works".
3. Sign in to Apify when asked (a free account works).

## Cursor, VS Code and other MCP clients

Add this to your MCP configuration (for Cursor, `~/.cursor/mcp.json`), using an Apify API token from **Apify Console > Settings > API & Integrations**:

```json
{
  "mcpServers": {
    "dataset-works": {
      "url": "https://mcp.apify.com/?tools=datasetworks/public-tenders,datasetworks/company-jobs,datasetworks/web-to-text,datasetworks/website-tech-stack,datasetworks/domain-dns-ssl-lookup,datasetworks/website-seo-audit,datasetworks/shopify-store-products,datasetworks/news-trend-monitor",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

Clients that only support local servers can use `npx mcp-remote` with the same URL and header.

## ChatGPT

ChatGPT supports remote MCP servers as connectors in developer mode. Add a new connector with the URL above and sign in to Apify.

## What each tool answers

| Ask about | Tool |
| --- | --- |
| New EU and UK public tenders and contract awards | [public-tenders](/tools/public-tenders/) |
| Open jobs at a list of companies | [company-jobs](/tools/company-jobs/) |
| Clean Markdown text of any web page | [web-to-text](/tools/web-to-text/) |
| A website's tech stack and company profile | [website-tech-stack](/tools/website-tech-stack/) |
| DNS, SSL expiry, SPF and DMARC for domains | [domain-dns-ssl-lookup](/tools/domain-dns-ssl-lookup/) |
| SEO issues and broken links on a site | [website-seo-audit](/tools/website-seo-audit/) |
| Products and prices from Shopify stores | [shopify-store-products](/tools/shopify-store-products/) |
| News mentions and trends for a topic | [news-trend-monitor](/tools/news-trend-monitor/) |

## Tips for good results

- Ask for small result sets first ("the 10 newest"), then widen. Each tool has a max results setting the assistant can use.
- Every tool returns the same field names on every run, so you can ask the assistant to save results as a table or compare this week with last week.
- Failed lookups are free, and you can see every run and its cost in your Apify account.
