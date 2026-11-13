---
title: How to check SSL certificate expiry for hundreds of domains at once
description: Find every SSL certificate that expires in the next 30 days across a list of domains, with issuer and days left, as a spreadsheet or JSON.
tool: domain-dns-ssl-lookup
---
An expired certificate takes a site offline for most visitors, and it usually happens to the domain nobody was watching: an old marketing site, a client's shop, a regional domain. Checking them one by one in a browser doesn't scale past a handful.

## What you get

For each domain, the [Bulk DNS, SSL Certificate & Email Security Lookup](/tools/domain-dns-ssl-lookup/) makes one normal TLS connection and returns:

- `sslValidTo` and `sslDaysLeft`: the expiry date and how many days remain
- `sslIssuer`: who issued it (Let's Encrypt, DigiCert, Google Trust Services...)
- `sslValid` and `sslError`: whether browsers would trust it, and why not
- `sslNames`: every hostname the certificate covers
- `tlsVersion`: e.g. TLSv1.3

## Steps

1. Open the tool on Apify and paste your domains into **Domains**, one per line. Full URLs work too.
2. Run it. A few hundred domains take about a minute.
3. Export as CSV or Excel and sort by `sslDaysLeft`. Anything under 30 needs attention; anything with `sslValid: false` is already a problem.

## Run it every day automatically

In Apify, add a **schedule** to the saved task (for example daily at 07:00). Connect the run to an email, Slack or webhook integration, or pull the results from the API into your own monitoring.

```
curl -X POST "https://api.apify.com/v2/acts/datasetworks~domain-dns-ssl-lookup/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"domains": ["example.com", "example.org"], "checkDns": false}'
```

Setting `checkDns` to `false` skips the DNS part when you only care about certificates.

## Cost

$1.50 per 1,000 domains. Checking 200 domains every day costs about $9 a month.
