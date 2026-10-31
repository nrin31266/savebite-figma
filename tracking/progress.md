# Progress · 26/10/2026

Gate: **AWAITING_OWNER_REVIEW (`B-PHASE1-010`)** · Target Figma: [SaveBite-V2 (`7suZz9C8oL5zV2NMxlsIVI`)](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1) · Chuẩn khung: **iPhone 15 (`393×852pt`, Dynamic Island)**.
DESIGN_REVIEW: **10/100** · BACKLOG: **90/100** · DONE: **0/100**. Lease **RELEASED**.

## 10 Màn Hình Đại Diện Phase 1 Đã Dựng Trực Tiếp Trên `SaveBite-V2`

| Màn | Archetype | Page Figma | Node ID & Link Trực Tiếp |
|---|---|---|---|
| `SB-002` · Onboarding 1 | `A1 · Story Entry` | `01 · Entry & Discovery` (`11:3`) | [17:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-2) |
| `SB-015` · Khám phá | `A3 · Market Discovery` | `01 · Entry & Discovery` (`11:3`) | [17:49](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-49) |
| `SB-016` · Bản đồ | `A4 · Spatial Map` | `01 · Entry & Discovery` (`11:3`) | [17:187](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-187) |
| `SB-019` · Tìm kiếm | `A5 · Search + iOS Keyboard` | `01 · Entry & Discovery` (`11:3`) | [17:282](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-282) |
| `SB-034` · Chi tiết offer | `A6 · Full-Bleed Showcase` | `02 · Offer & Merchant` (`11:4`) | [18:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=18-2) |
| `SB-051` · Chọn giờ nhận | `A7 · Tactile Slot` | `03 · Reserve & Orders` (`11:5`) | [19:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=19-2) |
| `SB-053` · Tóm tắt đặt trước | `A7 · Unified Receipt` | `03 · Reserve & Orders` (`11:5`) | [19:69](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=19-69) |
| `SB-056` · Đặt trước thành công | `A7 · Perforated QR Pass` | `03 · Reserve & Orders` (`11:5`) | [19:140](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=19-140) |
| `SB-075` · Tủ thực phẩm | `A8 · Calm Kitchen Pantry` | `04 · Pantry & Account` (`11:6`) | [20:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=20-2) |
| `SB-091` · Tài khoản | `A9 · Account & Impact Hub` | `04 · Pantry & Account` (`11:6`) | [20:109](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=20-109) |

- **Foundations (`0:1`):** [11:59](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=11-59) (`34 variables`, `12 text styles`, `3 effect styles`).
- **Components (`11:2`):** `29 shared components` khớp 1:1 với [components.csv](components.csv).
- **Assets (`assets/manifest.json`):** 6 ảnh thực phẩm/cửa hàng thật từ Pexels đã upload lên Figma và kiểm tra SHA-256.
- **Open issue (31/10/2026, mở lúc đọc live):** 5 màn đầu (`SB-002`, `015`, `016`, `019`, `034`) chưa đạt rubric — emoji làm icon, card-in-card ở peek sheet `SB-016`, bản đồ dạng wireframe + chấm vị trí giả, status bar/scrim `SB-034`, từ mồ côi, chưa nối prototype. Kế hoạch sửa: [Plan 1](../docs/plans/phase1-fix-sb002-sb034.md); dựng 100 màn: [Plan 2](../docs/plans/build-100-screens-prototype.md).
- **Batch B-PHASE1-011 (31/10/2026) — Plan 1 mục 1–4 thực thi, chờ owner review:**
  - Mục 2 (sửa từng màn): xong cho cả 5 màn — chi tiết lỗi/sửa nằm ở cột `notes` tương ứng trong [screens.csv](screens.csv). Component `CategoryTile` 3 instance (`Bánh mì`/`Bữa ăn`/`Rau củ` trên `SB-015`) và `MerchantRow`/`AllergenNotice` instance trên `SB-034` đã **detach cục bộ** để gắn icon/chevron riêng (lý do: component gốc chưa có property `Icon` instance-swap/`Icon` cho chevron; không ảnh hưởng instance dùng ở `SB-051`). `MapPricePin` main component (`16:16`, Components page) được thêm `PinTail` — propagate cho cả 3 pin, màu tail theo từng instance.
  - Mục 4 (nối prototype): **5/12 link trong bảng dự kiến không nối được** vì lý do kỹ thuật mới phát hiện — xem "Phát hiện quan trọng" bên dưới. 7 link cùng page đã nối và set 2 flow starting points (`SB-002`, `SB-034`).
  - Mục 3 (OfferCard title default, MapPricePin tail) xong trên Components page. Mục 5 (audit `SB-051/053/056/075/091`) xong: chấm rubric qua screenshot live, **không phát hiện vi phạm chặn** — 5 màn này đã đạt chuẩn từ trước, chi tiết ghi ở cột `notes` từng dòng trong [screens.csv](screens.csv). Plan 1 coi như hoàn tất mục 1–5; còn mục 6/7 (checkpoint cuối, do owner xác nhận) và Open conflict NAVIGATION bên dưới trước khi đóng hẳn.
- **⚠️ Phát hiện quan trọng — Figma Plugin API chặn prototype NAVIGATE liên trang:** `node.setReactionsAsync()` trả lỗi *"for NAVIGATE actions, destinations must be a different top-level frame on the same page"* cho mọi đích khác page với nguồn (đã thử và bị từ chối: `SB-015→SB-034`, `SB-016→SB-034`, `SB-019→SB-034`, `SB-034→SB-051`, `SB-015→SB-075/091`). Đây là giới hạn thật của Figma prototyping ("prototypes are per-page", không phải lỗi script). Ảnh hưởng trực tiếp tới kiến trúc 4-page hiện tại (`workflow.md` §"Kiến trúc Cô lập 6 Pages") vì **F-01..F-06 đều đi xuyên nhiều page** — cần quyết định trước khi chạy Plan 2 ở quy mô 90 màn: (a) gộp bớt page để các flow chính nằm chung 1 page, (b) chấp nhận mỗi page có flow riêng + nối liên-page thủ công trong Figma app (ngoài khả năng Plugin API), hoặc (c) phương án khác do owner chọn. Ghi `Open conflict: NAVIGATION` — chưa tự chọn, chờ quyết định.
  - 7 link đã nối cùng page: `SB-002 Tiếp tục/Bỏ qua → SB-015` (tạm, note rõ trong `screens.csv`), `SB-015 SearchField → SB-019`, `SB-015 Bản đồ → SB-016`, `SB-016 Danh sách → SB-015`, `SB-019 Hủy → Back`, `SB-034 Back → Back`.
  - 5 link KHÔNG nối được (liên trang): `SB-015 OfferCard → SB-034`, `SB-015 tab Tủ thực phẩm/Tài khoản → SB-075/SB-091`, `SB-016 peek → SB-034`, `SB-019 gợi ý → SB-034`, `SB-034 Chọn giờ nhận → SB-051`.
- **Lease (31/10/2026):** `RELEASED` tại checkpoint này — scope đã làm: 5 root node Phase 1 (`17:2`, `17:49`, `17:187`, `17:282`, `18:2`) + components (CategoryTile, OfferCard, OfferListRow, MapPricePin) trên page `11:2`/`11:3`/`11:4`.
- **Bước tiếp theo:** Xin owner quyết định cho Open conflict `NAVIGATION` (Phương án A/B/C ở Plan 2 mục 0) → ghi `DEC-013`; song song, trình 10 màn Phase 1 cho Owner duyệt look-and-feel (`design_baseline_version`) trước khi mở khóa 90 màn còn lại cho Plan 2.
