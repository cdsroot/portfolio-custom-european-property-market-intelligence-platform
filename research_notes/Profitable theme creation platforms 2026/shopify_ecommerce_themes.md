# Economics of building and selling e-commerce platform themes (Shopify focus, other commerce platforms for comparison) — data as of 2026-11-24

Label key used on every figure: **[P]** primary source (platform's own docs, filings, live marketplace page), **[SR]** self-reported by a company or individual about itself, **[3P]** third-party estimate or tracker. Dates are the date of the data or publication. "Fetched 2026-11-24" means the live page was read on that day and carries no date of its own. Anything dated before 2024 is flagged **STALE**.

Access notes that apply throughout: several pages could not be fetched (listed in each Gaps section). The Shopify Theme Store `robots.txt` disallows filtered listing URLs (`/themes?*`); two such pages were read before this was noticed, and no further listing pages were crawled. Counts of distinct themes and developers therefore come from the Theme Store's public sitemaps, which are published for crawlers.

---

## 1. Shopify Theme Store: revenue share, prices, catalogue size, developers, review requirements, submission status, exclusivity

### Takeaway
The "0% on the first USD 1M, then 15%" structure no longer applies to themes: since 1 January 2025 Shopify takes 15% of all Theme Store theme revenue, calculated on gross sales, plus a 2.9% processing fee. On 2026-11-24 the store showed 1,395 listings (24 free, 1,371 paid) that resolve to about 362 distinct themes from 126 developer pages, priced USD 100 to 500, and Theme Store themes may not be sold on any other marketplace.

### Cited Findings

**Revenue share and fees**
- [P, fetched 2026-11-24] "total theme revenues are subject to a 15% revenue share." It applies to all themes listed on the Theme Store. — [shopify.dev revenue share for Theme Store developers](https://shopify.dev/docs/storefronts/themes/store/revenue-share)
- [P, fetched 2026-11-24] "Revenue share is calculated based on gross sales, not net sales." App Store and referral income is excluded from the theme calculation. — [shopify.dev revenue share](https://shopify.dev/docs/storefronts/themes/store/revenue-share)
- [P, fetched 2026-11-24] There are "no fees for submitting themes for listing." — [shopify.dev revenue share](https://shopify.dev/docs/storefronts/themes/store/revenue-share)
- [P, fetched 2026-11-24] "All billing is subject to a 2.9% processing fee and applicable sales tax." "As of August 1, 2021, fees and taxes are charged separately." Sales to merchants in some countries may also carry a Regulatory Operating Fee. — [shopify.dev revenue share](https://shopify.dev/docs/storefronts/themes/store/revenue-share)
- [P, fetched 2026-11-24] "You keep 85% of all revenue from themes sold through the Shopify Theme Store." No threshold is stated for themes. Shopify retains sole discretion over payout terms. — [Shopify Help Center, Partner earnings](https://help.shopify.com/en/partners/how-to-earn)
- [P, 2024-06-13] Shopify announced: "Starting January 1, 2025, a 15% revenue share will be applied to all earnings from your public themes." It described the 0% rate on earnings under USD 1M as a pandemic-era subsidy: "We're phasing out this subsidy but leaving the reduced revshare in place." The earlier rate had been cut from 30% to 15%. — [Shopify Partners blog, Theme Store updates](https://www.shopify.com/partners/blog/theme-store-updates)
- Conflict: a search-engine snippet attributed to the older URL `shopify.dev/themes/store/revenue-share` still showed the pre-2025 wording ("For the first $1,000,000 USD you make each year on theme sales ... you pay 0% revenue share"). The live page fetched on 2026-11-24 states a flat 15% on total theme revenues. The live page and the June 2024 announcement agree; the snippet is treated as an outdated cached copy. — [live page](https://shopify.dev/docs/storefronts/themes/store/revenue-share); [older URL](https://shopify.dev/themes/store/revenue-share)
- For contrast, the App Store still has a tier: 0% on the first USD 1,000,000 of lifetime gross app revenue and 15% above, for developers under the USD 20M annual threshold [P, as summarised by search from the App Store revenue share doc; page not fetched directly]. — [shopify.dev App Store revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share)

**Catalogue size and developers (fresh scan, 2026-11-24)**
- [P, live page 2026-11-24] The Theme Store listing page reads "1-24 of 1395 themes". Price filter counts: Free (24), Paid (1,371). — [themes.shopify.com/themes](https://themes.shopify.com/themes)
- [P, live page 2026-11-24] Other filter counts: catalogue size One Product (29), Few 2-10 (108), Some 11-100+ (926), Lots 500+ (332). Feature tags: Mega menu (1,345), Sticky header (1,376), Color swatches (1,355), Quick view (1,300), Stock counter (1,272), Quantity pricing (527), Quick order list (411). — [themes.shopify.com/themes](https://themes.shopify.com/themes)
- [P, sitemap lastmod 2026-11-23, counted 2026-11-24] The English theme sitemap contains 1,397 preset URLs of the form `/themes/{theme}/presets/{preset}`, covering 362 distinct theme slugs. Distribution: 36 themes with 1 preset, 23 with 2, 72 with 3, 56 with 4, 175 with 5. — [themes.shopify.com sitemap_theme_en.xml](https://themes.shopify.com/sitemap_theme_en.xml)
- [P, sitemap lastmod 2026-11-23, counted 2026-11-24] The English designer sitemap contains 126 distinct `/designers/{name}` pages, one of which is Shopify itself. — [themes.shopify.com sitemap_designer_en.xml](https://themes.shopify.com/sitemap_designer_en.xml)
- [P, live page 2026-11-24] Shopify's own designer page lists 24 themes, all free: Fabric, Savor, Vessel, Dwell, Tinker, Pitch, Atelier, Heritage, Ritual, Horizon, Rise, Trade, Spotlight, Publisher, Origin, Refresh, Colorblock, Ride, Studio, Taste, Sense, Crave, Craft, Dawn. — [themes.shopify.com/designers/shopify](https://themes.shopify.com/designers/shopify)
- [3P, counted 2026-11-03, published 2026-11-04] An independent count found 24 free themes and 1,335 paid listings, de-duplicated to 354 themes (24 free, 330 paid). The author notes each preset appears as a separate listing. — [vincentschmalbach.com](https://www.vincentschmalbach.com/are-shopify-themes-free/)
- Conflict: older third-party roundups give lower totals (268 themes with 23 free and 245 paid; 224 themes; 306 paid). These are undated in the search results and predate the July 2025 switch to per-preset listings. — [meetanshi.com](https://meetanshi.com/blog/shopify-themes-statistics/); [branvas.com](https://branvas.com/blogs/news/shopify-ecosystem-statistics)

**Prices**
- [P, live page 2026-11-24] The first 24 paid listings on the default sort ranged from USD 190 (Tenor) to USD 500 (Impulse). Other visible prices: Prestige 400, Impact 400, Focal 320, Broadcast 420, Symmetry 420, Palo Alto 420, Enterprise 420, Release 420, Concept 400, Hyper 400, Pebble 400, Wonder 390, Be Yours 380, Stiletto 380, Multiply 380, Omega 380, Ignite 380, Eurus 350, Sleek 350, Blaze 320, Crush 320, Coco 270. — [themes.shopify.com/themes](https://themes.shopify.com/themes)
- [P, live page 2026-11-24] With paid themes sorted low to high, all 24 listings on the first page were priced USD 100. — [themes.shopify.com/themes, paid filter](https://themes.shopify.com/themes?sort_by=price_low_to_high&price%5B%5D=paid)
- [3P, 2026-11-03] Cheapest paid theme USD 100, most expensive USD 500; paid themes are one-time purchases. — [vincentschmalbach.com](https://www.vincentschmalbach.com/are-shopify-themes-free/)

**Exclusivity (the "ThemeForest restriction")**
- [P, fetched 2026-11-24] "Themes listed on the Shopify Theme Store can only be distributed through the Shopify Theme Store." "Themes on the Theme Store must not be distributed on other marketplaces." The page does not name ThemeForest; the rule covers every other marketplace. Theme files may not contain designer credits or affiliate links. — [shopify.dev Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements)
- [SR, 2026-09-21] A theme partner on Shopify's developer forum states that themes must be sold exclusively through the Theme Store, which limited the partner's ability to diversify. — [community.shopify.dev thread, page 2](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670?page=2)

**Review and approval requirements**
- [P, fetched 2026-11-24] "Your theme must be fundamentally different from other themes on the Shopify Theme Store." Cosmetic changes (spacing, colour, typography, a few added settings or sections) do not count as differentiation. — [shopify.dev requirements](https://shopify.dev/docs/storefronts/themes/store/requirements)
- [P, fetched 2026-11-24] Shopify's Skeleton Theme is the only approved starting codebase. "New theme submissions built on or derived from Dawn or Horizon are not eligible." — [shopify.dev requirements](https://shopify.dev/docs/storefronts/themes/store/requirements)
- [P, fetched 2026-11-24] Minimum average Lighthouse performance score of 60 and accessibility score of 90 across home, product and collection pages, desktop and mobile. — [shopify.dev requirements](https://shopify.dev/docs/storefronts/themes/store/requirements)
- [P, fetched 2026-11-24] Required features include sections everywhere (Online Store 2.0), accelerated checkout buttons, faceted filtering, predictive search, selling plans, Shop Pay Installments, unit pricing, pickup availability, country and language selectors, gift card template, product recommendations, and Follow on Shop. — [shopify.dev requirements](https://shopify.dev/docs/storefronts/themes/store/requirements)
- [P, fetched 2026-11-24] Every preset needs at least one demo store matching its tagged industry and catalogue size; demo stores cannot use apps or placeholder text. — [shopify.dev requirements](https://shopify.dev/docs/storefronts/themes/store/requirements)
- [P, fetched 2026-11-24] Review has five stages: (1) features and Online Store 2.0 compatibility, (2) Lighthouse performance and accessibility, (3) technical requirements, (4) design and UX, (5) pre-launch checks. A theme must pass each stage to advance. — [shopify.dev submit a theme](https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme)
- [P, fetched 2026-11-24] "You can have only one theme submitted for review at a time." The limit does not apply to partners who already have a published theme. — [shopify.dev submit a theme](https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme)
- [P, fetched 2026-11-24] After a rejection a partner must make substantial changes and wait 30 days before resubmitting. Resubmitting without fixing the rejection reasons can lead to temporary suspension from submitting. — [shopify.dev submit a theme](https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme)
- [P, 2025-05-15] New requirements took effect 15 May 2025: a `/listings` folder in the zip, naming rules per preset, up to two industry tags from 20 categories and one catalogue-size tag from four per preset. Existing themes had to be resubmitted by 22 June 2025 to stay listed after the July 2025 redesign. Shopify warned of delays for submissions between 15 May and 1 July 2025. — [shopify.dev changelog](https://shopify.dev/changelog/updated-shopify-theme-store-requirements-and-submission-process-effective-may-15-2025)
- [P, 2024-06-13] Shopify announced theme licence checks (anti-piracy) for July 2024, and ratings and performance scores on theme cards. — [Shopify Partners blog](https://www.shopify.com/partners/blog/theme-store-updates)

**Submission status**
- [P, fetched 2026-11-24] The submission flow is documented as live: Partner Dashboard, Themes, "Submit a theme". No pause notice appears on the requirements, submission or overview pages. — [shopify.dev submit a theme](https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme); [shopify.dev Theme Store overview](https://shopify.dev/docs/storefronts/themes/store)
- [SR, 2026] Developer forum threads from February 2026 ("Delays with new theme version submission"), March 2026 (a submission server error) and October 2026 (whether Skeleton-based block-first themes qualify) show partners actively submitting during 2026. — [community.shopify.dev Theme Store category](https://community.shopify.dev/c/theme-store/34)

### Inferences
- Calculation, net proceeds per sale. Inputs: 15% revenue share on gross and 2.9% processing fee, both from the Shopify doc above. Assumption: the 2.9% fee is charged on the gross theme price. On a USD 400 theme: 400 − 60.00 − 11.60 = USD 328.40 (82.1% of list). On a USD 100 theme: USD 82.10. On a USD 500 theme: USD 410.50. Limitations: excludes sales tax, the Regulatory Operating Fee, refunds and currency conversion; the doc does not state the base on which 2.9% is applied.
- Calculation, distinct paid themes. Inputs: 362 distinct theme slugs in the sitemap and 24 free Shopify themes. 362 − 24 = 338 distinct paid themes. Limitation: assumes every free theme appears in the sitemap and every sitemap slug is live. The independent 2026-11-03 count gave 330 paid, a difference of 8.
- Calculation, third-party developers. Inputs: 126 designer pages minus Shopify = 125 developer brands. Limitation: brands are not owners. Tiny's WeCommerce owns several (Pixel Union, Out of the Sandbox, Archetype, Clean Canvas), so the number of independent companies is lower, and a designer page may exist for a brand with few or no live themes.
- Calculation, average paid themes per developer brand: 338 ÷ 125 ≈ 2.7. Same limitations as above.
- Calculation, listings per paid theme: 1,371 ÷ 338 ≈ 4.1 presets. This matches the sitemap distribution, where 175 of 362 themes have the maximum of 5 presets.
- Submissions appear to be open as of 2026-11-24: the documented flow is live and partners were submitting during 2026. This is an inference from the absence of a pause notice, not a Shopify statement.
- The entry bar is set by rule rather than by a published quota: one theme in review at a time for new partners, a 30-day lock after rejection, a mandatory original codebase, and a "fundamentally different" test.

### Gaps
- Acceptance or rejection rate: Shopify publishes none, and no third-party figure was found.
- Review turnaround time: the submission page gives no duration.
- Allowed price points: no pricing rule was found on the requirements, submission or revenue share pages. The observed range is USD 100 to 500.
- Partner registration fee: the theme docs say there is no fee to submit a theme. Whether any Partner account fee applies to theme partners was not stated on the pages fetched.
- Full price distribution (median, share of themes at each price): not collected, because the filtered listing URLs are disallowed by `robots.txt`.
- Themes per developer: not collected (would need 126 designer page fetches).
- Date on which the Skeleton-only rule was introduced: not found.
- Payout schedule for theme partners: not stated on the revenue share page.

---

## 2. Shopify partner ecosystem payouts and disclosed theme studio revenue and acquisitions

### Takeaway
Shopify reports paying more than USD 1.3 billion to ecosystem developers in 2025 but does not break out themes, and no theme studio publishes revenue. The only hard prices are WeCommerce's purchases of Archetype Themes (up to USD 32M, 2021) and Clean Canvas (USD 11.5M plus up to USD 1.2M, 2023), and their owner Tiny now describes the theme and app business as crowded and difficult.

### Cited Findings

**Shopify-published totals**
- [SR by Shopify, 2026-04-28] "Shopify paid out more than $1.3 billion" to ecosystem developers last year (2025). Over 21,000 apps are live; active app installs grew nearly 20% in a year. The article contains no theme figures. — [Shopify News, billion-dollar ecosystem](https://www.shopify.com/news/billion-dollar-ecosystem)
- [SR by Shopify, 2026-07-28] The partner ecosystem generated USD 6.86 for every dollar Shopify earned in 2025; 40,000 partners referred a new merchant in 2025; the ecosystem supported more than 1.5 million jobs. The article refers to the app ecosystem earning USD 1.3 billion and does not mention themes. Based partly on a survey of 2,501 partners. — [Shopify News, a world with more builders](https://www.shopify.com/news/a-world-with-more-builders)
- [P, FY2025 Form 10-K, as of 2025-12-31] "more than 21,000 apps were available in the Shopify App Store." Shopify recognises revenue from "the sale of themes" within subscription solutions on a net basis. No theme count, theme revenue or theme partner payout is disclosed. — [Shopify FY2025 10-K](https://s27.q4cdn.com/572064924/files/doc_financials/2025/q4/SHOP-Q4-2025-10K.pdf)
- [P, FY2025 results] Shopify's 2025 revenue was about USD 11.6 billion, up 30% (as summarised by search from Shopify's results). — [Shopify Q4 2025 results](https://www.shopify.com/news/shopify-q4-2025-financial-results)

**Acquisitions with disclosed prices**
- [P via press coverage, 2021-08-06, STALE] WeCommerce agreed to buy Archetype Themes for up to USD 32 million: USD 20 million cash at closing, described as about five times EBITDA, plus up to USD 12 million contingent. Archetype's themes were used by over 60,000 Shopify merchants, and its Impulse theme ranked first by popularity in the Theme Store. With Pixel Union and Out of the Sandbox, "WeCommerce-owned themes will comprise five of the top-seven most popular paid themes in the Shopify Theme Store." — [Techcouver](https://techcouver.com/2021/08/06/wecommerce-acquires-archetype-themes-shopify/); original release (HTTP 403 on fetch): [Business Wire](https://www.businesswire.com/news/home/20210806005134/en)
- [P via press release syndication, 2023-09-07, STALE] Tiny's WeCommerce completed the purchase of Clean Canvas (UK) for USD 11.5 million cash upfront plus an earn-out of up to USD 1.2 million tied to 18 months of performance. Clean Canvas themes had been used by over 80,000 Shopify merchants. The release said the Themes segment was "performing well both on top line growth and profitability." Read from search summaries; the syndicated page failed to load. — [FinancialContent syndication](https://markets.financialcontent.com/worldnow/article/bizwire-2023-9-7-tiny-completes-acquisition-of-clean-canvas); [Techcouver](https://techcouver.com/2023/09/11/tiny-wecommerce-clean-canvas-shopify-theme/)
- [3P, 2023-09-07, STALE] A deal database records the Clean Canvas total as USD 13M. — [Mergr](https://mergr.com/transaction/wecommerce-acquires-clean-canvas)

**Owner commentary on the theme business (Tiny Ltd, parent of WeCommerce)**
- [SR, shareholder letter dated 2026-06-08, covering 2025] "WeCommerce had a tougher year." "the third-party app and theme marketplace around Shopify is more crowded than it used to be. The number of competing apps and themes has grown meaningfully, merchants are scrutinizing software spend more closely, and the easy growth available in previous years is behind us." — [Tiny Ltd 2025 Annual Shareholder Letter (PDF)](https://s202.q4cdn.com/676416790/files/doc_financials/2025/sr/Tiny-Ltd-2025-Annual-Shareholder-Letter.pdf)
- [SR, 2026-06-08] "Some portfolio assumptions proved too optimistic. WeCommerce is the clearest example. Shopify remains attractive, but the third-party app and theme market became more crowded, more mature, and more competitive than we expected." "We expect this difficult environment to persist for this segment." — [Tiny Ltd 2025 Annual Shareholder Letter (PDF)](https://s202.q4cdn.com/676416790/files/doc_financials/2025/sr/Tiny-Ltd-2025-Annual-Shareholder-Letter.pdf)
- [P, 2026-03-30] Tiny's FY2025 release describes WeCommerce as "a collection of leading application and theme businesses," records a goodwill impairment in the Software and Apps segment, and reports total FY2025 asset impairment of 37.0 million (currency not confirmed in the fetched text). It lists "reliance on the Shopify platform" as a risk. No WeCommerce or theme revenue is given. — [Tiny Q4 and FY2025 results](https://investors.tiny.com/news/news-details/2026/Tiny-Reports-Q4-2025-and-Full-Year-2025-Results/default.aspx)
- [P, 2026-08-06, read from search summary only; page returned HTTP 503] Tiny's Q2 2026 release reports organic revenue down 4% year over year, "primarily reflecting revenue decline at WeCommerce and Digital Services," and an impairment of 80.7 million "as a result of a decline in recoverable asset value at WeCommerce and Creative Market." — [Tiny Q2 2026 results on Nasdaq](https://www.nasdaq.com/press-release/tiny-reports-q2-2026-results-2026-08-06)

**Self-reported studio and indie figures**
- [SR, undated, read from search summary only; page returned HTTP 403] An Indie Hackers post by a team selling mainly through the Theme Store says their themes made around USD 10k to 20k per month and that they are pivoting to a USD 25 per month model for a theme sold outside the marketplace. — [Indie Hackers](https://www.indiehackers.com/post/we-built-shopify-themes-to-20k-month-now-we-have-to-pivot-af4b47b772)
- [SR, 2026-09-20 and 2026-09-21] Theme partner "opal": "let go of 80% of our team in June"; for five straight months "revenue wasn't even enough to cover salaries and the rest of our costs"; the decline began around February to March 2026 and was clear by May. — [community.shopify.dev thread, page 2](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670?page=2)
- [SR, 2026-09] Theme partner Liam_Sarsfield reports laying off a team of 15. — [community.shopify.dev thread](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670)

### Inferences
- Calculation, Archetype EBITDA at acquisition. Inputs: USD 20M upfront described as about 5× EBITDA. 20 ÷ 5 ≈ USD 4M EBITDA. Limitations: "approximately" in the source, the EBITDA period is not defined, and the figure is from 2021.
- Shopify's USD 1.3 billion figure is labelled as developer or app-ecosystem payout in both Shopify articles. It cannot be read as a theme figure, and no split is available.
- Tiny's commentary and the forum posts point the same way for 2025 to 2026 (falling theme income, more competition). Tiny attributes it to crowding and merchant budgets; forum partners attribute it to reduced Theme Store discovery. Neither is quantified at theme level.

### Gaps
- Revenue of Out of the Sandbox, Pixel Union, Maestrooo, Fuel Themes, Archetype (post-2021) and Clean Canvas (any year): no disclosed figures found.
- Purchase prices for Out of the Sandbox and Pixel Union: not found. A tiny.com company page gives an ownership history that conflicts with press releases and cites no price.
- Any acquisition of Maestrooo or Fuel Themes: none found.
- WeCommerce or Tiny "Themes" segment revenue for 2024 to 2026: not in the releases fetched. Tiny's MD&A on SEDAR+ was not retrieved.
- Total paid by Shopify to theme partners specifically, in any year: not published.
- Number of theme partners above any income threshold: not published.

---

## 3. Demand side: live Shopify stores, Shopify Plus stores, free versus paid theme share, most-used paid themes

### Takeaway
Store Leads counted 3,353,136 live Shopify stores and 84,179 Shopify Plus domains on 2026-11-20, and nine of its ten most-used themes are free Shopify-made themes, with Horizon already on 296,422 stores. The best-ranked paid Theme Store themes (Prestige, Impulse, Impact) each hold roughly 2% to 4% of stores depending on the tracker, and no source publishes an overall free-versus-paid split.

### Cited Findings

**Store counts**
- [3P, updated 2026-11-20] 3,353,136 live Shopify stores. Quarterly series: 2025 Q1 2,527,881; Q2 2,587,750; Q3 2,692,227; Q4 2,859,828; 2026 Q1 2,804,211; Q2 2,867,778; Q3 3,108,808; Q4 to date 3,353,138. The page reports 15% year-over-year growth for 2026 Q3. — [Store Leads Shopify report](https://storeleads.app/reports/shopify)
- [3P, updated 2026-11-20] By country: United States 1,326,871 (39.6%), United Kingdom 252,057 (7.5%), Canada 152,560, Australia 145,112, India 131,150, France 120,985, Germany 107,097, Spain 73,010, Netherlands 69,437, Italy 63,033. — [Store Leads Shopify report](https://storeleads.app/reports/shopify)
- [3P, updated 2026-11-20] In the last 90 days 33,349 stores switched to Shopify and 23,338 switched away. — [Store Leads Shopify report](https://storeleads.app/reports/shopify)
- [3P, updated 2026-11-20] 84,179 Shopify Plus domains, representing approximately 56,119 distinct merchants. — [Store Leads Shopify Plus report](https://storeleads.app/reports/shopify/list-of-shopify-plus-stores)
- [P, as of 2025-12-31] Shopify's 10-K states "millions of merchants from more than 175 countries": 44% in the United States, 31% in EMEA, 16% in Asia Pacific, Australia and China, 5% in Canada, 5% in Latin America. No exact merchant count or Plus merchant count is disclosed. — [Shopify FY2025 10-K](https://s27.q4cdn.com/572064924/files/doc_financials/2025/q4/SHOP-Q4-2025-10K.pdf)
- [3P, dataset "3,500,000+" stores, updated 2026-11-24] ShopThemeDetector tracks more than 3.5 million live Shopify stores. — [ShopThemeDetector statistics](https://shopthemedetector.com/shopify-statistics/2026)

**Theme usage, all stores**
- [3P, 2026-11-20] Store Leads top themes by store count: trademark 470,894 (14.0%), horizon 296,422 (8.8%), dawn 279,296 (8.3%), savor 187,476, tinker 170,413, rise 129,288, debut 112,465, origin 81,946, spotlight 66,105, refresh 65,254. Store Leads tracks over 7,500 themes. — [Store Leads Shopify report](https://storeleads.app/reports/shopify)
- [3P, 2026-11-24] ShopThemeDetector top 20 by share: Dawn 15.1%, Horizon 8.5%, Prestige 4.3%, Impulse 3.9%, Shrine PRO 3.3%, Impact 2.3%, Minimog OS 2.0 2.1%, Ella 2.0%, Kalles 1.7%, Broadcast 1.6%, Symmetry 1.4%, Concept 1.3%, Refresh 1.3%, Sense 1.2%, Be Yours 1.1%, Focal 1.0%, Atelier 0.8%, Palo Alto 0.8%, Motion 0.8%, Debut 0.8%. — [ShopThemeDetector statistics](https://shopthemedetector.com/shopify-statistics/2026)
- Conflict: Store Leads puts Dawn at 8.3% and ranks "trademark" first at 14.0%; ShopThemeDetector puts Dawn at 15.1% and does not list trademark. The two trackers use different datasets and detection methods. — [Store Leads](https://storeleads.app/reports/shopify); [ShopThemeDetector](https://shopthemedetector.com/shopify-statistics/2026)

**Theme usage, Shopify Plus**
- [3P, 2026-11-20] Top themes on Shopify Plus domains: dawn 8,675 (10.3%), trademark 3,953 (4.7%), horizon 3,348 (4.0%), prestige 3,061, impulse 2,517, impact 2,476, rise 2,312, debut 2,301, refresh 1,454, focal 1,394. — [Store Leads Shopify Plus report](https://storeleads.app/reports/shopify/list-of-shopify-plus-stores)

**Paid themes outside the Theme Store (ThemeForest)**
- [P, live page 2026-11-24] ThemeForest's Shopify category advertises "over 2,800 Shopify themes and templates." Visible prices run from USD 19 to USD 99. Lifetime sales shown: Ella 48.2K at USD 79, Wokiee 27.5K at USD 59, Kalles 26.1K at USD 89, Minimog 16.9K at USD 88, Shella 14.1K at USD 39. — [ThemeForest Shopify category](https://themeforest.net/category/ecommerce/shopify)
- [SR, 2026-09-24] A forum poster citing ThemeForest data says the top three Shopify themes there sell about 20 to 30 copies each per week, against 70 to 90 per week in August 2025, with prices around USD 60, down from about USD 80. — [community.shopify.dev thread, page 2](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670?page=2)

**Installed-base claims by studios (all STALE)**
- [SR, 2021-08, STALE] Archetype: over 60,000 merchants. — [Techcouver](https://techcouver.com/2021/08/06/wecommerce-acquires-archetype-themes-shopify/)
- [SR, 2023-09, STALE] Clean Canvas: over 80,000 merchants. — [Techcouver](https://techcouver.com/2023/09/11/tiny-wecommerce-clean-canvas-shopify-theme/)

### Inferences
- Calculation, share of stores on current free Shopify themes within the Store Leads top ten. Inputs: horizon, dawn, savor, tinker, rise, origin, spotlight and refresh, all of which appear on Shopify's list of 24 free themes; denominator 3,353,136. Sum = 1,276,200 stores = 38.1%. Adding debut (112,465) gives 1,388,665 = 41.4%. Limitations: Debut is not among the 24 themes Shopify currently lists and its status was not verified in this research; the other 16 current free themes are not counted because their store counts were not shown; "trademark" (14.0%) is excluded because it is not on Shopify's designer page and its origin was not identified.
- Calculation, paid Theme Store themes in the Plus top ten. Inputs: prestige 3,061, impulse 2,517, impact 2,476, focal 1,394; denominator 84,179. Sum = 9,448 = 11.2% of Plus domains. Theme Store prices seen on 2026-11-24: Prestige USD 400, Impulse USD 500, Impact USD 400, Focal USD 320. Limitation: store counts are current installs, not sales, and a store may run a modified or unlicensed copy.
- Calculation, the same four paid themes are not in the Store Leads all-stores top ten; the tenth entry there has 65,254 stores (1.9%), so each of them is below 1.9% of all stores on Store Leads' measure. ShopThemeDetector's higher figures (Prestige 4.3%, Impulse 3.9%) conflict with that ceiling.
- Calculation, Shopify Plus share of live stores: 84,179 ÷ 3,353,136 = 2.5% of domains (Store Leads data, 2026-11-20). Limitation: domains, not merchants.
- Three of the top paid themes in ShopThemeDetector's list (Minimog, Ella, Kalles) are sold on ThemeForest rather than in the Theme Store, and Shrine PRO is not in the Theme Store listings seen. The paid-theme market outside the Theme Store is therefore material in installed-base terms, though it sells at USD 19 to 99 rather than USD 100 to 500.

### Gaps
- Overall share of stores on free versus paid versus custom themes: neither Store Leads nor ShopThemeDetector publishes it on the pages fetched.
- Identity of the "trademark" theme (14.0% on Store Leads): not established.
- Install or sales counts for individual Theme Store themes: Shopify publishes none; only tracker estimates of live stores exist.
- BuiltWith Shopify counts: the page redirected to a human-verification check and was not read. A secondary source cites about 6.9 million live Shopify websites on BuiltWith, unverified.
- W3Techs figures: not retrieved.
- Shopify Plus merchant count from Shopify: not disclosed. A search summary of the Q4 2025 earnings call says Plus was 34% of monthly recurring revenue; this was not verified against the transcript.

---

## 4. Impact of Shopify's own moves in 2024 to 2026 on third-party theme demand

### Takeaway
Documented facts: Shopify ended the 0% theme subsidy (January 2025), shipped Horizon and ten free themes with built-in AI (May 2025), extended Sidekick block generation to every Theme Store theme (December 2025), and added AI theme generation and theme edits (Winter '26). Horizon reached about 296,000 stores within 18 months, and theme partners report sharp revenue declines and layoffs in 2026, but Shopify has published no figures on third-party theme sales and no reply to those partners was found.

### Cited Findings

**Shopify's documented actions**
- [P, 2024-06-13] Revenue share on all theme earnings from 1 January 2025; anti-piracy licence checks from July 2024; ratings and performance scores on theme cards; more exposure promised for new themes. — [Shopify Partners blog](https://www.shopify.com/partners/blog/theme-store-updates)
- [P, 2025-05-23] Horizon is Shopify's new theme foundation, built on Theme Blocks, introduced with the Summer '25 Edition with 10 design presets. "This theme foundation has built-in AI that lets any store owner bring their brand to life." The same Edition included an "AI store builder". — [Shopify News, Summer '25 Edition design](https://www.shopify.com/news/summer-25-edition-design)
- [P, 2025-05-15 and 2025-07] New Theme Store requirements from 15 May 2025 and a redesigned Theme Store in July 2025 with a separate listing page for every preset. — [shopify.dev changelog](https://shopify.dev/changelog/updated-shopify-theme-store-requirements-and-submission-process-effective-may-15-2025)
- [P, 2025-12-10] "AI block generation for all Theme Store themes": Sidekick block generation now works with every Theme Store theme, not only Horizon. "Describe what you want in plain language, and Sidekick will code it for you on the spot." — [Shopify changelog](https://changelog.shopify.com/posts/ai-block-generation-for-all-theme-store-themes)
- [P, Winter '26 Edition, date not stated on page] "Over 250 Horizon theme improvements." "All Horizon themes support built-in volume pricing, quantity rules, and quick order lists." "Generate theme edits": "Tell Sidekick the specific design updates you want and watch it adjust your theme instantly." Theme generation from the mobile app. "AI will generate a custom store, even without a Shopify account." "Custom app generation" by Sidekick. "Improved theme discovery" in the Theme Store. "Vibe code with Lovable." — [Shopify Editions Winter '26](https://www.shopify.com/editions/winter2026)
- [P, fetched 2026-11-24] New Theme Store submissions derived from Dawn or Horizon are not eligible; Skeleton is the only approved base. — [shopify.dev requirements](https://shopify.dev/docs/storefronts/themes/store/requirements)
- [3P press, 2025] TechRadar reported that the AI store builder generates up to three personalised themes for free (as summarised by search; article not fetched). — [TechRadar](https://www.techradar.com/pro/shopify-just-dropped-150-updates-including-a-new-ai-store-theme-builder)

**Measured adoption of Shopify's own themes**
- [3P, 2026-11-20] Horizon is on 296,422 stores (8.8%), ahead of Dawn at 279,296 (8.3%). Horizon-family free themes Savor (187,476) and Tinker (170,413) rank fourth and fifth. — [Store Leads Shopify report](https://storeleads.app/reports/shopify)
- [3P, 2026-11-24] ShopThemeDetector puts Horizon at 8.5% of stores (8.3% elsewhere on the same page). — [ShopThemeDetector statistics](https://shopthemedetector.com/shopify-statistics/2026)
- [3P, 2026-11-20] On Shopify Plus domains Horizon is on 3,348 (4.0%). — [Store Leads Shopify Plus report](https://storeleads.app/reports/shopify/list-of-shopify-plus-stores)

**Partner-reported effects (all self-reported, Shopify developer forum, September to October 2026)**
- [SR, thread opened 2026-09-16] Since 27 August 2026 new merchants reportedly see a changed "Discover themes" area in admin: the "Explore more themes" card linking to the Theme Store was replaced by Dwell, a free Shopify theme, leaving a smaller "Visit Theme Store" button. — [community.shopify.dev thread](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670)
- [SR, secondhand, 2026-09] A partner reports that at Shopify's DotDev event a Shopify speaker said Theme Store traffic fell while conversion rose after the July 2025 redesign, and that part of the traffic drop was tied to removing the prompt to visit the Theme Store when a merchant installs a theme. This is a partner's account of staff remarks, not a Shopify publication. — [community.shopify.dev thread](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670)
- [SR, 2026-09] One partner cut 80% of the team in June 2026 after five months in which revenue did not cover costs; another laid off a team of 15; a third says sales no longer justify a full team and will ship only occasional fixes. — [thread](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670); [thread page 2](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670?page=2)
- [SR, 2026-10-04] The same partner predicts there will be no Theme Store in 8 to 12 months. This is a prediction by one partner, not a fact. — [thread page 2](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670?page=2)
- [P, 2026-09] No Shopify staff reply appears on either page of the thread read. — [thread](https://community.shopify.dev/t/theme-store-discovery-reduced-for-new-merchants/37670)

**Stated positions**
- [SR by Shopify, 2026-07-28] Shopify says it changed partner incentives to reward merchant success and that partners will soon be able to earn commission on sales driven through Shopify Catalog experiences. Themes are not mentioned. — [Shopify News](https://www.shopify.com/news/a-world-with-more-builders)
- [SR, 2026-06-08] Tiny, owner of four theme studios, attributes WeCommerce's weakness to a "more crowded, more mature, and more competitive" app and theme market and tighter merchant budgets, and expects the difficulty to persist. — [Tiny shareholder letter](https://s202.q4cdn.com/676416790/files/doc_financials/2025/sr/Tiny-Ltd-2025-Annual-Shareholder-Letter.pdf)
- [P, FY2025 10-K] Shopify's risk factors say the platform's success depends in part on third-party apps and themes remaining available and compatible. — [Shopify FY2025 10-K](https://s27.q4cdn.com/572064924/files/doc_financials/2025/q4/SHOP-Q4-2025-10K.pdf)

### Inferences
- Timeline, assembled from the sources above: June 2024 subsidy removal announced; January 2025 15% on all theme revenue; May 2025 Horizon, AI blocks and new submission rules; July 2025 store redesign with per-preset listings; December 2025 AI block generation on all themes; Winter '26 AI theme generation and Sidekick theme edits; August 2026 partner-reported reduction of the Theme Store link in admin.
- Horizon overtook Dawn on Store Leads within about 18 months of launch (May 2025 to November 2026). Together with Savor and Tinker, the three Horizon-family themes named in the top five total 654,311 stores, or 19.5% of live stores (calculation from Store Leads counts; limitation: other Horizon-family presets are not counted).
- AI block generation works on third-party Theme Store themes too, so it is not exclusive to Shopify's free themes. Its effect on paid theme purchases is not measured anywhere found.
- The partner accounts of decline are consistent with each other and with Tiny's disclosures, but they come from a small number of forum posters and one corporate owner. They do not establish market-wide theme revenue.

### Gaps
- Any Shopify-published figure on third-party theme sales, Theme Store traffic or conversion: none found. The traffic and conversion statement exists only as a partner's secondhand account.
- An official Shopify statement on the future of the Theme Store or on the August 2026 admin change: none found.
- Hydrogen and headless adoption: no reliable count found. Store Leads returned only a New Zealand figure (26 stores) and StoreCensus showed zero, which conflicts with other sources. Hydrogen did not appear in the portion of the Winter '26 page that was read (the final part of that page was not read).
- Summer '26 Edition theme items: only a third-party blog summary surfaced; Shopify's own page was not fetched.
- The exact date of the Winter '26 Edition: not stated on the page.

---

## 5. Comparison platforms: marketplace terms, prices and catalogue size

### Takeaway
Published developer shares range from 85% (Shopify Theme Store, Adobe Commerce Marketplace) through 70% (WooCommerce Marketplace) to 50% (Envato ThemeForest from July 2026); Hyvä's Magento theme became free in November 2025 and monetises through add-ons. BigCommerce, PrestaShop, Shopware and OpenCart do not publish a theme commission rate on the pages that could be reached, and no third-party theme marketplace terms were found for Salesforce Commerce or Squarespace.

### Cited Findings

| Platform or marketplace | Developer share or commission | Price range seen | Catalogue size | Label and date |
|---|---|---|---|---|
| Shopify Theme Store | Developer keeps 85%; 2.9% processing fee; exclusive | USD 100 to 500 one-time | 1,371 paid listings, about 338 paid themes | [P] 2026-11-24 |
| ThemeForest (Shopify category) | Flat 50% author fee from 2026-07-01 | USD 19 to 99 | "over 2,800" | fee [3P] 2026-07-02; rest [P] 2026-11-24 |
| WooCommerce Marketplace | 70% to vendor | not retrieved | not retrieved | [P] fetched 2026-11-24, undated page |
| Adobe Commerce Marketplace | 85% to provider, 15% to Adobe | not retrieved | not retrieved | [P] fetched 2026-11-24 |
| Hyvä (Magento) | Not a marketplace; theme free, add-ons paid | EUR 0 theme; EUR 250 to 7,500 add-ons | "7,000+" stores | [SR] 2026-06-01 and 2026-11-24 |
| Shopware Store | Commission exists, rate not published | from EUR 39.00 per month rental | 149 themes | [P] 2026-11-24 |
| PrestaShop Addons | Not confirmed; annual fee per addon | not retrieved | not retrieved | see below |
| BigCommerce Theme Marketplace | Not found | USD 145 to 235 (undated release) | "220+" incl. 15 free | [3P], undated |
| Wix Studio templates | 100% to partner until 2025-06-30; later rate not stated | not stated | not stated | [P] fetched 2026-11-24 |
| OpenCart | Official terms not found | not found | not found | gap |
| Salesforce Commerce | Nothing found | n/a | n/a | gap |
| Squarespace | Nothing official found | n/a | n/a | gap |

- [P, 2026-11-24] Shopify Theme Store row: see section 1. — [shopify.dev revenue share](https://shopify.dev/docs/storefronts/themes/store/revenue-share)
- [P, live page 2026-11-24] ThemeForest Shopify category: "over 2,800 Shopify themes and templates", prices USD 19 to 99. — [ThemeForest](https://themeforest.net/category/ecommerce/shopify)
- [3P, published 2026-07-02] Envato moved all authors to a "flat 50% author fee" from 1 July 2026 and ended the exclusive author model. The article links to Envato's Author Hub announcement, which was not read directly; Envato's Author Terms page returned HTTP 403. — [Purethemes](https://purethemes.net/envato-author-exclusivity-merchant-of-record/); [Envato Author Hub announcement (not fetched)](https://author.envato.com/hub/changes-to-envato-market-revenue-share-and-exclusivity-what-you-need-to-know/)
- [P, pre-July 2026 structure, as summarised by search from Envato help pages] Before the change non-exclusive authors paid a 55% author fee and exclusive authors 12.5% to 37.5%. — [Envato historical payment rates](https://help.author.envato.com/hc/en-us/articles/360000618863-Historical-Payment-Rates)
- [P, fetched 2026-11-24, page undated] WooCommerce Marketplace: "The commercial terms are based on a revenue share model, with 70% of sales going to the vendor." Themes are in scope ("Build and thoroughly test your extension or theme"). Process: apply for a partner account, submit after approval, review for functionality, security, compatibility and UX. No fees are listed and exclusivity is not mentioned. — [WooCommerce developer docs](https://developer.woocommerce.com/docs/woo-marketplace/getting-started/)
- [3P, undated] Earlier WooCommerce structures were 60% for exclusive and 40% for non-exclusive vendors, and before that 50%. These are described as superseded. — [Business Bloomer](https://www.businessbloomer.com/would-i-launch-on-the-woocommerce-marketplace-today/); [Post Status](https://poststatus.com/woocommerce-offering-20-higher-rates-trade-third-party-developers-offering-support/)
- [P, fetched 2026-11-24] Adobe Commerce Marketplace: all sales are "subject to a 85/15 revenue share split", 85% to the provider. Payout through PayPal, less any US tax withholding. The page does not mention themes specifically. — [Adobe Commerce Marketplace revenue share](https://developer.adobe.com/commerce/marketplace/guides/sellers/revenue-share)
- [SR, fetched 2026-11-24] Hyvä Theme is "Now entirely Open Source and Free", under OSL and AFL licences, on GitHub and via free licence keys (up to 5 per account, 50 per agency partner group). — [hyva.io licence page](https://www.hyva.io/hyva-theme-license.html)
- [3P, as summarised by search] The date Hyvä Theme became open source is given as 10 November 2025. — [Plumrocket](https://plumrocket.com/blog/magento-hyva-theme-news)
- [SR, published 2026-06-01] Hyvä pricing from 1 July 2026: Hyvä Enterprise EUR 7,500 for the first year and EUR 5,000 per year from year two, per Adobe Commerce instance (five years upfront EUR 27,500); Hyvä Commerce EUR 3,000 per year; Hyvä Checkout EUR 1,000 one-time for five years of updates or EUR 250 per year; Hyvä UI EUR 250; Hyvä Theme free. — [hyva.io blog](https://www.hyva.io/blog/news/new-hyva-enterprise-all-inclusive.html)
- [SR, fetched 2026-11-24] Hyvä adoption: the site navigation says "Trusted by 7,000+ Online Stores" while the logo section of the same page says "Trusted by 6,000+ merchants". The two figures conflict and neither is dated. — [hyva.io licence page](https://www.hyva.io/hyva-theme-license.html)
- [3P, 2026-09, as summarised by search] A scandiweb study reports Hyvä stores passing all three Core Web Vitals on mobile 66.4% of the time against 44.6% for Magento overall. — [scandiweb](https://scandiweb.com/blog/?p=26883)
- [P, fetched 2026-11-24] Shopware: extension partners "receive a commission on the sales of your extensions in the Shopware Store", paid automatically "on the 15th of the following month". No percentage is published on the page. — [Shopware docs, commissions](https://docs.shopware.com/en/account-en/extension-partner/commissions)
- [P, live page 2026-11-24] Shopware Store themes category shows 149 extensions; visible premium themes rent "from €39.00* /month" (ThemeWare Modern Pro by TC-Innovations, Horizon Pro and Atmos Pro by Zenit Design). — [Shopware Store themes](https://store.shopware.com/en/themes/)
- [P, as summarised by search; page returned HTTP 403 on fetch] PrestaShop: each addon (module or theme) carries its own annual fee, requested before a new addon is submitted for validation; "the revenue share model remains unchanged". The fee amount and the percentage were not visible. — [PrestaShop partner help centre](https://helpcenter-partners.prestashop.com/hc/en-us/articles/18768854603410-Paying-the-annual-fee)
- [P, as summarised by search] PrestaShop applies extended quality checks to submitted modules and themes since 29 April 2024. — [PrestaShop validation process](https://helpcenter-partners.prestashop.com/hc/en-us/articles/18497178944914-Validation-Process-for-your-addons)
- [SR forum post, undated, unverified, likely STALE] A PrestaShop forum thread describes a 70/30 split for Addons purchases and 50/50 for purchases made through the back-office catalogue. It does not say whether themes are covered. — [PrestaShop forums](https://www.prestashop.com/forums/topic/347269-new-contributor-terms-confusion-with-commission)
- [P, last reviewed 2026-09-08] BigCommerce: the marketplace has "free and premium" themes, all on the Stencil platform. BigCommerce supports Cornerstone plus Capacity, Fortune, Merchant and Peak; other themes are supported by their creators. No price range or count is given. — [BigCommerce support](https://support.bigcommerce.com/articles/en_US/Knowledge/The-Bigcommerce-Themes-Marketplace)
- [3P, undated, as summarised by search] BigCommerce theme counts and prices: 220+ themes including 15 free (WebsitePlanet); an undated BigCommerce release priced new themes at USD 145 to 235; one review cites USD 300 for a single theme. — [WebsitePlanet](https://www.websiteplanet.com/blog/best-bigcommerce-templates); [BigCommerce press release](https://bigcommerce.com/press/releases/bigcommerce-announces-new-modern-themes-designed-to-drive-sales-for-retailers)
- [P, as summarised by search] BigCommerce's parent Commerce applies a 20% revenue share to public apps. This is an app term; no theme term was found. — [Commerce partner agreement change summary](https://www.commerce.com/partner-agreement/change-summary/)
- [P, fetched 2026-11-24] Wix Studio template marketplace: "No fees offer is valid until June 30, 2025" (the FAQ on the same page says "In 2024 we won't charge any fees"). Payouts need at least USD 200 in earnings on a net-60 cycle. Wix aims to review submissions within 60 business days. Partners may sell the same templates elsewhere. No commission rate after the offer is stated. — [Wix Studio submit and sell](https://www.wix.com/studio/partner-program/submit-and-sell)
- [3P, undated, as summarised by search] TemplateMonster pays authors 50% to 65% on exclusive OpenCart and Shopify templates and 40% on non-exclusive ones. This is a third-party marketplace, not OpenCart's own. — [TemplateMonster helpdesk](https://helpdesk.templatemonster.com/?p=575)

### Inferences
- On published terms alone, Shopify's Theme Store pairs the highest developer share (85%) with the highest unit prices (USD 100 to 500), but it is the only one of these channels with a documented exclusivity rule. ThemeForest pays 50% on USD 19 to 99 items and no longer requires exclusivity.
- Calculation, developer proceeds per unit at list price, before taxes and payment fees. Shopify Theme Store USD 400 theme: USD 340 at 85% (USD 328.40 after the 2.9% fee, see section 1). ThemeForest USD 79 theme: USD 39.50 at 50%. Limitations: ignores Envato buyer fees and tax handling, which were not verified, and assumes the 50% applies to the full list price.
- Hyvä's switch to a free theme means there is no longer a licence-resale or theme-sale market for the base Magento storefront theme; paid work in that ecosystem is implementation and add-ons.
- Shopware's premium themes are rented monthly (from EUR 39), which is a recurring model, unlike Shopify's one-time theme purchase.

### Gaps
- BigCommerce theme partner revenue share, submission terms, live count and live prices: the Theme Store page returned no listings to the fetch tool and no partner terms were found.
- PrestaShop commission percentage and annual fee amount: the help centre returned HTTP 403, the Addons theme catalogue returned HTTP 403, and `growth.prestashop.com` (Premium Seller page) did not resolve from this session and would need to be allowed in the session's network settings.
- Shopware commission percentage: not on the public docs page; it is in the partner agreement inside the Shopware Account.
- WooCommerce Marketplace theme count and prices: the themes category page returned only navigation to the fetch tool.
- OpenCart official marketplace commission: not found.
- Salesforce Commerce Cloud: no theme marketplace or terms found.
- Squarespace: no official third-party template marketplace terms found. A search summary mentioned third-party template shops charging USD 80 to 1,000, unverified.
- Hyvä's previous licence price and number of licences sold before November 2025: not verified in this research.
- Envato's own wording of the July 2026 change and current buyer fee: not read directly.
- Wix's commission after 30 June 2025: not stated on the page.

---

## 6. Custom theme build work: published price ranges

### Takeaway
Clutch's September 2026 guide puts Shopify development at USD 25 to 49 per hour, the same band as Magento, WooCommerce and BigCommerce, with most reviewed e-commerce projects under USD 10,000. Shopify Partner Directory listings show self-declared starting prices from USD 50 to about USD 4,000 for theme and store design work, and agency blogs quote USD 2,500 to 20,000 or more for a custom theme, without a consistent definition of scope.

### Cited Findings
- [3P, updated 2026-09-21] Clutch lists the average hourly cost for Shopify development at USD 25 to 49, identical to Adobe Commerce/Magento, WooCommerce and BigCommerce. The guide-wide average e-commerce project cost is USD 51,943.13, while the page also says most reviewed projects cost less than USD 10,000. Figures are "Based on reviews on Clutch"; no sample size is given. — [Clutch e-commerce development pricing](https://clutch.co/developers/ecommerce/pricing)
- [3P, 2026, as summarised by search] Clutch's Shopify page says the average cost of Shopify development projects reviewed typically sits below USD 10,000. — [Clutch Shopify developers](https://clutch.co/developers/shopify.md)
- [SR by agency, read from search results 2026-11-24] Shopify Partner Directory listings: BrightPearl Commerce lists custom store design at USD 4,000 and theme-based setup at USD 2,500. — [Shopify Partner Directory, BrightPearl Commerce](https://www.shopify.com/partners/directory/partner/brightpearlcommerce)
- [SR by agency, 2026-11-24] NomadsArc: starting at USD 3,000. — [Shopify Partner Directory, NomadsArc](https://www.shopify.com/partners/directory/partner/nomadsarc)
- [SR by agency, 2026-11-24] Niva Commerce: USD 2,000 to 8,000 for theme-based design, custom development, redesign or migration. — [Shopify Partner Directory, Niva Commerce](https://www.shopify.com/partners/directory/partner/nivacommerce)
- [SR by agency, 2026-11-24] Supportcenter: starting at USD 1,000 for a build including a theme and speed optimisation. — [Shopify Partner Directory, Supportcenter](https://www.shopify.com/partners/directory/partner/supportcenter)
- [SR by agency, 2026-11-24] Cartmade Commerce: starting at USD 500 for Liquid template customisation. — [Shopify Partner Directory, Cartmade Commerce](https://www.shopify.com/partners/directory/partner/cartmade-commerce)
- [SR by agency, 2026-11-24] Devmont Digital: starting at USD 100. Brisk Developers: starting at USD 50. — [Devmont Digital](https://www.shopify.com/partners/directory/partner/devmont-digital); [Brisk Developers](https://www.shopify.com/partners/directory/partner/brisk-developers)
- [3P, 2026] A freelance rate guide titles its range "Cost to Hire Freelance Shopify Developer: $49-$127/hr - 2026". — [Second Talent](https://www.secondtalent.com/cost-to-hire/shopify-developer/)
- [3P, 2026, as summarised by search] Lemon.io's benchmark: mid-level Shopify developer USD 27.50 per hour, senior USD 37.20 per hour. — [Lemon.io rate calculator](https://lemon.io/rate-calculator/shopify-developers/)
- [SR by agencies, 2026, as summarised by search; the individual figure-to-page mapping was not verified] Agency blog ranges for a custom Shopify theme: USD 5,000 to 20,000+; USD 3,000 to 15,000+; USD 2,500 to 10,000+. Small tweaks of 1 to 5 hours: USD 150 to 700. One guide spans USD 5,000 for a focused theme change to USD 250,000 for a full Shopify Plus migration with custom apps. Candidate sources: — [Black Belt Commerce](https://www.blackbeltcommerce.com/shopify-custom-development-cost/); [GetDevDone](https://getdevdone.com/blog/?p=12956); [OuterBox](https://www.outerboxdesign.com/web-design-articles/shopify-website-design-pricing); [CartCoders](https://cartcoders.com/blog/shopify-development/shopify-developer-cost-hourly-project-retainer/)
- [SR by agency, 2026, as summarised by search] CartCoders says a basic theme customisation can cost up to USD 500 and large enterprise Shopify projects over USD 120,000. — [CartCoders](https://cartcoders.com/blog/shopify-development/shopify-developer-cost-hourly-rate-project-pricing/)

### Inferences
- Clutch reports the same USD 25 to 49 hourly band for all four platforms, so its data does not show a rate premium for any one platform's theme work.
- Calculation, sales needed to match one custom build. Input: USD 328.40 net per USD 400 Theme Store sale (section 1). A USD 4,000 custom build equals about 12 theme sales; a USD 10,000 build equals about 30. Limitations: ignores the unpaid build, review and support time of a Theme Store theme and compares gross service revenue with net product revenue.
- Partner Directory "starting at" prices are entry points chosen by each agency for different scopes. The USD 50 to 100 entries describe small edits, not a full custom theme, so the spread should not be read as a market range for one deliverable.

### Gaps
- Shopify does not publish aggregate pricing statistics for its Partner Directory; only individual listings exist. The listings above were read from search results rather than fetched one by one.
- No Clutch figure specific to Shopify theme builds (as opposed to Shopify development generally), and no Clutch sample size.
- No Clutch minimum project size for Shopify work was found.
- Agency blog ranges are marketing content with undisclosed methods; which blog states which range was not individually verified.
- No published data on how custom theme build prices changed after Horizon and AI theme generation.
