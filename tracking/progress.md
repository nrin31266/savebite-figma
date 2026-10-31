# Progress · 31/10/2026

Gate: **AWAITING_OWNER_REVIEW (`B-PHASE1-010`)** · Target Figma: [SaveBite-V2 (`7suZz9C8oL5zV2NMxlsIVI`)](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1) · Chuẩn khung: **iPhone 15 (`393×852pt`, Dynamic Island)**.
DESIGN_REVIEW: **10/100** · BACKLOG: **90/100** · DONE: **0/100**. Lease **RELEASED**.

## 10 Màn Hình Đại Diện Phase 1 — Một Page Duy Nhất, Click-Through Liền Mạch (`DEC-013`)

| Màn | Archetype | Section (page `App · All Screens`, `11:3`) | Node ID & Link Trực Tiếp |
|---|---|---|---|
| `SB-002` · Onboarding 1 | `A1 · Story Entry` | `01 · Entry & Discovery` | [17:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-2) |
| `SB-015` · Khám phá | `A3 · Market Discovery` | `01 · Entry & Discovery` | [17:49](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-49) |
| `SB-016` · Bản đồ | `A4 · Spatial Map` | `01 · Entry & Discovery` | [17:187](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-187) |
| `SB-019` · Tìm kiếm | `A5 · Search + iOS Keyboard` | `01 · Entry & Discovery` | [17:282](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-282) |
| `SB-034` · Chi tiết offer | `A6 · Full-Bleed Showcase` | `02 · Offer & Merchant` | [18:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=18-2) |
| `SB-051` · Chọn giờ nhận | `A7 · Tactile Slot` | `03 · Reserve & Orders` | [19:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=19-2) |
| `SB-053` · Tóm tắt đặt trước | `A7 · Unified Receipt` | `03 · Reserve & Orders` | [19:69](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=19-69) |
| `SB-056` · Đặt trước thành công | `A7 · Perforated QR Pass` | `03 · Reserve & Orders` | [19:140](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=19-140) |
| `SB-075` · Tủ thực phẩm | `A8 · Calm Kitchen Pantry` | `04 · Pantry & Account` | [20:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=20-2) |
| `SB-091` · Tài khoản | `A9 · Account & Impact Hub` | `04 · Pantry & Account` | [20:109](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=20-109) |

- **Foundations (`0:1`):** [11:59](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=11-59) (`34 variables`, `12 text styles`, `3 effect styles`).
- **Components (`11:2`):** `29 shared components` khớp 1:1 với [components.csv](components.csv).
- **Assets (`assets/manifest.json`):** 6 ảnh thực phẩm/cửa hàng thật từ Pexels, xem mục Asset expansion bên dưới cho các ảnh mới thêm.

## Batch B-PHASE1-011 (31/10/2026) — Plan 1 hoàn tất, Open conflict NAVIGATION đã đóng

- **Sửa 5 màn đầu** (`SB-002/015/016/019/034`): hết emoji làm icon, hết card-in-card ở peek sheet `SB-016`, bỏ chấm GPS giả (D-017), bản đồ lấp khoảng trống, status bar/scrim `SB-034` đúng chuẩn, hết từ mồ côi. Chi tiết lỗi/sửa từng màn ở cột `notes` trong [screens.csv](screens.csv). `CategoryTile` 3 instance và `MerchantRow`/`AllergenNotice` trên `SB-034` detach cục bộ (component gốc chưa có property Icon swap — theo dõi ở Plan 2). `MapPricePin`, `OfferCard` main component sửa trên Components page.
- **Audit 5 màn còn lại** (`SB-051/053/056/075/091`): không phát hiện vi phạm chặn; fix thêm 1 emoji lẻ (🔒 → text) trên `SB-075`, 1 emoji lẻ (📍 → vector icon) trên `SB-056`.
- **⚠️→✅ Open conflict `NAVIGATION` (phát hiện rồi đóng trong cùng batch):** Figma Plugin API chặn `NAVIGATE` reaction liên-page ("prototypes are per-page"). Owner chọn **Phương án A** (31/10/2026): *"Cái nào cùng màn, cùng chức năng thì gộp thành 1 trang để phục vụ việc nối màn"* → ghi **`DEC-013`**. Đã gộp 4 page hi-fi (`01..04`) thành **1 page `App · All Screens` (`11:3`)**, tổ chức bằng 4 Section cùng tên; xóa 3 page rỗng (`11:4/11:5/11:6`). `docs/workflow.md` đã cập nhật kiến trúc page + kế hoạch 2 agent sang Section-isolated.
- **Prototype:** toàn bộ 10 màn Phase 1 giờ là **một click-through liền mạch** trên 1 flow starting point (`F01 | Guest-to-Rescue pilot | v1` tại `SB-002`): `002→015→034→051→053→056→015` (vòng lặp), `015↔016`, `015→019`, `019→back/034`, `034→back`, tab `Pantry/Account→Khám phá`. Đã bấm thử ở Present mode. `prototype_verified=true` cho cả 10 dòng trong `screens.csv`.
- **Asset expansion (xem dưới):** thêm ảnh mới vào `assets/manifest.json` để phục vụ batch 20 màn tiếp theo.

## Batch B-PHASE1-012 (31/10/2026) — Mở rộng asset pool cho 90 màn còn lại

Trạng thái: xem [assets/manifest.json](../assets/manifest.json) cho danh sách đầy đủ, nguồn và SHA-256. Ghi tóm tắt ở đây sau khi tải xong (cập nhật cùng batch dựng 20 màn).

## Batch B-PHASE1-013 (31/10/2026) — Dựng 20 màn đầu của 90 màn còn lại (Plan 2 Batch B1 + đầu B2)

Trạng thái: cập nhật khi batch chạy xong — xem chi tiết screen-by-screen trong [screens.csv](screens.csv), node IDs và QA ở đây sau khi hoàn tất.

## Lease & bước tiếp theo

- **Lease (31/10/2026):** `RELEASED` tại checkpoint batch B-PHASE1-011/012.
- **Bước tiếp theo:** Hoàn tất dựng 20 màn Batch B-PHASE1-013; sau đó trình toàn bộ (10 Phase 1 + 20 mới) cho Owner duyệt `design_baseline_version` trước khi mở khóa phần còn lại của Plan 2.
