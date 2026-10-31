# Plan 1 · Sửa 5 màn đầu Phase 1 (`SB-002`, `SB-015`, `SB-016`, `SB-019`, `SB-034`)

Kế hoạch sửa tại chỗ 5 frame đầu trên [SaveBite-V2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1) sau lần đọc Figma live ngày 31/10/2026 (screenshot + metadata). Đọc cùng [visual-direction](../visual-direction.md), [ios-guidelines](../ios-guidelines.md), [screen-art-direction](../screen-art-direction.md), [design-system](../design-system.md) và rubric trong [workflow](../workflow.md). Kế hoạch tiếp theo: [Plan 2 · Dựng đủ 100 màn + prototype](build-100-screens-prototype.md).

Trạng thái: `SPECIFIED` · chưa thao tác canvas · gate sau khi xong: `AWAITING_OWNER_REVIEW`.

---

## 1. Kết luận đánh giá

5 màn **chưa đạt** Aesthetic Rubric. Phần nền móng đúng hướng (iOS status bar/home indicator thật, palette, font, `SB-034` gần đạt), nhưng còn lỗi thuộc các luật cứng:

| # | Lỗi chung | Màn bị ảnh hưởng | Luật |
|---|---|---|---|
| G1 | Emoji/ký tự Unicode làm icon: `✨`, `🗺`, `☰`, `🔥`, `⏰`, `📍`, `🥖`, `↺`, `↗` (↗ render thành ô emoji xanh) | `SB-002`, `SB-016`, `SB-019` | Rubric #6, [design-system](../design-system.md) §1.4 |
| G2 | Tên món rớt 1 từ xuống dòng ("Bánh mì men tự / nhiên", "Bánh sừng bò bơ / Pháp") | `SB-002`, `SB-015` | Rubric #4 |
| G3 | Chưa có prototype interaction nào (`prototype_verified=false`) | cả 5 | Checklist màn #5, Gate 5 |

## 2. Lỗi riêng từng màn và cách sửa

Giữ nguyên root node ID; chỉ sửa node con hoặc swap instance. Không tạo frame mới, không xóa frame.

### `SB-002` · Onboarding 1 (`17:2`) — archetype `A1`

| Hiện trạng | Sửa |
|---|---|
| `HeroStoryStage` (`17:22`): `OfferCard` đè lên ảnh rau, pill `17:34` dính sát đáy card, ellipse `17:23` bị cắt mép trông như lỗi | Dựng lại collage: vòm `#EDF3E7` nguyên vẹn làm nền; ảnh produce lùi ra sau, `OfferCard` nghiêng −4° ở trước; pill tách khỏi card ≥12pt, bỏ `✨`, icon Phosphor `Storefront` |
| Eyebrow "CỨU THỰC PHẨM CUỐI NGÀY · BƯỚC 1/3" (`17:37`) lặp ý với `PageDots` | Bỏ phần "BƯỚC 1/3", giữ eyebrow ngắn hoặc bỏ hẳn |
| Khoảng trống chết ~60pt giữa body và `PageDots` | Tăng chiều cao hero (≈55% vùng trên theo A1) hoặc dồn cụm copy xuống, PageDots cách CTA 24pt |
| CTA `17:45` "Tiếp tục khám phá →" | Đổi thành "Tiếp tục" theo contract |
| Tiêu đề card wrap mồ côi | Xem G2 (sửa tại component `OfferCard`) |

### `SB-015` · Khám phá (`17:49`) — archetype `A3`

