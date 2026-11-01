# Native27 keyboard /100 device frames ·01/11/2026 ·DEC-035

**AWAITING_OWNER_REVIEW ·DEC-035/036.** Full requested UI work delivered. Sole file SaveBite-V2,100 original393×852 roots,195 reconciled component records,native editable content. Lease codex/native27-device RELEASED after checkpoint checks. No agents,app/backend code,commit or push.

## Owner correction: glyphs, fresh imports and cleanup ·DEC-036

The earlier box-only comparison missed the owner-visible z–m glyph defect. It was not sufficient evidence of keyboard alignment. Replaced all three previously swapped instances with **fresh exact imports** from the subscribed27 library, retaining native key geometry/fonts and applying only localized return labels/tint/callbacks,visibility and square outer surface.

| Screen | Fresh instance | Exact source asset key |
|---|---|---|
|009|791:8389|7c10fa3da64a14e5d99f13ce9a77b931d1ba794c Email|
|019|791:8498|bf2a52082f2a1eca4e3f9d91fe34c64a9410dd32 Lower Case|
|020|791:8597|bf2a52082f2a1eca4e3f9d91fe34c64a9410dd32 Lower Case|

Old100:1885/17:345/542:5107 removed from App tree; no external prototype reference to those instances existed. All fresh instances393×307,y545. Native19pt return-label text frame93×43 retains CENTER/CENTER; no font-size or glyph-position patch inside alphabet keys. Proof:[009 at200%](evidence/native27-device/keyboard-009-200.png),[019 at200%](evidence/native27-device/keyboard-019-200.png),[020 row3 at300%](evidence/native27-device/keyboard-020-row3-300.png),[actual Present020](evidence/native27-device/present-020-fresh.png),[final live IDs](evidence/native27-device/final-live.json). Fresh import at native402pt and adapted393pt was also visually compared before replacement.

Cleanup:[all-page reference graph/mutation](evidence/native27-device/fresh-keyboards-cleanup.json). App hidden/visible instances and prototype destinations plus Foundations checked; component dependencies/prototype transitions and complete referenced variant families retained. Removed10 top-level objects containing20 local main/set/variant nodes:seven unused icons,two old toggle families,unused six-style Sticker family. Removed15 specimen cells including their obsolete labels. Components local master/set nodes136→116;read-back confirms all20 IDs absent from page traversal. Six brand/seven icon source records now explicitly historical/unused;original SVGs/licenses/hashes retained.

Registry207→195:remove26 unused entries (including11 old cached keyboard-source records),add14 actual used source/dependency records (Spinner plus13 nested mains missed by historical inventory). This is not14 new standalone UI controls. All current nested App main IDs map to the final195 records;current100 root mappings/screenshots refreshed. [Registry reconciliation record](evidence/native27-device/registry-cleanup-preview.json) preserves removed entries for traceability.

## Keyboard: exact source comparison and correction

- Previous291pt container was wrong for the current kit source. Native phone Keyboard750:12279/12282 is402×332; with suggestions hidden its Auto Layout height is307. The old291pt frame held a307pt stack, overflowing16pt and crowding bottom controls.
-009/019/020 use native Auto Layout393×307 at y545. DEC-036 subsequently replaces the three instance IDs as above, retaining source masters/native rows/keycaps/localized returns. Background stays square per DEC-034;device root provides rounded screen clipping.009 CTA477 leaves16pt above keyboard.020 viewport410pt,home indicator818.
- Initial comparison measured33/31 key-instance containers:maximum position/size delta0.0000153pt. **That did not validate glyph rendering and was superseded by enlarged fresh-instance/Present checks in DEC-036.** Temporary references removed. Return callbacks read back:009→010;019→020 with visibility flags;020 hides keyboard. No callback logic changed or full input test claimed.
- [Current009](evidence/native27-device/after/SB-009.png),[019](evidence/native27-device/after/SB-019.png),[020](evidence/native27-device/after/SB-020.png),[source comparison/mutation/live read-back](evidence/native27-device/live-readback.json).

## All100 iPhone roots

- Initial audit:100/100 roots had radius0. Actual subscribed27 phone Examples/Keyboard775:2591 has Screen775:2603 at402×874/radius50. The other similarly named29d2… example is iPad1210×834 and was excluded after inspection.
- New primitive780:1021=50 and semantic radius/deviceScreen780:1022 alias it, scoped CORNER_RADIUS. All four corners on all100 roots bind to the semantic token; clipsContent=true,cornerSmoothing0 matching the source Screen. Existing393×852 viewport/safe areas remain. **This is a visual adaptation of a kit example, not a measured iPhone15 hardware radius or a device-size migration.** Card, sheet, field and keycap radii remain separate.
- Fresh independent native captures for all100 roots, visually reviewed across ten sheets. Rounded clipping leaves status/home indicators, glass nav, full-bleed media, sheets, maps and primary controls readable. Scoped393×852 default-state UI review, not every variable-state permutation/device test.

