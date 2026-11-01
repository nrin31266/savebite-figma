# Apple27 / Pantry / full UI refinement ·01/11/2026

**AWAITING_OWNER_REVIEW.** Requested UI pass delivered; not owner acceptance. Sole target SaveBite-V2,100 SB root IDs retained,194 registered component entries, DONE0. Lease codex/apple27-e2e RELEASED; no commit/push in this goal.

## Owner scope

Full UI scope retained: compact075, status/storage filtering, semantic labels across App, actual Apple27 adoption, floating transparent navigation, important screen clusters, longer lists, product copy cleanup and final onboarding preview reset. Owner reduced exhaustive/repeated logic testing only; full implementation cases deferred until code. No app/backend code or invented user research.

Frontend-design, ui-ux-pro-max, brainstorming and native Figma skills used. Project-local mobile-ios-design installed/read; pinned source/hash in the seven-entry skill manifest.

## Delivered

-075:88pt light-kitchen hero/Mầm64pt,112pt icon rows; Sắp hạn/Còn hạn/Quá hạn/Chưa rõ badges separate from neutral44pt Dùng/Bỏ. Two native Apple27 Popup Buttons652:8472/8476 share row652:8471; genuine menus/checkmarks. Status intersects storage/active. Fixed reference19/10/2026; unknown≤0 or≥10000. No freshness/safety score.
- Shared BottomNav15:122:actual TabBar641:10609,22 callers,393×95 at y757. Native glass/selected-unselected SF symbols, forest tint, transparent outside. Z-order above scroll content; page extends behind capsule, final inset exposes last content.
- Actual Apple27 Switch648:1543/1542 in local64×48 hit-area set659:1022 adopted085/097; inline DatePicker648:1647 and date-type segments670:8651 on079;44pt glass month arrows and Map016 controls; Row Tall690:1136/native separators in089/095. Source masters unchanged. Imports work, no restart needed.
- Home013/014/015 share five canonical offers, including existing vegetable offer. Greeting/pending card retained; Home/Profile viewport extends behind nav. No new inventory/stock/merchant.
-081:compact104pt category-icon hero700:8159, bound semantic expiry card, neutral outlined disposal action. Existing per-item flags retained; eggs use Egg glyph.
-089/095:category/context icons and readable native rows; eight seed historical events and seven notification events create longer lists. Dynamic history slots, group filters and unread markers retained.
- Whole-App labels:waiting/near amber, ready green, unavailable neutral, expired red. Removed visible debug/demo/fixture copy; display units3 đơn/4 món. Safety/unknown/photo provenance retained. SB-001/SB-A125 remain synthetic display codes; QR unchanged.
-070:native062 order context708:11442 behind dimmed cancel sheet, replacing blank grey backdrop. Background interactions removed; original sheet actions retained.
- Visual review:all ten North-Stars002/015/016/019/034/051/053/056/075/091 plus018/038/060/070/077–081/085/087/089/095/097 and shared callers. Scoped UI review, not every state of100 screens.

## Data/provenance

[Product defaults](../docs/product.md) own synthetic events/fixed dates. Added notifications/history are UI events only; seven current items,3 received orders,4 historical used items and90K paid unchanged. No new bitmap/photo pool:30 canonical photo records,32 brand SVG records and existing icons reused. [Native contracts](evidence/apple27-e2e/a27FinalContracts.json) record actual keys/properties. Technical import does not establish redistribution rights; map/provider publication status unchanged.

## Evidence and checks

- PASS structural:[final100-root mapping](evidence/apple27-e2e/a27InventoryFinal.json),194 registry entries.145 mains in visible/variable-bound UI plus one configured calendar state; registry also retains existing fallback/candidate mains.194 is not a screen count.
- PASS scoped native screenshots:[075](evidence/apple27-e2e/after/SB-075.png),[Home](evidence/apple27-e2e/after/SB-015.png),[Map](evidence/apple27-e2e/after/SB-016.png),[detail](evidence/apple27-e2e/after/SB-081.png),[history](evidence/apple27-e2e/after/SB-089.png),[notifications](evidence/apple27-e2e/after/SB-095.png),[cancel context](evidence/apple27-e2e/after/SB-070.png). Native menu visible bounds238×236/slot222×220; previous hidden-height concern RESOLVED.
- PASS scoped experience:Soon→milk+bread, Soon+Dry→bread; one independent notification toggle; Nov15→form→reopen selected date. [Pantry scroll](evidence/apple27-e2e/runtime/pantry-scrolled.png) reaches final items/history/data footer with fixed floating nav.
- PASS preview reset:Splash76:652 auto→first Onboarding17:2; [capture](evidence/apple27-e2e/runtime/onboarding-restored.png).
- PASS visible copy scan:no debug/demo/fixture/sample-data strings in visible App text. Fixture truth remains in docs.
- PASS final repo checks:python3 scripts/validate.py (100 IDs,194 components,30 photo hashes,7 skill hashes,DONE0); git diff --check;27 PNGs and27 JSON files decoded; registry/local links checked. These checks do not establish license, full runtime or owner acceptance.
- NOT CHECKED by owner scope:full F-01..F-06 logic matrix, all date/filter permutations, production persistence/payment/QR scan, multi-device accessibility/usability.
- OPEN:Present/browser capture sometimes omits static layers after state changes; reentry/native exports restore them. Minimum calendar-state updates reduce ghosting; no global render fix/full Present PASS.

[Phase3 records](evidence/apple27-e2e/a27Phase3.json) retain mutation IDs, copy/data updates and visible menu geometry. Earlier captures are historical; registry screenshot paths identify current exports.
