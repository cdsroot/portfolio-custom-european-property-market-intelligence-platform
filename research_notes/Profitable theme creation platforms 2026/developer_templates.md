# Economics of code-based templates, themes, UI kits and boilerplates sold to developers (as of 2026-11-24)

**How to read these notes**

- Retrieval date for every "live page" figure is **2026-11-24** unless another date is given. Many live prices were captured during Black Friday promotions, so both the promotional and the list price are recorded where the page showed both.
- Evidence labels used on every figure:
  - **[PRIMARY]** = official page of the company/marketplace concerned (fee page, pricing page, item page, official blog).
  - **[SELF-REPORTED]** = founder/company statement, unaudited.
  - **[VERIFIED]** = payment-processor-linked figure (e.g. TrustMRR via Stripe/Lemon Squeezy API key). Note TrustMRR is owned by Marc Lou, so for his own products it is processor-linked but not independent.
  - **[THIRD-PARTY ESTIMATE]** = database or blogger estimate, not a disclosure.
  - **[SECONDARY]** = press/blog reporting of a primary statement that I could not open directly.
  - **[STALE]** = data older than 2024.
- All page reads were made through a fetch tool that summarises pages with a small model. Numbers are as returned by that tool; where it could not quote verbatim this is noted. Search-engine snippets of TrustMRR pages proved unreliable (two snippets contradicted the live pages), so only directly fetched TrustMRR figures are used.

---

## 1. Flagship products: pricing, licence model, disclosed revenue or sales counts

### Takeaway
The two best-documented flagships both collapsed between 2024 and 2026: Tailwind Labs reported revenue "down close to 80%" (January 2026), laid off three of four engineers, and on 9 September 2026 joined Shopify and closed Tailwind Plus to new customers; ShipFast went from a founder-stated $126,000/month (2024) to $2,000/month (2026), with $548 Stripe-verified in the 30 days to 24 November 2026. Almost every surviving product is sold as a one-time "lifetime" licence in the roughly $50-$400 range for individuals, and few publish revenue; the ones that do (ThemeSelection, Dracula Pro, TrustMRR-listed boilerplates) show five- to low-six-figure annual revenue, not seven.

### Cited Findings

