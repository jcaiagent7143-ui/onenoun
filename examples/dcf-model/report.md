# onenoun audit — claude-for-financial-services/…/financial-analysis/skills/dcf-model/SKILL.md

approx tokens: **12377 → 10304** (+17%)  ·  units: 919 total, 209 touchable, 321 guarded  ·  labels: FACT 117, METHOD 0, FILLER 92, UNSURE 0
driver: claude, 1 call(s), $0.801

| # | lines | label | term | tokens | saved | why |
|---|---|---|---|---|---|---|
| 6 | 10-10 | FACT |  | 56 |  | States a project-specific output spec: sensitivity analysis lives at the bottom of the DCF sheet. |
| 10 | 14-14 | FACT |  | 26 |  | Names specific data-sourcing channels (user, MCP servers) particular to this skill's workflow. |
| 19 | 23-23 | FACT |  | 55 |  | Project-specific translation guidance between openpyxl and Office JS, naming both tools. |
| 25 | 42-42 | FACT |  | 40 |  | Enumerates the specific sections of this DCF where the merged-cell pitfall applies. |
| 28 | 45-45 | FACT |  | 38 |  | Core non-negotiable rule specific to this skill: every derived cell must be a live formula. |
| 30 | 47-47 | FACT |  | 46 |  | Specific enumerated list of the only permitted hardcodes in this DCF model. |
| 31 | 48-48 | FILLER |  | 34 | 34 | Restates the formulas-over-hardcodes rule already given in units 28 and 30. |
| 33 | 50-50 | FACT |  | 16 |  | Names a specific workflow constraint of this skill: staged user verification instead of end-to-end build. |
| 34 | 51-51 | FACT |  | 31 |  | Specific checkpoint content (raw inputs block) particular to this skill's staged process. |
| 35 | 52-52 | FACT |  | 27 |  | Specific checkpoint content (revenue projections) particular to this skill's staged process. |
| 36 | 53-53 | FACT |  | 20 |  | Specific checkpoint content (FCF schedule) particular to this skill's staged process. |
| 37 | 54-54 | FACT |  | 18 |  | Specific checkpoint content (WACC) particular to this skill's staged process. |
| 38 | 55-55 | FACT |  | 29 |  | Specific checkpoint content (equity bridge) particular to this skill's staged process. |
| 39 | 56-56 | FACT |  | 34 |  | Concrete example (margin assumption error cascading into sensitivity tables) motivating the checkpoint approach. |
| 45 | 62-62 | FACT |  | 23 |  | Specific numeric spec: 3 tables × 25 cells = 75 formulas. |
| 46 | 63-63 | FACT |  | 18 |  | Names the specific tool (openpyxl/Office JS loops) required for this task. |
| 47 | 64-64 | FACT |  | 17 |  | Specific enumerated prohibitions for sensitivity table population. |
| 48 | 65-65 | FILLER |  | 16 | 16 | Restates the requirement already stated in 45 and 47 that every cell must fully recalc. |
| 51 | 68-68 | FACT |  | 13 |  | Specific workflow timing rule: comments added as each input is created. |
| 52 | 69-69 | FACT |  | 19 |  | Exact required comment format string, a concrete convention of this skill. |
| 53 | 70-70 | FACT |  | 16 |  | Specific rule tying comment completion to section progression. |
| 54 | 71-71 | FILLER |  | 11 | 11 | Restates the same 'add comments as created, not later' rule from unit 51. |
| 57 | 74-74 | FACT |  | 15 |  | Specific build-order constraint (define rows before formulas) particular to this skill's process. |
| 59 | 76-76 | FACT |  | 12 |  | Specific ordered step in the row-planning process. |
| 60 | 77-77 | FACT |  | 12 |  | Specific ordered step in the row-planning process. |
| 66 | 83-83 | FACT |  | 15 |  | Names the exact Excel error types that must be zero before delivery. |
| 70 | 87-87 | FACT |  | 17 |  | Specific layout convention: assumptions shown horizontally across years within scenario blocks. |
| 78 | 95-95 | FACT |  | 15 |  | Specific list of data sources this skill pulls from. |
| 81 | 98-98 | FACT |  | 21 |  | Names a specific provider example (Daloopa) and data type priority. |
| 82 | 99-99 | FACT |  | 16 |  | Specific data-source priority tier particular to this workflow. |
| 83 | 100-100 | FACT |  | 17 |  | Specific data-source priority tier and content (prices, beta, debt, cash). |
| 86 | 103-103 | FACT |  | 13 |  | Domain-specific validation item: net debt vs net cash distinction is critical. |
| 87 | 104-104 | FACT |  | 18 |  | Domain-specific validation item about diluted shares and buybacks/issuances. |
| 88 | 105-105 | FACT |  | 15 |  | Domain-specific validation item about margin consistency with business model. |
| 96 | 113-113 | FACT |  | 16 |  | Specific set of margin metrics to track (gross, EBIT, FCF). |
| 97 | 114-114 | FACT |  | 13 |  | Specific capital intensity metrics (D&A, CapEx as % of revenue). |
| 98 | 115-115 | FACT |  | 16 |  | Specific working capital efficiency metric definition. |
| 107 | 133-133 | FACT |  | 16 |  | Specific methodological starting point for revenue projections (LTM/most recent FY). |
| 109 | 135-135 | FACT |  | 12 |  | Specific presentation requirement: show both dollar amounts and growth %. |
| 117 | 143-143 | FACT |  | 13 |  | Exact formula for revenue projection. |
| 118 | 144-144 | FACT |  | 14 |  | Exact formula for growth percentage. |
| 128 | 158-158 | FACT |  | 19 |  | Specific numeric range for S&M as % of revenue. |
| 129 | 159-159 | FACT |  | 17 |  | Specific numeric range for R&D as % of revenue. |
| 130 | 160-160 | FACT |  | 22 |  | Specific numeric range for G&A as % of revenue. |
| 133 | 163-163 | FACT |  | 12 |  | Domain-specific rule that opex percentages are based on revenue, not gross profit. |
| 134 | 164-164 | FACT |  | 15 |  | Domain-specific modeling principle about operating leverage. |
| 135 | 165-165 | FACT |  | 11 |  | Specific structural requirement to keep S&M/R&D/G&A separate. |
| 136 | 166-166 | FACT |  | 10 |  | Exact EBIT formula definition. |
| 148 | 190-190 | FACT |  | 12 |  | Specific methodology for calculating NWC as % of revenue change. |
| 149 | 191-191 | FACT |  | 10 |  | Specific numeric range for NWC as % of revenue change. |
| 150 | 192-192 | FACT |  | 14 |  | Domain-specific sign convention (negative = source of cash). |
| 151 | 193-193 | FACT |  | 13 |  | Domain-specific sign convention (positive = use of cash). |
| 156 | 198-198 | FILLER |  | 13 | 13 | Generic guidance with no specific number or rule beyond what's already stated about CapEx. |
| 173 | 238-238 | FACT |  | 14 |  | Specific rule: net cash position makes Net Debt negative, a domain-specific edge case. |
| 188 | 253-253 | FACT |  | 9 |  | Exact discount factor formula. |
| 195 | 270-270 | FACT |  | 14 |  | Specific guidance on projection period for high-growth companies. |
| 209 | 289-289 | FACT |  | 14 |  | Specific constraint that terminal growth must not exceed risk-free rate/GDP growth. |
| 219 | 311-311 | FACT |  | 14 |  | Specific numeric sanity-check threshold (>75%) for terminal value share of EV. |
| 220 | 312-312 | FACT |  | 14 |  | Specific numeric sanity-check threshold (<40%) for terminal value share of EV. |
| 229 | 334-334 | FACT |  | 11 |  | Exact net debt formula. |
| 230 | 335-335 | FACT |  | 13 |  | Specific sign-handling rule for positive net debt. |
| 231 | 336-336 | FACT |  | 14 |  | Specific sign-handling rule for net cash (negative net debt). |
| 232 | 337-337 | FACT |  | 17 |  | Specific rule to use diluted shares including options/RSUs/converts. |
| 245 | 362-362 | FACT |  | 25 |  | Names one of the three required sensitivity tables and its purpose. |
| 246 | 363-363 | FACT |  | 22 |  | Names one of the three required sensitivity tables and its purpose. |
| 247 | 364-364 | FACT |  | 18 |  | Names one of the three required sensitivity tables and its purpose. |
| 249 | 366-366 | FACT |  | 79 |  | Clarifies the specific Excel feature (Data Table) that must NOT be used, a concrete tool-specific constraint. |
| 253 | 370-370 | FILLER |  | 20 | 20 | Generic section-framing sentence with no independent content. |
| 257 | 374-374 | FACT |  | 16 |  | States the specific design decision that scenarios get separate blocks, foundational to this skill's structure. |
| 259 | 376-376 | FACT |  | 13 |  | Specific structural requirement: three rows per section header. |
| 263 | 395-395 | FACT |  | 56 |  | Mandatory structural rule (column header row showing years) with concrete rationale. |
| 265 | 397-397 | FACT |  | 16 |  | Introduces the specific consolidation-column pattern name used throughout this skill. |
| 266 | 398-398 | FACT |  | 16 |  | Specific cell-reference convention (B6, 1/2/3 mapping) for the case selector. |
| 267 | 399-399 | FACT |  | 24 |  | Specific formula approach (INDEX/OFFSET) for the consolidation column. |
| 268 | 400-400 | FILLER |  | 19 | 19 | Restates unit 267's point that projections reference the consolidation column. |
| 269 | 401-401 | FILLER |  | 20 | 20 | Restates the horizontal-layout point already made in units 70 and 257. |
| 275 | 409-409 | FILLER |  | 22 | 22 | Restates the 'easier to audit' rationale that recurs throughout the file. |
| 279 | 413-413 | FILLER |  | 22 | 22 | Restates the consolidation-column-with-INDEX pattern already given in 267. |
| 287 | 423-423 | FACT |  | 18 |  | Concrete example cell reference ($E$10) tying the pattern to an actual model layout. |
| 290 | 426-426 | FILLER |  | 40 | 40 | Restates the audit-ease rationale already given (275). |
| 294 | 430-430 | FILLER |  | 22 | 22 | Restates the consolidation-column pattern already given in 267/279. |
| 299 | 441-441 | FILLER |  | 45 | 45 | Restates 287/290's point about INDEX formulas and auditability. |
| 301 | 443-443 | FILLER |  | 23 | 23 | Restates the lock-row-positions-before-formulas rule already established. |
| 314 | 463-463 | FACT |  | 17 |  | Specific structural requirement: three elements per scenario block. |
| 316 | 465-465 | FACT |  | 17 |  | Concrete example of a section header label. |
| 317 | 466-466 | FILLER |  | 16 | 16 | Restates the mandatory column-header-row rule already stated in 263. |
| 323 | 493-493 | FILLER |  | 43 | 43 | Near-verbatim restatement of unit 263's rationale. |
| 325 | 495-495 | FACT |  | 60 |  | Adds a new specific detail not stated before: consolidation column is 'the next column to the right'. |
| 332 | 511-511 | FILLER |  | 12 | 12 | Restates step already given in unit 59. |
| 334 | 513-513 | FILLER |  | 14 | 14 | Restates step already given in unit 60. |
| 339 | 518-518 | FILLER |  | 14 | 14 | Generic construction analogy carrying no project-specific fact. |
| 340 | 519-519 | FILLER |  | 13 | 13 | Generic construction analogy carrying no project-specific fact. |
| 343 | 522-522 | FILLER |  | 14 | 14 | Restates the headers-before-formulas rule already established. |
| 344 | 523-523 | FILLER |  | 13 | 13 | Restates the formula-breakage risk already covered in the 'Formula Row References Off' mistake section. |
| 348 | 527-527 | FACT |  | 58 |  | Names the specific Excel 'Data Table' feature and clarifies it is disallowed — a concrete tool distinction. |
| 352 | 531-531 | FACT |  | 63 |  | Gives the specific technical reason (cannot be automated via openpyxl) that Excel's Data Table feature is unusable here. |
| 372 | 560-560 | FACT |  | 22 |  | Specific recommended implementation approach for sensitivity formulas. |
| 376 | 565-565 | FILLER |  | 53 | 53 | Restates the 75-cells/no-placeholder requirement already given in 45, 47, and 348. |
| 381 | 577-577 | FILLER |  | 29 | 29 | Restates the 'no manual steps required' requirement already given in 47 and 352. |
| 387 | 583-583 | FILLER |  | 19 | 19 | Generic section-framing sentence with no independent content. |
| 399 | 607-607 | FILLER |  | 25 | 25 | Restates the Data Table feature prohibition already established in 348/352. |
| 400 | 608-608 | FILLER |  | 24 | 24 | Restates that sensitivity tables are simple grids, already established. |
| 403 | 611-611 | FACT |  | 26 |  | Specific technical rationale for why linear approximation formulas are invalid. |
| 404 | 612-612 | FACT |  | 16 |  | Distinct technical rationale (non-linearity) for rejecting approximation shortcuts. |
| 410 | 618-619 | FACT |  | 33 |  | Names a specific anticipated failure mode (rationalizing a manual note) worth flagging explicitly. |
| 412 | 621-621 | FILLER |  | 54 | 54 | Restates the already-established rule that all 75 formulas must be written via a loop. |
| 414 | 623-623 | FILLER |  | 33 | 33 | Restates the full-recalculation requirement already given in unit 48. |
| 430 | 639-639 | FILLER |  | 16 | 16 | Restates the 'add comments as created' rule already given in unit 51. |
| 440 | 652-652 | FACT |  | 12 |  | Explains a concrete technical consequence (#REF! errors) of building formulas before headers. |
| 442 | 654-654 | FILLER |  | 13 | 13 | Restates the lock-layout-first rule already given in 57/60. |
| 448 | 664-664 | FACT |  | 23 |  | First substantive explanation of why the vertical single-row-per-assumption layout is hard to read. |
| 451 | 667-667 | FILLER |  | 20 | 20 | Restates the same point made in unit 448. |
| 452 | 668-668 | FILLER |  | 17 | 17 | Restates the same point made in units 448/451. |
| 456 | 672-672 | FILLER |  | 14 | 14 | Restates the separate-scenario-blocks instruction already established multiple times. |
| 457 | 673-673 | FILLER |  | 18 | 18 | Restates the horizontal-layout convention already given in unit 70. |
| 458 | 674-674 | FILLER |  | 18 | 18 | Restates the review-ease rationale already given elsewhere. |
| 478 | 694-694 | FACT |  | 11 |  | Specific enumerated mistake: using only fill colors without font color distinction. |
| 479 | 695-695 | FACT |  | 9 |  | Specific enumerated mistake: confusing blue vs black font usage. |
| 486 | 702-702 | FILLER |  | 24 | 24 | Restates the blue/black/green font convention already established in the Formatting Standards section. |
| 493 | 710-710 | FILLER |  | 13 | 13 | Restates the revenue-not-gross-profit rule already given in unit 133. |
| 501 | 719-719 | FILLER |  | 20 | 20 | Summary bullet restating the row-reference-first rule covered earlier in detail. |
| 502 | 720-720 | FILLER |  | 18 | 18 | Summary bullet restating the cell-comment-timing rule covered earlier in detail. |
| 503 | 721-721 | FILLER |  | 26 | 26 | Summary bullet restating the sensitivity-table-completeness rule covered earlier in detail. |
| 504 | 722-722 | FILLER |  | 24 | 24 | Summary bullet restating the scenario-block-correctness rule covered earlier in detail. |
| 505 | 723-723 | FILLER |  | 19 | 19 | Summary bullet restating the mandatory-borders rule covered earlier in detail. |
| 510 | 728-728 | FACT |  | 12 |  | Specific WACC error type (mixing book and market values) not previously enumerated. |
| 511 | 729-729 | FACT |  | 15 |  | Specific WACC error type (equity vs asset/unlevered beta) not previously enumerated. |
| 512 | 730-730 | FACT |  | 10 |  | Specific WACC error type (wrong tax rate application to cost of debt) not previously enumerated. |
| 513 | 731-731 | FACT |  | 14 |  | Specific WACC error type (incorrect risk-free rate source) not previously enumerated. |
| 514 | 732-732 | FILLER |  | 12 | 12 | Restates the net debt/net cash adjustment rule already given in units 173/229-231. |
| 524 | 742-742 | FILLER |  | 13 | 13 | Restates the two terminal-value methods already described in detail in Step 8. |
| 525 | 743-743 | FACT |  | 16 |  | Gives a specific >80% threshold for terminal value over-reliance; note this conflicts with the >75% threshold in unit 219. |
| 530 | 748-748 | FILLER |  | 14 | 14 | Third restatement of the revenue-not-gross-profit rule (see 133, 493). |
| 536 | 754-754 | FILLER |  | 22 | 22 | Generic encouragement to re-read a section, no new content. |
| 548 | 766-766 | FACT |  | 32 |  | Names a specific external dependency (the xlsx skill) this skill relies on. |
| 553 | 771-771 | FILLER |  | 19 | 19 | Generic quality-rubric restatement of the historical-analysis emphasis already covered. |
| 554 | 772-772 | FILLER |  | 18 | 18 | Generic quality-rubric restatement of the CAPM/WACC section already covered. |
| 564 | 782-782 | FACT |  | 21 |  | Specific input option ('use consensus') not clearly stated elsewhere as an accepted user shortcut. |
| 577 | 795-795 | FILLER |  | 16 | 16 | Restates the sheet architecture (DCF sheet with sensitivity at bottom) already given earlier. |
| 580 | 798-798 | FACT |  | 34 |  | First explicit statement that sensitivity tables must NOT be on a separate sheet, with rationale. |
| 592 | 814-814 | FACT |  | 14 |  | Specific tool behavior: recalc.py recalculates via LibreOffice. |
| 593 | 815-815 | FACT |  | 21 |  | Specific tool behavior: scans for a defined list of Excel error types. |
| 594 | 816-816 | FACT |  | 13 |  | Specific tool output format (detailed JSON). |
| 606 | 847-847 | FACT |  | 40 |  | Clarifies the specific division of responsibility between this skill and the xlsx skill. |
| 610 | 851-851 | FACT |  | 13 |  | Attributes font-color mandate specifically to the xlsx skill. |
| 612 | 853-853 | FACT |  | 14 |  | Specific RGB value convention for formula text. |
| 615 | 856-856 | FACT |  | 24 |  | Names the specific default fill palette and its override condition. |
| 616 | 857-857 | FACT |  | 43 |  | Specific stylistic constraint restricting fills to blue/grey only. |
| 623 | 864-864 | FILLER |  | 17 | 17 | Restates the blue/grey-only constraint already given in unit 616. |
| 624 | 865-865 | FACT |  | 21 |  | Specific override rule: user templates/preferences take precedence over defaults. |
| 627 | 868-868 | FACT |  | 14 |  | Concrete pairing of font+fill meaning (input cell). |
| 628 | 869-869 | FACT |  | 16 |  | Concrete pairing of font+fill meaning (formula cell). |
| 629 | 870-870 | FACT |  | 18 |  | Concrete pairing of font+fill meaning (sheet link). |
| 630 | 871-871 | FACT |  | 17 |  | Concrete pairing of font+fill meaning (key output). |
| 632 | 873-873 | FILLER |  | 28 | 28 | Mnemonic recap of units 627-630 with no new information. |
| 646 | 887-887 | FACT |  | 12 |  | Specific list item under medium border standards particular to this model's sections. |
| 649 | 890-890 | FACT |  | 14 |  | Specific list item under thin border standards particular to this model's tables. |
| 652 | 893-893 | FACT |  | 17 |  | Specific rule about where borders should NOT be applied. |
| 654 | 895-895 | FILLER |  | 21 | 21 | Restates the mandatory-borders requirement already stated in the Border Standards section and Top 5 Errors. |
| 666 | 907-907 | FILLER |  | 41 | 41 | Exact duplicate of the comment format string already given in units 52/53. |
| 668 | 909-909 | FILLER |  | 18 | 18 | Restates the 'add comments as created' rule already given in units 51/54. |
| 684 | 938-938 | FACT |  | 36 |  | Introduces a concrete example label ('Selected Case') for the consolidation column not given before. |
| 692 | 967-967 | FILLER |  | 26 | 26 | Restates the 'easier to audit' rationale repeated many times in this file. |
| 696 | 971-971 | FILLER |  | 28 | 28 | Restates the row-reference verification rule already given multiple times. |
| 701 | 987-987 | FACT |  | 13 |  | Concrete example cell mapping ($E$21 = D&A%) tied to specific row numbers. |
| 702 | 988-988 | FACT |  | 14 |  | Concrete example cell mapping ($E$22 = CapEx%) tied to specific row numbers. |
| 703 | 989-989 | FACT |  | 13 |  | Concrete example cell mapping ($E$23 = NWC%) tied to specific row numbers. |
| 707 | 993-993 | FACT |  | 28 |  | Adds a new actionable technique ('test one column, then copy across') not stated elsewhere. |
| 721 | 1065-1065 | FACT |  | 68 |  | Gives the specific Excel menu path (Data → What-If Analysis → Data Table), a new concrete detail. |
| 723 | 1067-1067 | FACT |  | 14 |  | Specific row range (87+) for sensitivity table placement, not given elsewhere. |
| 731 | 1075-1075 | FILLER |  | 16 | 16 | Restates the '75 formulas' figure already given in units 45 and 376. |
| 733 | 1077-1077 | FILLER |  | 79 | 79 | Restates prohibitions already established in units 45-48, 376, 410-414. |
| 736 | 1080-1080 | FILLER |  | 19 | 19 | Restates the table-structure concept already illustrated concretely in the earlier example. |
| 740 | 1084-1084 | FILLER |  | 14 | 14 | Restates the full-DCF-recalculation requirement already given in unit 48. |
| 741 | 1085-1085 | FILLER |  | 12 | 12 | Restates the implied-share-price output already established for sensitivity cells. |
| 742 | 1086-1086 | FILLER |  | 13 | 13 | Restates the 'all cells must work' requirement already given in units 47/381. |
| 743 | 1087-1087 | FACT |  | 24 |  | New specific detail (green/red conditional formatting scale); note this conflicts with the blue/grey-only palette rule in units 616/623. |
| 747 | 1091-1091 | FILLER |  | 28 | 28 | Restates the no-manual-intervention requirement already given in units 381/742. |
| 754 | 1098-1098 | FILLER |  | 14 | 14 | Restates the Bear case growth characterization already established in Step 3's scenario framework. |
| 776 | 1120-1120 | FILLER |  | 43 | 43 | Restates the consolidation-column-over-nested-IF rule already given many times (267, 684, etc.). |
| 782 | 1128-1128 | FILLER |  | 22 | 22 | Restates the audit/maintain rationale repeated throughout the file. |
| 789 | 1135-1135 | FILLER |  | 42 | 42 | Restates the same three named sensitivity tables and sheet structure already given in units 245-247/577. |
| 792 | 1138-1138 | FILLER |  | 39 | 39 | Restates deliverable checklist items already scattered throughout the file. |
| 797 | 1143-1143 | FILLER |  | 17 | 17 | Generic best-practice advice restating the staged-build approach already established. |
| 798 | 1144-1144 | FILLER |  | 15 | 15 | Generic advice restating the test-immediately rule already given. |
| 799 | 1145-1145 | FILLER |  | 18 | 18 | Generic advice with no project-specific content. |
| 800 | 1146-1146 | FILLER |  | 16 | 16 | Generic advice with no concrete specifics beyond what's already implied. |
| 801 | 1147-1147 | FILLER |  | 16 | 16 | Generic advice with no project-specific content. |
| 804 | 1150-1150 | FILLER |  | 16 | 16 | Restates the documentation/cell-comment requirement already established. |
| 805 | 1151-1151 | FILLER |  | 14 | 14 | Restates the cite-data-sources requirement already established in the cell comment format section. |
| 811 | 1157-1157 | FILLER |  | 17 | 17 | Restates the sensitivity analysis requirement already established in Step 10. |
| 852 | 1198-1198 | FILLER |  | 13 | 13 | Restates the MCP-server data priority already given in units 81-83. |
| 853 | 1199-1199 | FILLER |  | 17 | 17 | Restates the web-search data priority already given in unit 83. |
| 854 | 1200-1200 | FILLER |  | 11 | 11 | Restates the user-request fallback already implied in units 81-83. |
| 858 | 1204-1204 | FILLER |  | 10 | 10 | Restates the user-fallback data priority already given in unit 82. |
| 861 | 1207-1207 | FILLER |  | 19 | 19 | Generic self-referential framing sentence. |
| 865 | 1211-1211 | FILLER |  | 18 | 18 | Restates the formulas-not-hardcodes rule already given in units 28/30/31. |
| 866 | 1212-1212 | FILLER |  | 18 | 18 | Restates the xlsx-skill-dependency already given in unit 606. |
| 867 | 1213-1213 | FACT |  | 23 |  | Specific rule about when to apply fill colors; note this appears to conflict with unit 615's 'default unless user specifies otherwise' framing. |
| 872 | 1218-1218 | FILLER |  | 18 | 18 | Checklist item restating scenario block structure already covered extensively. |
| 873 | 1219-1219 | FILLER |  | 18 | 18 | Checklist item restating case selector/consolidation column already covered extensively. |
| 874 | 1220-1220 | FILLER |  | 15 | 15 | Checklist item restating sensitivity table location already given in units 580/723. |
| 875 | 1221-1221 | FILLER |  | 14 | 14 | Checklist item restating the font color convention already given multiple times. |
| 888 | 1234-1234 | FILLER |  | 17 | 17 | Restates the row-reference correctness concern already covered extensively. |
| 889 | 1235-1235 | FACT |  | 17 |  | Specific QA action (change case selector, verify consolidation column updates) not stated in this exact form elsewhere. |
| 890 | 1236-1236 | FILLER |  | 19 | 19 | Restates the consolidation-column-not-nested-IF point already covered extensively. |
| 896 | 1242-1242 | FILLER |  | 16 | 16 | Restates the MCP data source point already given in unit 81. |
| 897 | 1243-1243 | FILLER |  | 17 | 17 | Restates the web search data point already given in unit 83. |
| 907 | 1253-1253 | FILLER |  | 12 | 12 | Restates the two-sheet architecture already given multiple times (577, 580, 789). |

## Guarded (never sent to the model)

- lines 18-18 · lead_in · These constraints apply throughout all DCF model building. Review before starting:
- lines 20-20 · short · **Environment: Office JS vs Python/openpyxl:**
- lines 21-21 · backtick · **If running inside Excel (Office Add-in / Office JS environment):** Use Office JS directl
- lines 22-22 · backtick · **If generating a standalone .xlsx file (no live Excel session):** Use Python/openpyxl as 
- lines 25-25 · backtick · **⚠️ Office JS merged cell pitfall:** When building section headers with merged cells, do 
- lines 44-44 · short · **Formulas Over Hardcodes (NON-NEGOTIABLE):**
- lines 46-46 · backtick · When using openpyxl: `ws["D20"] = "=D19*(1+$B$8)"` is correct; `ws["D20"] = calculated_rev
- lines 58-58 · short · **Sensitivity Tables:**
- lines 59-59 · number_unit · **Use an ODD number of rows and columns** (standard: 5×5, sometimes 7×7) — this guarantees
- lines 60-60 · version · **Center cell = base case.** Build the axis values so the middle row header and middle col
- lines 61-61 · backtick · **Highlight the center cell** with the medium-blue fill (`#BDD7EE`) + bold font so it's im
- lines 67-67 · short · **Cell Comments:**
- lines 73-73 · short · **Model Layout Planning:**
- lines 75-75 · short · Write ALL headers and labels first
- lines 78-78 · short · Test formulas immediately after creation
- lines 80-80 · short · **Formula Recalculation:**
- lines 81-81 · backtick · Run `python recalc.py model.xlsx 30` before delivery
- lines 82-82 · short · Fix ALL errors until status is "success"
- lines 85-85 · short · **Scenario Blocks:**
- lines 86-86 · short · Create separate blocks for Bear/Base/Bull cases
- lines 88-88 · backtick · Use IF formulas: `=IF($B$6=1,[Bear cell],IF($B$6=2,[Base cell],[Bull cell]))`
- lines 89-89 · short · Verify formulas reference correct scenario block cells
- lines 97-97 · short · **Data Sources Priority:**
- lines 102-102 · short · **Validation Checklist:**
- lines 106-106 · short · Cross-check revenue growth rates with industry benchmarks
- lines 107-107 · short · Verify tax rate is reasonable (typically 21-28%)
- lines 111-111 · short · Analyze and document:
- lines 112-112 · short · **Revenue growth trends**: Calculate CAGR, identify drivers
- lines 116-116 · short · **Return metrics**: ROIC, ROE trends
- lines 118-118 · short · Create summary tables showing:
- lines 132-132 · short · **Methodology:**
- lines 134-134 · short · Apply growth rates for each projection year
- lines 137-137 · short · **Growth Rate Framework:**
- lines 138-138 · short · Year 1-2: Higher growth reflecting near-term visibility
- lines 139-139 · short · Year 3-4: Gradual moderation toward industry average
- lines 140-140 · short · Year 5+: Approaching terminal growth rate
- lines 142-142 · short · **Formula structure:**
- lines 146-146 · short · **Three-scenario approach:**
- lines 155-155 · short · **Fixed/Variable Cost Analysis:**
- lines 157-157 · short · Operating expenses should model realistic operating leverage:
- lines 162-162 · short · **Key principles:**
- lines 168-168 · short · **Margin expansion framework:**
- lines 177-177 · short · **Build FCF in proper sequence:**
- lines 189-189 · short · **Working Capital Modeling:**
- lines 195-195 · short · **Maintenance vs Growth CapEx:**
- lines 196-196 · short · Maintenance CapEx: Sustains current operations (~2-3% revenue)
- lines 197-197 · short · Growth CapEx: Supports expansion (additional 2-5% revenue)
- lines 202-202 · short · **CAPM Methodology for Cost of Equity:**
- lines 213-213 · short · **Cost of Debt Calculation:**
- lines 224-224 · short · **Capital Structure Weights:**
- lines 237-237 · short · **Special Cases:**
- lines 239-239 · short · Debt Weight may be negative
- lines 240-240 · short · WACC calculation adjusts accordingly
- lines 241-241 · short · **No Debt**: WACC = Cost of Equity
- lines 243-243 · short · **Typical WACC Ranges:**
- lines 244-244 · short · Large Cap, Stable: 7-9%
- lines 245-245 · short · Growth Companies: 9-12%
- lines 246-246 · short · High Growth/Risk: 12-15%
- lines 250-250 · short · **Mid-Year Convention:**
- lines 251-251 · short · Cash flows assumed to occur mid-year
- lines 252-252 · version · Discount Period: 0.5, 1.5, 2.5, 3.5, 4.5, etc.
- lines 255-255 · short · **Present Value Calculation:**
- lines 268-268 · short · **Projection Period Selection:**
- lines 269-269 · short · **5 years**: Standard for most analyses
- lines 271-271 · short · **3 years**: Mature, stable businesses
- lines 275-275 · short · **Perpetuity Growth Method (Preferred):**
- lines 284-284 · short · **Terminal Growth Rate Selection:**
- lines 285-285 · version · Conservative: 2.0-2.5% (GDP growth rate)
- lines 286-286 · version · Moderate: 2.5-3.5%
- lines 287-287 · version · Aggressive: 3.5-5.0% (only for market leaders)
- lines 291-291 · short · **Exit Multiple Method (Alternative):**
- lines 301-301 · short · **Present Value of Terminal Value:**
- lines 309-309 · short · **Terminal Value Sanity Check:**
- lines 310-310 · short · Should represent 50-70% of Enterprise Value
- lines 316-316 · short · **Valuation Summary Structure:**
- lines 333-333 · short · **Critical Adjustments:**
- lines 338-338 · short · **Other adjustments** (if applicable):
- lines 339-339 · short · Minority interests
- lines 340-340 · short · Pension liabilities
- lines 341-341 · short · Operating lease obligations
- lines 343-343 · short · **Valuation Output Format:**
- lines 360-360 · lead_in · Build **three sensitivity tables** at the bottom of the DCF sheet showing how valuation ch
- lines 403-404 · backtick · **Recommended consolidation column pattern (using INDEX):**
- lines 406-407 · backtick · **NOT this - scattered IF statements throughout:**
- lines 415-416 · backtick · **Step 1 - Consolidation column for FY1 growth:**
- lines 418-419 · backtick · **Step 2 - Revenue projection references the consolidation column:**
- lines 421-421 · short · Where:
- lines 422-422 · short · D29 = Prior year revenue
- lines 424-424 · short · $B$6 = Case selector (1=Bear, 2=Base, 3=Bull)
- lines 432-432 · short · **Consolidation column approach:**
- lines 447-447 · short · **Every hardcoded value needs this format:**
- lines 449-449 · short · "Source: [System/Document], [Date], [Reference], [URL if applicable]"
- lines 451-451 · short · **Examples:**
- lines 467-467 · short · **Data rows** with assumption values
- lines 469-469 · short · **Structure:**
- lines 499-499 · short · **1. Write ALL headers and labels FIRST:**
- lines 515-515 · short · **4. Test formulas immediately after creation**
- lines 517-517 · short · **Think of it like construction:**
- lines 521-521 · short · **Excel version:**
- lines 529-529 · short · **Programmatic Population with Formulas:**
- lines 533-533 · short · **Implementation approach - CONCRETE EXAMPLE:**
- lines 535-535 · number_unit · **Table Structure — 5×5 grid (ODD dimensions, base case centered):**
- lines 537-537 · version · If the model's base WACC = 9.0% and base terminal growth = 3.0%, build the axes symmetrica
- lines 550-550 · backtick · **★ = the center cell.** Its formula output MUST equal the model's actual implied share pr
- lines 552-552 · backtick · **Rule for axis values:** `axis_values = [base - 2*step, base - step, base, base + step, b
- lines 554-554 · version · **Formula Pattern - Cell B88 (WACC=8.0%, Terminal Growth=2.0%):**
- lines 556-556 · lead_in · The formula in B88 should recalculate the implied price using:
- lines 557-557 · backtick · WACC from row header: `$A88` (8.0%)
- lines 558-558 · backtick · Terminal Growth from column header: `B$87` (2.0%)
- lines 562-563 · backtick · **Example formula structure:**
- lines 567-567 · short · **Python implementation pattern:**
- lines 587-587 · short · **Don't use linear approximations:**
- lines 597-597 · short · **Don't leave placeholder text:**
- lines 606-606 · short · **Don't confuse terminology:**
- lines 610-610 · short · **Why these shortcuts are wrong:**
- lines 613-613 · short · Placeholder text requires manual user intervention
- lines 614-614 · short · Model is not immediately usable when delivered
- lines 615-615 · short · Not professional or client-ready
- lines 616-616 · short · Empty cells = incomplete deliverable
- lines 627-627 · short · **Don't do this:**
- lines 628-628 · short · Create all hardcoded inputs without comments
- lines 629-629 · short · Think "I'll add them later"
- lines 630-630 · short · Write "TODO: add source"
- lines 631-631 · short · Leave blue inputs without documentation
- lines 633-633 · short · **Why it's wrong:**
- lines 634-634 · short · Can't verify where data came from
- lines 635-635 · short · Fails xlsx skill requirements
- lines 636-636 · short · Not audit-ready
- lines 637-637 · short · Wastes time fixing later
- lines 643-646 · backtick · **Symptom:**
- lines 648-648 · short · **Why this happens:**
- lines 649-649 · short · Formulas written first
- lines 650-650 · short · Then headers inserted
- lines 651-651 · short · All row references shifted
- lines 658-658 · short · **Don't structure assumptions like this:**
- lines 666-666 · short · **Why it's wrong:**
- lines 669-669 · short · Less intuitive for reviewing scenario logic
- lines 671-671 · short · **Instead:**
- lines 678-678 · short · **Don't deliver a model without borders:**
- lines 679-679 · short · No section delineation
- lines 680-680 · short · All cells blend together
- lines 681-681 · short · Hard to read and unprofessional
- lines 683-683 · short · **Why it's wrong:**
- lines 684-684 · short · Not client-ready
- lines 685-685 · short · Difficult to navigate
- lines 686-686 · short · Looks amateur
- lines 688-688 · short · **Instead:** Add borders around all major sections
- lines 692-692 · short · **Don't do this:**
- lines 693-693 · short · All text is black
- lines 697-697 · short · **Why it's wrong:**
- lines 698-698 · short · Can't distinguish inputs from formulas
- lines 699-699 · short · Auditing becomes impossible
- lines 700-700 · short · Violates xlsx skill requirements
- lines 706-707 · backtick · **Don't do this:**
- lines 709-709 · short · **Why it's wrong:**
- lines 711-711 · short · Produces unrealistic margin progression
- lines 712-712 · short · Not how businesses actually operate
- lines 714-715 · backtick · **Instead:**
- lines 725-725 · short · In addition, be aware of these errors:
- lines 735-735 · short · Terminal growth > WACC (creates infinite value)
- lines 736-736 · short · Projection growth rates inconsistent with historical performance
- lines 737-737 · short · Ignoring industry growth constraints
- lines 738-738 · short · Revenue growth not aligned with unit economics
- lines 739-739 · short · Margin expansion without operational justification
- lines 744-744 · short · Inconsistent terminal margins with steady state assumptions
- lines 745-745 · short · Wrong discount period for terminal value
- lines 749-749 · short · D&A/CapEx percentages misaligned with business model
- lines 750-750 · short · Working capital changes not properly calculated
- lines 751-751 · short · Tax rate inconsistency between years
- lines 752-752 · short · NOPAT calculation errors
- lines 760-760 · backtick · **This skill uses the `xlsx` skill for all spreadsheet operations.** The xlsx skill provid
- lines 761-761 · short · Standardized formula construction rules
- lines 762-762 · short · Number formatting conventions
- lines 763-763 · backtick · Automated formula recalculation via `recalc.py` script
- lines 764-764 · short · Comprehensive error checking and validation
- lines 770-770 · short · Every DCF model must maximize for:
- lines 773-773 · short · **Comprehensive sensitivity analysis** showing valuation ranges
- lines 774-774 · short · **Clear terminal value calculation** with supporting rationale
- lines 775-775 · short · **Professional model structure** enabling scenario analysis
- lines 776-776 · short · **Transparent documentation** of all key assumptions
- lines 781-781 · short · **Company identifier**: Ticker symbol or company name
- lines 783-783 · short · **Optional parameters**:
- lines 784-784 · short · Projection period (default: 5 years)
- lines 785-785 · short · Scenario cases (Bear/Base/Bull growth and margin assumptions)
- lines 786-786 · version · Terminal growth rate (default: 2.5-3.0%)
- lines 787-787 · short · Specific WACC inputs if not using CAPM
- lines 793-793 · short · Create **two sheets**:
- lines 796-796 · short · **WACC** - Cost of capital calculation
- lines 802-802 · path · After creating or modifying the Excel model, **recalculate all formulas** using the recalc
- lines 808-808 · short · Example:
- lines 813-813 · short · The script will:
- lines 818-818 · short · **Expected output format:**
- lines 828-828 · lead_in · **If errors are found**, the output will include details:
- lines 843-843 · path · **Fix all errors** and re-run recalc.py until status is "success" before delivering the mo
- lines 849-849 · short · **Color Scheme - Two Layers**:
- lines 852-852 · big_number · **Blue text (RGB: 0,0,255)**: ALL hardcoded inputs (stock price, shares, historical data, 
- lines 854-854 · big_number · **Green text (RGB: 0,128,0)**: Links to other sheets (WACC sheet references)
- lines 858-858 · short · **Default fill palette:**
- lines 859-859 · backtick · **Section headers**: Dark blue (RGB: 31,78,121 / `#1F4E79`) background with white bold tex
- lines 860-860 · backtick · **Sub-headers/column headers**: Light blue (RGB: 217,225,242 / `#D9E1F2`) background with 
- lines 861-861 · backtick · **Input cells**: Light grey (RGB: 242,242,242 / `#F2F2F2`) background with blue font — or 
- lines 862-862 · short · **Calculated cells**: White background with black font
- lines 863-863 · backtick · **Output/summary rows** (per-share value, EV, etc.): Medium blue (RGB: 189,215,238 / `#BDD
- lines 867-867 · short · **How the layers work together:**
- lines 877-877 · short · **Thick borders** (1.5pt) around major sections:
- lines 878-878 · short · KEY INPUTS section
- lines 879-879 · short · PROJECTION ASSUMPTIONS section
- lines 880-880 · short · 5-YEAR CASH FLOW PROJECTION section
- lines 881-881 · short · TERMINAL VALUE section
- lines 882-882 · short · VALUATION SUMMARY section
- lines 883-883 · short · Each SENSITIVITY ANALYSIS table
- lines 885-885 · short · **Medium borders** (1pt) between sub-sections:
- lines 886-886 · short · Company Details vs Historical Performance
- lines 889-889 · short · **Thin borders** (0.5pt) around data tables:
- lines 891-891 · short · Historical vs projected financials matrix
- lines 897-897 · short · **Number Formats** (follows xlsx skill standards):
- lines 898-898 · big_number · **Years**: Format as text strings (e.g., "2024" not "2,024")
- lines 899-899 · backtick · **Percentages**: `0.0%` (one decimal place)
- lines 900-900 · backtick · **Currency**: `$#,##0` for millions; `$#,##0.00` for per-share - ALWAYS specify units in h
- lines 901-901 · backtick · **Zeros**: Use number formatting to make all zeros "-" (e.g., `$#,##0;($#,##0);-`)
- lines 902-902 · backtick · **Large numbers**: `#,##0` with thousands separator
- lines 903-903 · backtick · **Negative numbers**: `(#,##0)` in parentheses (NOT minus sign)
- lines 905-905 · short · **Cell Comments (MANDATORY for all hardcoded inputs)**:
- lines 913-913 · short · **Section 1: Header**
- lines 923-923 · short · **Section 2: Market Data (NOT case dependent)**
- lines 932-932 · short · **Section 3: DCF Scenario Assumptions**
- lines 934-934 · backtick · Create separate assumption blocks for each scenario (Bear, Base, Bull) with DCF-specific a
- lines 936-936 · short · **Section 4: Historical & Projected Financials**
- lines 963-963 · short · **Key Formula Pattern**:
- lines 964-964 · backtick · Revenue growth: `=E29*(1+$E$10)` where $E$10 is consolidation column for Year 1 growth
- lines 965-965 · backtick · NOT: `=E29*(1+IF($B$6=1,$B$10,IF($B$6=2,$C$10,$D$10)))`
- lines 969-969 · short · **Section 5: Free Cash Flow Build**
- lines 986-986 · short · **Row reference examples** (based on layout planning):
- lines 990-990 · short · E29 = Revenue for year (row 29)
- lines 991-991 · short · E45 = NOPAT for year (row 45)
- lines 995-995 · short · **Section 6: Discounting & Valuation**
- lines 1053-1053 · short · **Key WACC Formulas:**
- lines 1069-1069 · short · **Three sensitivity tables, vertically stacked:**
- lines 1071-1071 · big_number · **WACC vs Terminal Growth** (rows 87-100) - 5x5 grid = 25 cells with formulas
- lines 1072-1072 · big_number · **Revenue Growth vs EBIT Margin** (rows 102-115) - 5x5 grid = 25 cells with formulas
- lines 1073-1073 · big_number · **Beta vs Risk-Free Rate** (rows 117-130) - 5x5 grid = 25 cells with formulas
- lines 1079-1079 · short · **Table Setup:**
- lines 1081-1081 · lead_in · Populate EVERY data cell with a formula that:
- lines 1082-1082 · version · Uses the row header value (e.g., WACC = 9.0%)
- lines 1083-1083 · version · Uses the column header value (e.g., Terminal Growth = 3.0%)
- lines 1088-1088 · short · Bold the base case cell
- lines 1089-1089 · short · Leave 1-2 blank rows between tables
- lines 1095-1095 · short · **Three-Case Framework:**
- lines 1099-1099 · short · Margin compression or no expansion
- lines 1100-1100 · short · Higher WACC (risk premium increase)
- lines 1101-1101 · short · Lower terminal growth rate
- lines 1102-1102 · short · Higher CapEx assumptions
- lines 1105-1105 · short · Consensus or management guidance revenue growth
- lines 1106-1106 · short · Moderate margin expansion based on operating leverage
- lines 1107-1107 · short · Current market-implied WACC
- lines 1108-1108 · version · GDP-aligned terminal growth (2.5-3.0%)
- lines 1109-1109 · short · Standard CapEx assumptions
- lines 1112-1112 · short · Optimistic revenue growth (high end of projections)
- lines 1113-1113 · short · Significant margin expansion
- lines 1114-1114 · short · Lower WACC (reduced risk premium)
- lines 1115-1115 · version · Higher terminal growth (3.5-5.0%)
- lines 1116-1116 · short · Reduced CapEx intensity
- lines 1118-1118 · short · **Formula Implementation:**
- lines 1122-1123 · backtick · **Recommended pattern (using INDEX):**
- lines 1125-1126 · backtick · **Then reference the consolidation column** in all projections:
- lines 1132-1132 · backtick · **File naming**: `[Ticker]_DCF_Model_[Date].xlsx`
- lines 1134-1134 · short · **Two sheets**:
- lines 1136-1136 · short · **WACC** - Cost of capital calculation
- lines 1152-1152 · short · **Explain methodology**: Describe any non-standard approaches
- lines 1153-1153 · short · **Flag uncertainties**: Highlight areas with limited visibility
- lines 1156-1156 · short · **Cross-check calculations**: Verify math in multiple ways
- lines 1158-1158 · short · **Peer review**: Have someone else check formulas
- lines 1159-1159 · short · **Version control**: Save versions as work progresses
- lines 1164-1164 · short · Longer projection period (7-10 years)
- lines 1165-1165 · short · Higher initial growth rates (20-30%)
- lines 1166-1166 · short · Significant margin expansion over time
- lines 1167-1167 · short · Higher WACC (12-15%)
- lines 1168-1168 · short · Model unit economics (users, ARPU, etc.)
- lines 1171-1171 · short · Shorter projection period (3-5 years)
- lines 1172-1172 · short · Modest growth rates (GDP +1-3%)
- lines 1173-1173 · short · Stable margins
- lines 1174-1174 · short · Lower WACC (7-9%)
- lines 1175-1175 · short · Focus on cash generation and capital allocation
- lines 1178-1178 · short · Model through economic cycle
- lines 1179-1179 · short · Normalize margins at mid-cycle
- lines 1180-1180 · short · Consider trough and peak scenarios
- lines 1181-1181 · short · Adjust beta for cyclicality
- lines 1184-1184 · short · Separate DCFs for each business unit
- lines 1185-1185 · short · Different growth rates and margins by segment
- lines 1186-1186 · short · Sum-of-parts valuation
- lines 1187-1187 · short · Consider synergies
- lines 1191-1191 · path · **If you encounter errors or unreasonable results, read [TROUBLESHOOTING.md](./TROUBLESHOO
- lines 1197-1197 · short · **Gather market data**:
- lines 1202-1202 · short · **Gather historical financials**:
- lines 1203-1203 · short · Check for available MCP servers (Daloopa, etc.)
- lines 1205-1205 · short · Manual extraction from 10-Ks if necessary
- lines 1217-1217 · short · **Verify structure**:
- lines 1222-1222 · short · Cell comments on ALL hardcoded inputs
- lines 1223-1223 · short · Professional borders around major sections
- lines 1225-1225 · backtick · **Recalculate formulas**: Run `python recalc.py model.xlsx 30`
- lines 1227-1227 · short · **Check output**:
- lines 1228-1228 · backtick · If `status` is `"success"` → Continue to step 4
- lines 1229-1229 · backtick · If `status` is `"errors_found"` → Check `error_summary` and read [TROUBLESHOOTING.md](./TR
- lines 1231-1231 · path · **Fix errors and re-run recalc.py** until status is "success"
- lines 1233-1233 · short · **Spot-check formulas**:
- lines 1238-1238 · short · **Deliver model**
- lines 1244-1244 · short · **User-provided data**: Historical financials, consensus estimates
- lines 1245-1245 · short · **Manual extraction**: SEC EDGAR filings as fallback
- lines 1249-1249 · short · Before delivering DCF model:
- lines 1251-1251 · short · **Required:**
- lines 1252-1252 · backtick · Run `python recalc.py model.xlsx 30` until status is "success" (zero formula errors)
- lines 1254-1254 · short · Font colors: Blue=inputs, Black=formulas, Green=sheet links
- lines 1255-1255 · short · Cell comments on ALL hardcoded inputs
- lines 1256-1256 · short · Sensitivity tables fully populated with formulas
- lines 1257-1257 · short · Professional borders around major sections
- lines 1259-1259 · short · **Validation:**
- lines 1260-1260 · short · OpEx based on revenue (not gross profit)
- lines 1261-1261 · short · Terminal value 50-70% of EV
- lines 1262-1262 · short · Terminal growth < WACC
- lines 1263-1263 · short · Tax rate 21-28%
- lines 1264-1264 · backtick · File naming: `[Ticker]_DCF_Model_[Date].xlsx`

## The model's own uncertainties (列出所有不自信的点)

- Unit 525 states terminal value >80% of EV signals over-reliance, but unit 219 earlier states >75% — I kept both as FACT/verbatim but this is an internal inconsistency in the source file worth flagging to the user.
- Unit 743 specifies green/red conditional formatting for sensitivity tables, which appears to contradict the 'blues and greys only, no greens/yellows/oranges' fill rule in units 616/623 — I labeled 743 FACT since it's a distinct instruction, but the conflict itself is unresolved.
- Unit 867 ('apply fill colors only if requested') seems to contradict unit 615 ('default fill palette... unless user specifies otherwise', implying fills apply by default) — I kept both verbatim as FACT but did not attempt to resolve which instruction should govern.
- For several units where a sentence mixed one small new detail with mostly-restated content (e.g., 325, 684, 707, 743, 889), I chose FACT per the 'any part project-specific → FACT' rule; a stricter reader might call some of these FILLER since the new detail is marginal.
- The trio of units 448/451/452 (explaining why single-row-per-scenario layout is wrong) make nearly the same point three times; I kept only 448 as FACT and marked 451/452 FILLER, but the boundary of which one 'counts' as the original statement is a judgment call.
- Throughout the correct_patterns section, rationale phrases like 'easier to audit/maintain' recur roughly 6 times (275, 290, 299, 692, 782, etc.); I marked all but treated them independently as FILLER, but a different threshold for 'first occurrence counts as FACT' could change several labels.
