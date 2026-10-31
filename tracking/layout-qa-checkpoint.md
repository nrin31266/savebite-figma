# Layout and flow QA contract · 31/10/2026

Docs-derived review, integrated and corrected by lead. This is a test specification, **not** a live canvas audit or a test result. No competitor interface was independently verified in this review. The patterns below are proposals grounded in existing SaveBite art direction, not research findings.

## Invariants and known issues

- DEC-012 authorizes full implementation, not baseline acceptance. Owner fields remain empty and DONE=0 until actual approval.
- No invented CO₂, merchant verification, ratings or savings. Demo pickup counts, grounded savings and Pantry used-in-time counts remain separate; no money saved without an evidenced reference price.
- Undeclared ingredients/allergens remain UNKNOWN; confirmation does not make an unsafe or unknown item safe. Surprise bags disclose variable contents prominently.
- Fixture examples in product are not a blanket override of the detailed asset/art-direction mappings. Lead is reconciling that drift; the sourdough order chain stays 25.000đ, quantity 1, 17:00–18:00 unless explicitly changed consistently.
- Known from earlier docs, **not reverified by this reviewer**: detached category/merchant/allergen layouts, missing Theme/ActiveTab properties, static stepper/checkbox/segmented controls, and orphan dependencies. Foundation worker must inspect live before fixing.
- A Plugin API exception may leave partial mutation. Read back IDs before retrying; do not assume automatic rollback or create duplicates.
- A histogram is illustrative demo inventory, not student spending research. Icon metadata JSON is not SVG source.
- Every demo payment/pickup/state remains simulation; prototype interactions cannot prove backend inventory, authentication or local persistence.

## Six-flow test specification

All tests below are **NOT RUN** here. Read-back and Present-mode execution must be recorded separately. Prototype hotspot contract is ≥48×48pt; physical accessibility/usability tests remain separate.

| Flow | Required route | Assertions before a pass |
|---|---|---|
| F-01 | 001→002→003→004→011→012→005→013→023→024→023→021→034→059→050→051→053→054→055→056→062→063→072→100 | Full non-skip onboarding route and skip→005 both work; guest intent survives labeled demo auth; same item/quantity/slot/payment through receipt/pass; UNKNOWN disclosure; no consumer self-confirm pickup; staff hotspot clearly documented as simulation; only completed pickup enters impact. |
| F-02 | 015→016→017→034→038→039 | Selected pin corresponds to preview item/price; map never invents GPS consent; close preview preserves map context; route is illustrative; external map action static/labeled if not linked. |
| F-03 | 053→054→055→058→053→054→055→056; alternate 055→057→055 | Hidden failure branches documented/reachable despite delay; selection preserved; quantity correction is explicit and receipt total coherent; no offline success claim. |
| F-04 | 062→070→071→015; 067→068→069 | Cutoff and retain/cancel actions distinct; cancellation/no-show gives no rescue/savings; expiry branch navigable; support/recovery exists; completion animation not a real stock update. |
| F-05 | 074→076→077→078→077→079→077→080→075→083→086→089 | No auth gate for local Pantry; category/date selections demonstrable; Use-by vs Best-before explicit; no unsafe consumption suggestion; used vs discarded separate; partial-use amounts consistent; notifications/persistence only claimed as simulated design behavior. |
| F-06 | 011→018→015→091→098→011 | Manual area and optional permission both available; manual area retained in demo view; no GPS dot without permission; settings path returns correctly; real OS permission is not claimed tested. |

## Pattern proposals by group

| Screens | Differentiated composition within the shared family |
|---|---|
| 001–012 | Brand story collage for intro, quiet single-column forms for auth; keyboard-aware controls and adjacent validation. Permission explainer differs from a form and offers non-coercive alternatives. |
| 013–033 | Guest featured horizontal meal vs auth active-pickup strip; market hero/grid/rail rhythm; compact flat rows for search; immersive map; progressive filter sheets. Different categories get distinct focal image/crop, not only recoloring. |
| 034–049, 059 | Full-bleed exact-item showcase vs unmistakable kraft surprise-bag composition; flat trust rows; ingredient/safety sheets; recovery alternatives on sold-out/closed states. Demo reviews labeled, never invented as genuine. |
| 050–058, 060–073 | Quantity/slot controls, one unified receipt and wallet-like pickup pass, not nested-card checkout; urgent order timeline vs calm history; cancellation/recovery states include next actions. |
| 074–090 | Calm storage-first inventory, expiry text/date type and discrete category illustration; forms, date sheet, item detail and usage history have distinct jobs. No marketplace price/CTA leakage. |
| 091–100 | Quiet grouped settings, editable switches/notification states, clear privacy controls and impact based only on labeled fixture evidence. No arbitrary environmental metric. |

## Per-screen release checklist

- [ ] Live unique SB-ID/root exists in correct section, native 393×852 editable frame.
- [ ] Correct purpose/state and fixtures, explicit demo data, safety/payment invariants.
- [ ] Text/copy, crop, contrast, safe areas, clipping, overlay order visually inspected.
- [ ] Main-component mapping and genuine exposed properties/variants read back; no unexplained detach.
- [ ] Input controls and key state changes operable or clearly labeled static limitations.
- [ ] Incoming/outgoing edges match Interaction Map; destinations exist, no unjustified orphan.
- [ ] Screenshot evidence saved, viewable and linked to actual frame/checkpoint.
- [ ] Present test executed and recorded separately; keep prototype_verified=false if blocked.
- [ ] 375×812 / 393×852 / 430×932 reflow and long Vietnamese copy checked, not merely bounds inferred.
- [ ] Real-device/assistive-technology/usability checks tracked honestly; owner acceptance distinct.
