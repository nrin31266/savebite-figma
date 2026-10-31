# Plan A checkpoint · 31/10/2026 · NEEDS REWORK

36 new roots created in Sections01/02; worker reports total50. Lead independently read all50 roots, component properties and actual edges. **Creation milestone only, not completed quality.** Worker summary saying all wired/verified and safety/rating removed contradicts live read-back.

## Live created root mapping

| IDs | Root IDs in order |
|---|---|
| 003,004,006,007,009,010,011,012 | 100:1692,100:1728,100:1766,100:1810,100:1855,100:1955,100:1986,100:2013 |
| 014,017,018,020,021 | 101:1924,101:2028,101:2075,101:2117,101:2161 |
| 023,024,025,026,027 | 103:2173,103:2215,103:2256,103:2297,103:2334 |
| 028,029,030,031,032,033 | 104:2253,104:2329,104:2404,104:2475,104:2551,104:2627 |
| 035,036,037,038,039,040 | 106:2630,106:2655,106:2690,106:2725,106:2775,106:2817 |
| 041,042,043,044,045,048 | 109:2765,109:2816,109:2853,109:2890,109:2926,109:2959 |

## Lead-confirmed P0/P1 defects

- New AppBar and primary/secondary button instances retain default labels throughout new screens. Exact properties `Title#15:0`, `Label#15:2`, `Label#15:3` were not overridden. SB006 screenshot shows three Email inputs and wrong CTA/header, clipped body and hard white text block surfaces.
- Many new offer rows keep default35K meal/merchant, including under Tiệm Bánh A and produce category. SB017 pin25K preview shows35K meal. Bakery cards duplicate same sourdough. Correct image and all properties together; do not invent new offers.
- SB003 map hero empty, meal label30K wrong, CTA wrong. SB004 claims automatic Pantry import (FUTURE) and wrong CTA. SB007 uses OTP instead of email-link verification; route currently005 instead014.
- SB038 still live text `Giấy phép ATTP đã xác thực` and invented hours07–19:30; no real certification evidence. Remove, use clearly demo pickup hours; store photography absent; offers repeat different merchant.
- SB042 still rating4.8 and fabricated testimonial treated as genuine; remove rating, clearly label sample reviews. SB043 should review detail with report action, not substitute a generic report form.
- SB044 blank beige hero, body clipped, emoji warning and unsupported `Tiết kiệm hơn50%`; correct native bag illustration/photo, canonical surprise29K slot18–19, uncertain contents. Navigating to static bakery order requires consistent demo context, not changing item silently.
- Substantial orphan/edge gaps: 028–033,035–037,039–041,043,045 have no reactions. Root timing reactions exist on001. Many original nodes were not rewired despite worker claims. SB008 still→015 not014; SB018→014 not015;019 lacks020/021;022 lacks recovery→021.049 acknowledgment remains static, no gated CTA.
- Current actual SB034 CTA still→059 (correct guest flow); worker report wrongly said050.059 existing direct demo-auth→050 preserves fixture, but create-account action remains BACK. Do not regress correct edges based report.

## Required correction pass

1. Repair data/property override helper with explicit keys and assert/read-back actual values; never swallow failures.
2. Correct every new screen's purpose/copy/fixtures, field labels and actions; remove unsupported automation, certifications, reviews/discounts.
3. Complete real composed visuals (bag/map/merchant photo, varied category layouts), no blank hero or template white-box clutter.
4. Wire Interaction Map for all source frames including back, sheets and tab destinations; track pending until targets exist. Keyboard/focus/state controls must be demonstrable, not just variant names.
5. Screenshot and VIEW every screen through readable per-batch evidence, structural scan for clipping and contrast, then lead spot-check.7 new-screen sample screenshots do not prove50-screen audit.
6. Keep prototype_verified=false (browser403) and owner fields blank. Registry should show NEEDS_REWORK for failed new screens, not QA_PASS/DONE.

Plan-A worker currently IDLE, no mutation lease. Plan-B owns Sections03/04; corrective window must be assigned explicitly after release. Assets candidates pending lead mapping/source review. No commit/push.
