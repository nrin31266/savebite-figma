# Cluster UI critique/refinement ·01/11/2026

**AWAITING_OWNER_REVIEW.** Owner asked for an independent, strict designer review of UI/UX only, including the previous visual direction/native-kit/component requirements. Full business-logic testing excluded.100 current root frames captured,30 roots revised,195 registered component entries. Owner acceptance remains pending/DONE0.

## Review method and coverage

Read current repo and live Figma, then captured all100 default frames at0.65 scale into before/. Reviewed ten comparison sheets and the affected screens at full native393×852 scale. Final sheets combine the30 revised full-size exports with70 retained images as marked. This proves static UI coverage, not every runtime state or device width.

| Cluster | Evidence | Result |
|---|---|---|
|001–010 Entry/Auth |[sheet](evidence/cluster-ui/final-cluster-001.jpg)|003 wording cleaned; forms/auth direction retained.|
|011–020 Home/Location/Search |[sheet](evidence/cluster-ui/final-cluster-011.jpg)|013 login entry redesigned; other default layouts retained.|
|021–030 Search/Filters/Categories |[sheet](evidence/cluster-ui/final-cluster-021.jpg)|Search copy/scroll insets;028–030 compact listing-first headers.|
|031–040 Discovery/Offer |[sheet](evidence/cluster-ui/final-cluster-031.jpg)|031 unique time-ordered offers;032 inset;033 header search. Offer detail/photo/safety hierarchy retained.|
|041–050 Merchant/Offer variants |[sheet](evidence/cluster-ui/final-cluster-041.jpg)|041 copy;042/043 feedback icon;047 state clock/copy.|
|051–060 Reservation |[sheet](evidence/cluster-ui/final-cluster-051.jpg)|Default states retained after visual comparison; no logic retest.|
|061–070 Pickup/Cancel |[sheet](evidence/cluster-ui/final-cluster-061.jpg)|067 clock,070 destructive color; existing ticket and pickup hierarchy retained.|
|071–080 Confirmation/Pantry entry |[sheet](evidence/cluster-ui/final-cluster-071.jpg)|071 hierarchy/actions;072 clock;073 inset;075/076 top tools;078 backdrop.|
|081–090 Pantry |[sheet](evidence/cluster-ui/final-cluster-081.jpg)|083 semantic/symmetric rows;084 copy;090 export hierarchy.|
|091–100 Account/Help |[sheet](evidence/cluster-ui/final-cluster-091.jpg)|092 feedback/form;095/096 settings;098/099 icons and help semantics.|

## Findings fixed

| Finding | Severity | Implemented result |
|---|---|---|
|Guest login buried in a feed strip with an oversized100pt target/negative local y; guest header looked like signed-in controls.|High|013 native SDS secondary104×44 sage pill at header; remove old footer strip and guest heart/bell overlays. Market and optional guest entry unchanged.|
|History/data/preferences required reaching list end.|High|075/076 native overflow menus in header;095/09644pt preferences icon. Removed duplicate footer actions.033 header search, removing its repeated Explore button.|
|Category marketing occupied342pt before count/list.|High|028–030128pt horizontal intro; list starts at body y206 instead of428 (222pt earlier). Meal/produce guidance84/102pt; remove duplicate Pantry CTA;029 related bag is existing canonical offer row rather than a large promo/button.|
|031 repeats meal three times and labels a17:30 slot as opening within60min of16:00.|High|Three unique canonical offers ordered16:00/17:00/17:00; neutral “Khung nhận gần nhất”. No new SKU/stock.|
|Native floating nav over short legacy viewport cut list content early.|Moderate|021/028–030/032/033/073/075/076 extend viewport to818 and ensure104pt end inset; bar remains above content with transparent surroundings.|
|078 category sheet shows blank grey background.|Moderate|Native077 context721:9043 behind scrim, background interactions stripped.|
|Cancellation confirmation looks like search; copy panel/priority weak.|Moderate|EmptyState98:109 exposes Icon swap;071 Check icon,22pt heading/flat canvas, primary Orders and secondary Explore.070 destructive CTA error-red/white.|
|Clock contradicts closed/closing/completed state.|Moderate|04718:30,06717:45,07217:30; closed copy removes unsupported next-day opening claim. These are static fixture-state clocks.|
|083 dairy uses plant and has a one-off full-width milk shortcut.|Moderate|Correct milk glyph; two symmetric353×80 rows with chevrons/context from canonical milk/bread rows; remove shortcut.|
|False saved feedback visible before editing; profile helper is clutter.|Moderate|Remove092 saved banner/avatar helper; align form upward12pt; Save returns091. No persistence claim.|
|Data page lacks hierarchy and includes prototype-only navigation.|Moderate|090 native Apple27 Row Tall, JSON/CSV format badges, neutral captions, red trash header; remove empty-state preview button/cloud-roadmap footer. Export/delete runtime not implemented by this UI pass.|
|FAQ questions jump directly to cancellation or a date editor.|High|099 rows are informational with inline answers; no task-changing navigation. Report-issue CTA remains. Search copy uses a neutral placeholder; no search engine claim.|
|Unrelated food/leaf icons used for reviews, date and data.|Minor|Native Phosphor chat-circle-text for042/043; calendar/pickup-pass/pantry icons for help/privacy. New icon source+MIT/hash recorded.|
|Visible “mẫu/MVP” copy distracts from product tasks.|Minor|003/022/041/083/084/099 cleaned; source/fixture/safety truth kept in domain docs.|

