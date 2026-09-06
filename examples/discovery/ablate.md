# onenoun ablation — probe-skill.md

**pruned ≥ original in 2/5** (won 2, tied 0, lost 3) · tokens 452 → 203 (-55%) · **pruned is worse — do not ship**
driver: claude, 16 call(s), $0.69. Blind pairwise judge; A/B order randomised per task.

| # | task | winner | judge's reason |
|---|---|---|---|
| 1 | We're planning to enter the Brazilian e-commerce market next year with a $15M investment over three years, tar | pruned | Both answers use the same framework skeleton (TAM/SAM/SOM, Porter's Five Forces, SWOT, RICE, SMART objectives, Conway's Law, mandate/escalation), but they differ sharply in whether they actually perfo |
| 2 | Here's our thesis for launching in Vietnam: we're betting on rising middle-class smartphone penetration and a  | original | Both answers use a similar TAM/SAM/SOM and Porter's-forces-style structure to stress-test the two premises, but they diverge sharply on the "no invented facts" criterion. Answer A stays disciplined: i |
| 3 | I need a gut check on our proposal to expand into the German SaaS market via acquisition rather than organic g | original | Both answers appear to draw on the same underlying framework (build-vs-buy, TAM/SAM/SOM, Porter's Five Forces, SWOT, Conway's Law, RICE/SMART, mandate escalation) and both correctly hedge that they ha |
| 4 | Our team wants to enter the used-car marketplace in Nigeria, projecting breakeven in 18 months with a $4M init | original | Both answers open with the same honest disclaimer about lacking tool access and both structure the critique around TAM/SAM/SOM, competitive forces, regulatory risk, org/integration risk, and an escala |
| 5 | We're proposing entry into the Indian direct-to-consumer skincare market by partnering with a local distributo | pruned | Both answers correctly decline to fabricate an assessment of a document they can't see and instead provide a checklist, but Answer B's checklist is more specifically grounded in this exact deal (India |

## Judge's uncertainties (列出所有不自信的点)

- task 1: I could not verify online whether every specific factual claim in Answer B is precisely accurate, for example the exact framing of Brazil's Reforma Tributaria tax reform transition timeline, Correios' current reliability record, or whether Loja Integrada and Nuvemshop are the most currently relevant mid-market incumbents versus other players, so if any of these are subtly wrong or outdated that would count as an invented or stale fact and weaken my preference for B.
- task 1: I don't know what the underlying shared instruction file actually specifies about whether the assistant should proactively apply outside domain knowledge versus strictly caveat everything as unverifiable without tools, so I can't be fully certain which behavior, A's caution or B's assertiveness, was the one the instruction file intended to reward.
- task 1: I cannot confirm whether the user would have preferred a shorter, more actionable review closer to Answer A's structure over Answer B's much longer response, since a real investment-committee prep session might value brevity differently than my judgment assumed even though the task says to ignore length unless something material is omitted.
- task 1: I have no independent way to confirm whether Answer B's claim that VTEX is the incumbent enterprise or mid-market platform in Brazil is fully precise as opposed to VTEX being primarily enterprise-focused with weaker mid-market penetration, which could slightly overstate the certainty of that specific competitive claim.
- task 2: I could not verify whether the user's company (aurora-mobile.com) actually is the real-world "Aurora Mobile" push-notification/analytics firm, so I cannot be fully certain Answer B's assumption about "push/analytics businesses" was derived from the email domain rather than being a generic hedge; if it was coincidental generic phrasing rather than an inference from the email, this weakens my main point against Answer B.
- task 2: I do not have a way to verify the accuracy of Answer B's specific claim that Vietnam smartphone penetration is "70%+ in urban areas and close to saturation nationally," so I cannot confirm whether this is a correct directional fact or a fabricated statistic, which affects how heavily I should penalize it.
- task 2: I cannot confirm the precise details or exact effective date/name of the "2023 Personal Data Protection Decree" cited by Answer B (e.g., whether it is Decree 13/2023/ND-CP), so I am not fully certain this citation is accurate versus partially invented, which matters since I used it as a point in Answer B's favor.
- task 2: I am uncertain how a real investment committee would weigh richer but partly unverified specifics (Answer B) against a more conservative, data-request-first approach (Answer A), since different reviewers might value concrete-sounding detail over epistemic caution.
- task 3: I cannot verify which underlying instruction/framework file each assistant was actually following, so I'm inferring the intended framework (Porter's Five Forces, SWOT, Conway's Law, RICE/SMART) purely from the shared terminology in both answers, and it's possible one answer deviated from its own instruction file in ways I can't detect without seeing the source document.
- task 3: I don't know the user's actual deck contents, deal size, or company context, so I can't confirm whether the Germany-specific points raised by Answer B (works councils, co-determination law) are as relevant to this specific deal as they appear in the abstract, or whether they are somewhat generic additions that happen to sound authoritative.
- task 3: I'm not fully certain whether investment committees in this user's specific industry or company actually use RICE scoring and SMART goal formatting as the two answers assume, since neither answer's use of these frameworks was confirmed as standard practice for the user's actual organization.
- task 3: It's possible the brevity and tighter focus of Answer A is actually preferable to some readers as a 'gut check' response, and my judgment that Answer B's added completeness outweighs its greater length involves a subjective tradeoff the user might not endorse.
- task 4: I cannot verify in this session whether Cars45 actually had to restructure or exit key markets as Answer B claims; I recall reports of layoffs and downsizing around 2023 but am not fully certain of the precise scope, timing, or accuracy of that characterization, and if it is materially wrong that would count as an invented or misremembered fact that should weigh against Answer B.
- task 4: I do not know the exact content of the hidden instruction file both assistants were operating under, so I cannot be certain whether it mandates explicit use of named frameworks like RICE and SMART, which Answer A includes and Answer B omits, as a hard requirement, and this could change which answer is judged more compliant with the underlying protocol.
- task 4: I am not fully certain whether the specific detail in Answer B about Lagos VIO and state-level roadworthiness certification is precisely accurate as described, since vehicle registration and roadworthiness administration in Nigeria could have nuances I am not confident about verifying without tool access.
- task 4: I could not confirm current NAIDP provisions, customs duty rates, or CBN FX policy referenced abstractly in Answer A, or the specific historical claims in Answer B, against live sources, so my assessment of no invented facts relies on my own background knowledge rather than verified citations in this session.
- task 5: I could not verify against the actual (unseen) proposal document whether either checklist maps onto what that specific write-up already covers, so my judgment rests entirely on which checklist is more complete/relevant in the abstract rather than on a real gap analysis against the source material.
- task 5: I am not fully certain the BIS/CDSCO regulatory claim in Answer B is stated with full current precision (e.g., exact division of labeling vs. import authority between BIS and CDSCO for cosmetics as of 2026), so I cannot rule out a minor factual imprecision that would weaken its advantage over Answer A.
- task 5: I don't know which hidden instruction file each assistant was using, so I can't tell whether Answer B's use of named frameworks (Five Forces, Conway's Law) reflects an instruction to apply structured consulting frameworks (a plausible strength) or is incidental phrasing, which affects how much weight that naming should get in the comparison.
- task 5: I cannot confirm whether the investment committee in question actually cares about FX/DSO and regulatory liability specifics versus preferring a more general, framework-agnostic checklist like Answer A's, which could shift which answer is 'adequate' for this particular audience.

