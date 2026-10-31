# Progress · 31/10/2026

Gate: **AWAITING_OWNER_REVIEW (`B-PHASE1-010`)** · Target Figma: [SaveBite-V2 (`7suZz9C8oL5zV2NMxlsIVI`)](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1) · Chuẩn khung: **iPhone 15 (`393×852pt`, Dynamic Island)**.
DESIGN_REVIEW: **30/100** · BACKLOG: **70/100** · DONE: **0/100**. Lease **RELEASED**.

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
- **Prototype:** reaction của 10 màn Phase 1 đã được ghi và đọc lại (Plugin API không cho chạy Present mode). **Đính chính 31/10/2026:** bản ghi trước đó viết "đã bấm thử Present mode PASS" là chưa đúng sự thật — chưa ai chạy Present mode; `prototype_verified` đặt lại `false` cho mọi dòng cho tới khi owner/người dùng chạy thật.
- **Asset expansion (xem dưới):** thêm ảnh mới vào `assets/manifest.json` để phục vụ batch 20 màn tiếp theo.

## Batch B-PHASE1-012 (31/10/2026) — Mở rộng asset pool cho 90 màn còn lại

Thêm 3 ảnh Pexels thật (biến thể góc chụp cho 3 offer đã duyệt): `bakery-rolls-2000498`, `rice-bowls-5127769`, `produce-crates-2679261` — tổng 9 ảnh, SHA-256 đã kiểm. Một ứng viên bị loại vì thấy rõ mặt người. Chưa tìm được ảnh Pexels phù hợp cho túi giấy kraft và kệ Pantry (hoãn tới batch Pantry/Túi bất ngờ). 3 ảnh mới **chưa upload lên Figma** nên các màn hiện dùng lại 4 ảnh đã có trong file.

## Batch B-PHASE1-013 (31/10/2026) — Dựng 20 màn đầu của 90 màn còn lại (Plan 2 Batch B1 + đầu B2)

Đã dựng 20 màn (tất cả `DESIGN_REVIEW`, QA kỹ thuật = screenshot + read-back; **chưa** rubric chính thức/owner review, a11y chưa kiểm):

| Section | Màn mới |
|---|---|
| `01` | `SB-001`, `005`, `008`, `013`, `022` |
| `02` | `SB-046`, `047`, `049`, `059` |
| `03` | `SB-050`, `054`, `055`, `057`, `058`, `060`, `062`, `063`, `067`, `072` |
| `04` | `SB-100` |

- Node ID từng màn: xem [screens.csv](screens.csv). Component mới: `TextField` (set `75:56`, CANDIDATE).
- **Chuỗi F-01 đã nối đầu-cuối trên Figma (reaction đọc lại, chưa chạy thật):** `001→002→(Bỏ qua)005→013→034→059→050→051→053→054→055→056→062→063→072→100`; nhánh lỗi `055⇢057/058` qua hotspot demo ẩn; `063` có hotspot ẩn mô phỏng nhân viên quét (D-011). `008→015` thay tạm cho `SB-014` (chưa dựng).
- **Chưa có đường vào (orphan có lý do):** `SB-022` (chờ `SB-021`), `046/047/049` (chờ `SB-021/031/048/033`), `067` (chờ `SB-061/095`). Lối ra tới màn chưa dựng ghi `pending` trong `notes`.
- **Hạn chế đã biết:** stepper `SB-050`, checkbox `SB-049`, segmented `SB-060` chỉ là hình tĩnh; `iOSStatusBar/HomeIndicator/AppBar/BottomNav` không có variant Theme/ActiveTab như registry từng ghi — trạng thái sáng/active làm bằng override (đã ghi drift vào [components.csv](components.csv)).
- Skill đã đọc theo yêu cầu: frontend-design, ui-ux-pro-max, design-critique, figma-use, figma-generate-design/library (không emoji, lỗi ngay cạnh trường, touch ≥44pt, copy nêu rõ hành động).

## Lease & bước tiếp theo

- **Lease (31/10/2026):** `RELEASED` tại checkpoint batch B-PHASE1-011/012.
- **Bước tiếp theo:** Owner chạy Present mode từ `SB-001` và duyệt look-and-feel 30 màn; sau đó batch kế (Plan 2: `SB-014`, `021`, `031`, `048`, `061`, `064–066`, `068–071`…) và upload 3 ảnh mới lên Figma khi cần dùng.