**Tailwind UI / Tailwind Plus (Tailwind Labs)**
- [SELF-REPORTED, 2020-08-02, STALE] Adam Wathan wrote that Tailwind UI was "about to cross $2 million in revenue" about five months after its February 2020 early-access release, and that the business had "over $4m in revenue in under 2 years". — [adamwathan.me](https://adamwathan.me/tailwindcss-from-side-project-byproduct-to-multi-mullion-dollar-business/)
- [SELF-REPORTED, 2026-01-07, primary GitHub comment] Wathan: "75% of the people on our engineering team lost their jobs here yesterday"; "Traffic to our docs is down about 40% from early 2023 despite Tailwind being more popular than ever"; "our revenue is down close to 80%"; "The docs are the only way people find out about our commercial products". No absolute revenue figure was given. — [GitHub PR #2388](https://github.com/tailwindlabs/tailwindcss.com/pull/2388) ([direct comment link](https://github.com/tailwindlabs/tailwindcss.com/pull/2388#issuecomment-3717222957))
- [SECONDARY, 2026-01-08] Three engineers were laid off (75% of the engineering team); five staff remained (three co-founders plus two); Wathan said that "if nothing changed, then in about six months we would no longer be able to meet payroll obligations". Vercel and Google AI Studio announced sponsorship afterwards. — [DevClass](https://www.devclass.com/ai-ml/2026/01/08/tailwind-labs-lays-off-75-percent-of-its-engineers-thanks-to-brutal-impact-of-ai/4079571)
- [SECONDARY, January 2026] Sponsors named after the layoffs included Google AI Studio, Vercel, Supabase, Gumroad and Lovable; no sponsorship amounts were published. — [OfficeChai](https://officechai.com/ai/google-vercel-lovable-others-come-forward-to-sponsor-tailwind-after-company-reveals-75-ai-related-layoffs); [PPC Land](https://ppc.land/tech-giants-rush-to-sponsor-tailwind-css-after-devastating-layoffs/)
- [PRIMARY, 2026-09-09] "Tailwind Labs is joining Shopify". On the commercial products: "we're closing sign ups for new customers to focus on Tailwind CSS at Shopify"; "All existing customers will of course maintain their access to products like Tailwind Plus and ui.sh"; "On the commercial side, we'll no longer be trying to grow the business around Tailwind"; "We built a great little website template business around Tailwind over the years." Tailwind CSS is "installed over 110 million times per week" and stays MIT-licensed. No financial terms disclosed. — [tailwindcss.com blog](https://tailwindcss.com/blog/tailwind-is-joining-shopify)
- [SECONDARY, 2026-09-09] Financial terms of the Shopify deal were not disclosed. — [BetaKit](https://betakit.com/tailwind-finds-stable-long-term-home-with-shopify-acquisition/)
- [SECONDARY, pricing before closure] Tailwind Plus was a one-time purchase: $299 personal and $979 team (up to 25 people). I could not confirm this on the official site on 2026-11-24 because `tailwindcss.com/plus` returned only a login screen. — [Tailkits blog](https://tailkits.com/blog/tailwind-plus-replaced-tailwind-ui/)

**ShipFast (Marc Lou) — Next.js SaaS boilerplate**
- [PRIMARY, live 2026-11-24] Pricing: Starter $199 (list $299), All-in $249 (list $349), ShipFast + CodeFast bundle $299 (list $648); all one-time; "Pay once. Build unlimited projects!"; page claims "8451 makers"; the page states the last update was 9 months ago. — [shipfa.st](https://shipfa.st/)
- [VERIFIED via Stripe API key on founder-owned TrustMRR, last updated 2026-11-24 20:00] All-time revenue $1,273,440; revenue in the last 30 days $548; no active subscriptions. — [TrustMRR ShipFast](https://trustmrr.com/startup/shipfast)
- [SELF-REPORTED, 2026-10-20] Marc Lou's own post gives ShipFast monthly revenue as 2023: $0/mo; 2024: $126,000/mo; 2025: $25,000/mo; 2026: $2,000/mo. The post states no cause. — [marclou.com](https://marclou.com/tweets/shipfast-went-from-0-mo-to-126-000-mo-then-back-down)
- [SELF-REPORTED, 2026-09-08] ShipFast launched 1 September 2023; "By the end of the month, ShipFast made $40,000"; "By the end of 2023, ShipFast alone made almost $200,000 in total revenue"; peak of "$133,000 in monthly revenue in April 2024". — [marclou.com](https://marclou.com/p/i-ve-made-3m-with-my-36-startups)
- [SECONDARY, 2026-10] A third-party article reports that on 11 September 2026 Marc Lou discontinued the ShipFast and CodeFast affiliate programmes and attributed the drop mainly to AI and lower 2026 conversion rates; it also records TrustMRR at $1,272,892 lifetime and about $1,993 for the prior 30 days on 21 October 2026. I did not open the underlying Bluesky post. — [aiidelist](https://aiidelist.com/blog/shipfast-revenue-collapse-marc-lou-2026.md)
- [CALCULATION, labelled] TrustMRR lifetime moved from $1,272,892 (21 Oct 2026, secondary) to $1,273,440 (24 Nov 2026, fetched) = $548 in about 34 days. Inputs are one secondary and one fetched reading; it matches the "last 30 days $548" figure on the live page.

**ThemeSelection (admin templates; sister brand Pixinvent sells Vuexy on ThemeForest)**
- [SELF-REPORTED, published 2025-12-19, page updated 2026-11-17] "2025 Wrapped": lifetime revenue passed $1,000,000+; 2025 revenue "200K+"; earnings "fell nearly 50%" versus the prior period; average monthly sales were 280 (Jan-Jul 2024), 180 (Aug-Dec 2024), 151 (Jan-Jun 2025) and 130 (last six months of 2025). The page also reports search click-through rate falling from 7% to 2% and weekly users from 25,000 to 11,000, and attributes reduced demand for traditional admin templates to AI tools and Google AI Overviews. Their new shadcn/studio product sold 550+ since September 2025 (the page also says 520+). The fetch tool flagged internal inconsistencies on the page (e.g. "200K+ (down 38.4k)" alongside "nearly 50%"). — [ThemeSelection blog](https://themeselection.com/blog/2025-wrapped-year-in-review/)

**Dracula Pro (editor/terminal theme pack) — see also section 4**
- [SELF-REPORTED, live 2026-11-24, undated on page] "Our Journey to $442,775.23"; "Dracula Pro reached 8,101 sales to date." — [draculatheme.com/pro/journey](https://draculatheme.com/pro/journey)
- [PRIMARY, live 2026-11-24] Price $79 list, $47 during a 40%-off promotion; one-time payment; up to 3 active devices; sold through Gumroad; "Join 8,101 creators". — [draculatheme.com/pro](https://draculatheme.com/pro)

**shadcn/ui ecosystem paid kits**
- [PRIMARY/SELF-REPORTED, live 2026-11-24] shadcnblocks: Pro $89 (list $149), Premium $179 (list $299), Elite $239 (list $399), CMS add-ons $227 (list $379); all one-time lifetime; a 40% Black Friday code was advertised. Page claims 7,831 Pro customers and 41,781 free users, established 2023. No revenue disclosed. — [shadcnblocks.com/pricing](https://www.shadcnblocks.com/pricing)
- [CALCULATION, labelled, illustrative only] 7,831 Pro customers x $149 lowest list price = $1.17M; x $89 lowest promotional price = $0.70M. Limitations: tier mix, historical prices, discounts, refunds and team licences are unknown, and the customer count is self-reported. This is not a revenue disclosure.
- [PRIMARY, live 2026-11-24] Aceternity UI: 1-Year Licence $169 (regular $249), Lifetime Access $199 (regular $299), Team $1,590 (regular $1,990, up to 10 members); all one-time. No customer count or revenue disclosed. — [ui.aceternity.com/pricing](https://ui.aceternity.com/pricing)
- [SECONDARY] Magic UI Pro is listed at $199 by a competitor's comparison post; the official pricing URL I tried returned 404. — [Untitled UI blog](https://www.untitledui.com/blog/tailwind-plus-alternatives)
- [PRIMARY, 2025-01-22] Vercel acquired Tremor; Tremor's paid product, Tremor Blocks, became "free and open source for all users" under an MIT licence; both co-founders joined Vercel's Design Engineering team; Tremor had 16,000+ GitHub stars and 300,000 monthly downloads. No financial terms. — [Vercel blog](https://vercel.com/blog/vercel-acquires-tremor)

**SaaS starter kits and boilerplates**
- [PRIMARY, live 2026-11-24] MakerKit: Pro (1 developer) $226.85 (list $349) or $199 for the Cloudflare kit; Teams (up to 5) $421.85 (list $649) or $399; "One-time payment, no subscriptions"; lifetime updates; unlimited projects. No customer count or revenue on the page. — [makerkit.dev/pricing](https://makerkit.dev/pricing)
- [PRIMARY/SELF-REPORTED, live 2026-11-24] SaaS Pegasus (Django): Unlimited licence $299 on sale (list $649), one-time, lifetime updates, unlimited projects, 7-day refund; "Join 1918 developers and businesses using Pegasus today." — [saaspegasus.com/pricing](https://www.saaspegasus.com/pricing/)
- [PRIMARY, live 2026-11-24] SaaS Pegasus founder's open-revenue page now shows blank values and states "I stopped publishing this data in November, 2022." — [coryzue.com/open](https://www.coryzue.com/open/)
- [THIRD-PARTY ESTIMATE, undated, about 2024] supastarter (Jonathan Wilke): about $10K/month, labelled by the publisher as "Estimated from public sources"; launched at $49 in August 2021 and later raised to $299 one-time. — [Starter Story](https://www.starterstory.com/supastarter-breakdown)
- [PRIMARY, live 2026-11-24] Bedrock (Max Stoiber): $396 (shown as 12% off $450), one licence per product, lifetime use, 14-day money-back guarantee. No sales disclosed; the page shows no changelog or dates. — [bedrock.mxstbr.com](https://bedrock.mxstbr.com/)
- [PRIMARY/SELF-REPORTED, live 2026-11-24] Gravity (Node/React SaaS boilerplate): one-time purchase with 12 months of updates, then $195/year renewal ($250/year if lapsed); "Used by 1,200+ developers". Tier prices were not on the page fetched. — [usegravity.app](https://usegravity.app/)
- [PRIMARY, live 2026-11-24] Laravel Nova: $99 single project (renewal $79/year) or $299 unlimited (renewal $249/year); one-time purchase with one year of updates. — [nova.laravel.com](https://nova.laravel.com/)
- [SELF-REPORTED, STALE, about 2019-2021] Divjoy (Gabe Ragland): "$10,041 in 4 days" from a feature launch and "$16,285 in sales last month". Dates not confirmed in my search; treat as stale. — [DEV post 1](https://dev.to/gabe_ragland/how-my-dev-tool-made-10-041-in-4-days-28ac); [DEV post 2](https://dev.to/gabe_ragland/how-my-dev-tool-did-16-285-in-sales-last-month-20im)

**Tailwind/HTML template shops**
- [PRIMARY/SELF-REPORTED, live 2026-11-24] Cruip: Classic Bundle $39.50 and Modern Bundle $74.50 under a "50% off all bundles" Black Friday banner; single templates mostly $49 (Mosaic $69, Artifact $129); "Trusted by 60K+ developers" (not stated whether these are paying customers). — [cruip.com](https://cruip.com/)
- [PRIMARY, 2026] Cruip's terms page notes "New in 2026: choose the Classic or Modern Bundle", with the old Unlimited Access plan grandfathered into the Classic Bundle. — [cruip.com/terms](https://cruip.com/terms/)
- [PRIMARY/SELF-REPORTED, live 2026-11-24] Tailkit: Developer $49 (list $79, one project), Unlimited $79 (list $199), Team $349 (list $549, up to 10 people); one-time, free lifetime updates; "More than 20,000 people worldwide have used our projects" (all of the seller's projects, not Tailkit alone). — [tailkit.com/pricing](https://tailkit.com/pricing)
- [PRIMARY/SELF-REPORTED, live 2026-11-24] Creative Tim now sells an annual "Access Pass" subscription instead of leading with one-off themes: Basic $199/year, PRO $349/year, Business $599/year, bundled with AI credits, an AI App Builder, hosted AI agents and 436 shadcn/ui blocks; claims "Trusted by 2.8 million developers and teams". — [creative-tim.com](https://www.creative-tim.com/)
- [THIRD-PARTY ESTIMATE] Creative Tim revenue: Latka lists about $3M (October 2024) and $2.3M for 2023; RocketReach lists $4M. These disagree and neither is a company disclosure. — [Latka](https://getlatka.com/companies/creative-tim); [RocketReach](https://www.rocketreach.co/creative-tim-profile_b549fc0bf9e2fb4d)
- [SELF-REPORTED, STALE, 2018] Creative Tim founders wrote "We made $1,052,000 in 2018 selling UI tools". — [freeCodeCamp](https://www.freecodecamp.org/news/we-made-1-052-000-in-2018-selling-ui-tools-here-is-what-we-learned-38920d86a296/)

**Refactoring UI (book + design resources by Wathan and Schoger)**
- [PRIMARY/SELF-REPORTED, live 2026-11-24] Complete Package $149, Essentials $99; "Over 30,000 copies sold" (another section says "Over 20,000 people are already using Refactoring UI"). — [refactoringui.com](https://www.refactoringui.com/)
- [CALCULATION, labelled, illustrative only] 30,000 copies x $99 = $2.97M; x $149 = $4.47M. Limitations: launch pricing, discounts, tier mix and taxes are unknown; this is not a disclosed revenue figure. A secondary aggregator quotes "over $2.5 million" without a primary citation. — [yespress.io](https://yespress.io/adam-wathan)

**TrustMRR-listed boilerplates (processor-verified, all fetched 2026-11-24)**
- [VERIFIED via Lemon Squeezy API key] TurboStarter: all-time $85,610; last 30 days $3,401; Core Kit $249, Bundle $399, lifetime licences. — [TrustMRR TurboStarter](https://trustmrr.com/startup/turbostarter)
- [VERIFIED via Stripe API key] MkSaaS (Next.js boilerplate, $129 one-time): all-time $109,826; last 30 days $1,099. — [TrustMRR MkSaaS](https://trustmrr.com/startup/mksaas)
- [VERIFIED via Stripe API key] Nuda Kit (SaaS starter kit, $99/$199 one-time): all-time $199. — [TrustMRR Nuda Kit](https://trustmrr.com/startup/nuda-kit)

### Inferences
- The dominant licence model in this segment is a one-time payment with lifetime updates. Wathan's statements and the Shopify post are consistent with that model producing strong early revenue and weak recurring revenue; the only flagships with renewal revenue found here are Laravel Nova, Gravity and Aceternity's 1-year tier, and Creative Tim has moved to annual subscriptions bundled with AI services.
- Disclosed customer counts are small relative to free-user counts (shadcnblocks: 7,831 paying against 41,781 free users, about 19% of the free base as a simple ratio of the two self-reported numbers).
- The verified long tail is thin: of three directly fetched TrustMRR boilerplates other than ShipFast, lifetime totals were $199, $85,610 and $109,826, and trailing-30-day revenue was $1,099 to $3,401 where shown.

### Gaps
- Tailwind Labs has never published an absolute current revenue figure; only the percentage decline and the 2020 milestones are public. Shopify deal terms are undisclosed.
- No revenue disclosure found for Cruip, Flowbite, MakerKit, Bedrock, Gravity, Aceternity UI, Magic UI, shadcnblocks, Tailkit, Laravel Spark/Nova or AstroWind/paid Astro themes. Flowbite's pro page returned HTTP 403; supastarter, Cruip and Creative Tim `/pricing` URLs returned 404 (prices above for Cruip and Creative Tim come from their home pages).
- supastarter's only figure is a third-party estimate. SaaS Pegasus stopped publishing in November 2022.
- Laravel Spark, Divjoy's current status, AstroWind and Astro paid themes were not researched to a citable standard.
- Marc Lou's statement attributing the decline to AI is known to me only through a secondary article.

---

## 2. Marketplaces for code templates: fees, terms and top-seller sales counts

### Takeaway
The marketplace landscape changed materially in 2026: Envato moved every ThemeForest and CodeCanyon author to a flat 50% author fee and removed exclusivity from 1 July 2026, the official Bootstrap Themes marketplace is shutting down with checkout disabled, and Lemon Squeezy stopped accepting sign-ups and will close on 31 March 2027. Direct selling through a merchant of record costs roughly 5% + $0.50 (Polar Starter) to 10% + $0.50 (Gumroad direct), against a 50% author fee on Envato.

### Cited Findings

**Envato Market (ThemeForest / CodeCanyon)**
- [PRIMARY, effective 2026-07-01] "The author fee for all authors will move to 50%"; "Exclusivity requirements will be removed entirely"; non-exclusive authors' fee falls "from 55% to 50%", and exclusive authors' fee rises to 50%; "The updated terms take effect on 1 July 2026" and first show in the 15 August payout; stated reason: "Envato Market has faced challenging market conditions for some time", plus alignment with Envato Elements. — [Envato Author Hub](https://author.envato.com/hub/changes-to-envato-market-revenue-share-and-exclusivity-what-you-need-to-know/)
- [SECONDARY, competitor blog citing Envato pages] Before July 2026 exclusive authors paid 37.5% falling to 12.5% after $75,000 of sales, and non-exclusive authors paid 55%. The fee is calculated on the item price (list price minus Envato's fixed buyer fee). Worked example given: on a $39 item with a $5 buyer fee the item price is $34 and the author now receives $17, against $29.75 for a top-tier exclusive author before. The same source says open author applications are paused, new authors join by invitation only, and Envato is not inviting authors into Theme or Code (citing an Envato help page updated 25 September 2026). I could not open that Envato help page (HTTP 403), so the application freeze is unverified at primary level. — [ChargePanda](https://www.chargepanda.com/blog/post/envato-july-2026-changes-wordpress-authors-guide)
- [PRIMARY, live 2026-11-24] ThemeForest Admin Templates category has 2,802 items. Top ten by sales (name, author, regular price, sales, last update): Metronic, keenthemes, $49, 120.4K, 04 Jun 2026; Vuexy, PIXINVENT, $39, 30.7K, 02 Oct 2026; Fuse Angular, srcn, $32, 26K, 12 Aug 2026; Velzon, Themesbrand, $25, 14.5K, 19 Mar 2026; Limitless, Kopyov, $28, 13.9K, 03 Sep 2023; Materialize, PIXINVENT, $39, 12.7K, 02 Oct 2026; Pages, ace, $35, 11.4K, 24 May 2023; Fuse React, withinpixels, $29, 11.4K, 10 Feb 2026; Porto Admin, Okler, $12, 9.9K, 21 Jan 2025; Isomorphic, redqteam, $24, 8.4K, 26 Mar 2025. — [ThemeForest admin templates, best sellers](https://themeforest.net/category/site-templates/admin-templates?sort=sales)
- [PRIMARY, live 2026-11-24] Metronic: 120,417 sales; $49 regular / $969 extended licence; 4.89 stars from 8.1K ratings; listed "14 years ago"; last update 4 June 2026. — [ThemeForest Metronic](https://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469)
- [PRIMARY, live 2026-11-24] Vuexy: 30,707 sales; $39 regular / $799 extended; 4.90 stars from 988 ratings; listed "8 years ago"; last update 2 October 2026. — [ThemeForest Vuexy](https://themeforest.net/item/vuexy-vuejs-html-laravel-admin-dashboard-template/23328599)
- [CALCULATION, labelled, illustrative only] Metronic 120,417 sales x $49 current regular price = $5.90M gross over about 14 years; Vuexy 30,707 x $39 = $1.20M over about 8 years. Limitations: the price has changed over time, extended-licence sales ($969/$799) are not separated, the figure is before Envato's buyer fee and author fee (now 50%), refunds and taxes, and it is cumulative rather than current. These are not earnings figures.

**Other template marketplaces**
- [PRIMARY, observed 2026-11-24] `themes.getbootstrap.com/sell` now redirects to a "Sunsetting Bootstrap Themes Customer FAQ" Notion page, and marketplace pages carry the banner "Bootstrap Themes is shutting down. Checkout is disabled." The FAQ body could not be read, so the shutdown date and reasons are unconfirmed. — [Bootstrap Themes store page](https://themes.getbootstrap.com/store/webuildthemes); [redirect target](https://glow-limpet-524.notion.site/Sunsetting-Bootstrap-Themes-Customer-FAQ-1c54f54098ac804e9d69d4b2d7c14bd5)
- [PRIMARY, page updated 2023-07-17, STALE] WrapBootstrap pays authors 70% for exclusive items and 40% for non-exclusive items (as returned by search; page not opened). — [WrapBootstrap fee structure](https://support.wrapbootstrap.com/help/fee-structure)
- [SECONDARY, undated reviews] Codester pays a flat 70% commission regardless of exclusivity or volume. Not confirmed on Codester's own terms. — [WPLift](https://wplift.com/?p=43412); [Line25](https://line25.com/?p=7914)

**Direct-sale / merchant-of-record platforms**
- [PRIMARY, live 2026-11-24] Gumroad: 10% + $0.50 per transaction on direct sales; 30% on sales to new customers through Gumroad Discover; Gumroad is merchant of record ("Since January 1, 2025, Gumroad handles ALL your tax obligations"). The pricing page does not itemise card-processing fees. — [gumroad.com/pricing](https://gumroad.com/pricing)
- [SECONDARY, 2026] Gumroad's direct rate is reported as 10% + $0.50 plus 2.9% + $0.30 card processing, an effective 14.5% on $10,000/month of sales in one comparison. — [Flavio Copes](https://flaviocopes.com/payment-provider-fees/)
- [PRIMARY, live 2026-11-24] Lemon Squeezy: 5% + 50c per transaction, merchant of record; banner: "Lemon Squeezy is no longer accepting new sign-ups and will shut down on March 31, 2027." — [lemonsqueezy.com/pricing](https://www.lemonsqueezy.com/pricing)
- [SECONDARY, November 2026] Lemon Squeezy closed to new sign-ups on 16 November 2026; merchants are directed to Stripe Managed Payments, with promotional merchant-of-record pricing of 1.5% through 1 December 2027 on top of standard Stripe processing; Managed Payments lacks Lemon Squeezy's affiliate tools, digital-download delivery and storefront builder. — [Michael Tsai blog](https://mjtsai.com/blog/2026/11/19/lemon-squeezy-shutting-down/); [checkoutpage.com](https://checkoutpage.com/blog/lemon-squeezy-shutting-down)
- [PRIMARY, live 2026-11-24] Polar (merchant of record): Starter free, 5% + 50c; Pro $20/month, 3.8% + 40c; Growth $100/month, 3.6% + 35c; Scale $400/month, 3.4% + 30c; +1.5% on international (non-US) cards; payout costs $2/month plus 0.25% + $0.25 per payout; $15 per dispute. Organisations created before 27 May 2026 keep an "Early Member" rate of 4% + 40c. — [polar.sh pricing](https://polar.sh/resources/pricing)
- [PRIMARY, live 2026-11-24] GitHub Sponsors: "does not charge any fees for sponsorships from personal accounts"; sponsorships from organisation accounts carry up to 6% (3% card processing + 3% GitHub service fee). — [GitHub Docs](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors)

**Fee comparison on one sale (CALCULATION, labelled)**
- Inputs: a $49 template sold once. Envato: item price = $49 minus a fixed buyer fee; using the $5 buyer fee from the secondary worked example above (the site-template buyer fee was not confirmed), author receives 50% x $44 = $22.00. Gumroad direct: $49 - (10% x $49 + $0.50) = $43.60, before any separately charged card processing. Polar Starter, US card: $49 - (5% x $49 + $0.50) = $46.05, before payout fees. Limitations: taxes, payout fees, refunds, international-card surcharges and the true Envato buyer fee for this category are excluded or assumed as stated; Envato supplies buyer traffic that direct sale does not.

### Inferences
- A new seller's realistic marketplace options narrowed in 2026: ThemeForest's author share fell to 50% for everyone (and, per one secondary source, Theme/Code applications are closed), the official Bootstrap marketplace is closing, and Lemon Squeezy is closing. Gumroad, Polar and Stripe-based options remain for direct sale.
- Several of ThemeForest's ten best-selling admin templates have not been updated since 2023-2025, while the top two were updated in 2026; cumulative sales counts therefore describe a decade of history rather than current demand.

### Gaps
- Envato's fixed buyer-fee table for site templates could not be opened (HTTP 403), so the exact net per sale in the admin-template category is unconfirmed.
- The Envato author-application freeze rests on one competitor blog.
- No revenue-share figure was found for the Bootstrap Themes marketplace before its closure.
- Vercel Templates, the Astro Themes directory and Next.js template listings: I found no documented seller payout or revenue-share terms and did not verify how paid themes are listed there. Creative Tim's home page shows no seller programme.
- Current sales velocity (sales per month) for ThemeForest items is not published; only cumulative counts are.

---

## 3. Mobile/app templates (Flutter, React Native)

### Takeaway
CodeCanyon's Mobile category is large (14,080 items) and its best sellers are Flutter and native Android/iOS products at $25-$109 with 3,400 to 7,300 cumulative sales; no React Native item is in the top ten. I found no disclosed revenue for Instamobile/Instaflutter, and the only FlutterFlow Marketplace data point is one seller reporting a collapse from 1-2 sales a day to 2 sales in a month.

### Cited Findings
- [PRIMARY, live 2026-11-24] CodeCanyon Mobile category shows 14,080 results. Top ten by sales (name, author, price, sales, last update, platform): Fluxstore WooCommerce, InspireUI, $34 (was $69), 7.3K, 14 Nov 2026, Flutter; Universal Android App, sherdleapps, $29, 7.3K, 04 Aug 2025, Android; WebViewGold for iOS, onlineappcreator, $109, 4.1K, 24 Nov 2026, iOS; MaterialX, dream_space, $25, 4.1K, 07 Oct 2025, Android; ProKit Flutter UI Kit, iqonicdesign, $49, 4K, 28 Apr 2026, Flutter; 6Valley Multi-Vendor, sixamtech, $79, 3.9K, 18 Oct 2026, Flutter; 6amMart, sixamtech, $99, 3.8K, 24 Nov 2026, Flutter; Fluxstore Multi Vendor, InspireUI, $39 (was $79), 3.7K, 14 Nov 2026, Flutter; Universal for iOS, sherdleapps, $29, 3.5K, 29 Mar 2025, iOS; Active eCommerce Flutter App, ActiveITzone, $49, 3.4K, 26 Jul 2026, Flutter. Platform labels were inferred by the fetch tool from listing metadata. — [CodeCanyon Mobile, best sellers](https://codecanyon.net/category/mobile?sort=sales)
- [PRIMARY, effective 2026-07-01] CodeCanyon authors are covered by the same flat 50% author fee as ThemeForest. — [Envato Author Hub](https://author.envato.com/hub/changes-to-envato-market-revenue-share-and-exclusivity-what-you-need-to-know/)
- [SELF-REPORTED, single seller, July 2025] A FlutterFlow Marketplace seller (Mo Tarek) reported averaging about 1-2 sales per day, then "only 2 sales all month" from early July 2025, with unchanged prices and listings; no official FlutterFlow reply was visible. — [FlutterFlow community](https://community.flutterflow.io/discussions/post/sudden-drop-in-flutterflow-marketplace-sales---seeking-insights-july-2025-iCPPrpsJrIbLdZC)
- [PRIMARY, undated] FlutterFlow's marketplace terms say a percentage of each transaction "may be paid to or retained by Company" as set out in separate Pricing and Payment Terms, and FlutterFlow's Creator FAQ says FlutterFlow projects cannot be sold on other marketplaces (non-circumvention clause). The percentage itself was not found. — [FlutterFlow Marketplace ToS](https://flutterflow.io/tos-marketplace); [Creator FAQs](https://docs.flutterflow.io/marketplace/creators-hub/creator-faqs)
- [SECONDARY, undated] Instamobile sells React Native and Flutter app templates as one-time perpetual licences listed at $99-$999 by one directory; another directory lists $149-$249/month. The two disagree. — [AlternativeTo](https://alternativeto.net/software/instamobile/about); [SaaS Browser](https://saasbrowser.com/ca/saas/214383/instamobile)

### Inferences
- The best-selling mobile templates on CodeCanyon are complete vertical apps (e-commerce, multi-vendor delivery, WebView wrappers) rather than generic UI kits; only two of the top ten (MaterialX, ProKit) are UI kits.
- Cumulative sales counts for the top mobile items (3.4K-7.3K) are an order of magnitude below the top admin template on ThemeForest (120.4K).

### Gaps
- No founder-disclosed or verified revenue for Instamobile or Instaflutter was found. A Latka page for "InstaMobile" describes a different, defunct company and was excluded.
- FlutterFlow's seller revenue-share percentage was not found in public documents.
- Current live prices on instamobile.io and instaflutter.com were not fetched.
- No data found for dedicated React Native template marketplaces beyond CodeCanyon.

---

## 4. Editor and developer-tool themes

### Takeaway
Paid editor themes are a small, mostly direct-sold niche: Dracula Pro is the only one with published figures, at $442,775.23 from 8,101 sales to date, sold at $79 list through Gumroad. JetBrains Marketplace is the one editor store with native paid distribution (15% commission); sources from 2026 say the VS Code Marketplace still has no native payment mechanism.

### Cited Findings
- [SELF-REPORTED, live 2026-11-24, page undated] Dracula Pro: "Our Journey to $442,775.23" and "8,101 sales to date". — [draculatheme.com/pro/journey](https://draculatheme.com/pro/journey)
- [SELF-REPORTED, undated, earlier snapshot] A second URL on the same site shows "Our Journey to $418,387.38" with 7,748 sales (from search results; an earlier or cached state of the same counter). — [draculatheme.com/journey](https://draculatheme.com/journey)
- [CALCULATION, labelled] $442,775.23 / 8,101 sales = $54.66 average revenue per sale. Inputs are both self-reported from the same page; whether the dollar figure is gross or net of Gumroad fees is not stated.
- [PRIMARY, live 2026-11-24] Dracula Pro price $79 list ($47 at 40% off), one-time, up to 3 devices, 30-day refund, checkout through Gumroad; includes 20 themes, 8 variants and 4 monospaced fonts. — [draculatheme.com/pro](https://draculatheme.com/pro)
- [SELF-REPORTED, STALE, about 2020-2021] Zeno Rocha's Indie Hackers posts record $3,149.37 in under 24 hours at launch, "From $0 to $20,145.92 in 2 months" and "How I made $101,578.04 selling colors online". Posts could not be opened (HTTP 403), so exact dates are unconfirmed. — [Indie Hackers post](https://www.indiehackers.com/post/how-i-made-101-578-04-selling-colors-online-1690e49618)
- [PRIMARY, live 2026-11-24] Monokai Pro is offered for Sublime Text, VS Code, Cursor, JetBrains, Terminal.app and iTerm2 among others; it can be evaluated indefinitely and a licence removes registration pop-ups; one licence covers any number of the licensee's own computers. Neither page fetched showed the current price. — [monokai.pro](https://monokai.pro/); [monokai.pro/license](https://monokai.pro/license)
- [SELF-REPORTED, 2017, STALE] Monokai Pro's licence was €9.95 at launch. — [monokai.com article](https://monokai.com/articles/monokai-pro-beautiful-functionality-for-professional-developers/)
- [PRIMARY, live 2026-11-24] JetBrains Marketplace: "The commission on each plugin purchase is set to 15%"; it "can never be more than 25%" and changes require one month's notice; reseller commissions come out of JetBrains' share; payouts are monthly once $200/€200 is reached. The page covers paid plugins and does not mention themes specifically. — [JetBrains Marketplace docs](https://plugins.jetbrains.com/docs/marketplace/revenue-sharing-and-fees.html)
- [SECONDARY, vendor blog, March 2026] "The VS Code Marketplace is strictly for free distribution. There is no 'Buy' button and no API for checking if a user has paid"; the usual workaround is a free listing with features gated behind a licence key sold elsewhere. The author sells a payments product. — [Dodo Payments blog](https://dodopayments.com/blogs/sell-vscode-extensions)

### Inferences
- Dracula Pro's launch year is 2020 from my background knowledge, not from a page fetched in this session. If that is right, roughly $443K over about six and a half years averages under $70K a year as simple arithmetic on self-reported figures. The early Indie Hackers milestone titles ($20,145.92 in 2 months, later $101,578.04) suggest revenue was front-loaded, but their dates were not confirmed.
- A paid VS Code theme has to be sold off-marketplace (own site, Gumroad or similar) with its own licence handling; JetBrains is the only editor ecosystem found here with built-in billing.

### Gaps
- No official 2026 Microsoft statement on paid VS Code extensions was found; the "no native paid extensions" status rests on third-party sources.
- Monokai Pro's current price and any sales data are unknown. No revenue disclosure found for Shades of Purple or any other paid VS Code theme.
- Whether JetBrains permits paid pure-theme plugins, and under which terms, was not confirmed on the commission page.
- Raycast themes/extensions and terminal-theme monetisation: nothing citable found; not researched in depth.

---

## 5. UI kits and design-system files (UI8, Untitled UI, Figma Community)

### Takeaway
Untitled UI publishes prices but not revenue: its only revenue numbers are third-party guesses. Figma Community charges a flat 15% on paid resources but is not approving new sellers, which closes that channel to a newcomer.

### Cited Findings
- [PRIMARY, live 2026-11-24] Untitled UI, one-time pricing with lifetime updates. Figma kit: PRO SOLO $129 (list $149), STUDIO $399 (up to 8 users), BUSINESS $999 (up to 20), ENTERPRISE $2,499. React library: PRO SOLO $349 (list $499), STUDIO $999, BUSINESS $2,499, ENTERPRISE $8,999. Icons: PRO SOLO $59. "Pay once, use forever in unlimited projects." — [untitledui.com/pricing](https://www.untitledui.com/pricing)
- [SECONDARY, undated] An Indie Hackers post describes Jordan Hughes building Untitled UI "to nearly 100,000 users within 3 years" (users, not paying customers). — [Indie Hackers](https://www.indiehackers.com/post/how-jordan-hughes-built-a-template-biz-to-nearly-100-000-users-within-3-years-5c17a546a4)
- [THIRD-PARTY ESTIMATE, December 2023, STALE] A blogger estimated "$25,000+ each month" by assuming 5 sales a day; this is an assumption, not a disclosure. A separate database lists estimated annual revenue of $171,110. The two estimates conflict. — [Goodreads-hosted post](https://www.goodreads.com/author_blog_posts/24333927-this-daily-practice-helps-him-earn-25k-each-month?tab=book); [Prospeo](https://prospeo.io/c/untitled-ui-revenue)
- [PRIMARY, live 2026-11-24] Figma Community paid resources: flat 15% fee per sale; only approved individual creators may sell; "We are not approving new creators to sell paid files on Community at this time"; $2 minimum price; cash-out available 30 US business days after a sale; buyers can self-refund within 24 hours. — [Figma Help](https://help.figma.com/hc/en-us/articles/12067637274519-About-selling-Community-resources)
- [SECONDARY, conflicting] UI8 author share is reported as 70% on standard sales and 90% on "exclusive sales" in text quoted on a review site, and as 60-70% elsewhere. UI8's own sell page returned HTTP 403. — [Trustpilot page](https://ca.trustpilot.com/review/www.ui8.net?page=5); [TemplateTrip](https://www.templatetrip.com/blog/top-websites-to-sell-figma-templates-2026)

### Inferences
- Untitled UI now prices its coded React library ($349 solo) well above its Figma file ($129 solo), which shows the coded version carrying the higher price point within the same product line.

### Gaps
- No founder-disclosed or verified revenue for Untitled UI.
- UI8's commission terms are unverified at primary level; no UI8 payout statistics found.
- No distribution-of-earnings data for Figma Community sellers.

---

## 6. Documented effect of AI code generation on the segment, 2025-2026

### Takeaway
Named founders and companies have attributed large declines to AI: Tailwind Labs (revenue down close to 80%, docs traffic down about 40%, layoffs, then absorbed by Shopify with paid products closed to new buyers), ThemeSelection (monthly sales from 280 to 130, earnings down nearly 50%), ShipFast (from $126,000 to $2,000 a month) and Envato ("challenging market conditions", a flat 50% fee). Documented responses are pivots toward shadcn-based products, AI-bundled subscriptions, acquisition, and withdrawal from sale.

### Cited Findings
- [SELF-REPORTED, 2026-01-07] Wathan attributed the layoffs to "the brutal impact AI has had on our business" (as quoted in press) and wrote that revenue was "down close to 80%" while docs traffic was "down about 40% from early 2023". — [GitHub PR #2388](https://github.com/tailwindlabs/tailwindcss.com/pull/2388); [DevClass](https://www.devclass.com/ai-ml/2026/01/08/tailwind-labs-lays-off-75-percent-of-its-engineers-thanks-to-brutal-impact-of-ai/4079571)
- [PRIMARY, 2026-09-09] Tailwind Labs joined Shopify and closed Tailwind Plus and ui.sh to new customers. — [tailwindcss.com blog](https://tailwindcss.com/blog/tailwind-is-joining-shopify)
- [SELF-REPORTED, 2025-12-19] ThemeSelection wrote that AI tools generating templates and UI components sharply reduced demand for traditional admin templates and that AI Overviews cut click-through (7% to 2%); monthly sales fell from 280 (Jan-Jul 2024) to 130 (second half of 2025). In the same period its new shadcn/studio product recorded 550+ sales from September 2025, 210+ of them in November 2025. — [ThemeSelection blog](https://themeselection.com/blog/2025-wrapped-year-in-review/)
- [SELF-REPORTED, 2026-10-20; VERIFIED 2026-11-24] ShipFast: $126,000/mo (2024), $25,000/mo (2025), $2,000/mo (2026); $548 in the 30 days to 24 November 2026. The founder's post itself names no cause; a secondary article says he attributed it mainly to AI in a September 2026 post. — [marclou.com](https://marclou.com/tweets/shipfast-went-from-0-mo-to-126-000-mo-then-back-down); [TrustMRR](https://trustmrr.com/startup/shipfast); [aiidelist](https://aiidelist.com/blog/shipfast-revenue-collapse-marc-lou-2026.md)
- [PRIMARY, 2026] Envato cited "challenging market conditions for some time" and customers moving toward subscriptions and bundles when it cut author terms to a flat 50%. Envato's statement does not name AI. — [Envato Author Hub](https://author.envato.com/hub/changes-to-envato-market-revenue-share-and-exclusivity-what-you-need-to-know/)
- [PRIMARY, 2025-01-22] Vercel (maker of v0) acquired Tremor and made its paid blocks free under MIT; the founders now work on components for "the Vercel Dashboard, v0, and more". — [Vercel blog](https://vercel.com/blog/vercel-acquires-tremor)
- [PRIMARY, live 2026-11-24] Creative Tim's home page now leads with an AI App Builder, hosted AI agents and credit-based annual subscriptions ($199-$599/year). — [creative-tim.com](https://www.creative-tim.com/)
- [OPINION, 2026] Counter-argument published on DEV: the Tailwind revenue loss was caused less by AI itself than by the free shadcn/ui, which AI tools default to. This is commentary, not data. — [DEV Community](https://dev.to/adioof/tailwind-laid-off-75-of-engineering-ai-didnt-do-that-shadcn-did-1njm)
- [SELF-REPORTED, single seller, July 2025] FlutterFlow Marketplace seller reported sales falling from 1-2 a day to 2 in a month; no cause established. — [FlutterFlow community](https://community.flutterflow.io/discussions/post/sudden-drop-in-flutterflow-marketplace-sales---seeking-insights-july-2025-iCPPrpsJrIbLdZC)

### Inferences
- Every dated revenue series found for this segment points down from a 2024 peak: Tailwind (about -80% by January 2026), ThemeSelection (monthly unit sales -54% from early 2024 to late 2025, computed from 280 and 130), ShipFast (-98% from the 2024 to the 2026 monthly figure, computed from $126,000 and $2,000). I found no named founder in this segment publicly reporting growth over the same period, other than ThemeSelection's new shadcn-based product line.
- The mechanism named by two independent founders (Wathan, ThemeSelection) is the same: loss of search/docs traffic that used to convert into template sales, in addition to substitution by generated UI.

### Gaps
- No traffic dataset (e.g. Similarweb) was obtained for template sites; the traffic figures above are founder-reported.
- No public statements with numbers found from Cruip, Flowbite, Untitled UI, shadcnblocks, Aceternity, Magic UI, MakerKit or supastarter about AI's effect on sales.
- Causation is asserted by the founders, not independently measured; lifetime-licence saturation and free alternatives (shadcn/ui) are confounders raised in commentary.
- No documented shutdowns of template shops attributed to AI were found beyond Tailwind Plus closing to new customers and the Bootstrap Themes marketplace closure (whose stated reasons I could not read).

---

## 7. Distribution of outcomes

### Takeaway
Available data show a steep power law: third-party analyses of Gumroad put the median creator at about $70 a month or year depending on the dataset, and directly fetched TrustMRR boilerplate listings range from $199 to $1.27M lifetime, with even the largest now earning $548 a month.

### Cited Findings
- [VERIFIED, fetched 2026-11-24] Lifetime revenue of four processor-verified boilerplates on TrustMRR: ShipFast $1,273,440 (last 30 days $548); MkSaaS $109,826 (last 30 days $1,099); TurboStarter $85,610 (last 30 days $3,401); Nuda Kit $199. This is a convenience sample of four listings, not the full category. — [ShipFast](https://trustmrr.com/startup/shipfast); [MkSaaS](https://trustmrr.com/startup/mksaas); [TurboStarter](https://trustmrr.com/startup/turbostarter); [Nuda Kit](https://trustmrr.com/startup/nuda-kit)
- [SECONDARY, 2020 data, STALE] The median Gumroad creator made about $70 in 2020 and the top 1% of creators earned about 60% of payouts; Gumroad processed $142M in 2020. — [Silicon Florist](https://siliconflorist.com/2021/01/12/what-happened-in-the-gumroad-creator-community-in-2020/); [Sacra](https://sacra.com/research/gumroad-android-creator-economy/?highlight=podia)
- [THIRD-PARTY ESTIMATE, 2026, internally inconsistent] A scraped dataset claims fewer than 5% of Gumroad creators make over $1,000 a month, a median of $72 a month, and that 44% of products earn $0; its own pages give conflicting concentration figures (top 1% capturing 99.5% vs 77.3% of revenue). Another third-party site reports about 2.5% of Gumroad products have a recorded sale. Not official Gumroad data. — [InsightRaider](https://insightraider.com/en/data/gumroad-statistics-2026); [profitable.app](https://profitable.app/gumroad/stats)
- [PRIMARY, live 2026-11-24] ThemeForest admin templates: 2,802 items; the top item has 120.4K sales, the tenth 8.4K. — [ThemeForest](https://themeforest.net/category/site-templates/admin-templates?sort=sales)
- [PRIMARY, live 2026-11-24] CodeCanyon Mobile: 14,080 items; the top item has 7.3K sales, the tenth 3.4K. — [CodeCanyon](https://codecanyon.net/category/mobile?sort=sales)

### Inferences
- In the ThemeForest admin category the best seller has about 14 times the cumulative sales of the tenth best seller (120.4K / 8.4K), out of 2,802 items; the distribution below rank ten was not sampled.
- Among verified boilerplates, current monthly revenue does not track lifetime revenue: the product with the largest lifetime total (ShipFast) had the lowest trailing-30-day figure of the three with data.

### Gaps
- No official earnings distribution is published by Gumroad, Envato, Polar or TrustMRR for the template/boilerplate category specifically. A full TrustMRR category listing was not retrieved, and search-engine snippets of TrustMRR pages were contradicted by the live pages, so they were discarded.
- Sales counts for ThemeForest/CodeCanyon items outside the top ten (median and long tail) were not collected.
- No Indie Hackers verified-revenue listing for templates was retrieved (Indie Hackers pages returned HTTP 403).