## Components, cleanup and provenance

- New native Menu Item648:1085 (Selection=False) used by top menus724:8475/8745;195 registry entries. Source contracts/keys in [live readback](evidence/cluster-ui/live-final.json).
- EmptyState Icon#720:0 default98:62,07198:47. New Phosphor master731:1021,24pt token-bound vector, used twice. Existing source SVG/MIT license and hash in assets/icons/phosphor/sources.json.
- Removed retired075 summary instance20:23 and master16:161 from Components tree; removed duplicate031 rows104:2500/2508/2516 and superseded footer/feedback controls. Figma lookup retains a detached master object, but Components live traversal contains no16:161 and no App usage remains.
- Retained referenced source sheets, animation phases and runtime variants; zero default instances alone is insufficient proof to delete a state.
- No new bitmap/photo, no app/backend code, no new merchant/inventory/review/metric. Existing Apple27 native source masters not edited.
- Research: [Apple sheets](https://developer.apple.com/design/human-interface-guidelines/sheets?changes=_1), [lists](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables?changes=_5), [Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass), [KitchenPal publisher inventory example](https://kitchenpalapp.com/en/faqs/kitchen.html). Applied task-focused headers, readable rows and secondary tools separated from primary actions; no competitor assets/branding imported. Publisher screenshot is a static reference, not a current-app usability audit.

## Verification and limits

- PASS scoped native visual/read-back:100 baseline images,30 revised exports; ten final cluster sheets. Source copy, header targets, menu geometry238×104/slot222×88,222pt category-list advance and semantic icon IDs verified.
- PASS scoped browser:guest header login→008;075 overflow→089;029 list/end scroll with fixed nav. Native menu captures are complete; browser capture can still omit static layers after a variable change (known limitation, not closed).
- [Mutation records](evidence/cluster-ui/mutations.json), [root/component/navigation mapping](evidence/cluster-ui/live-final.json). Registry navigation edges are read-back, not full flow tests.
- PASS final repo checks:validator100 IDs/195 components/30 photo hashes/7 skills/DONE0; git diff --check;156 evidence images and2 JSON decoded before final onboarding/check report;36 Phosphor SVG hashes/license paths verified. Contrast:red/white6.57,forest/sage10.00,secondary/white5.36. [Final onboarding capture](evidence/cluster-ui/runtime/onboarding-restored.png) verified after load; [completion checks](evidence/cluster-ui/final-checks.json).
- NOT CHECKED:full logic/date/filter matrix, export/delete/persistence/search backend, real QR/payment, responsive/Dynamic Type/VoiceOver/usability or owner acceptance.
- No commit/push. Lease codex/cluster-ui RELEASED at this checkpoint.