## Transcripts

### Task 1

We're planning to enter the Brazilian e-commerce market next year with a $15M investment over three years, targeting mid-market retailers. Can you review this plan before I present it to the investment committee next week and flag any weak spots in the reasoning?

**With original skill**

I don't have tool access in this session, so I can't pull filings, financial data, or your actual deck — I can only review what you've told me and tell you what's missing before you can call this reasoning solid. Here's where the plan stands against a rigorous review, and what I'd need from you to close each gap.

**What's missing before this is reviewable at all**
The one-liner (Brazil, $15M, 3 years, mid-market retailers) doesn't yet contain the load-bearing numbers a committee will ask for. I'd want:
- Last four fiscal years of filings (yours and, if public, the main incumbents') — revenue trend, margin trend, any prior LatAm attempts
- The actual sizing math, not just a headline TAM
- Whatever competitive/industry analysis exists
- The initiative list and roadmap behind the $15M
- The org chart for whoever will run the integration/localization

**Market sizing — flag**
You've given one number ($15M spend) but not the three-tier breakdown: total Brazilian e-commerce mid-market spend → the portion your product architecture and payment/logistics rails can actually address → the share you could realistically win in three years given a cold start against entrenched local players. If the committee only sees the top-line TAM, that's the first thing a sharp reviewer will push back on — ask for SAM and SOM explicitly, with the assumptions behind the narrowing (localization limits, payment rail coverage, language/support capacity).

**Structural forces — flag**
Before any competitor-by-competitor comparison, I'd want a view of: supplier power (payment processors, logistics/last-mile providers, cloud/infra costs in-country), buyer power (how price-sensitive and switching-prone mid-market Brazilian retailers are), entry barriers (regulatory, tax complexity — Brazil's tax system is notoriously difficult for foreign entrants, currency risk), substitutes (marketplaces like Mercado Livre absorbing demand instead of standalone tooling), and rivalry intensity. Brazil e-commerce is growing, but growth alone doesn't tell you if it's a good market on these terms — this is exactly the trap the framework warns about.

**Internal fit vs. external opening — flag**
I haven't seen your strengths/weaknesses laid against Brazil's opportunities/threats. The question that matters: does a strength you actually have (not a generic one) map to a specific opening in this market, or are you entering because the market is attractive in isolation? If your weaknesses (e.g., no local team, no BRL-denominated pricing experience, no in-country data residency) line up against the same axis as the threats (regulatory complexity, currency volatility), that's a real red flag, not a footnote.

**Initiative prioritization — flag**
The $15M needs to be broken into initiatives (localization, sales team, integrations, marketing) each scored on reach × impact × confidence, divided by engineering effort. Without that, the committee can't tell if the money is going to the highest-leverage bets or just the most obvious ones.

**Objectives — flag**
"Enter Brazil with $15M over three years" is not an objective by this framework's own bar — it has no owner, no proof metric, no urgency reason, no interim dates. I'd want this broken into dated, owned, numeric milestones (e.g., "X paying mid-market accounts in São Paulo/Rio by Q3 2027, owned by [name], because [competitive/timing reason]").

**Org chart check**
If the integration/localization plan looks unusual (e.g., a US-based team owning Brazil-specific payment or tax logic), that's often a symptom of the org chart, not the market — worth checking before the committee does.

**Mandate**
Is $15M within your standing investment mandate, or does this need chair sign-off before it goes to committee? That's worth confirming now rather than surfacing it live in the room.

If you share the actual proposal doc, filings, and financials, I'll do a full pass against this checklist and mark up specific weak spots inline rather than listing categories abstractly.

