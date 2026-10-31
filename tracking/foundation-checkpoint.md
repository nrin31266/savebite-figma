# Foundation and live reconciliation · 31/10/2026

Target: [SaveBite-V2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=11-2). Worker batch followed by independent lead read-back; no owner acceptance.

## Observed inventory

- App page `11:3`: **39 unique native 393×852 roots**, sections 01/02/03/04 = 9/5/20/5. This corrects registry 30; it does not claim 39 visually accepted screens.
- Recovered pre-existing roots: `052 90:1408`, `061 90:1491`, `064 91:1487`, `065 91:1531`, `066 91:1652`, `068 92:1593`, `069 92:1642`, `092 94:1641`, `093 94:1684`. Do not recreate.
- Corrected stale IDs for 046/047/049/059/054/055/057/058/063/072/100 in [screens.csv](screens.csv). Earlier historical notes are not current mapping evidence.
- Components: 63 top-level mains/sets, including 3 pre-existing unregistered controls, 6 new controls and 24 icon mains. [components.csv](components.csv) now records actual exposed properties, not desired variants. Downgraded unsupported blanket visual-pass claims to STRUCTURAL_READBACK_ONLY/CANDIDATE.
- Edges cleared in registry pending complete source-hotspot read-back after screen writes; no invented links inferred from plan. Root reactions (timed splash/processing) need inclusion in final graph audit, not descendants only.

## New/recovered library inventory

| Component | Main/set | Confirmed properties / limits |
|---|---|---|
| iOSSwitchRow | set 88:40 | On=true/false; no reactions or text properties |
| NotificationRow | set 88:60 | Read=true/false; no Type variants or text properties |
| PantryCategoryTile | main 88:66 | No exposed properties |
| SheetContainer | main 98:99 | 393×480; no Height variants/content swap; dashed slot is authoring placeholder only |
| EmptyState | main 98:109 | Read-back height 272; no Kind/text properties |
| SegmentedControl | set 98:139 | Active=Tab1/Tab2/Tab3, variants 98:118/125/132; no reactions or label properties |
| FilterChip | set 98:144 | Selected=false/true, variants 98:140/142; visual height36 needs ≥48pt hotspot; no reactions |
| QuantityStepper | set 98:169 | State=Default/Min/Max, variants98:145/153/161; no count properties or reactions |
| SafetyCheckbox | set 98:183 | State=Unchecked/Checked/Warning, variants98:170/173/178; does not yet gate CTA |
| Icon/* | 24 mains in section98:26 | 24pt native vector. Worker claims official Phosphor regular source; precise source/license still to reconcile with asset curator. No certification/AI claim implied by ShieldCheck/Sparkle. |

These controls are **not yet production-ready**. A state variant alone is not an interactive control. Stepper screenshot clips right edge; needs frame/container QA. Lead also inspected SafetyCheckbox: label clips and Warning variant asks users to "cam kết chịu trách nhiệm đối với thành phần"—inappropriate liability-waiver copy. Must replace with plain acknowledgment and explicit request to ask merchant about ingredients; checked state never certifies safety. Icon sheet lacks labels and still needs category/duotone coverage. Component sets must not be instantiated directly—instantiate variant component and use its owning set properties.

## Lead-verified copy corrections

Worker summary incorrectly claimed bakery Bếp Xanh Campus, original70K/80K prices, 12 meals, 8 Pantry and 240K savings. **Rejected as unsupported**, not propagated to screens/product.

- SB-034 screenshot + text read-back: `Bánh mì men tự nhiên`, `Tiệm Bánh A (demo)`, `25.000đ`, `17:00–18:00`, UNKNOWN.
- SB-091: demo 3 confirmed pickups and 4 Pantry items used in time.
- SB-100: demo 3 pickup rows at25K/30K/35K, **90.000đ total paid**, explicitly no savings estimate because no original price, no CO₂ formula.
- Visual sample is [SB-034](evidence/foundation/SB-034.png), not permission to infer other screen QA.

## Evidence and remaining QA

Worker saved 10 old-screen samples and 6 component samples under [foundation evidence](evidence/foundation/). Lead inspected SB-034 and [stepper](evidence/foundation/QuantityStepper.png) directly; other copied screenshots are worker evidence, not automatically lead visual approval.

- [Icon sheet](evidence/foundation/Icons-Phosphor-Core.png)
- [SheetContainer](evidence/foundation/SheetContainer.png)
- [EmptyState](evidence/foundation/EmptyState.png)
- [SegmentedControl](evidence/foundation/SegmentedControl.png)
- [SafetyCheckbox](evidence/foundation/SafetyCheckbox.png)

Lead also inspected SB-075: overdue metadata competes with action button,4 rows shown vs total7 without verified scrolling, identical meter lengths despite different expiry labels. Need real overflow/scroll and freshness semantics check. SB-050 existing copy sets **max2 per order** while new stepper Max variant shows3; component must not silently override order policy.

Still required: audit all39 individually, controls/interactions/property exposure, missing61 screens, crop/contrast/reflow checks, graph and cross-flow wiring, licensed diversified photos/badges/crop sheet. Present mode blocked by browser authentication (403); retain prototype_verified=false.
