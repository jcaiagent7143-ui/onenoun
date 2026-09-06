# onenoun audit — ./probe-skill.md

approx tokens: **452 → 203** (+55%)  ·  units: 19 total, 8 touchable, 0 guarded  ·  labels: FACT 2, METHOD 5, FILLER 0, UNSURE 0, CANDIDATE 1
driver: claude, 7 call(s), $0.104

| # | lines | label | term | tokens | saved | why |
|---|---|---|---|---|---|---|
| 4 | 8-8 | FACT |  | 18 |  | Specific, arbitrary workflow instruction (exactly four fiscal years, from filings, done before starting) that is particular to this review process, not a named method. |
| 6 | 10-13 | CANDIDATE |  | 67 |  | proposed term ['TAM/SAM/SOM'] not yet verified. Re-explains the TAM/SAM/SOM market-sizing framework without adding any project-specific detail beyond the generic instruction to report all three. |
| 8 | 15-19 | METHOD | Porter's Five Forces | 98 | 87 | proposed term ["Porter's Five Forces"] verified by activation test. Re-explains Porter's Five Forces (supplier power, buyer power, new entrants, substitutes, rivalry) with no project-specific content. |
| 10 | 21-23 | METHOD | SWOT analysis | 50 | 32 | proposed term ['SWOT analysis'] verified by activation test. Describes the classic SWOT 2x2 matrix (internal strengths/weaknesses vs external opportunities/threats) with no added project-specific detail. |
| 12 | 25-28 | METHOD | RICE scoring | 64 | 54 | proposed term ['RICE scoring'] verified by activation test. Re-explains RICE scoring (reach, impact, confidence, effort) exactly matching the standard formula. |
| 14 | 30-32 | METHOD | SMART goals | 51 | 43 | proposed term ['SMART goals'] verified by activation test. Re-explains a SMART-style goal-writing checklist (specific, measurable, owned, relevant, time-bound) with no project-specific content beyond the five-part rule itself. |
| 16 | 34-36 | METHOD | Conway's Law | 46 | 33 | proposed term ["Conway's Law"] verified by activation test. Restates Conway's Law verbatim in its classic form, applied generically to advise checking the org chart. |
| 18 | 38-38 | FACT |  | 16 |  | Specific escalation rule naming a specific role (committee chair) and a project-specific trigger (deal exceeds the mandate). |

## The model's own uncertainties (列出所有不自信的点)

- Unit 14 replaces the standard SMART criterion 'Achievable' with 'an owner' (assignable), so it may not be pure textbook SMART but a project-specific variant; I labelled it METHOD (SMART goals) but this is the labelling I'm least sure about.
- Unit 10 never names 'SWOT' explicitly, it only describes the quadrant layout; I inferred the term from the description, which I'm fairly but not fully confident matches the canonical SWOT framework rather than some other 2x2 matrix.
- Unit 4 could arguably be read as an application of a known financial-analysis convention (e.g. trailing-four-year trend analysis) rather than a pure project-specific fact, but I treated the specific number and workflow placement as FACT since no established named method matches it exactly.
