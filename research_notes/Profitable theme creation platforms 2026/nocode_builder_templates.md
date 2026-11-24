# Economics of creating and selling templates on hosted website-builder / no-code platforms (as of 2026-11-24)

**How to read these notes**

- Evidence labels: **[P]** = primary source (platform's own page, filing, press release); **[SR]** = self-reported by a creator/company, unaudited; **[3P]** = third-party estimate or secondary reporting; **[SCAN]** = my own scan of the live marketplace page or sitemap, retrieved 2026-11-24 (method below).
- "(snippet)" = the figure came from a web-search result summary of that URL; the page itself could not be fetched (403, client-rendered, or not attempted). Treat as lower confidence until re-checked.
- **STALE** = data older than 2024.
- Live-scan method (2026-11-24): pages and XML sitemaps were downloaded with curl and parsed locally. For Webflow and Framer, 400 template URLs were drawn at random (fixed seed) from each marketplace sitemap and the price was read from each page's JSON-LD `offers.price`. Sample statistics are sample statistics, not catalogue censuses. Sitemap URL counts can include delisted or duplicate entries and are an upper-bound proxy for catalogue size, not an official count.

---

## 1. Per-platform marketplace terms: does an official paid marketplace exist, is it open, what is the revenue share, what do templates sell for, how many templates/creators, and are there affiliate commissions?

### Takeaway
Take rates on official marketplaces range from 0% (Framer, Ghost: listing only, creator runs own checkout) through 5% (Webflow), 8% + $0.40 (Notion), 10% + transaction fees (Kajabi), 15% (Figma, closed to new file sellers), 25% (Bubble), 30% (Carrd) to 25–40% (Showit Design Market); Squarespace and Softr have no official paid third-party template store, and Canva pays usage royalties at undisclosed rates. Observed median list prices cluster at $59–$89 for Framer/Webflow/Ghost/Wix Studio and around $450 for Showit.

### Cited Findings

**Summary table (details and sources in the bullets below)**

| Platform | Official paid marketplace? | Open to new creators? | Platform take | Observed prices (USD) | Catalogue / creators (2026-11-24 scan) | Creator affiliate/referral |
|---|---|---|---|---|---|---|
| Webflow | Yes | Application + QA vetting | 5% (creator keeps 95%) since 2025-10-21 | Sample n=400: min 24, median 79, max 169 | Page title "7000+"; sitemap 12,004 template URLs, 1,264 designer URLs | Separate affiliate programme: 50% of first subscription up to 12 months |
| Framer | Yes (listing; no Framer checkout) | Yes; pre-publication review removed 2026-06-16 | 0% | Sample n=400: 36.5% paid; paid min 2, median 59, max 200 | Sitemap 17,200 template URLs, 4,669 creator profile URLs | 50% of referred subscription for 12 months |
| Wix Studio | Yes (Wix Marketplace) | Wix Partners only; review target 60 business days | Not verifiable for 2026 (page still shows a 0% promo that expired 2025-06-30) | First-page sample n=20: min 28, median 69.5, max 149 | "2,420 Studio templates" | Partner revenue share on plans (20%/30% Studio plans) |
| Squarespace | No official third-party store found | n/a | n/a (independent shops) | Third-party shops: $99–$495 [3P] | n/a | Not researched |
| Ghost | Yes (showcase gallery linking to creator's site) | Anyone can submit; curated | 0% | 242 paid themes: min 35, median 89, mean 96.9, max 149 | 278 theme URLs in sitemap; 51 distinct sellers on page | None found |
| Notion | Yes | Apply + waitlist ("may take a few months") | 8% + $0.40 per transaction (+1% FX outside US) | Not scanned | Page title "30,000+"; search box "70,000+" | Not found |
| Canva | Royalty programme (not per-sale) | Template Creator applications, in beta | Royalty rates not published | n/a | Not obtained | Not found |
| Figma Community | Yes, but **paid files closed to new sellers** | No (files); plugins open per Figma forum reply | 15% | Minimum $2, whole dollars | Not obtained | Not found |
| Carrd | No marketplace; "Maker Program" buy links | Any Pro Lite+ user, opt-in | 30% (seller earns 70%) | Seller-set / pay-what-you-want | Not obtainable (no gallery) | Not found |
| Bubble | Yes | Yes (Stripe-supported country); Bubble may moderate | 25% | Allowed: $3–$500 (individual licence), $10–$5,000 (developer licence) | Not obtained | Not found |
| Softr | No paid third-party marketplace found | n/a | n/a | Templates page lists free templates "from Softr" | Not obtained | Not found |
| Kajabi | Yes (Template Store) | Submit for review | 10% + transaction fees | Storefront homepage sample: $0–$797, median 249 | Not obtained (homepage only) | Not found |
| Showit | Yes (Design Market) | Approved Design Partners only; curated | 25–40% (designer earns 60–75%) | 810 priced designs: min 67, median 450, mean 479, max 1,297 | ~850 designs, 154 distinct sellers | Not found |

**Webflow**
- [P] Creators earn "95% commission on all template sales, with Webflow retaining only 5% to cover the cost of maintaining our global payments infrastructure", effective the day of the post, dated October 21, 2025. — [Webflow blog](https://webflow.com/blog/template-creator-enhancements)
- [P] The live application page (retrieved 2026-11-24) still states "Earn 95% commission on every template sale — Webflow keeps 5% to cover the cost of payment processing", and lists vetting requirements (design quality, class naming, CMS/Ecommerce knowledge, support availability, "willingness to absorb feedback … from the Template QA team"). — [Webflow template designer application](https://templates.webflow.com/applications)
- [P] "Fulfillment links" (launched 2025-10-21) let creators sell Webflow templates on their own site or third-party platforms at their own price and collect payment however they like; before that "the Webflow Marketplace has been the only place where Template Creators could sell their Webflow templates". — [Webflow blog](https://webflow.com/blog/template-creator-enhancements)
- [SCAN 2026-11-24] The templates landing page title reads "7000+ Free & Premium HTML Website Templates". — [webflow.com/templates](https://webflow.com/templates)
- [SCAN 2026-11-24] The marketplace sitemap contains 12,004 unique `/html/` template URLs and 1,264 unique `/designers/` URLs. This is higher than the "7000+" in the page title; the difference is unexplained (the sitemap may include retired or variant listings). — [templates.webflow.com/sitemap.xml](https://templates.webflow.com/sitemap.xml)
- [SCAN 2026-11-24] Random sample of 400 of those template pages: 396 paid (99.0%), 4 free. Paid prices: min $24, 25th percentile $49, median $79, 75th percentile $79, mean $71.6, max $169. Most common price points: $79 (157 of 396), $49 (90), $129 (37), $59 (34), $99 (23), $29 (21), $24 (14). 190 distinct designers appeared in the sample; most frequent were Flowmance (13), Webestica (13), Azwedo (11), wcopilot (10). — [templates.webflow.com/sitemap.xml](https://templates.webflow.com/sitemap.xml)
- [P] Webflow Affiliate Program (retrieved 2026-11-24): "50% commission on a new customer's first subscription for up to 12 months", 90-day cookie window, first-touch attribution; higher tiers add 10% or 15% revenue share for up to 12 additional months on renewal. Client referrals are excluded ("your clients' purchases are not eligible"); agencies and freelancers are directed to the Certified Partner Program. Applicants must be approved (reply "within 1–2 weeks"), paid via PartnerStack. — [Webflow affiliates](https://webflow.com/solutions/affiliates)

**Framer**
- [P] "You keep 100% of the revenue from your sales"; creators are auto-enrolled in the Creator Program after publishing a Template, Plugin, Component or Vector Set in the Marketplace or becoming a verified Framer Expert; otherwise they apply via their Community profile. Enterprise subscriptions are not eligible for referral commission. Page marked "Updated September 15, 2026". — [Framer help: How the Creator Program works](https://www.framer.com/help/articles/how-the-creator-program-works/)
- [P] "Keep 100% of your Marketplace earnings", "Framer takes a 0% cut from your work", "Get 50% of their subscription for 12 months when they upgrade", "Refer users and get up to 50% commission" (retrieved 2026-11-24). — [framer.com/creators](https://www.framer.com/creators)
- [P] "Framer does not process payments or handle transactions." Sellers create the product on an external platform (Contra, Stripe and Gumroad are named as examples), paste the checkout URL into the listing, and deliver access themselves; the checkout price must match the listing price. Updated September 15, 2026. — [Framer help: Accept payments in the Community](https://www.framer.com/help/articles/accept-payments-in-the-community/)
- [P] With Framer 3.0 (June 16, 2026), "resources will no longer go through a review process before they can be published"; pre-approval is replaced by ranking plus report-based moderation; a "request review" flow is not planned. — [Framer blog: Why Marketplace is becoming part of the new Framer Community](https://framer.com/blog/marketplace-new-framer-community/)
- [SCAN 2026-11-24] Marketplace sitemaps list 17,200 template URLs, 11,907 component URLs, 1,407 plugin URLs, 568 vector-set URLs and 4,669 creator profile URLs. — [Framer marketplace sitemap index](https://www.framer.com/marketplace/sitemap.xml), [templates sitemap](https://www.framer.com/marketplace/sitemap/resources-templates.xml), [creators sitemap](https://www.framer.com/marketplace/sitemap/creators.xml)
- [SCAN 2026-11-24] Random sample of 400 template pages: 146 paid (36.5%), 254 free (63.5%). Paid prices: min $2, 25th percentile $39, median $59, 75th percentile $79, mean $63.4, max $200. Most common paid prices: $49 (23), $79 (20), $99 (17), $39 (16), $69 (10). 337 distinct sellers appeared across the 400 templates. — [templates sitemap](https://www.framer.com/marketplace/sitemap/resources-templates.xml)
- [SCAN 2026-11-24] The marketplace templates page now has an "Agent Templates — New" category: "Templates with built-in skills, so agents can edit them for you." — [Framer Marketplace templates](https://www.framer.com/marketplace/templates/)

**Wix / Wix Studio**
- [P] "Any Wix Studio account that is part of the Partner program is eligible" to submit templates; "We aim to review submissions within 60 business days"; creators are "free to sell your template anywhere on the web"; payout requires total earnings of at least $200, then net 60 days (retrieved 2026-11-24). — [Wix Studio: submit templates](https://www.wix.com/studio/partner-program/submit-templates)
- [P] Fee status is unresolved: the live page still reads "keep 100% of the profits you earn through mid-2025* … *No fees offer is valid until June 30, 2025" and its FAQ says "In 2024 we won't charge any fees—100% of the sale goes to you." No post-June-2025 fee is stated on either page (both retrieved 2026-11-24, footer © 2006-2026). — [Wix Studio: submit and sell](https://www.wix.com/studio/partner-program/submit-and-sell)
- [P] Wix's revenue-share help article (last updated 2026-11-16) says payouts include "Studio template sales in the Wix Marketplace" but states no commission on template sales. Plan revenue share: Studio yearly/multi-year plans 20% for all Partners, 30% for Legend Partners; Premium yearly plans on Wix Editor or Harmony Editor sites 0% for all Partners, 20% for Legend Partners; $200 minimum payout. — [Wix help: receiving revenue share](https://support.wix.com/en/article/wix-studio-receiving-revenue-share)
- [SCAN 2026-11-24] The Wix Marketplace page shows "2,420 Studio templates". The 20 prices on the first page ranged $28–$149, median $69.5, mean $74.5 (small, non-random sample). — [Wix Marketplace templates](https://www.wix.com/marketplace/templates)

**Squarespace** — see Section 4.

**Ghost** — see Section 5.

**Notion** — see Section 6.

**Canva**
- [P, snippet] Canva Creators "receive royalties based on your content's performance"; for templates payment depends on template usages (exports). Template Creator applicants submit a portfolio; the programme "is currently in beta, and it may take up to a couple of months to receive an answer". Element Creator sign-ups are described as "on hold" on one page and open on another. Canva's help pages returned HTTP 403 to direct fetch, so this is from search summaries. — [Canva help: Creators program](https://www.canva.com/help/canva-creators-program/), [Canva help: contributor application](https://www.canva.com/help/contributor-application/)
- [P, snippet] With Canva AI, creators are paid only when a design that used their template is published, not when it is previewed or generated and abandoned. — [Canva help: creators earnings and Canva AI](https://www.canva.com/help/creators-earnings-canva-ai/)
- [P, snippet] An updated contributor agreement took effect 14 January 2026. — [Canva help](https://www.canva.com/en_gb/help/updates-to-contributor-agreement-jan-2026/)

**Figma Community (paid files)**
- [P] "We are not approving new creators to sell paid files on Community at this time" (retrieved 2026-11-24; no reopening date). Figma "collects a flat 15% fee"; minimum price $2.00, whole-dollar USD; files and widgets are one-time payment only; cash-out possible 30 US business days after a sale, at most once a week; only approved individual accounts can sell. — [Figma help: About selling Community resources](https://help.figma.com/hc/en-us/articles/12067637274519-About-selling-Community-resources)
- [P, snippet] A Figma forum reply states the pause applies to paid files and that selling plugins remains open subject to a Stripe-supported country; another user reports being unable to find an application route. — [Figma forum](https://forum.figma.com/ask-the-community-7/can-plugins-still-use-figma-native-payments-monetization-54336), [Figma forum](https://forum.figma.com/ask-the-community-7/how-do-i-actually-apply-to-sell-a-paid-plugin-support-chat-pointed-to-a-page-with-no-application-58465)

**Carrd**
- [P] Maker Program: designers sell templates to other Carrd users and "earn 70% on each sale"; seller sets a price or pay-what-you-want minimum and shares a buy link; "Requires Pro Lite or higher"; no marketplace or gallery is described (retrieved 2026-11-24). — [Carrd docs: Maker Program](https://carrd.com/docs/account/maker-program)

**Bubble**
- [P] "Bubble retains a 25% commission on all Template License payments" (also 25% on plugins); allowed prices: Individual Commercial Template License free or $3–$500, Developer Commercial Template License $10–$5,000; payouts remitted "during the subsequent month"; Bubble may moderate submissions. Policy last revised July 10, 2024. — [Bubble marketplace policies](https://bubble.io/support/en/articles/11049816-marketplace-policies)

**Softr**
- [SCAN 2026-11-24] Softr's templates page lists free templates described as "This free template from Softr…"; no paid or third-party listings were visible in the fetched page. — [softr.io/templates](https://www.softr.io/templates)
- [3P] A Softr community thread dated 2023-05-06 asks whether a marketplace for buying ready-built templates exists; the first post shows no confirmation of one. STALE. — [Softr community](https://community.softr.io/t/is-there-a-marketplace-for-buying-ready-built-templates/2927)

**Kajabi**
- [P] "The take rate is 10% + transaction fees on each template sale" in the Kajabi Template Store; eligible types are landing pages, website themes and product themes; the developer handles support. Page dated September 28, 2026. — [Kajabi help: Template developer FAQs](https://help.kajabi.com/en/articles/17175746-template-developer-faqs)
- [SCAN 2026-11-24] The templates.kajabi.com homepage showed 56 price labels ranging $0–$797 with a median of $249 (most frequent: $79 ×16, $497 ×10, $249 ×8). Homepage only; may contain duplicates; not the full catalogue. — [templates.kajabi.com](https://templates.kajabi.com/)

**Showit**
- [P] "The Showit Design Market is open to all approved Design Partners to submit their designs for consideration"; "Earn 60-75% on each sale"; "Set your own prices"; "We only select the most unique and creative website designs" (retrieved 2026-11-24). — [Showit help: Selling designs on the Design Market](https://learn.showit.com/en/articles/405661-selling-designs-on-the-design-market)
- [SCAN 2026-11-24] The Design Market page lists about 850 designs (851 "By <designer>" labels; 847 distinct design slugs) from 154 distinct sellers (including 22 by Showit itself). 810 carry a price: min $67, median $450, mean $479, max $1,297; 40 are free. Most common price points: $297 (56), $497 (51), $597 (42), $397 (35). — [showit.com/designs](https://showit.com/designs)

### Inferences
- Because Framer does not process template payments, the amounts Framer reports as "paid out to creators" (Section 3) cannot include template sale proceeds collected through creators' own checkouts; they are most plausibly referral/partner commissions. Framer does not state this breakdown explicitly.
- On observed list prices and take rates, net revenue per sale (calculation: list price × creator share; inputs are scan medians above; ignores payment-processor fees, refunds, discounts and VAT): Webflow $79 × 95% = $75.05; Framer $59 × 100% = $59 before the creator's own checkout fees; Ghost $89 × 100% = $89 before own checkout fees; Showit $450 × 60–75% = $270–$337.50. These say nothing about sales volume.
- Framer's catalogue is far less concentrated per seller than Webflow's in the samples (337 distinct sellers per 400 templates vs 190 per 400), consistent with an open, unreviewed marketplace versus a vetted one.

### Gaps
- Wix Studio template commission after the 30 June 2025 "no fees" promotion: not stated on any Wix page fetched; unverified.
- Webflow's creator commission before 21 October 2025: not confirmed from a primary source in this research (a competitor page, Getly, claims Webflow "takes 50%", which is unverified).
- Number of creators/templates for Bubble, Canva, Figma (paid files), Kajabi (full store) and Notion (paid vs free split): not obtained.
- Price distributions for Notion, Bubble, Canva and Figma: not scanned.
- Canva royalty rates: Canva does not publish them (per a September 2026 third-party guide, [Krea](https://www.krea.ai/blog/can-you-make-money-with-canva-creators-program-and-etsy-templates-in-2026)).
- Softr: no official statement found either confirming or denying a paid creator marketplace; absence is inferred from the templates page only.

---

## 2. Webflow: revenue share, published creator payouts, template count, price range, named creators' disclosed earnings

### Takeaway
Webflow's creator share is verified at 95% (since 2025-10-21, still live on 2026-11-24), the catalogue is "7000+" by Webflow's own page with a median paid price of $79 in a 400-page sample, but Webflow has published no cumulative creator-payout total; the only earnings figures are a 2022 press release and one creator's unit-sales claim.

### Cited Findings
- [P] 95% creator commission, Webflow keeps 5%, from October 21, 2025. — [Webflow blog](https://webflow.com/blog/template-creator-enhancements); still stated live on 2026-11-24 — [application page](https://templates.webflow.com/applications)
- [SCAN 2026-11-24] "7000+" templates (page title); 12,004 template URLs and 1,264 designer URLs in the sitemap; sample of 400: 99% paid, prices $24–$169, median $79, mean $71.6. — [webflow.com/templates](https://webflow.com/templates), [sitemap](https://templates.webflow.com/sitemap.xml)
- [P, STALE — Nov 9, 2022] "On average, top template creators earn over $3,000 per month, with some creators averaging closer to $9,000 per month. One template creator has surpassed $1 million in the last 12 months." Same release: "more than 7.5 million sites on Webflow". — [Webflow press release via PR Newswire](https://prnewswire.com/news-releases/webflow-unveils-marketplace-as-sites-created-on-visual-development-platform-surpasses-7-5-million-301672774.html)
- [SR, published in Webflow's blog, Oct 2025] Kausik Dutta, Radiant Web Design: "Since joining in 2022, we've sold over 4,000 templates and expanded our team from 15 to 30 full-time designers and developers." No revenue figure given. — [Webflow blog](https://webflow.com/blog/template-creator-enhancements)
- [SR, undated testimonial on Webflow's application page; refers to 2020 — STALE] A template designer states: "Between my template sales, brand exposure and new clients, 2020 will be the first year I bring in 6 figures." A BRIX Templates testimonial mentions "20 templates later". — [application page](https://templates.webflow.com/applications)
- [3P] A third-party Q&A page states Webflow "doesn't publicly disclose specific sales numbers for each designer or average earnings per person for template sales". — [Flowradar](https://flowradar.com/answer/average-earnings-and-number-sold-webflow-templates)
- [3P] Sacra interprets the 95% payout as Webflow lowering take rates to increase supply and volume (analyst inference, not a Webflow statement). — [Sacra](https://sacra.com/chat/h/9ac1fc51-0119-4242-b30e-503a04b96640/)

### Inferences
- Labelled calculation (illustrative bounds only): Radiant's "over 4,000 templates" sold since 2022 × the observed 2026 price range $24–$169 = roughly $96,000–$676,000 gross list value over about three years; × the sample median $79 = about $316,000. Limitations: actual prices, discounts (Webflow was running a 50%-off sale banner on its submit page in the search results), the commission rate in force before Oct 2025, and the exact period are all unknown, so this is not an earnings estimate.
- The absence of any Webflow-published payout total, contrasted with Framer's published $6.5M figure, means cross-platform creator-payout comparison is not possible from primary data.

### Gaps
- Total creator payouts published by Webflow: none found (searched Webflow blog, updates, press releases).
- Current (2024–2026) earnings disclosed by named Webflow template creators (BRIX Templates, Flowbase, Webestica, Flowmance etc.): no revenue figures found.
- Per-template sales counts are not exposed on Webflow listing pages in the fetched HTML.

---

## 3. Framer: marketplace terms in 2026, creator/partner programme, affiliate commission, total creator earnings announced, individual disclosures

### Takeaway
In 2026 Framer still takes 0% and still does not process template payments (creators link their own checkout); the affiliate rate is 50% of a referred subscription for 12 months; Framer reports $6.5M paid out to creators in 2025. The marketplace dropped pre-publication review on 2026-06-16, and my scan shows 85% of sampled listings carry a 2026 publish date.

### Cited Findings
- [P] 0% cut, 100% of Marketplace earnings kept; 50% of referred subscription for 12 months; "$753,000 total paid out to creators in November" (year not stated on the page; retrieved 2026-11-24); "2025 Creator Payout … $6.5M". — [framer.com/creators](https://www.framer.com/creators)
- [P] "In 2025, we paid out $6.5M to creators"; "10.5M" new sites from the Publish button; "5.3B" views; "50% earnings on every referral". — [Framer 2025 recap](https://www.framer.com/2025)
- [P, snippet] For 2024, Framer said creators earned $4M through Framer jobs on Contra plus $4M via the Partner Program. — [Framer 2024 in Review](https://framer.com/2024)
- [P] Framer does not process payments; creators paste an external checkout link. — [Framer help](https://www.framer.com/help/articles/accept-payments-in-the-community/)
- [P] Auto-enrolment in the Creator Program on publishing a Marketplace resource; manual applications "typically reviewed within a few days". — [Framer help](https://www.framer.com/help/articles/how-the-creator-program-works/)
- [P] Review removed with Framer 3.0 on June 16, 2026; Framer's FAQ says "Individual creator earnings may move up or down as rankings change and more people publish." — [Framer blog](https://framer.com/blog/marketplace-new-framer-community/)
- [SCAN 2026-11-24] Of 400 randomly sampled template pages, the "Published" date was in 2026 for 339 (84.75%), 2025 for 43, 2024 for 17 and 2023 for 1. Within 2026 by month: Jan 1, Feb 4, Mar 6, Apr 7, May 17, Jun 39, Jul 37, Aug 30, Sep 30, Oct 81, Nov 87 (to Nov 24). Of the 146 paid templates in the sample, 118 were dated 2026. Caveat: the "Published" field could reflect republication rather than first listing. — [templates sitemap](https://www.framer.com/marketplace/sitemap/resources-templates.xml)
- [3P, weak] A German news piece (Aug 14, 2026; AI-assisted, unnamed "industry observers") says the marketplace had about 1,400 templates in 2024. — [borncity.com](https://borncity.com/news/framer-marktplatz-2026-abschaffung-von-qualitaetspruefung-spaltet-creator/)
- [SR, snippet] Amar KZR: monthly Framer income rose from $11.60 (June 2025) to a peak of $2,832.69 (March 2026), with 16,206 clicks and 849 sales over the year; June 2026 "so far" $1,038.54. — [Framer community post](https://www.framer.com/community/posts/Ko5S7FzBxgNCUDitvoNe97/)
- [SR, snippet] Designbuds: templates "generated over $150,000 in affiliate revenue in the last 12 months"; a separate post reports June revenue of $13,294 (year not shown in the snippet). — [Framer profile @designbuds](https://www.framer.com/@designbuds/)
- [SR, snippet; page returned 403] Templifica reports about $30k/month from one-time template purchases plus the Framer affiliate programme, with its biggest template alone generating over $100k (post date not retrieved). — [Indie Hackers](https://www.indiehackers.com/post/xPLu5JJpLVosWRaTovXr)
- [3P] A May 2026 blog guide says top creators earn five figures a month and mid-tier creators with five to ten templates "often earn $1K–$5K monthly"; unaudited blog estimate. — [framerwebsites.com](https://framerwebsites.com/blog/framer-creator-program-guide)

### Inferences
- Labelled calculation: 84.75% × 17,200 sitemap URLs ≈ 14,600 listings with a 2026 publish date. Limitations: n=400 sample (sampling error of a few percentage points), sitemap may include non-live URLs, "Published" may be a republish date.
- Labelled calculation: $6.5M (2025 payouts) ÷ 4,669 creator profile URLs (Nov 2026 sitemap) ≈ $1,392 per profile. Limitations: mismatched periods (2025 dollars, late-2026 creator count, and the creator count grew sharply in 2026 per the scan), a mean not a median, and payout distribution is unknown and almost certainly highly skewed. Do not present as typical earnings.
- The "$753,000 … in November" figure is probably November 2025 (November 2026 had not ended when the page was fetched), but the page does not say; if it is one month of 2025, it is about 11.6% of the $6.5M annual figure.

### Gaps
- Framer community posts are client-rendered and could not be fetched; all individual creator figures above come from search-result summaries and should be re-verified.
- No Framer-published 2026 creator-payout total, no official creator count, and no split between affiliate commissions and other payments.
- Framer Partner Program terms beyond the Creator Program page (e.g. tiering) were not separately verified; framer.com/partner resolves to the same "Get paid to create" page per search results.

---

## 4. Squarespace and Wix: 2026 status of paid third-party theme stores, the independent template-shop economy, disclosed revenue

### Takeaway
No official Squarespace third-party paid template store was found as of November 2026; the economy remains independent shops (typical prices $99–$495) plus third-party aggregators, with the only market-level data a 2023 survey (GMV $1.5–3M, 70+ shops). Wix does now run an official Wix Studio template marketplace (2,420 templates) restricted to Partners, but its current fee is unverifiable and no creator revenue has been disclosed.

### Cited Findings
- [SCAN 2026-11-24] Squarespace's own templates page navigation promotes "AI Website Builder" and "Build with AI"; no third-party seller listings or submission route appear in the fetched page. — [squarespace.com/templates](https://www.squarespace.com/templates)
- [3P] Third-party marketplaces exist outside Squarespace: SquareKicker describes a "Squarespace Template Marketplace—the first of its kind" (vendor's own claim, not independently confirmed), and Squaremuse runs "Squaremuse Market", a curated collaboration with designers. — [G2 SquareKicker listing](https://www.g2.com/products/squarekicker/discuss), [Squaremuse](https://squaremuse.com/blog/introducing-squaremuse-market)
- [3P] Premium third-party Squarespace templates "range from $99 to $495"; one review site says it has reviewed 500+ premium templates from 50+ designers/companies. — [JPK Design Co (2026)](https://www.jpkdesignco.com/blog/squarespace-templates), [SQSP Themes guide (2025)](https://www.sqspthemes.com/blog/premium-squarespace-templates)
- [3P survey, STALE — 2022 sales data, published 2023; respondent count not stated] 2023 Squarespace Template Industry Report: estimated industry GMV "between $1.5M and $3M"; "over 70 active shops as of 2023"; "a significant number of shops earned between $5,000 and $50,000" in 2022, "a handful" under $1,000, "a few surpassing the $100,000 mark"; almost half of templates sold were priced $200–$300; the majority of shops sold 10–50 templates in 2022 with a few outliers over 500; the majority of designers make less than 50% of total income from templates; 68.75% use no paid marketing. — [SQSP Themes industry report](https://www.sqspthemes.com/industry-report-full)
- [3P] A 2026 seller guide describes the Squarespace template market as "quite saturated in 2026" (opinion). — [Applet Studio](https://www.applet.studio/blog/create-squarespace-templates)
- [SR, marketing] Showit/Squarespace-adjacent shop claims: Grace & Gold says its Showit template shop earns "tens of thousands of dollars a month" (August 2025; it sells a course on the topic); Davey & Krista cite 5,000+ shop sales. — [Grace & Gold](https://withgraceandgold.com/2025/08/how-to-sell-showit-templates-courses-for-showit-designers/), [Davey & Krista](https://10k.daveyandkrista.com)
- [P] Wix Studio marketplace terms, counts and prices: see Section 1 (2,420 Studio templates; Partners only; 60-business-day review target; $200 payout minimum; fee after 2025-06-30 not stated). — [Wix submit templates](https://www.wix.com/studio/partner-program/submit-templates), [Wix Marketplace](https://www.wix.com/marketplace/templates)
- [3P] When Wix opened template selling in 2024, TechRadar reported it was not known whether Wix would take a commission. — [TechRadar](https://techradar.com/pro/website-building/wix-studio-users-can-now-boost-profits-by-selling-templates-on-wix-marketplace)

### Inferences
- Labelled calculation: the 2023 report's GMV ($1.5M–$3M) ÷ "over 70" shops ≈ $21,000–$43,000 average per shop for 2022. Limitations: STALE, survey-based with unknown sample size, an average over a skewed distribution, and "over 70" is a floor.
- Showit's official Design Market (≈850 designs, median $450) shows materially higher list prices than Webflow/Framer/Wix Studio, consistent with the $200–$500 price band reported for independent Squarespace shops; the buyer base (photographers, coaches, creatives) differs from SaaS/agency buyers.

### Gaps
- No 2024–2026 market-level revenue data for independent Squarespace or Showit template shops was found; the only survey is the 2023 report.
- No disclosed revenue from any Wix Studio template seller was found.
- Whether Squarespace has announced any plan for an official third-party template store: nothing found; absence of evidence only.
- Etsy/Creative Market sales counts for Squarespace/Showit sellers were not scanned.

---

## 5. Ghost: marketplace listing terms, paid theme prices, number of themes, seller revenue

### Takeaway
Ghost's marketplace is a curated, commission-free showcase that links to the creator's own store; on 2026-11-24 it listed about 265 themes (242 paid, median $89, range $35–$149) from 51 sellers. No theme seller's revenue has been disclosed.

### Cited Findings
- [P] "Anyone is welcome to submit a theme to the marketplace", but "we only accept the very best themes"; "We do not take any cut, commission or credit for the work of theme developers"; the marketplace is "a very simple showcase gallery with direct links to creators"; themes are ordered by an internal 5-star ranking; technical requirements include passing GScan and a live demo. Page also states "Last week, 28,339 brand new publications got started with Ghost" (retrieved 2026-11-24). — [Ghost: Submit your theme](https://ghost.org/themes/submit)
- [P, snippet] Clicking "buy" on a marketplace theme goes to the theme creator's own site and terms. — [Ghost forum](https://forum.ghost.org/t/question-about-premium-themes/40170)
- [SCAN 2026-11-24] The themes sitemap holds 278 theme URLs. The marketplace page lists 242 paid themes: min $35, median $89, mean $96.9, max $149; most common prices $89 (57), $149 (57), $99 (32), $69 (26), $59 (19), $79 (15). About 23 themes are free. — [Ghost themes sitemap](https://ghost.org/sitemap-themes.xml), [Ghost Marketplace](https://ghost.org/themes/)
- [SCAN 2026-11-24] 51 distinct sellers appear; the largest catalogues are Fueko (19 themes), Ghost itself (18), T-Rex Themes (17), Aspire Themes (17), Bright Themes (16), Storied Themes (13), High Five Themes (12). — [Ghost Marketplace](https://ghost.org/themes/)
- [SR, snippet] One creator reported on the Ghost forum that a theme submitted around March 23, 2026 had received no status update by mid-May 2026. — [Ghost forum](https://forum.ghost.org/t/theme-submission-status-submitted-around-march-23-2026/62880)
- [3P opinion, snippet, date not shown] A Ghost forum developer wrote that making Ghost theme development economically viable is hard "even when you have a best-selling premium theme", that there were about half a dozen professional Ghost theme developers, and that marketplace inclusion "has a huge effect" on sustainability. — [Ghost forum](https://forum.ghost.org/t/how-can-we-incentivize-the-creation-of-more-ghost-themes/29220)

### Inferences
- Ghost's paid catalogue is small and concentrated: the six largest third-party sellers account for 94 of roughly 265 listed themes (calculation from the scan counts above; "Ghost" official themes excluded).
- With about 30,000 paying Ghost(Pro) customers (Section 7), the addressable buyer base for paid themes is orders of magnitude smaller than Webflow's or Wix's, though self-hosted Ghost installs are not counted in that figure.

### Gaps
- No disclosed revenue or sales counts for any Ghost theme seller (Fueko, Aspire Themes, Bright Themes, etc.) was found.
- Review turnaround and acceptance rate for marketplace submissions are not published.
- ThemeForest Ghost-theme sales counts were not scanned.

---

## 6. Notion: marketplace commission, creator earnings, number of templates

### Takeaway
Notion's current English help page states a fee of 8% + $0.40 per transaction (a Japanese-language version says 10% + $0.40, an unresolved conflict), selling directly requires approval via a waitlist that "may take a few months", and the marketplace advertises 30,000+ to 70,000+ templates. Headline creator earnings (Thomas Frank, Easlo) are self-reported and date from 2022–2024.

### Cited Findings
- [P] "Notion charges a 8% fee plus 40 cents per transaction" (covers payment processing, purchase support, refunds, fraud monitoring); payouts biweekly on Thursdays; funds held 14 days; $20 minimum payout; creators outside the US pay an additional 1% FX fee; Notion handles sales tax/VAT; to sell directly creators apply and join a waitlist — "it may take a few months to get reviewed"; creators in ineligible countries can list paid templates linking to a third-party payment site (retrieved 2026-11-24). — [Notion help: Selling templates on Marketplace](https://www.notion.com/help/selling-on-marketplace)
- [P, snippet — conflict] The Japanese-language version of the same help article states 10% + 40 cents. Not resolved; could be a stale translation or a different rate. — [Notion help (ja)](https://www.notion.com/ja/help/selling-on-marketplace)
- [P] "Anyone can create a template and list it on Marketplace"; "All templates are reviewed by the Notion team before they are officially listed"; templates refundable within 14 days. — [Notion: become a creator](https://www.notion.com/become-a-creator)
- [SCAN 2026-11-24] Marketplace page title: "Choose from 30,000+ Notion templates"; the search box placeholder on the same page reads "Search 70,000+ templates"; category counts shown include Personal Productivity 26,419, Freelance 14,138, Personal Planner 10,153, Student Life 8,054; "Browse 349 categories". Category counts overlap, so they cannot be summed. — [Notion Marketplace](https://www.notion.com/templates)
- [SR, STALE — 2022] Thomas Frank: about $1 million in Notion template sales for January–December 2022, sold via Lemon Squeezy; the thread's per-product breakdown (Ultimate Brain $760k; Creator's Companion bundle $298k; Ultimate Tasks $86k; CC Base $17k) sums to about $1.16M, higher than the headline, unexplained. — [Thomas Frank on Typefully](https://typefully.com/TomFrankly/dollar1-million-in-notion-template-sales-kuFT0iD)
- [3P] A case study citing Starter Story puts Thomas Frank's business at about $175,000/month, mostly templates; not a direct statement by Frank. — [Foundry](https://www.builtbyfoundry.io/blog/thomas-frank-notion-templates-2m-creator-business)
- [SR/3P, STALE — 2022–2023, snippet] Easlo (Jason Chin): $239,000 in one year selling Notion templates (Insider as-told-to piece, which said it verified revenue with documentation); about $20,000/month by October 2022; "halfway … to my first US$1 million revenue" in March 2023; "$500K+" per a repost of his own Threads post. — [Yahoo/Insider](https://money.yahoo.com/made-239-000-selling-budgeting-120626735.html), [Indie Hackers](https://www.indiehackers.com/post/YQNh2atLObz6Jj4SYeBl), [HelpKit case study](https://helpkit.so/blog/easlo-notion-template-business-case-study), [Kajabi blog (Sep 2024)](https://kajabi.com/blog/can-you-make-money-selling-notion-templates)
- [3P estimate] GetLatka estimates Easlo's revenue at about $779K a year (October 2024) and notes Easlo has not published its revenue. — [GetLatka](https://www.getlatka.com/companies/easlo.co)

### Inferences
- The headline Notion earners built their revenue mainly through their own audiences and external checkouts (Lemon Squeezy/Gumroad) before the Notion Marketplace had native payments; their figures are not evidence of what the marketplace itself delivers.
- Labelled calculation: on a $20 template sold to a US buyer by a US creator, Notion's fee at 8% + $0.40 is $2.00 (10.0% effective); on a $5 template it is $0.80 (16.0% effective). The fixed 40 cents weighs heavily on low-priced templates. At the Japanese-page rate (10% + $0.40) these would be $2.40 and $0.90.

### Gaps
- No 2025–2026 self-reported earnings for Thomas Frank or Easlo were found.
- Notion has not published total creator payouts, creator counts or the paid/free split.
- Which fee (8% or 10%) applies in a given country was not confirmed.

---

## 7. Platform size as a demand proxy: sites/customers/paying users and revenue

### Takeaway
By disclosed scale, Canva (265M MAU, 31M paid, $4B annualised), Wix ($1.99B FY2025 revenue, 6.11M premium subscriptions) and Figma ($1.5B FY2026 guidance) dwarf Webflow (300,000+ organisations; no current official ARR), Framer ($50M ARR reported August 2025) and Ghost ($11.1M ARR, 30,144 customers); Squarespace has published nothing since Q2 2024.

### Cited Findings
- **Wix** [P] Q3 2026 (quarter ended Sep 30, 2026): revenue $570.2M (+13% y/y), bookings $573.0M (+11%), total ARR $2.021B (+15%), Creative Subscriptions revenue $406.7M, Business Solutions $163.5M, Partners revenue $212.4M (+11%), Base44 ARR "close to $250 million". — [Wix Form 6-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001576789/000162828026072477/thirdquarter2026results.htm)
- **Wix** [P, snippet of the FY2025 release, Mar 4, 2026] FY2025 revenue $1.99B (+13%); Creative Subscriptions $1.41B; bookings $2.07B; ARR $1.836B; Partners revenue $750.3M (+23%); 6.11 million premium subscriptions at Dec 31, 2025, inclusive of Base44. — [Wix FY2025 results (Seeking Alpha copy)](https://seekingalpha.com/pr/20423147), [Wix press room](https://www.wix.com/press-room/home/post/wix-reports-fourth-quarter-and-full-year-2025-results)
- **Squarespace** [P, snippet of SEC exhibit — last public data, Q2 2024] revenue $296.8M (+20% y/y); bookings $319.8M; unique subscriptions "over 5.2 million" (+21%). A third-party tracker gives annual run-rate revenue of $1,179.5M at June 30, 2024. Permira's take-private closed October 2024 (about $7.2B per secondary sources). — [Squarespace 8-K exhibit, Aug 2, 2024](https://www.sec.gov/Archives/edgar/data/1496963/000149696324000070/sqsp-08022024x8kexhibit991.htm), [TechCrunch on the Permira deal](https://techcrunch.com/2024/05/13/permira-is-taking-squarespace-private-in-6-6-billion-deal)
- **Squarespace** [3P] July 2026 report of a price increase of up to 26%. — [PetaPixel](https://petapixel.com/2026/07/17/squarespace-is-increasing-prices-by-up-to-26/)
- **Webflow** [P, undated] "trusted by more than 300,000 of the world's leading organizations". — [Webflow customers page](https://webflow.com/customers)
- **Webflow** [P, STALE — 2022] about $100M annualised recurring revenue and 200,000+ customers at its Series C ($4B valuation, March 2022); 7.5M+ sites (Nov 2022). — [SiliconANGLE](https://siliconangle.com/?p=575078), [PR Newswire](https://prnewswire.com/news-releases/webflow-unveils-marketplace-as-sites-created-on-visual-development-platform-surpasses-7-5-million-301672774.html)
- **Webflow** [3P estimates, conflicting] Sacra: $200M ARR in 2023 (from $135M in 2022) and about $280M for 2024; another aggregator lists $213M for 2024. No official 2025–2026 figure found. — [Sacra](https://sacra.com/c/webflow/)
- **Framer** [P/press] $100M Series D at a $2B valuation announced August 28, 2025; a company spokesperson reported $50M ARR with an aim to exceed $100M the following year (TechCrunch); Framer's own post says "more than half a million" monthly users, "hundreds of thousands" of sites, and break-even for the past year. — [Framer blog: Series D](https://www.framer.com/blog/series-d/), [TechCrunch](https://www.techcrunch.com/2025/08/28/no-code-website-builder-framer-reaches-2b-valuation/), [Business Wire](https://www.businesswire.com/news/home/20250828901842/en)
- **Framer** [P] 10.5M new sites published and 5.3B views in 2025. — [Framer 2025 recap](https://www.framer.com/2025)
- **Ghost** [P, live feed retrieved 2026-11-24] Annual run rate $11,135,254; monthly run rate $927,937; 30,144 active customers; net churn 2.9%; 100,000,000+ installs to date; 28,339 new publications in the last week. — [ghost.org/about](https://ghost.org/about/)
- **Notion** [3P/press, snippet] 100 million users announced September 2024; annual revenue passed $500M (dated to September 2025); more than 50% of ARR from AI-enabled customers at end-2025; Sacra estimates $610M ARR at end-2025 and $865M in July 2026; $11B valuation after a January 2026 tender offer. — [Notion blog: 100 million of you](https://notion.com/blog/100-million-of-you), [Fortune (Jun 2026)](https://fortune.com/2026/06/12/it-isnt-our-goal-for-design-to-be-distinctive-says-notion-design-head-randy-hunt-on-prioritizing-quality-over-novelty-when-building-ai-apps/), [Sacra](https://sacra.com/c/notion/)
- **Canva** [press, company-stated, snippet] more than 265 million monthly active users and over 31 million paid users in 2025; over $4B annualised revenue (TechCrunch, Feb 18, 2026). — [TechCrunch](https://techcrunch.com/2026/02/18/canva-gets-to-4b-in-revenue-as-llm-referral-traffic-rises/)
- **Figma** [P, snippet of 8-K] Q3 2026 revenue $391.4M (+43% y/y); 16,566 paid customers with more than $10,000 ARR; FY2026 revenue guidance $1.497–$1.499B. — [Figma 8-K press release](https://www.sec.gov/Archives/edgar/data/0001579878/000162828026070133/q326pressrelease.htm)
- **Carrd** [SR, STALE] founder AJ's Indie Hackers AMA: 2.5M sites, 1.6M users, $1M ARR; a later Indie Hackers piece reports 2023 revenue of $2M. — [Indie Hackers AMA](https://www.indiehackers.com/post/hi-im-aj-maker-of-carrd-and-after-2-5m-sites-1m-arr-and-a-funding-round-probably-time-for-an-ama-1b7fcf52fe), [Indie Hackers](https://www.indiehackers.com/post/dbeoP4bDlEL3zzsivdgj)

### Inferences
- Platform size does not map directly onto template demand: the largest platforms by users (Canva, Wix, Squarespace) either pay royalties at undisclosed rates, restrict selling to partners, or have no third-party store, while the two platforms with the most creator-friendly terms (Webflow 95%, Framer 100%) are an order of magnitude smaller by revenue.
- Labelled calculation: Ghost's ARR ÷ active customers = $11,135,254 ÷ 30,144 ≈ $369 per customer per year, against a median paid theme price of $89 (inputs from ghost.org/about and the Section 5 scan, same date). This is context only, not a conversion estimate.

### Gaps
- Webflow: no official ARR, customer or site count dated 2025–2026 was found.
- Squarespace: no company-reported figures after Q2 2024; aggregator numbers for 2025–2026 conflict and were excluded.
- Wix registered-user count and Wix Studio account numbers: not retrieved (the FY2025 press-room page fetched did not show them; the 20-F was not opened).
- Bubble, Softr, Kajabi and Showit user/customer counts: not researched or not found.

---

## 8. Documented evidence on how AI site generation has affected template sales

### Takeaway
The only dated, platform-specific evidence found concerns Framer after its June 16, 2026 Framer 3.0 release, where creators report sharp click and sales declines and my scan shows a surge of new listings; but these reports attribute the drop to several simultaneous causes (review removal, ranking changes, seasonality, AI) and none isolates AI. No platform has published data on AI's effect on template sales.

### Cited Findings
- [P] Framer 3.0 ("with Agents, Branching, and a new Community") launched June 16, 2026, and removed pre-publication review for Marketplace resources the same day. — [Framer blog: Framer 3.0](https://framer.com/blog/framer-3/), [Framer blog: Marketplace](https://framer.com/blog/marketplace-new-framer-community/)
- [P] Framer's own FAQ on the change: "Individual creator earnings may move up or down as rankings change and more people publish." — [Framer blog: Marketplace](https://framer.com/blog/marketplace-new-framer-community/)
- [SCAN 2026-11-24] In a 400-template random sample, monthly "Published" counts rose from 1–7 per month (Jan–Apr 2026) to 17 (May), 39 (Jun), 37 (Jul), 30 (Aug), 30 (Sep), 81 (Oct) and 87 (Nov 1–24). — [Framer templates sitemap](https://www.framer.com/marketplace/sitemap/resources-templates.xml)
- [P] Framer now lists "Agent Templates … Templates with built-in skills, so agents can edit them for you", and template listing descriptions carry the line "Build on it with Framer's agent, directly on the canvas." — [Framer Marketplace](https://www.framer.com/marketplace/templates/)
- [SR, snippet] One Framer creator reported template clicks falling from 978 in the four weeks before the 3.0 update to 224 in the four weeks after (a 77% drop, per the search summary) and no template sales since. — [Framer community: "Framer 3.0 killed the marketplace"](https://www.framer.com/community/posts/YPRZZsoLusd5S5wsZ1PXmB/)
- [SR, snippet] Another creator: "4-5 of my templates that were generating 4-5 sales per day went almost completely dry after the update." — [Framer community post by Basit A. Khan](https://www.framer.com/community/posts/2L46qQhdaTVG69e8GiN7sS/)
- [SR, snippet] A creator (Erfan, X post dated July 23, 2026) said he spoke with 10–15 top template creators and "almost everyone" reported sales slowing dramatically, drying up, or dipping significantly; he added that Webflow template sales "are down too, but not as slow as Framer", and listed possible causes as seasonality, AI tools changing how people build, and heavy marketplace updates on both platforms. — [X post](https://x.com/pentaclay/status/2080192027317121307), [Framer community copy](https://www.framer.com/community/posts/HwyXgGX9RgqP2vLM7d9NsP/)
- [SR, snippet] Counter-evidence: one creator reported their best revenue month despite others stepping away; a post by Artem Meshkov notes larger creators reported dramatic drops while some smaller creators reported unusually strong sales after the 3.0 Marketplace launch. — [Framer community: @hamzah](https://www.framer.com/community/creator/@hamzah/), [Framer community post](https://www.framer.com/community/posts/QnuRRmx7iDwJZjYuknUhyu/)
- [SR, snippet] Creator commentary that buyers increasingly prefer having AI build a personalised site over browsing templates, and the counter-argument that starting from a template can save AI credits. — [Framer community: "Is the Framer Marketplace Really Dead?"](https://www.framer.com/community/posts/QrrpRW1vzBi5d2KJ731x8x/)
- [P, snippet] Canva pays template creators for Canva AI usage only when the resulting design is published. — [Canva help](https://www.canva.com/help/creators-earnings-canva-ai/)
- [P] Wix: Base44 (AI app builder) reached about $100M ARR by the Q4 2025 release and "close to $250 million" by Q3 2026; management said "Early Wix Harmony performance is better-than-expected". Neither release mentions template sales. — [Wix Q4 2025 release](https://www.wix.com/press-room/home/post/wix-reports-fourth-quarter-and-full-year-2025-results), [Wix Q3 2026 6-K](https://www.sec.gov/Archives/edgar/data/0001576789/000162828026072477/thirdquarter2026results.htm)
- [3P, single secondary source, unverified] TechRadar reports a Bluehost-commissioned survey in which 53% of small-business owners had adopted AI website builders instead of professional developers, and Freelancer.com data showing website-design job advertisements down 59% between Q2 2024 and Q3 2026. These concern web-design services, not template sales. — [TechRadar](https://www.techradar.com/pro/the-collapse-of-web-coding-gigs-is-getting-ugly-ai-takes-over-routine-website-development-jobs-and-business-owners-are-very-happy-with-its-job-so-far)
- [3P, unverified against primary] A search summary of coverage of Wix's Q3 2026 results says management estimated that restructuring and "a sharper-than-expected slowdown in its partners business" would reduce 2026 bookings by about $50M and revenue by about $25M. This wording was not found in the Wix press-room release or the 6-K text as fetched, so treat as unconfirmed. — [24/7 Wall St](https://247wallst.com/cards/wix-q3-2026-earnings-wix-01m72jzf2wx07zns419hjb9zx6), [Ynet](https://www.ynetnews.com/business/article/hk6zdplrgx)

### Inferences
- The Framer evidence shows a supply shock (unreviewed listings surging from mid-2026) coinciding with the launch of on-canvas AI agents; creator-reported declines cannot be attributed to AI specifically from the available data.
- The one cross-platform remark (Webflow sales "down too, but not as slow as Framer") is a single creator's hearsay summary of 10–15 conversations, not measured data.
- Platforms are repositioning templates as starting points for AI agents (Framer "Agent Templates", Canva AI template royalties) rather than removing them, which is a documented product direction, not evidence about sales volumes.

### Gaps
- No platform (Webflow, Framer, Wix, Squarespace, Notion, Canva) has published template sales or payout data segmented before/after its AI builder launch.
- No evidence found specifically linking Lovable, v0 or Bolt to template sales changes.
- No Webflow creator has published dated before/after sales numbers; no evidence either way for Squarespace, Showit, Ghost, Notion or Wix Studio template sellers.
- The uxdesign.cc article "Framer is killing the marketplace… or are they?" returned HTTP 403 and was not read. — [uxdesign.cc](https://uxdesign.cc/framer-is-killing-the-marketplace-or-are-they-cc96a67763b3)
- All Framer community figures are from search summaries of client-rendered pages and need direct verification before being quoted as exact numbers.