| Hiện trạng | Sửa |
|---|---|
| 4 `CategoryTile` dùng chung icon "4 ô vuông" | Swap icon Phosphor Duotone: `SquaresFour` (Tất cả), `Bread` (Bánh mì), `BowlFood` (Bữa ăn), `Carrot` (Rau củ) |
| `BrandHeader`: dòng khu vực kết thúc bằng `•` | Thay bằng `CaretDown` 16pt; rút gọn "Đà Nẵng · Khu học xá ▾" theo contract |
| Ảnh croissant nền tối đứng cạnh ảnh bánh mì sáng | Chỉnh crop để lộ phần nền gỗ sáng hoặc phủ overlay ấm 8–10% để đồng bộ tông; không thay asset nếu chưa cập nhật [manifest](../../assets/manifest.json) |
| `OfferListRow` (`17:151`) dính sát `BottomNav`, không thấy còn nội dung | Tạo `ScrollViewport` có peek: hàng cuối bị `BottomNav` che một phần + viền mảnh `#E8E2D8` trên tab bar (ios §4.3) |
| Nhịp điệu: thiếu dải ngang theo luật 6 | Tùy chọn: đổi hàng cuối thành rail ngang "Gần trường" nếu đủ chỗ; không bắt buộc ở batch này |

### `SB-016` · Bản đồ (`17:187`) — archetype `A4` — **ưu tiên cao nhất**

| Hiện trạng | Sửa |
|---|---|
| `MapCanvas` trông như wireframe: lưới chữ nhật trắng, khoảng trống lớn y≈400–600 | Vẽ lại `MapCanvas` (`16:3`): khối nhà `#F3EFE6`, công viên `#E2ECE4`, sông Hàn `#CFE2E0` uốn theo cạnh phải, đường chính rộng hẹp khác nhau, vài nhãn địa danh nhỏ; phủ đều khung nhìn |
| Nhãn đường bị cắt ("Đ. Nguyễn", "u học xá" bị pin che) | Đặt nhãn dọc theo đường, không chồng pin; kiểm collision sau khi đặt pin |
| `MapPricePin` không có đuôi, có `★` thừa | Thêm đuôi tam giác 8pt vào component; variant `Selected` phóng 1.15x, màu `#B34021`, bỏ `★` |
| Chấm vị trí người dùng + tuyến đi bộ (`22:311..313`) trong khi GPS là tùy chọn (D-017) | Xóa 3 node này (do phiên trước tạo, đã đọc ID); thay bằng mốc cố định "Khu học xá ĐH Đà Nẵng" và vòng bán kính 1 km quanh mốc |
| Peek sheet (`17:245`) trắng chứa `OfferListRow` có viền → card-in-card | Thêm variant `OfferListRow Surface=Flat` (không viền, không nền) và dùng trong sheet; sheet bo 28pt, có grabber |
| Text bị cắt "Còn 3 ph" | Rút gọn meta: "17:00–18:00 · Còn 3" hoặc cho meta xuống dòng |
| Search bar không có nền kính mờ, dính sát status bar; chip `🗺 Bản đồ (3)` / `☰ Danh sách` | Floating bar `rgba(255,252,246,0.88)` + blur 20, cách status bar 8pt; toggle Bản đồ/Danh sách thành `SegmentedControl` 2 nút với icon Phosphor `MapTrifold` / `ListBullets`; chip lọc ngang cuộn được |

### `SB-019` · Tìm kiếm (`17:282`) — archetype `A5`

| Hiện trạng | Sửa |
|---|---|
| Chip lọc nhanh dùng `🔥 ⏰ 📍 🥖` | Swap icon Phosphor: `Tag`, `Clock`, `MapPin`, `Bread` (Regular 16pt, màu `#004337`) |
| Dòng tìm gần đây dùng `↺` và `↗` | `ClockCounterClockwise` bên trái, `ArrowUpLeft` bên phải (điền từ khóa vào ô, kiểu iOS) |
| Khối "Gợi ý khớp ngay" là card có viền đứng đơn lẻ | Hàng phẳng trên canvas với đường kẻ 1pt, thumbnail 52pt bo 8pt |
| Khoảng trống giữa gợi ý và bàn phím | Chấp nhận (màn có bàn phím); kiểm lại ở 375×812 xem không bị bàn phím che |

### `SB-034` · Chi tiết offer (`18:2`) — archetype `A6`

