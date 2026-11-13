---
title: Track a Shopify competitor's products and prices
description: Export every product, variant, price and stock status from any public Shopify store, and spot new launches and discounts.
tool: shopify-store-products
---
Shopify stores publish their product catalogue in a standard format, which makes them easy to monitor: new products, price changes, discounts and items going out of stock.

## What you get

[Shopify Store Products](/tools/shopify-store-products/) returns one row per product with `title`, `vendor`, `productType`, `tags`, `priceMin`, `priceMax`, `compareAtPriceMax`, `onSale`, `available`, `variantCount`, `imageUrl`, `publishedAt`, `updatedAt`, and a `variants` list with SKU, price and availability.

## Steps

1. Enter store domains, e.g. `allbirds.com`.
2. Run and export to a spreadsheet.
3. Filter `onSale = true` for current discounts, or sort by `publishedAt` for the newest launches.

## Watch for changes

Schedule a daily run and compare datasets by `productId`: price differences, new IDs (launches) and `available` flipping to false (sell-outs). An AI agent can write the daily summary.

```
curl -X POST "https://api.apify.com/v2/acts/datasetworks~shopify-store-products/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" -d '{"stores": ["allbirds.com"], "maxProductsPerStore": 500}'
```

Stores that block automated access are skipped, not bypassed.

Cost: $0.80 per 1,000 products.