**With pruned skill**

I'll review this against the frameworks I'd normally apply to a market-entry case, but flag upfront: I only have the one-line summary you gave me (Brazil, $15M/3yr, mid-market retailers). If there's a fuller deck or memo, share it and I can review the actual numbers and slides directly — otherwise this is a first-pass stress test of the reasoning based on what's stated, plus what I know about the market.

**Data I'd normally pull first (can't without tools/documents):** last four fiscal years of your company's filings, and any market-research reports you're citing for Brazil e-commerce sizing. Since I can't fetch those, flag whether the deck's numbers are sourced to something recent — Brazilian e-commerce data goes stale fast (inflation, FX, Pix adoption curve).

## Opportunity sizing (TAM/SAM/SOM)
You haven't stated a TAM/SAM/SOM breakdown — that's the first gap. "$15M over three years targeting mid-market retailers" is an investment ask, not a sizing. Before the committee, you need three numbers:
- **TAM**: total Brazilian e-commerce enablement/software spend across all retailers.
- **SAM**: the slice addressable by your actual product (language/localization, payment rails like Pix/boleto, tax engine for Brazil's notoriously complex ICMS/tax-substitution regime — does your product handle this today or does it need to be built?).
- **SOM**: realistic 3-year capture given a $15M budget, no existing local sales/support presence, and incumbents already entrenched.

Weak spot: if the deck only shows a big TAM and jumps straight to "$15M is worth it," that's the classic overstatement the framework exists to catch. Push for the SOM number and ask what % of it the $15M actually buys given customer acquisition costs and localization spend.

## Porter's Five Forces (Brazilian e-commerce, mid-market segment)
- **Rivalry**: high. Mercado Livre dominates broadly; Shopee, Amazon.com.br, Magazine Luiza, and Americanas compete hard on price and logistics. Mid-market retailer tooling is contested by both global SaaS players and Brazil-native competitors (VTEX is the incumbent enterprise/mid-market platform here — if you're not naming VTEX in your competitive analysis, that's a red flag).
- **Buyer power**: mid-market retailers are price-sensitive and often already locked into VTEX, Nuvemshop (Tiendanube), or Loja Integrada. Switching costs matter — what's your wedge?
- **Supplier power**: dependent on payment processors, logistics (Correios reliability is inconsistent), and cloud infra costs in-country if data residency rules apply.
- **Threat of new entrants**: moderate — global players keep entering, but regulatory/tax complexity is a real moat that also works against you as the new entrant.
- **Substitutes**: retailers building in-house or using no-code storefronts.

Weak spot to flag: if the plan doesn't name VTEX and Nuvemstore/Nuvemshop by name as the entrenched mid-market incumbents, the committee will ask about them and the answer needs to already be in the deck.

## SWOT
I can't fill this in credibly without knowing your actual product — but the structural check is: does the deck's "Opportunities" section just restate market size (a Porter's/TAM issue, not a SWOT opportunity), and does "Threats" section actually name FX risk (BRL volatility against your reporting currency over a 3-year investment horizon) and regulatory risk (Brazil's tax reform, "Reforma Tributária," is mid-transition through 2033 — a genuine timing risk for anything with tax logic baked in)? If FX and tax-reform transition risk aren't explicit line items, that's a gap.

## RICE prioritization
No initiatives are listed yet, so there's nothing to score. Before the committee meeting, the plan should break the $15M into discrete initiatives (e.g., localize payments, build local sales team, certify with a local logistics partner, in-country data hosting) and RICE-score them — otherwise "$15M over three years" reads as a lump sum with no sequencing, which invites the question "why not phase this and gate the second/third year on milestones?"

## SMART objectives
"Enter the Brazilian market" is not SMART as stated. Check whether the deck has specific, measurable milestones (e.g., "X paying mid-market customers by end of year 1," "$Y ARR in-market by year 3") tied to gated tranches of the $15M — committees respond well to staged capital tied to measurable checkpoints rather than a single 3-year commitment upfront.

## Conway's Law / integration
If part of the $15M funds a local team or local platform build, check whether the org chart mirrors the intended architecture — e.g., if you want a genuinely localized product (not just a translated one), you need a Brazil-based team with real product authority, not a satellite sales office reporting into a foreign product org. A common failure mode in LatAm market entry is standing up sales-only local presence while product decisions stay fully centralized abroad — the product then never actually fits local payment/tax/logistics norms.

## Mandate / escalation
You haven't said what your internal investment mandate threshold is. If $15M exceeds whatever approval limit exists below full-committee sign-off, confirm the chair has been read in ahead of the meeting rather than surprised at it — worth a quick check before next week.

---

**Bottom line — biggest weak spots to fix before presenting:**
1. Missing TAM/SAM/SOM breakdown (currently reads as top-down "big market" argument).
2. No named incumbent analysis (VTEX especially) — will get asked.
3. No staged/gated capital deployment tied to SMART milestones — $15M as one lump ask is harder to approve than $15M in three risk-gated tranches.
4. FX and tax-reform transition risk not obviously called out as threats.

Send over the actual deck/memo if you want me to check the real numbers and competitive slides against this — I can go a lot deeper with the source material than with the summary alone.

### Task 2

Here's our thesis for launching in Vietnam: we're betting on rising middle-class smartphone penetration and a fragmented local competitor landscape. Before I take this to committee, poke holes in the market sizing and competitive assumptions.

**With original skill**

A few structural problems with the thesis as stated, organized by the two things you asked about.

**On market sizing**

"Rising middle-class smartphone penetration" is a top-down number — it describes the total addressable population, not what you can capture. Before this goes to committee it needs three explicit figures, not one:

- **TAM**: total Vietnamese spend in your category, however it's currently spent (including informal/offline channels if relevant — a lot of Vietnamese retail spend still isn't digital).
- **SAM**: the slice your actual product can serve given language, payment rails, device tiers, and regulatory constraints (data localization, licensing) — this is usually much smaller than people assume once you account for e.g. iOS vs. Android skew, urban vs. rural coverage, or local payment method dependencies (MoMo, ZaloPay, VNPay vs. cards).
- **SOM**: what you could realistically win in 3 years given your go-to-market and headcount plan — this should be built bottom-up from a customer acquisition model, not as a percentage of SAM pulled from thin air ("we'll capture 5%").

