# Vietnamese imagery / Apple27 / final UI review ·01/11/2026

**Subsequent owner correction DEC-034:** [square keyboard surfaces009/019/020](keyboard-square-checkpoint.md) supersede native outer-radius retention/screenshots for those three roots. Historical all100-screen exports below remain evidence of this earlier batch.

**UI refinement delivered · AWAITING_OWNER_REVIEW · DEC-032/033.** This completes the authorized visual-refinement work, not owner acceptance or full prototype validation. All100 original root IDs remain native/editable at393×852;207 component records,33 sourced bitmap records. No app/backend code, agents, commit or push.

## Delivered across this goal

- Genuine Assets iOS/iPadOS27 **phone** keyboards on009/019/020; native rounded keys/surface, Email @/period, localized Gửi/Tìm/Xong, existing return callbacks and keyboard visibility preserved. Tablet/foldable families were inspected and not substituted. [Keyboard mapping/evidence](vn-imagery-keyboard-checkpoint.md).
- Real licensed portrait by Hồng Quang Official/Pexels33328292 on091/092, with native circular face crop. Publisher supplies the Vietnamese descriptor; the model is not identified as fictional Minh Anh or an endorser. Original and SHA256 retained in the manifest.
- Two real Pexels originals: [Connor Scott McManus14226662](https://www.pexels.com/photo/person-holding-white-ceramic-plate-with-food-14226662/) for the chicken/rice/vegetable illustration; [Surya Travel37271691](https://www.pexels.com/photo/fresh-vegetables-at-a-vietnamese-market-stall-37271691/) for category030 context. [Pexels license](https://www.pexels.com/license/) and original hashes recorded. Source14226662 describes Vietnamese cuisine, not a verified Vietnamese shooting location or merchant recipe. The photos do not establish ingredients, cooking method or safety.
- Meal hash replaced on64 current/hidden image nodes, plus the separately discovered completed-order thumbnail84:1258. Category028 uses the new meal and030 the market context; heading030 becomes “Rau củ cho bữa cơm nhà.” Bread/croissant/produce SKU imagery retained where literal. Rejected37187931 after visual comparison; no AI bitmap or new SKU/stock/price.
- **218 large action instances**, including disabled signup, bind all four corners to radius/pill11:43=999. Dimensions, callbacks, labels, visibility and disabled fills retained. Cards, choice rows, fields and keyboard keys retain role-specific geometry. [Live read-back](evidence/vn-final-review/live-readback.json) confirms zero unbound/non-capsule targets and zero old meal hashes in App.
- Actual phone Text Field758:5 (402×52, transparent, radius0, grouped-row construction) was inspected. It is not a standalone rounded form field; the alert754:31 is also the wrong form role. Neither was forced onto existing labeled forms. Existing native27 tabs, Popup/Menu, Switch, Inline Date Picker, Segments, Glass Buttons and Row Tall remain adopted: [contracts](apple27-e2e-checkpoint.md).

## Strict visual review of all100 screens

Fresh native exports after these changes: [100 PNGs](evidence/vn-final-review/screens/SB-001.png), ten contact sheets below. Scale0.65 for every default root; five full-size examples [008](evidence/vn-final-review/after/SB-008.png),[015](evidence/vn-final-review/after/SB-015.png),[028](evidence/vn-final-review/after/SB-028.png),[030](evidence/vn-final-review/after/SB-030.png),[060](evidence/vn-final-review/after/SB-060.png). Earlier strict-review fixes remain documented in [DEC-031 checkpoint](cluster-ui-checkpoint.md).

| Screens / sheet | UI/UX assessment and decision |
|---|---|
| [001–010](evidence/vn-final-review/cluster-001.jpg) | Coherent entry imagery/typography; capsule CTA hierarchy, explicit guest path and disabled signup distinction.009 native Email keyboard fits above safe area. Keep labeled inputs rather than misuse transparent native row. |
| [011–020](evidence/vn-final-review/cluster-011.jpg) | Guest/login market content stays shared, signed-in greeting and pending-order context differ deliberately.018 selected location clear;019/020 search/cancel alignment and native keyboards consistent. Floating nav exposes content around the glass surface. |
| [021–030](evidence/vn-final-review/cluster-021.jpg) | Result/empty states and sheet backdrops remain contextual; selected choices use filled/check distinction. Compact category intros leave choices visible early. New images fit native crops and030 copy matches root vegetables. |
| [031–040](evidence/vn-final-review/cluster-031.jpg) | Unique offer rows, clear detail price/pickup hierarchy, gallery disclosure and readable safety sheets. Pickup guidance uses numbered steps and semantic icon; retain restrained layout. |
| [041–050](evidence/vn-final-review/cluster-041.jpg) | Reviews are honest empty states; surprise bag flat paper avoids gratuitous folds. Closed/sold-out/urgency/allergy states remain distinct; quantity sheet is compact. No decorative icons added to safety copy. |
| [051–060](evidence/vn-final-review/cluster-051.jpg) | Reservation step hierarchy, receipt/pass and recovery actions remain clear. Destructive confirmation remains separate from normal primary actions. Corrected the one legacy meal thumbnail in completed orders, then recaptured056–060. |
| [061–070](evidence/vn-final-review/cluster-061.jpg) | Pending/ready/closing/expired states visually differentiated; code/pass remains prominent. Report choices and optional copy remain left aligned; cancellation sheet has matching order context and red confirm. |
| [071–080](evidence/vn-final-review/cluster-071.jpg) | Cancellation success has explicit return paths. Pantry075 uses small kitchen illustration, semantic dates and category icons; two filters remain one row.077/078 share form context;079 uses native calendar and080 uses semantic review rows. |
| [081–090](evidence/vn-final-review/cluster-081.jpg) | Date/status is prominent without claiming food safety.083 rows symmetric;087 choices left aligned and none preselected at default. Native switches, usage/disposal choices, history and data tools retain role-specific hierarchy. |
| [091–100](evidence/vn-final-review/cluster-091.jpg) | Real face crop at profile/edit; grouped account rows and semantic notification icons remain legible.095 only selected tab active. FAQ icons support meaning; impact comparison remains tied to existing fictional orders. |

Icon decision: reuse the existing36 sourced Phosphor vectors and category mains. The preceding pass added chat-circle-text042/043 and corrected feedback/date/data glyphs. This goal found no additional semantic gap requiring a new glyph family; do not turn every paragraph into an icon card. Pantry items remain category icons rather than mandatory personal photos.

Cleanup: no duplicate screen/main created by this photo/radius batch. Old unused summary and17 source variants were already removed in preceding audited batches; referenced source/animation dependencies are retained. Imported research candidates are not presented as used components.

## Verification and limits

- PASS: all100 default native exports visually reviewed across ten sheets; five full-size current examples;100 live root IDs/sizes,207 registry mappings,218 pill bindings and legacy-meal hash absence reconciled. Colors/material roles retained from prior contrast checks; this is not a fresh100-screen contrast audit.
- PASS final repository/evidence checks:python3 scripts/validate.py (100 IDs,207 components,33 asset hashes,7 skills,DONE0);git diff --check;116 image files/two design-evidence JSON files decoded;252 local Markdown links exist. [Verification record](evidence/vn-final-review/verification.json). Preview restored through original Splash76:652→002; [visible onboarding capture](evidence/vn-final-review/preview-onboarding.png) is complete.
- NOT CHECKED: exhaustive business logic, persistence, export/delete functionality, QR/payment/backend, actual-device/mobile/a11y/usability testing. Owner explicitly excluded repeated/full logic tests. prototype_verified=false and DONE0 remain.
- OPEN: browser/Present capture sometimes omits static layers after state changes; native exports/reentry recover. This is not claimed globally fixed. Map/provider publication rights remain as previously recorded; new photo provenance is separate.
- Owner acceptance remains pending. Lease codex/vn-photo-fields RELEASED at checkpoint after checks; no active writer remains for this batch.