| Hiện trạng | Sửa |
|---|---|
| Dải kem mờ phủ đỉnh ảnh (y 0–~95) + `iOSStatusBar` Dark trên ảnh | Ảnh `FullBleedHeroPhoto` (`18:3`) tràn từ y=0, bỏ lớp kem; thêm gradient scrim 104pt `rgba(0,0,0,0.45)→0`; status bar `Theme=Light` |
| Nút CTA trong `StickySplitDock` lệch lề phải (x=190, w=196 → còn 7pt) | Dock theo lề 20pt: khối giá trái, CTA phải kết thúc ở x=373 |
| Khoảng trống chết y≈690–750 trên dock | Thêm hàng chạm "Chất lượng & hạn dùng" (→ `SB-037`) hoặc giảm khoảng để nội dung lấp đầy và có peek cuộn |
| Hàng Merchant/Pickup/Allergen không có affordance chạm | Thêm `CaretRight` cuối hàng: Merchant → `SB-038`, Allergen → `SB-036`; vùng chạm cả hàng ≥48pt |

## 3. Sửa ở tầng component (làm trước, vì ảnh hưởng nhiều màn)

| Component | Thay đổi | Màn kiểm lại |
|---|---|---|
| Icon (mới) | Bộ `Icon/*` từ Phosphor (Regular + Duotone/Fill), khung 24pt, dùng instance-swap | Toàn bộ 10 màn Phase 1 |
| `CategoryTile` (`15:153`) | Property `Icon` instance-swap | `SB-015` |
| `OfferCard` (`15:160`) | Title cân bằng 2 dòng (giảm 1pt hoặc nới width text), không mồ côi từ | `SB-002`, `SB-015` |
| `OfferListRow` (`15:169`) | Variant `Surface=Card/Flat` | `SB-015`, `SB-016`, `SB-019` |
| `MapPricePin` (`16:16`) | Thêm đuôi, bỏ ký tự trang trí, `Selected` scale 1.15 | `SB-016` |
| `MapCanvas` (`16:3`) | Vẽ lại như mục `SB-016` | `SB-016` (sau này `SB-017`, `039`, `065`, `094`) |
| `SegmentedControl` (mới) | 2–3 segment, active `#004337` | `SB-016` (sau này `SB-033`, `SB-060`) |

Mỗi thay đổi component: ghi vào [components.csv](../../tracking/components.csv) (variants, usage_screen_ids), không detach instance.

## 4. Nối prototype cho subset 5 màn

Chỉ nối tới frame đã tồn tại; đích chưa có thì ghi chú để Plan 2 nối lại. Hotspot ≥48×48pt.

**⚠️ Phát hiện khi thực thi (31/10/2026):** `node.setReactionsAsync()` của Figma Plugin API từ chối mọi `NODE`/`NAVIGATE` reaction có đích khác page với nguồn (`"for NAVIGATE actions, destinations must be a different top-level frame on the same page"`) — đúng với mô hình prototyping gốc của Figma ("prototypes are per-page"), không phải lỗi script. `SB-034` nằm ở page `02 · Offer & Merchant` (`11:4`) khác page với `SB-002/015/016/019` (`01 · Entry & Discovery`, `11:3`), và `SB-051` ở page `03 · Reserve & Orders` (`11:5`) khác `SB-034`. Kết quả:

| Từ | Phần tử | Đích | Kiểu | Animation | Trạng thái |
|---|---|---|---|---|---|
| `SB-002` | `Tiếp tục` | `SB-015` (tạm; Plan 2 đổi thành `SB-003`) | Navigate | Move In ←, 300ms ease-out | ✅ Nối (cùng page) |
| `SB-002` | `Bỏ qua` | `SB-015` (tạm; Plan 2 đổi thành `SB-005`) | Navigate | Dissolve 200ms | ✅ Nối (cùng page) |
| `SB-015` | `OfferCard` Bánh mì | `SB-034` | Navigate | Smart Animate 320ms (Signature #1) | ❌ Bị từ chối — khác page |
| `SB-015` | `SearchField` | `SB-019` | Navigate | Dissolve 150ms | ✅ Nối (cùng page) |
| `SB-015` | `Bản đồ →` | `SB-016` | Navigate | Dissolve 200ms | ✅ Nối (cùng page) |
| `SB-015` | Tab `Tủ thực phẩm` / `Tài khoản` | `SB-075` / `SB-091` | Navigate | Instant | ❌ Bị từ chối — khác page (`SB-075/091` ở `11:6`) |
| `SB-016` | Peek sheet / pin `25.000đ` | `SB-034` | Navigate | Move In ↑ 300ms | ❌ Bị từ chối — khác page |
| `SB-016` | Segment `Danh sách` | `SB-015` | Navigate | Dissolve 200ms | ✅ Nối (cùng page) |
| `SB-019` | `Hủy` | Back | Back | — | ✅ Nối |
| `SB-019` | Hàng gợi ý Bánh mì | `SB-034` | Navigate | Move In ← 300ms | ❌ Bị từ chối — khác page |
| `SB-034` | `Back` | Back | Back | — | ✅ Nối |
| `SB-034` | `Chọn giờ nhận` | `SB-051` | Navigate | Move In ← 300ms | ❌ Bị từ chối — khác page |

7/12 hotspot cùng page đã nối và bấm thử được ở Present mode trong page `11:3`. 5 hotspot liên trang (tất cả đích `SB-034`/`SB-051`/`SB-075`/`SB-091`) **không nối được bằng Plugin API**; để nguyên reaction cũ (không có) và ghi `notes` trong `screens.csv`. Đã set flow starting point `F01 | Phase1 subset | v1` tại `SB-002` (page `11:3`) và `F01 | Offer & Merchant | v1` tại `SB-034` (page `11:4`) làm 2 điểm bắt đầu Present riêng cho từng page.

Đây là một phát hiện ảnh hưởng tới kiến trúc 4-page hiện có (ghi ở `tracking/progress.md` mục Open conflict `NAVIGATION`) vì toàn bộ 6 flow `F-01..F-06` trong `docs/experience.md` đều đi xuyên nhiều page. **Cần quyết định của owner trước khi Plan 2 nối prototype ở quy mô 90 màn** — xem mục "Gate mở khóa" trong [Plan 2](build-100-screens-prototype.md).

## 5. Audit 5 màn còn lại của Phase 1

Trước khi đóng plan này, chụp và chấm rubric `SB-051` (`19:2`), `SB-053` (`19:69`), `SB-056` (`19:140`), `SB-075` (`20:2`), `SB-091` (`20:109`). Lỗi cùng loại G1–G2, lệch lề, card-in-card thì sửa luôn trong batch này; lỗi khác ghi vào progress để owner quyết.

## 6. Trình tự thực thi

1. Preflight: `whoami`, đọc live metadata 5 root node, ghi lease vào [progress](../../tracking/progress.md) (owner, scope = 5 node + components mục 3).
2. Load skill `figma-use` (+ `figma-generate-library` cho components).
3. Sửa components (mục 3) → read-back ID.
4. Sửa lần lượt `SB-016` → `SB-034` → `SB-015` → `SB-002` → `SB-019`; sau mỗi màn `get_screenshot` và tự chấm rubric.
5. Nối prototype (mục 4).
6. Audit 5 màn còn lại (mục 5).
7. QA + checkpoint (mục 7), release lease.

## 7. QA và tiêu chí hoàn tất

- Gate 4–6 trong [workflow](../workflow.md): screenshot thật từng màn, rubric 8 tiêu chí không còn Red Flag.
- Kiểm co giãn 375×812 / 393×852 / 430×932, contrast ≥4.5:1, hotspot ≥48pt.
- Hết lỗi: 0 emoji, 0 card-in-card, 0 từ mồ côi, lề 20pt, status bar đúng Light/Dark.
- Toàn bộ hotspot ở mục 4 bấm được; `screens.csv` cập nhật `linked_to`, `prototype_verified=true` (chỉ khi đã bấm thật), `qa_result`.
- `python3 scripts/validate.py` PASS.
- Dừng ở `AWAITING_OWNER_REVIEW`; không tự chuyển `DONE`.