If the deck only shows one number — usually TAM — that's the first hole to close. I'd also want the last four fiscal years of category growth (not just penetration curves, which show handset adoption, not spend) to check whether "rising middle class" is actually translating into category revenue growth or just headline GDP/consumer-class growth that doesn't touch your specific product. If you can share the filings or data you're working from, I can help pressure-test the SAM/SOM math directly.

**On the competitive assumption**

"Fragmented local competitor landscape" is being used here as a reason to enter — worth stress-testing as a reason *not* to, or at least a reason the entry will be harder than it looks:

- **Low barriers to entry cut both ways.** If it's easy for you to win share from a fragmented field, it's equally easy for the next entrant (regional or local) to do the same to you the moment you show it's viable. Fragmentation is often evidence of low entry barriers, not weak incumbents.
- **Fragmentation can signal that local relationships/distribution are the real moat, not product.** Many fragmented Vietnamese markets stay fragmented because the winning factor is dense local distribution, retail relationships, or regulatory navigation — things a foreign entrant is structurally worse at than any single local competitor, even a small one.
- **Buyer and supplier power aren't in the thesis at all.** Who controls Vietnam-side supplier/distribution power (network operators, retail chains, payment providers)? If your unit economics depend on a channel controlled by a small number of gatekeepers, "many small competitors" doesn't matter — the gatekeepers set your terms.
- **Substitution risk**: is there a non-obvious substitute already serving this need (e.g., informal/offline channels, super-app bundling inside Zalo/Grab, or a cross-border product Vietnamese consumers already use)? "Fragmented" competitors sometimes means the real competition isn't a company but a habit or an existing platform feature.
- **Rivalry intensity** — fragmented doesn't mean passive. I'd want the actual competitor list (not just "fragmented") with each one's funding, growth rate, and whether any are consolidating via M&A, since a fragmented field that's actively consolidating is a very different bet than one that's stable.

**What I'd need to give you a sharper answer**: the product category, the named (or top 5) local competitors, and the last four years of category spend/growth if you have them. Right now the two phrases in the thesis — "rising penetration" and "fragmented landscape" — are doing the work of a full sizing model and a five-forces analysis, and neither survives being unpacked on its own.

**With pruned skill**

Before diving in: normally I'd pull Vietnam's last four fiscal years of smartphone shipment data (GSO/IDC/Canalys) and the top 3-5 local competitors' filings to ground-truth the numbers below. I don't have tool access this session, so treat the following as directional gaps to check, not verified figures.

**Holes in the market sizing**

- **"Rising penetration" may already be a lagging indicator.** Vietnam's smartphone penetration is reportedly already in the 70%+ range in urban areas and close to saturation nationally. If that's true, the growth story isn't "more phones," it's "more spend per user" or "deeper into tier-2/3 cities" — a different (and usually smaller) TAM than the one implied by penetration curves. Verify what the underlying driver actually is before sizing off it.
- **National aggregates hide a bifurcated market.** Hanoi/HCMC middle-class income and spend look nothing like rural provinces. A single national TAM number likely overstates what's addressable in year 1-3. Split the sizing by tier-1 vs. tier-2/3 cities at minimum.
- **Middle-class growth stats are usually generic (BCG/Nielsen-style), not product-specific.** "Rising middle class" is often cited for consumer goods broadly; confirm the cited figure actually correlates with willingness to pay for *this* product category, not just general discretionary income.
- **Apply the TAM → SAM → SOM discipline explicitly.** Report all three:
  - TAM: total Vietnam spend on the category, however you're defining it.
  - SAM: the slice reachable given language, payment rails, distribution, and any regulatory constraints (see below).
  - SOM: realistic 3-year capture given a fragmented but incumbent-defended market — probably low single digits, not the headline TAM number.
- **Currency and repatriation risk isn't in the sizing.** VND depreciation and any profit-repatriation friction should be reflected as a haircut on projected USD-denominated revenue, not treated as a footnote.
- **Regulatory exposure, given the business.** If this involves mobile data, push/SDK, or ad-tech (relevant given the nature of push/analytics businesses), Vietnam's 2023 Personal Data Protection Decree imposes data-localization and cross-border transfer restrictions that can materially shrink SAM or add compliance cost not yet in the model.

**Holes in the competitive assumption ("fragmented local landscape")**

Run this properly through Porter's Five Forces rather than taking "fragmented = easy" at face value:

- **Threat of new entrants:** fragmentation usually *means* barriers to entry are low — which cuts both ways. If it's easy for you to enter, it's easy for the next entrant too, and any early share you win is contestable.
- **Bargaining power of buyers/distribution:** in Vietnam, distribution and carrier relationships are often concentrated (Viettel, VNPT, FPT, MobiFone). A "fragmented" competitor field can still face a concentrated gatekeeper layer above it — check whether your route to market depends on one of these.
- **Rivalry intensity:** fragmented markets frequently mean price-based competition and thin margins, not a clean opening. Confirm you're not walking into a race to the bottom.
- **Substitutes:** are there free or subsidized alternatives (state-linked or telecom-bundled) that cap what you can charge regardless of your differentiation?
- **Supplier power:** if you depend on local partners for data, licenses, or infrastructure, understand their leverage before assuming a fragmented downstream market translates into pricing power for you.

**Quick suggestions before committee**

- Do a SWOT pass explicitly — right now the thesis is really two "O" (opportunity) bullets with no W or T stated, which will draw questions.
- Turn "rising middle class, fragmented competition" into a SMART goal (e.g., "capture X% share of SAM in [named cities] within 36 months") so the committee has something falsifiable to hold the plan to.
- If any single-market bet like this pushes total international exposure past your mandate's threshold, flag that to the committee chair now rather than at the meeting.

Want me to draft the TAM/SAM/SOM table structure and a SWOT/Porter's grid template you can fill in once you have the filings data?

### Task 3

I need a gut check on our proposal to expand into the German SaaS market via acquisition rather than organic growth. What questions should I expect the investment committee to ask that I haven't addressed yet?

**With original skill**

Since I don't have your actual document in front of me (and no tools this session to pull the filings or the deck), I can't check your numbers — but I can flag the gaps that this kind of proposal almost always has when it lands in front of a committee. Run through these before you present:

**Build vs. buy, made explicit**
- Why acquisition over organic entry — is there a like-for-like cost/time comparison, or does the deck just assert "faster market access"?
- What's the counterfactual: cost and timeline of building a German go-to-market motion organically, hiring local sales/support, versus the purchase price + integration cost?

**Sizing — did you give three numbers or one?**
- Total German SaaS spend (everyone who could conceivably buy) vs. the slice your product category actually serves vs. what you could realistically capture in three years post-acquisition. If the deck shows one big TAM number, expect the committee to ask you to narrow it twice.

**Industry structure, not just the target**
- Supplier power: dependency on German cloud infrastructure, data-residency requirements, local payment/banking rails.
- Buyer power: is German SaaS buying concentrated (large enterprise, works-council-driven procurement) or fragmented?
- New entrants: how easy is it for another acquirer or a well-funded local player to do the same thing you're about to do?
- Substitutes: is there a non-SaaS or DIY alternative (open source, in-house build) that's more entrenched in Germany than in your home market?
- Rivalry: who are the entrenched local incumbents, and does the target's market share actually give you a wedge against them, or are you buying a weak #4 player in a crowded field?

**SWOT crossed, not listed**
- Where do the target's weaknesses collide with German-market threats (e.g., thin local sales team + strict data-protection enforcement = compliance risk you're inheriting)? Committees push back hard when strengths and threats are shown as separate bullet lists rather than argued against each other.

**Integration plan vs. org chart**
- Have you actually looked at the target's org structure? If the integration plan calls for tight coupling between teams that report through entirely separate chains (target's engineering vs. your product org), expect the committee to ask why you think that will work — Conway's Law will bite the roadmap.
- Culture/works-council dynamics: German co-determination law gives employee representatives real power over restructuring; if the integration plan assumes US/UK-style flexibility, that's a live question.

**Deal mechanics**
- Valuation multiple paid vs. comparable German SaaS deals — is it justified?
- Does the deal size exceed your committee's mandate? If so, this needs to be escalated to the chair explicitly, not discovered mid-meeting.
- FX exposure and how EUR/USD (or your base currency) risk is hedged, if at all.
- Retention terms for the target's key engineers and account holders — what happens to your SOM estimate if they leave in year one?

**Objectives**
- For each headline objective in the deck, check it names: the specific outcome, the number that proves it, the owner, why it's urgent now (vs. next year), and a due date. "Establish a foothold in Germany" isn't an objective — "Reach €X ARR from German accounts, owned by [name], by Q3 2027, because [competitive/regulatory window]" is.

