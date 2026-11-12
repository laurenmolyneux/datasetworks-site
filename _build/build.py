#!/usr/bin/env python3
"""Builds the static datasetworks.dev site from tools.json + live Apify actor metadata.
Usage: APIFY_TOKEN=... python3 build.py OUT_DIR   (needs `pip install markdown`)"""
import json, os, sys, shutil, html, urllib.request, datetime, re
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
DW = os.path.dirname(ROOT)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dist")
SITE = "https://datasetworks.dev"
AFFILIATE = ""  # e.g. "?fpr=abc123" once Lauren's Apify affiliate code exists
H = {"Authorization": "Bearer " + os.environ["APIFY_TOKEN"]}

def api(path):
    return json.load(urllib.request.urlopen(urllib.request.Request("https://api.apify.com/v2" + path, headers=H), timeout=60))["data"]

def price_text(info):
    if not info: return "Free"
    ev = info[-1].get("pricingPerEvent", {}).get("actorChargeEvents", {})
    parts = []
    for e in ev.values():
        p = e.get("eventPriceUsd")
        if p is None: continue
        parts.append(f"${p*1000:,.2f} per 1,000 {e['eventTitle'].lower().replace(' returned','').replace(' analysed','').replace(' converted','')}s" if p < 0.005 else f"${p:.2f} per {e['eventTitle'].lower()}")
    return " + ".join(parts) or "Pay per result"

CSS = """
:root{--navy:#12263F;--teal:#2DD4BF;--teal-d:#0D9488;--bg:#fff;--fg:#1f2937;--muted:#6b7280;--card:#f8fafc;--line:#e5e7eb}
@media (prefers-color-scheme:dark){:root{--bg:#0b1626;--fg:#e5e7eb;--muted:#9ca3af;--card:#12263F;--line:#1f3a5c;--teal-d:#2DD4BF}}
*{box-sizing:border-box}body{margin:0;font:16px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--fg)}
a{color:var(--teal-d)}header,main,footer{max-width:960px;margin:0 auto;padding:16px}
header{display:flex;align-items:center;gap:12px}header img{width:40px;height:40px}header a.brand{font-weight:700;font-size:20px;color:var(--fg);text-decoration:none}
.hero{padding:40px 0 8px}.hero h1{font-size:clamp(28px,5vw,44px);line-height:1.15;margin:0 0 12px}.hero p{color:var(--muted);font-size:18px;max-width:680px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin:24px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px;display:flex;flex-direction:column}
.card h2{font-size:18px;margin:0 0 8px}.card h2 a{color:var(--fg);text-decoration:none}.card p{color:var(--muted);margin:0 0 12px;flex:1}
.price{font-size:14px;font-weight:600;color:var(--teal-d)}.btn{display:inline-block;background:var(--teal-d);color:#fff;padding:10px 16px;border-radius:8px;text-decoration:none;font-weight:600}
.btn:hover{opacity:.9}article{max-width:780px}article table{border-collapse:collapse;display:block;overflow-x:auto;font-size:14px}
article th,article td{border:1px solid var(--line);padding:6px 10px;text-align:left}article code{background:var(--card);padding:1px 5px;border-radius:4px;font-size:90%}
article pre{background:var(--card);padding:12px;overflow-x:auto;border-radius:8px}.points{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin:32px 0}
.points div{border-left:3px solid var(--teal);padding-left:12px}footer{color:var(--muted);font-size:14px;border-top:1px solid var(--line);margin-top:48px}
"""

def page(title, desc, body, path):
    canon = SITE + path
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:site_name" content="Dataset Works">
<meta property="og:image" content="{SITE}/logo-icon-512.png"><link rel="icon" href="/logo-icon.svg"><link rel="stylesheet" href="/style.css"></head><body>
<header><img src="/logo-icon.svg" alt=""><a class="brand" href="/">Dataset Works</a></header>
<main>{body}</main>
<footer><p>Dataset Works builds data tools that do one job well, from public business data only. Tools run on the <a href="https://apify.com{AFFILIATE}" rel="sponsored">Apify</a> platform, which handles accounts and billing. Questions or bugs: open an issue on the tool's Apify page.</p><p>© {datetime.date.today().year} Dataset Works</p></footer>
</body></html>"""

def main():
    tools = json.load(open(os.path.join(DW, "tools.json")))
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    for f in ("logo-icon.svg", "logo-icon-512.png"): shutil.copy(os.path.join(DW, f), OUT)
    open(os.path.join(OUT, "style.css"), "w").write(CSS)
    open(os.path.join(OUT, "CNAME"), "w").write("datasetworks.dev\n")
    cards, urls = [], ["/"]
    for t in tools:
        a = api(f"/acts/{t['id']}")
        if not a.get("isPublic"): continue
        store = f"https://apify.com/datasetworks/{a['name']}{AFFILIATE}"
        price = price_text(a.get("pricingInfos"))
        readme = ""
        try:
            b = api(f"/acts/{t['id']}/versions")["items"]
            v = b[-1] if b else None
            files = (v or {}).get("sourceFiles") or []
            readme = next((f.get("content", "") for f in files if f.get("name") == "README.md"), "")
        except Exception: pass
        if not readme:
            local = os.path.join(DW, "actors", f"{a['name']}-v1", "README.md")
            if os.path.exists(local): readme = open(local).read()
        readme = re.sub(r"^# .*\n", "", readme, count=1)
        body_md = markdown.markdown(readme, extensions=["tables", "fenced_code"])
        path = f"/tools/{a['name']}/"
        body = f"""<section class="hero"><h1>{html.escape(a['title'])}</h1><p>{html.escape(a.get('description',''))}</p>
<p><a class="btn" href="{store}" rel="sponsored">Try it on Apify</a> <span class="price">{html.escape(price)}</span></p></section>
<article>{body_md}</article><p><a class="btn" href="{store}" rel="sponsored">Open {html.escape(a['title'])} on Apify</a></p>"""
        os.makedirs(OUT + path, exist_ok=True)
        open(OUT + path + "index.html", "w").write(page(f"{a['title']} | Dataset Works", a.get("description", "")[:160], body, path))
        urls.append(path)
        cards.append(f"""<div class="card"><h2><a href="{path}">{html.escape(a['title'])}</a></h2><p>{html.escape(a.get('description',''))}</p>
<div class="price">{html.escape(price)}</div><p style="margin-top:12px"><a class="btn" href="{path}">Details</a></p></div>""")
    home = f"""<section class="hero"><h1>Clean data tools for spreadsheets, apps and AI agents</h1>
<p>Each tool does one job well: jobs from company career boards, website tech stacks, news trends, product catalogs, clean web text. Same fields every run, pay only for results, callable from the Apify API or MCP.</p></section>
<div class="points"><div><b>Pay per result</b><br>No subscription. Failed lookups are free.</div><div><b>Built for AI agents</b><br>Fixed output fields, works through API and MCP.</div>
<div><b>Maintained daily</b><br>Automated checks every day; broken tools are fixed fast.</div><div><b>Responsible</b><br>Public business data only. No personal data, no bypassing logins or blocks.</div></div>
<div class="grid">{''.join(cards)}</div>"""
    open(os.path.join(OUT, "index.html"), "w").write(page("Dataset Works: clean data tools for AI agents and spreadsheets", "Pay-per-result data tools for jobs, website tech stacks, news trends, Shopify products and web-to-markdown. Public business data, built for AI agents.", home, "/"))
    today = datetime.date.today().isoformat()
    open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>" for u in urls) + "</urlset>\n")
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print(f"Built {len(urls)} pages into {OUT}")

main()
