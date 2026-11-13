---
title: Check SPF, DMARC and email provider for a list of domains
description: Audit email security across many domains, or segment leads by Google Workspace vs Microsoft 365, from public DNS records.
tool: domain-dns-ssl-lookup
---
Every domain publishes how it handles email in public DNS: which provider receives its mail (MX records), which servers may send for it (SPF) and what receivers should do with spoofed mail (DMARC). Reading those records for one domain is easy; for a few hundred it's tedious.

## Two common reasons to do this

**Security and deliverability audits.** Agencies, MSPs and IT teams check client domains for a missing DMARC record, a weak `p=none` policy, or an SPF record ending in `+all`. Since 2024 Gmail and Yahoo require SPF, DKIM and DMARC from bulk senders, so gaps here cost real deliverability.

**Sales segmentation.** If you sell a Microsoft 365 add-on, you want the companies that use Microsoft 365. The MX record tells you.

## What you get

The [Bulk DNS, SSL Certificate & Email Security Lookup](/tools/domain-dns-ssl-lookup/) returns one row per domain with:

| field | example |
| --- | --- |
| `emailProvider` | Google Workspace, Microsoft 365, Proofpoint, Zoho Mail... |
| `spf` / `spfAll` | the SPF record, and whether it ends in fail, softfail or neutral |
| `hasDmarc` / `dmarcPolicy` | true / reject, quarantine or none |
| `dnsProvider` | Cloudflare, Amazon Route 53, GoDaddy... |
| `verifications` | services the domain is verified with (google, facebook, apple...) |

## Steps

1. Paste your domains into the tool and run it (set `checkSsl` to `false` if you only need DNS).
2. Export to a spreadsheet and filter: `hasDmarc = false`, or `dmarcPolicy = none`, or `emailProvider = Microsoft 365`.

## What it doesn't do

It reads public DNS only. It doesn't look up who owns a domain, and it leaves out DMARC report addresses and other contact details on purpose.

Cost: $1.50 per 1,000 domains.