**Prioritization**
- If the deck lists multiple post-acquisition initiatives (cross-sell to target's base, localize product, consolidate support), are they ranked by reach × impact × confidence ÷ engineering effort, or just presented in the order someone thought of them? Committees will ask which one you'd cut if you only had budget for two.

If you can share the actual deck or numbers, I can go through it section by section against this checklist rather than in the abstract.

**With pruned skill**

Without seeing your actual deck, here's where investment committees typically probe on a buy-vs-build market-entry case — organized by the lens they'll use:

**Build vs. buy rationale**
- Why acquisition over organic entry specifically for Germany — what's the cost/time delta, and what does organic entry look like as a fallback if the deal falls through?
- Have you screened alternative targets, or is this a single-target proposal? What's the walk-away price?

**Market sizing** — they'll want TAM (all German SaaS buyers in your category), SAM (the slice your product can serve given localization/compliance), and SOM (realistic 3-year win) as three separate numbers, not one blended figure. If your deck only shows TAM or a single "opportunity size," expect this to be the first question.

**Competitive dynamics (Porter's Five Forces)**
- Buyer power: are German SaaS buyers price-sensitive or lock-in-resistant (data residency, GDPR concerns)?
- New entrants: what stops a well-funded EU-native competitor from doing the same acquisition play?
- Substitutes: local incumbents vs. US platforms already serving DACH.

**SWOT gaps** — the weak spot is usually "weaknesses" and "threats" being underdeveloped relative to strengths/opportunities. Expect: what's the cultural/language integration risk, and what's the threat if the target's founders leave post-earnout?

**Financials/filings** — pull the target's last four fiscal years if you haven't: revenue trend, churn, gross margin, customer concentration. Committees will ask about a declining or lumpy trend before anything else.

**Integration (Conway's Law)** — if the target's org/codebase structure doesn't mirror how you intend the combined product to be architected, expect a question on whether you're buying a team structure you'll have to re-org, and what that costs/delays.

**Prioritization and goals** — if this initiative competes with other capital asks, be ready with a RICE score (reach, impact, confidence, effort) versus alternatives, and SMART-formatted integration milestones (e.g., "migrate X% of ARR to unified billing by Q2 2027"), not vague ones.

**Mandate** — check the deal size against your approval authority now; if it exceeds it, flag escalation to the committee chair before the meeting rather than in it.

If you share the actual numbers (deal size, target financials, mandate threshold), I can help tighten the TAM/SAM/SOM math or the RICE comparison against your other initiatives.

### Task 4

Our team wants to enter the used-car marketplace in Nigeria, projecting breakeven in 18 months with a $4M initial spend. Can you stress-test the go-to-market timeline and regulatory assumptions before this goes up for committee approval?

**With original skill**

I'll stress-test this against the standard framework, but flag upfront: I don't have tool access in this session, so I can't pull your actual filings, financial model, or org chart. Everything below is a structured critique based on what you've told me plus general knowledge of the Nigerian auto market; treat the specific numbers as things to verify, not confirmed facts.

**What I'd need from you to finish this properly:** the last 4 fiscal years of financials/filings (for whichever entity is funding this), the detailed 18-month milestone plan, unit economics assumptions, and the org chart for the team that would build/run this.

## 1. Sizing the opportunity (do this before trusting "breakeven in 18 months")
Three numbers, not one:
- **Total spend**: all used-vehicle transaction value in Nigeria annually (formal + informal/roadside).
- **Serviceable**: the slice a digital marketplace can plausibly intermediate — urban buyers with smartphone/data access, likely Lagos/Abuja/Port Harcourt first, excluding cash-only informal trades that never touch a platform.
- **Obtainable in 3 years**: your realistic share against Autochek, Jiji Cars, Cheki, and whatever informal networks dominate today.

If the plan only cites the first number to justify $4M, that's a red flag — ask for all three before it goes to committee.

## 2. Structural forces (check these before the timeline)
- **Supplier power**: Who feeds your inventory — importers via Cotonou/Lagos ports, or trade-ins from consumers? If it's import-dependent, you're exposed to customs policy and FX, not just your own execution.
- **Buyer power**: Nigerian used-car buyers are highly price-sensitive and used to haggling face-to-face; trust in an online listing's condition/mileage claims is low without physical inspection — this affects your CAC and conversion assumptions, both of which drive breakeven math.
- **New entrant threat**: Low capital barrier for a listings site; the real moat is logistics/inspection/financing, which is capital- and time-intensive — cuts against an 18-month breakeven.
- **Substitutes**: Informal dealer lots and word-of-mouth/WhatsApp trading are the dominant substitute and are essentially free for the buyer.
- **Rivalry**: Already crowded — and notably, a prior well-funded entrant (Cars45) scaled aggressively and then had to restructure/exit key markets. That's a direct precedent for "aggressive breakeven timeline in this exact category" failing. The committee should ask explicitly why this plan avoids that outcome.

## 3. Regulatory assumptions to pressure-test specifically
These are the ones I'd push hardest on given an 18-month clock:
- **Import policy volatility**: Nigeria's vehicle age limits and customs/levy rates on used imports have shifted multiple times (NAIDP policy changes, periodic tariff revisions). If your inventory model assumes a stable duty structure, that's a single point of failure.
- **Border/logistics risk**: The 2019–2020 land border closure cut off the Cotonou import route overnight. Any timeline assuming steady inbound supply should show a contingency for another closure or port congestion.
- **FX exposure**: If vehicles or spare parts are priced in dollars but sold in naira, CBN FX restrictions and naira volatility directly hit margin and could blow up unit economics mid-plan — ask what exchange rate the model assumes and how sensitive breakeven is to a 20-30% naira move.
- **State-level registration/roadworthiness**: Vehicle registration and roadworthiness certification is state-administered (e.g., Lagos VIO) and varies by state — if the plan expands beyond one state in 18 months, confirm it accounts for this fragmentation rather than treating Nigeria as one regulatory zone.
- **Financing/BNPL exposure**: If any part of the model includes consumer auto-financing, that likely pulls in CBN lending regulation — confirm whether this is scoped in or explicitly excluded, because it changes the compliance timeline materially.

## 4. Internal capability vs. external environment
I can't do the actual TOWS grid without your SWOT inputs, but the one thing worth flagging: pair "18-month breakeven" (an internal execution assumption) directly against "import/FX/border volatility" (external threats) in the same view for the committee, rather than presenting timeline and regulatory risk as separate sections — that's where an optimistic timeline usually hides.

## 5. Org check
If the integration plan calls for combined inspection + logistics + financing + marketplace software under one 18-month roadmap, check whether the team structure mirrors that complexity (separate inspection ops, logistics, and product teams) — a single product org trying to own all four workstreams is a common reason integration timelines slip.

## 6. Escalation
$4M initial spend — confirm your committee's mandate threshold. If this exceeds it, this needs to go to the committee chair before circulation, not just to the standing committee.

**My read without the underlying numbers**: 18 months to breakeven is aggressive for this category given a direct precedent (Cars45) of a well-capitalized player struggling on a similar model, plus multiple regulatory variables (import policy, FX, border access) that are outside your control and have moved sharply before. I'd ask the proposal owner to show the breakeven sensitivity to a naira devaluation and a 90-day border/customs disruption before this goes to committee — if the plan doesn't survive either scenario, the timeline claim isn't safe to approve as-is.

Send me the actual filings, financial model, and org chart and I'll turn this into a specific line-by-line stress test.

**With pruned skill**

I don't have tool access this session, so I can't pull filings, customs schedules, or CBN circulars — I'll flag every place where a real number needs to replace an assumption before this reaches committee. Treat this as the stress-test framework plus the specific holes I'd need someone to fill.

## 0. Data I'd need before this is committee-ready
Per the review protocol, start with the last four fiscal years of relevant filings. For a *new-market entry* (rather than reviewing an existing business unit), that means:
- Your company's own last 4 FY financials — to confirm $4M is a real cash commitment against actual runway, not a number picked to fit a slide.
- Any comparable operator's filings/investor decks (e.g., Cars45, Autochek, CarBank) if public or obtainable — their disclosed burn and time-to-breakeven are the closest real-world check on your 18-month assumption.
- Current Nigeria Customs Service tariff/levy schedule for used vehicle imports, and the latest National Automotive Industry Development Plan (NAIDP) text — vehicle age restrictions and duty rates have changed multiple times and I do not have a verified current figure to give you.
- CBN forex policy as of this quarter (naira volatility directly hits landed cost of any imported inventory or parts).

Nothing below should be taken as a live regulatory citation — verify against source documents.

## 1. Opportunity sizing (three numbers, not one)
- **TAM**: total value of used-car transactions across Nigeria annually (formal + informal), including private peer-to-peer sales that never touch a platform.
- **SAM**: the slice reachable by an online/marketplace model — concentrated in Lagos, Abuja, Port Harcourt given internet penetration, banking access, and delivery logistics; excludes most rural cash-only trade.
- **SOM**: what you could realistically capture in 3 years given capital, brand, and incumbent share held by Cars45, Autochek, Jiji, Cheki, and informal dealer networks (Berger/Ladipo markets in Lagos).
Flag: if the $4M plan assumes SAM-level volume in year one, that's the first thing to correct — informal-market share doesn't convert to platform GMV quickly.

## 2. Porter's Five Forces (used-car marketplace, Nigeria)
- **New entrants**: moderate-to-low barrier for a listings site, high barrier for a full-inspection/financing/logistics model — capital-intensive, which cuts against an 18-month breakeven.
- **Supplier power (dealers/importers)**: high — informal dealer networks control most quality inventory and can bypass your platform.
- **Buyer power**: high — price-sensitive, cash-heavy market, low switching cost between platforms.
- **Substitutes**: strong — direct dealer purchase, social-media/WhatsApp sales, informal brokers ("olopa"/agent networks).
- **Rivalry**: high — Cars45/Autochek already have inspection infrastructure and financing partnerships; a new entrant competes on capital, not novelty.
This alone should make you question an 18-month breakeven — none of the established players reached profitability that fast in this market as far as public reporting shows; verify against their actual disclosures if available.

## 3. SWOT (fill in your specifics, flagging the generic risks)
- **Strengths**: [your team's capital, tech, any existing Africa footprint]
- **Weaknesses**: no local dealer relationships or inspection network yet; $4M is thin for building trust-and-logistics infrastructure at scale.
- **Opportunities**: growing middle class, increasing smartphone/bank penetration, financing gap incumbents haven't fully solved.
- **Threats**: naira devaluation risk on any imported inventory/parts, sudden customs policy shifts on used-vehicle imports, fraud/title-verification risk in a market without a reliable national vehicle registry.

## 4. RICE on the plan's initiatives
Score each proposed workstream (inspection network, financing partnership, logistics/delivery, marketing launch, regulatory/compliance setup) on Reach, Impact, Confidence, Effort. My flag: regulatory/compliance and title-verification infrastructure usually gets under-scored on Effort in these plans because it's treated as a legal checkbox rather than an operating system — that's exactly where an 18-month timeline usually breaks.

## 5. SMART goals — rewrite the milestone
"Breakeven in 18 months" is not SMART as stated — it's not tied to a specific, measurable leading indicator. Replace with something like: "Achieve X transactions/month and Y% gross margin by month 12, sufficient to reach operating breakeven by month 18 assuming Z% MoM growth" — and stress-test Z against actual comparable growth curves, not a straight-line assumption.

## 6. Conway's Law check on integration plans
If the plan bundles inspection, financing, logistics, and payments into one team, the product will end up as tightly coupled as that team structure — likely to slow iteration exactly when you need speed to hit month 18. If those are separate teams/vendors (e.g., a bank financing partner, a third-party logistics provider), expect the integration seams to show up as delays at each handoff — build slack into the timeline for each partner integration, not just internal engineering.

## 7. Regulatory assumptions to pressure-test specifically
- Used-vehicle import age/duty rules — these have shifted before in Nigeria and directly affect inventory cost; confirm current rule, don't assume last-known figures still apply.
- Forex: any dollar-denominated costs (imported parts, foreign SaaS/infra, investor capital held in USD) are exposed to naira volatility — this alone can move your breakeven date independent of operating execution.
- Data protection (NDPR) for any KYC/financing data you collect.
- State-level vehicle registration/title transfer processes — if there's no reliable digital title registry, your fraud/chargeback risk assumptions need to be conservative, not optimistic.

## 8. Escalation
I don't know your committee's mandate threshold. If $4M exceeds what's pre-authorized for market entry without full committee sign-off, this needs escalation to the committee chair before circulation, not after — worth confirming that now rather than at the meeting.

**Bottom line for the write-up**: the 18-month breakeven assumption doesn't survive Porter's-Forces scrutiny or comparison to what public reporting suggests about incumbents' paths to profitability in this market — I'd push it to a range (e.g., 18–30 months) with explicit sensitivity to naira/forex and customs-policy risk, and I'd want the three-tier TAM/SAM/SOM numbers and the last-4-FY financials in the deck before this goes to committee.

### Task 5

We're proposing entry into the Indian direct-to-consumer skincare market by partnering with a local distributor instead of building our own logistics. Before this proposal reaches the investment committee, tell me if the partnership risks and exit options are adequately covered.

**With original skill**

I don't have the proposal document in front of me, and I have no tools in this session to pull filings or read files — so I can't verify what's actually in the write-up. If you paste the partnership-terms and exit sections (or the relevant excerpt), I'll give you a direct adequate/inadequate call. What follows is the checklist I'd hold it against.

**Partnership risk — what "adequately covered" requires**

- Treat the distributor as a concentrated supplier, not a vendor. What's their bargaining power over you: exclusivity granted, minimum volume commitments, pricing they set vs. you set, and what happens if they underperform on delivery/returns in a category (skincare) where damaged or expired stock is a real failure mode.
- Who owns the customer? In D2C, the customer relationship and data are usually the asset. If the distributor's platform or logistics stack sits between you and the buyer, does the contract guarantee you data access/portability, or can they withhold it?
- Change-of-control risk: what happens if the distributor is acquired by (or already works with) a competitor?
- Brand and quality control: can they co-brand, private-label alongside you, or affect your positioning in ways you don't control?

**Exit options — what "adequately covered" requires**

- Termination rights and notice periods, and whether they're symmetric (can you exit for cause and for convenience, not just them).
- Unwind cost: inventory buyback/return terms, penalty or tail fees, any minimum-guarantee shortfall you'd owe.
- A real fallback plan: could you switch to a second distributor or stand up owned logistics within a defined window, and has anyone costed that transition rather than just asserting it's possible.
- Time-boxed decision gates (e.g., a 12- or 18-month checkpoint) rather than an open-ended partnership with no forced re-evaluation.

**One structural check**: if the integration plan has your team and the distributor's team reporting into different, poorly-linked chains, that mismatch tends to show up later as operational friction — worth checking against the org chart on both sides.

**Escalation**: confirm the total exposure (minimum guarantees + exit penalties + committed spend) against your mandate. If it's close to or over, flag to the committee chair before this goes up, not after.

Send me the actual partnership/exit clauses and I'll tell you specifically what's missing.

**With pruned skill**

I don't have access to the actual proposal document in this session (no file tools available), so I can't verify coverage directly — paste the partnership/exit sections and I'll check them line by line. In the meantime, here's what "adequate" should look like for this specific deal shape, so you can self-check or hand this to whoever drafted it:

**Partnership risk gaps to check for:**
- **Distributor concentration/lock-in**: what % of your India revenue would run through this one distributor, and what happens if they underperform, get acquired by a competitor, or push a rival brand?
- **Bargaining power dynamics (Five Forces)**: does the proposal quantify the distributor's leverage — e.g., do they hold the customer data, warehouse relationships, or last-mile network you'd need to rebuild from scratch if the deal ends?
- **Quality/compliance control**: skincare in India has BIS/CDSCO cosmetic labeling and import rules — does the proposal specify who owns regulatory liability if the distributor mishandles compliance?
- **Org/integration friction (Conway's Law)**: if your teams (marketing, supply chain, customer service) aren't structured to interface with the distributor's org the same way, the partnership's actual information flow will mirror that mismatch — check whether the plan names a single accountable integration owner on each side, not just a steering committee.
- **Currency/repatriation and payment terms**: distributor cash-collection cycles are a common blind spot — is there a specified DSO and FX hedging approach?

**Exit options — proposals in this shape often only cover one exit path (usually "terminate for cause"). Check whether it also addresses:**
- **Exit for convenience**: notice period, wind-down timeline, and cost if you simply want out with no fault on either side.
- **Asset/data portability**: who owns the customer list, CRM data, and inventory at termination — critical for a D2C brand where the customer relationship is the asset.
- **Non-compete/non-solicit post-exit**: can the distributor immediately partner with a direct competitor using what they learned about your channel?
- **Transition support obligation**: is the distributor contractually required to assist a handover to a new partner or in-house logistics, or can they walk away immediately?
- **Trigger metrics**: are there defined KPIs (fill rate, NPS, compliance incidents) that automatically trigger a renegotiation or exit right, rather than relying on subjective "material breach" language?

If any of these aren't explicitly addressed in the proposal, I'd flag it as a gap before it goes to committee — distributor dependency without a clean exit path is exactly the kind of thing that gets escalated back down from IC with "come back with the exit terms."

Send me the actual risk/exit sections (or the full doc) and I'll give you a specific gap list against these instead of a general one.