| Cluster evidence | Reviewed scope |
|---|---|
| [001–010](evidence/native27-device/cluster-001.jpg) | Entry/auth, full-bleed welcome,009 keyboard/CTA clearance |
| [011–020](evidence/native27-device/cluster-011.jpg) | Home, floating nav, map/location, both search keyboards |
| [021–030](evidence/native27-device/cluster-021.jpg) | Results, bottom sheets, categories and clipped bottom corners |
| [031–040](evidence/native27-device/cluster-031.jpg) | Listing/detail/gallery, safety and map contexts |
| [041–050](evidence/native27-device/cluster-041.jpg) | Review/empty/urgent/closed/allergy/quantity states |
| [051–060](evidence/native27-device/cluster-051.jpg) | Reservation, native spinner055, receipts/pass/recovery/orders |
| [061–070](evidence/native27-device/cluster-061.jpg) | Pending/ready/urgent/expired/code/report/cancel sheet |
| [071–080](evidence/native27-device/cluster-071.jpg) | Success, Pantry/root/forms/category sheet/native calendar |
| [081–090](evidence/native27-device/cluster-081.jpg) | Detail/edit/reminder/choices/history/data |
| [091–100](evidence/native27-device/cluster-091.jpg) | Profile, locations, notifications/settings/FAQ/impact |

Capture note:97 screen files at scale0.65;fresh009/019 at1 and020 at0.9 replace affected roots after DEC-036,then scaled only for contact sheets. Full-size055/075 examples retained. Enlarged key/row and actual browser captures distinguish glyph verification from the earlier box-only check. Diagnostic captures retained separately;no global renderer fix claimed.

## What was explored and actually used

[Exact search/source contracts](evidence/native27-device/kit-catalog.json). Search restricted to the subscribed Assets **iOS and iPadOS27** library.

| Kit family | Actual decision / application |
|---|---|
| Phone Keyboard, examples | Correct307pt fit on009/019/020. Device example supplies screen-radius reference for100 roots; iPad/foldable layouts excluded by actual size. |
| Liquid Glass Regular Small641:10524 | New44pt source instance780:1023 in shared AppBar15:106. Back target/spacer40→44,padding12,glyph centered; existing Phosphor chevron and caller callbacks retained.63 AppBar screens inherit it; source glass appears on80 roots including prior nav/toolbars. [009](evidence/native27-device/after/SB-009.png). |
| Native Spinner777:1024 | New35pt instance781:11819 centered in existing44pt holder83:1228 on055. Forest tint preserves source bar opacities; two old ellipse children removed. [055](evidence/native27-device/after/SB-055.png). |
| Tabs, Popup/Menu, Switch, Inline Calendar, Segments, Glass Text buttons, Row Tall | Existing genuine27 adoption retained and reviewed with rounded device frames; source contracts in [previous native27 checkpoint](apple27-e2e-checkpoint.md). |
| iPhone17 hardware body | Inspected402×874/physical body asset; reference only. No bitmap device overlay added to100 editable screens and no switch from current viewport. |
| Alert775:1891 | Title/message/action-slot variants inspected. Not inserted into data deletion merely to display an asset:090 has no existing destructive confirmation contract. No data-clearing behavior invented. |
| Symbol Button782:1058 | Intrinsic50×50 inspected. Reference only for future larger toolbar; current48pt AppBar uses resizable glass surface with44pt hit target rather than squeezing this control. |
| Search results | Sidebar Search and keyboard Search accessory have different roles from the current phone top search. Shared existing SearchField/Cancel retained; no sidebar field substituted. |

No research specimen or temporary comparison instance remains on App canvas. Imported library candidates are not counted as adopted/registered components. Only actual used Spinner main is added to registry; source masters unchanged. No new bitmap;33 asset hashes retained.

## Checks and limits

- PASS live:100 IDs/sizes/four radius bindings/clipping;fresh keyboard source/glyph checks;63 shared AppBar callers;native spinner main/size.195 registry entries after cleanup/reconciliation,no root-ID change.100 default root captures reviewed,three affected captures refreshed after fresh replacement.
- PASS repository/evidence:python3 scripts/validate.py (100 IDs/195 components/33 asset hashes/7 skills/DONE0),git diff --check,121 image/seven JSON decode before adding final preview/verification records;32 brand/36 Phosphor original hashes checked.195 registry entries resolve every current nested App main. Cleanup read-back:116 local nodes,zero deleted nodes still present,zero unreachable retained nodes.
- PASS scoped Present020 with complete fresh keyboard and corrected glyphs. Preview restored through original Splash76:652→002;[capture](evidence/native27-device/preview-onboarding.png). [Final verification record](evidence/native27-device/verification.json) records final image/JSON totals and requirement evidence. No full-flow acceptance.
- NOT CHECKED:full logic matrix, actual-device/a11y/usability, production keyboard/input/persistence/payment/QR/export/delete. Owner acceptance pending;prototype_verified=false,DONE0.
- OPEN:static-layer omissions can occur in capture after shared/variable state; source geometry intact, separate exports/reentry recover. Map/provider publication status unchanged. No global render/full Present claim.
