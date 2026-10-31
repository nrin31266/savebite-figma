# Hệ thiết kế SaveBite (Design System & Component Architecture)

Nguồn chuẩn cho Design Tokens, Typography, Iconography và Kiến trúc Component trên Figma. Đọc cùng [router](README.md), [visual direction](visual-direction.md), [iOS guidelines](ios-guidelines.md), [chiến lược asset](asset-strategy.md) và [tiến độ](../tracking/progress.md) trước khi thay đổi.

## Checkpoint nguồn component trực tiếp · DEC-014

- Apple kit owner: source-native Search set `158:210` (main `158:211`) và Toggle set `158:197` (On `158:198`, Off `158:201`). Copy qua clipboard Figma đang đăng nhập thành công; source-key/library import Apple26 vẫn bị từ chối. Toggle giữ track51×31 và native Smart Animate200ms, nới component bounds64×48; Search app được chỉnh nền ấm, chữ Be Vietnam Pro, vùng48pt. Không coi toàn bộ Apple kit đã import.
- Figma Simple Design System: Button set `178:370`, primary `178:371`, neutral `178:374`; Input set `179:232`, default `179:234`, error `179:236`. Là remote source components; các app instance override tokens forest/cream, typography và radius. Không dùng lại giả định property `Label#15:*` của button cũ: source Button có `Label#2:0`; Input có `Label#280:41`, `Value#630:14`.
- Core icon24 được thay path từ Phosphor Regular chính thức, giữ main IDs; thêm4 Duotone. MIT/source/hash: `assets/icons/phosphor/sources.json`. Custom MilkCarton/PickupPass/Pantry và RescueMark forest/cream là native concept; SVG/source tại `assets/icons/savebite/`, chờ owner review.
- Pantry category set `150:246`:8 variants, native Auto Layout168×112 cố định, icon32 và label căn giữa. Đã sửa lỗi HUG62pt ở main và row48pt trong picker; không dùng `.resize()` để giả định Auto Layout đã thành fixed.
- Bảng kit sử dụng thực [Curated UI](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=198-189), [Icon Essentials](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=144-127), [Brand](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=137-44), [Photo Library](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=161-2). Registry ghi90 entries đã đăng ký, không khẳng định toàn bộ source variants đã QA.

Theo `DEC-011`, bản pilot v0.5 trên file cũ đã được xóa/nghỉ hưu. Tài liệu này quy định **Chuẩn Kiến trúc Hệ thống v1.0 (`CONFIRMED`)** trên file Figma mới [SaveBite-V2 (`7suZz9C8oL5zV2NMxlsIVI`)](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1): loại bỏ hoàn toàn hội chứng lạm dụng thẻ viền (*Boxitis*), áp dụng chuẩn **iPhone 15 (`393×852pt`, Dynamic Island)** và phục vụ 10 màn hình đại diện Phase 1 trước khi mở rộng ra toàn bộ 100 màn hình.

---

## 1. DESIGN DIRECTION & TOKENS — NGÔN NGỮ THỊ GIÁC CỦA APP

### 1.1. Định hướng cốt lõi: *Warm Editorial Rescue Market*
- Xem phân tích phê bình v0.5 và 10 quy tắc chống rập khuôn chi tiết tại [visual-direction.md](visual-direction.md).
- **Nguyên tắc vàng:** Ấm áp, giàu hình ảnh thực phẩm tự nhiên, minh bạch điều kiện nhận hàng và mang chất cảm của một ứng dụng iPhone bản địa (iOS-native).
- **Tránh lỗi từ slide thuyết trình & template AI:** Phong cách slide có thể dùng serif khổng lồ hoặc chia hộp dày đặc, nhưng **giao diện iPhone ưu tiên mặt phẳng mở (`Open Canvas #FFFCF6`)**, phân tách thông tin bằng khoảng trắng và đường kẻ mảnh `1pt #E8E2D8`, chỉ đóng thẻ trắng (`#FFFFFF`) cho các thực thể tương tác độc lập.

### 1.2. Hệ thống Màu sắc & Phân tầng Bề mặt (Color & Surface Tokens)

| Token | Hex | Cấp độ bề mặt / Vai trò | Quy tắc áp dụng & Accessibility |
|---|---|---|---|
| `color.brand.900` | `#004337` | **Level 3 · Brand Focal**: Primary CTA, Hero Banner, Slot đang chọn, Header Vé QR | Độ tương phản rất cao với chữ trắng `#FFFFFF` (`> 11:1`). |
| `color.brand.700` | `#2D7055` | Secondary brand action, nhãn phụ màu xanh, viền chọn | Đạt tương phản chuẩn AA trên nền kem `#FFFCF6` và trắng `#FFFFFF`. |
| `color.brand.100` | `#EDF3E7` | **Level 1 · Sage Tonal Well**: Nền chip đang chọn, hộp thông tin nhẹ, tag trạng thái | Dùng không viền (`0px stroke`); luôn đi kèm chữ đậm `#004337` hoặc `#092F29`. |
| `color.surface.canvas` | `#FFFCF6` | **Level 0 · Primary Canvas**: Nền chính của toàn ứng dụng | Ít nhất 35% diện tích màn hình phải để lộ nền Canvas thoáng, không phủ kín bằng thẻ. |
| `color.surface.subtle` | `#F4EFE6` | **Level 1 · Warm Sand Inset**: Khối nhóm cài đặt chìm, ô tìm kiếm, vùng phụ | Dùng để phân nhóm nhẹ nhàng mà không cần vẽ viền hộp. |
| `color.surface.card` | `#FFFFFF` | **Level 2 · Elevated Card**: Thẻ `OfferCard`, `RescueTicket`, `BottomSheet` | Chỉ dùng tối đa 1 lớp thẻ (cấm lồng thẻ trắng trong thẻ trắng). |
| `color.accent.orange` | `#D7834B` | Điểm nhấn đồ họa, thanh biểu đồ Pantry, huy hiệu lớn | **KHÔNG dùng làm chữ nhỏ trên nền kem/trắng** vì contrast thấp. |
| `color.accent.orangeText` | `#B34021` | **Giá tiền Rescue (`25.000đ`)** & Nhãn sắp đóng khung giờ | Đạt chuẩn tương phản AA cho chữ và số giá tiền trên nền sáng. |
| `color.text.primary` | `#092F29` | Tiêu đề và nội dung chính độ tương phản cao | Thay cho màu đen tuyền để giữ độ ấm đồng bộ với xanh rừng. |
| `color.text.secondary` | `#606E66` | Thông tin phụ, địa chỉ, giờ nhận, chú thích | Đã kiểm chứng contrast `≥ 4.74:1` trên cả `#FFFCF6`, `#FFFFFF` và `#EDF3E7`. |
| `color.border.default` | `#E8E2D8` | Đường kẻ phân cách mảnh (`1pt hairline`), viền ô nhập liệu | Dùng làm dòng kẻ ngang giữa các mục thay vì đóng khung 4 cạnh mọi thứ. |
| `color.semantic.error` | `#B42318` | Lỗi biểu mẫu, cảnh báo quá hạn sử dụng (`Use-by`), nút Hủy đơn | Đi kèm nền nhẹ `#FDF2F0` và biểu tượng cảnh báo rõ ràng. |
| `color.semantic.warning` | `#9A5400` | Sắp hết hạn Pantry (`1–2 ngày`), khung nhận sắp đóng, cảnh báo dị ứng | Đi kèm nền nhẹ `#FEF6EE`; không dùng màu đơn lẻ để kết luận an toàn thực phẩm. |
| `color.semantic.success` | `#25603C` | Đặt chỗ thành công, thực phẩm còn tươi hạn dài, đã xác nhận nhận món | Đi kèm nhãn văn bản rõ nghĩa. |

### 1.3. Typography, Thang kích thước & Hệ lưới (Grid, Spacing & Radius)

- **Font chữ chuẩn:**
  - Giao diện chính: **`Be Vietnam Pro`** (Regular 400, Medium 500, SemiBold 600, Bold 700) — hiển thị dấu tiếng Việt hoàn hảo.
  - Mã nhận hàng & ID đơn (`SB-056`, `SB-063`): **`JetBrains Mono`** hoặc **`SF Mono`** (Bold, tracking `+0.08em`) để tách biệt rõ từng ký tự `DEMO-A125`.
  - Thành phần hệ thống iPhone (Status Bar `16:00`, iOS Keyboard, System Alert): **`SF Pro Text / Display`** chuẩn Apple.
  - Tiêu đề cảm xúc (tùy chọn ở Onboarding `SB-001..004` & Impact `SB-100`): **`Fraunces`** / **`Newsreader`** hoặc `Be Vietnam Pro Bold` tracking `-0.02em`.
- **Thang chữ (Type Scale) & Quy tắc Số học:**
  - `Display`: `30/36` (hoặc `32/40`), `H1 / Large Title`: `26/34`, `H2 / Section`: `20/26` (hoặc `22/30`), `H3 / Card Title`: `16/22`–`18/26`, `Body`: `15/22`–`16/24`, `Secondary / Meta`: `13/18`–`14/20`, `Caption / Badge`: `12/16`.
  - **Bắt buộc bật `tabular-nums` (số đẳng độ rộng)** cho mọi giá tiền (`25.000đ`), khung giờ (`17:00–18:00`), số lượng (`Còn 3 phần`) và đếm ngược.
- **Lưới & Khoảng cách (Spacing Tokens):**
  - Base grid `4pt`, bước nhảy chuẩn: `4, 8, 12, 16, 20, 24, 32, 48`.
  - Lề ngang màn hình (`Horizontal Padding`): **`20pt`** (cho phép co về `16pt` trên màn hẹp `360–375pt`).
- **Phân cấp Độ bo góc (Corner Radius Hierarchy — Chống đồng phục hóa):**
  - `radius.xs = 8pt`: Nhãn trạng thái nhỏ (`Badge/Tag`), ảnh thu nhỏ `56×56pt` trong dòng tóm tắt.
  - `radius.sm = 14pt`: Ô nhập liệu (`TextField`), ô chọn khung giờ (`PickupSlot`), hộp cảnh báo (`AllergenNotice`), nhóm cài đặt chìm.
  - `radius.md = 20pt` (hoặc `24pt` trên pilot v0.5): Thẻ món ăn (`OfferCard`), Vé nhận món (`RescueTicket`), Banner Hero.
  - `radius.lg = 28pt`: Đỉnh tấm trượt (`Bottom Sheet`) và mặt phẳng nội dung đè lên ảnh Hero (`SB-034`).
  - `radius.pill = 999pt`: Nút bấm chính (`Button`), chip lọc (`FilterChip`), thanh tiến độ.
- **Khung thiết bị & Vùng an toàn iOS (Device & Safe Areas — `CONFIRMED` theo `DEC-011`):**
  - Chuẩn khung thiết bị bắt buộc: **iPhone 15 / 16 Standard — `393×852pt`** với **Dynamic Island (`59pt` top safe area)** và **Home Indicator (`34pt` bottom safe area)** (kiểm tra co giãn ở `375×812pt` và `430×932pt`). Xem quy định chi tiết tại [ios-guidelines.md](ios-guidelines.md).
  - Vùng chạm (Touch Target): Tối thiểu `44×44pt` theo Apple HIG và đạt **`48×48pt`** cho mọi hotspot kết nối trong prototype.

### 1.4. Hệ thống Ảnh, Icon & Copywriting
- **Ảnh thực phẩm:** Tuân thủ nghiêm ngặt [asset-strategy.md](asset-strategy.md). Ưu tiên ảnh thật từ **Pexels / Unsplash** có ánh sáng ban ngày ấm áp, đúng món, lưu đầy đủ nguồn và SHA-256 trong `assets/manifest.json`. **Cấm dùng trùng một bức ảnh ở 2 vị trí khác nhau trên cùng một màn hình.**
- **Iconography:** Chuẩn hóa về một bộ vector duy nhất là **Phosphor Icons** (MIT License) hoặc **Lucide Icons** (ISC License). Dùng nét `Regular (1.75–2pt)` cho trạng thái thường và `Duotone / Fill` cho trạng thái đang chọn hoặc danh mục thực phẩm. **Tuyệt đối không dùng emoji hoặc icon tự vẽ lệch tỷ lệ.**
- **Copywriting Tiếng Việt:**
  - Tự nhiên, rõ ràng, đúng ngữ cảnh sinh viên & người trẻ Việt Nam: *“Đặt giữ chỗ”*, *“Thanh toán tại quầy khi nhận”*, *“Còn 3 phần”*, *“Nhận 17:00–18:00”*, *“Thành phần chưa được cửa hàng cung cấp”*.
  - Định dạng tiền tệ: `25.000đ`; giờ 24h (`17:00–18:00`); ngày `dd/MM/yyyy` theo múi giờ `Asia/Ho_Chi_Minh`.

---

## 2. KIẾN TRÚC COMPONENT & CHIẾN LƯỢC TÁI SỬ DỤNG

### 2.1. Vòng đời Component (Component Lifecycle)
`LOCAL → CANDIDATE → SHARED → STABLE → DEPRECATED`
- Trước khi tạo bất kỳ component mới nào, bắt buộc tra cứu [components.csv](../tracking/components.csv) và trang `Components` (`11:2`) trên Figma hiện hành; ID khác từ file cũ không được dùng lại.
- Ưu tiên truyền nội dung qua **Component Properties** (`Text`, `Boolean`, `Instance Swap`) và chuyển đổi trạng thái qua **Variants** thay vì detach instance.

### 2.2. Danh mục Component Chuẩn cho Toàn bộ 100 Màn hình

| Nhóm | Tên Component | Variants / Properties bắt buộc | Màn hình tiêu biểu |
|---|---|---|---|
| **iOS System Chrome** | `iOSStatusBar`, `iOSHomeIndicator`, `iOSKeyboard`, `iOSSheetGrabber` | `Theme=Dark/Light` (cho StatusBar & HomeIndicator); `Type=Default/Search/Number` (cho Keyboard) | Toàn bộ `SB-001..100` (`Keyboard` ở `SB-009, 019, 020`) |
| **Navigation & Bars** | `BrandHeader`, `AppBar` (`PushNavBar`), `LargeTitleBar`, `MediaOverlayBar`, `BottomNav`, `SegmentedControl` | `Mode=Guest/Auth` (BrandHeader); `RightAction=None/Icon/Text` (AppBar); `ActiveTab=Explore/Orders/Pantry/Account` (BottomNav) | `SB-013..015`, `SB-034`, `SB-051..056`, `SB-060`, `SB-075`, `SB-091` |
| **Core Actions & Docks** | `Button`, `IconButton`, `StickySplitDock` | `Style=Primary/Secondary/Destructive/Tertiary`, `State=Default/Pressed/Disabled/Loading`; `StickySplitDock` có `Price`, `PaymentNote`, `CTALabel` | Toàn bộ màn hành động; `StickySplitDock` ở `SB-034, 044, 046..049` |
| **Discovery & Cards** | `OfferCard`, `OfferListRow`, `FeaturedOfferHero`, `CategoryTile`, `FilterChip`, `MapPricePin` | `Type=ExactItem/SurpriseBag`, `Status=Available/ClosingSoon/SoldOut`; `Photo` instance-swap, `Price`, `OriginalPrice?`, `PickupWindow`, `StockLeft` | `SB-013..033`, `SB-041` |
| **Offer & Trust** | `MerchantRow`, `PickupInfo`, `AllergenNotice`, `SurpriseBagHero`, `FreshnessTimelineCard` | `AllergenStatus=Unknown/Declared/Conflict`; `PickupStatus=Open/ClosingSoon/Closed` | `SB-034..049`, `SB-053` |
| **Reservation & Pass** | `ReservationProgress`, `OfferSummary`, `PickupSlot`, `UnifiedReceiptCard`, `PerforatedPickupPass`, `DemoQR` | `Stage=Time/Review`; `SlotState=Available/Selected/Expired`; `PassState=Confirmed/Ready/Completed/Expired` | `SB-050..058`, `SB-060..068`, `SB-072` |
| **Smart Pantry** | `FreshnessSummaryBanner`, `PantryItemRow`, `ExpiryStatusTag`, `PantryCategoryTile`, `UsageFractionSelector` | `DateType=UseBy/BestBefore/Unknown`, `Freshness=Safe/ExpiringSoon/Overdue/Consumed/Disposed` | `SB-074..090` |
| **Inputs, States & Hub** | `TextField`, `SearchField`, `EmptyState`, `ErrorRecoveryCard`, `iOSSwitchRow`, `ImpactHeroCard` | `FieldState=Default/Focused/Filled/Error/Disabled`; `StateKind=Empty/NoResult/NetworkError/StockChanged/Expired` | `SB-006..010`, `SB-019..022`, `SB-057..058`, `SB-073`, `SB-076`, `SB-091..100` |

---

## 3. KIẾN TRÚC COMPONENT PHASE 1 TRÊN FILE FIGMA MỚI (`7suZz9C8oL5zV2NMxlsIVI`)

Theo `DEC-011`, toàn bộ node ID cũ trên file `NLTv70kDZ2i3HpOnOKQCDY` đã được nghỉ hưu. Trên file mới [SaveBite-V2 (`7suZz9C8oL5zV2NMxlsIVI`)](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1), hệ thống Component Phase 1 tập trung vào đúng **24 Core Components** phục vụ trực tiếp 10 màn hình đại diện (`SB-002`, `SB-015`, `SB-016`, `SB-019`, `SB-034`, `SB-051`, `SB-053`, `SB-056`, `SB-075`, `SB-091`) và tái sử dụng cho 90 màn còn lại:
- **Mapping chi tiết:** Lưu tại [components.csv](../tracking/components.csv).
- **Trạng thái hiện tại:** tham chiếu từng dòng trong registry và read-back live, không áp dụng nhãn `BLOCKED_FIGMA_MCP` lịch sử cho mọi component. Theo `DEC-012`, batch end-to-end kiểm lại mains/variants/properties, bổ sung sheet dùng lại và sửa mapping; specification ở §2.2 không chứng minh variants đó đã tồn tại.

### End-to-end reconciliation (`DEC-012`, 31/10/2026)

63 mains/sets hiện được ghi registry sau read-back (39 màn hiện có). Đây là inventory, không phải thư viện đã được nghiệm thu. Phần lớn component gốc là plain COMPONENT, không có Theme/ActiveTab/State variants dù bảng specification yêu cầu; registry đã bỏ khai báo giả. 6 controls mới và24 icon mains đã tạo nhưng thiếu text/swap properties và tương tác, có lỗi crop/copy cần sửa; xem [foundation checkpoint](../tracking/foundation-checkpoint.md). Không nhân rộng trạng thái tĩnh dưới nhãn “interactive”. Các bảng dưới đây là **quy cách đích**, không chứng minh hiện thực.

### Bảng hướng dẫn sử dụng các Core Components Phase 1 v1.0

| Thành phần | Quy cách v1.0 trên `SaveBite-V2` (`393×852pt`) |
|---|---|
| `iOSStatusBar` / `iOSHomeIndicator` / `iOSKeyboard` | Thành phần hệ thống chuẩn iPhone 15 (`393×59pt` Dynamic Island, `393×34pt` Home Indicator `134×5pt`, `393×291pt` QWERTY Keyboard trên `SB-019`). |
| `BrandHeader` / `AppBar` / `LargeTitleBar` / `MediaOverlayBar` | 4 mẫu điều hướng đầu trang chuẩn HIG: `BrandHeader` ở `SB-015`, `MediaOverlayBar` ở `SB-034`, `AppBar` (Push Nav) ở `SB-051, 053`, `LargeTitleBar` ở `SB-075, 091`. |
| `BottomNav` | Thanh 4 tab chuẩn `D-002` (`Khám phá`, `Đơn của tôi`, `Tủ thực phẩm`, `Tài khoản`) cao `83pt` (`49pt` tab bar + `34pt` Home Indicator), dùng Phosphor Icons (`Duotone/Fill` khi active, `Regular` khi inactive). |
| `Button` / `StickySplitDock` | `Button` có `Primary`, `Secondary`, `PrimaryDisabled`, `PrimaryLoading` (`radius: 999pt`). `StickySplitDock` ở đáy `SB-034` tách rõ giá `25.000đ · Trả tại quầy` (trái) và nút `Chọn giờ nhận →` (phải). |
| `CategoryTile` / `OfferCard` / `OfferListRow` | Phục vụ `SB-015`: `CategoryTile` dùng icon Phosphor `32×32pt Duotone`; `OfferCard` lưới 2 cột bo góc `20pt` có badge giờ nhận & số phần đè góc ảnh; `OfferListRow` hàng ngang so sánh nhanh. |
| `MapCanvas` / `MapPricePin` | Phục vụ `SB-016`: nền bản đồ vector ấm `#F3EFE6` quanh Khu học xá Đà Nẵng kèm ghim giá `25.000đ` (`Active #B34021`) và `30.000đ`, `35.000đ` (`Default #004337`). |
| `SearchField` | Phục vụ `SB-019`: ô tìm kiếm cao `48pt`, `radius-14`, có trạng thái `Default` và `Focused` (viền `#004337 2pt`). |
| `MerchantRow` / `PickupInfo` / `AllergenNotice` | Phục vụ `SB-034, 051, 053`: `MerchantRow` và `PickupInfo` trình bày dạng hàng phẳng ngăn cách bằng đường kẻ `1pt #E8E2D8`; `AllergenNotice` dùng hộp nền ấm `#FEF6EE` hiển thị rõ trạng thái `UNKNOWN`. |
| `ReservationProgress` / `OfferSummary` / `PickupSlot` | Phục vụ `SB-051, 053`: thanh tiến độ 2 bước tích hợp ngay dưới `AppBar`; `OfferSummary` thu gọn thành strip ngang; `PickupSlot` có 3 variants (`Available`, `Selected #004337`, `Expired`). |
| `UnifiedReceiptCard` / `PerforatedPickupPass` / `DemoQR` | Phục vụ `SB-053, 056`: biên lai giấy đứt nét (`UnifiedReceiptCard`) không lồng thẻ; vé nhận món đục lỗ (`PerforatedPickupPass`) có 2 khuyết bán nguyệt `16pt`, `DemoQR` căn giữa tuyệt đối trên nền trắng và mã `DEMO-A125` font Monospace. |
| `FreshnessSummaryBanner` / `PantryItemRow` | Phục vụ `SB-075`: thanh tổng quan độ tươi 3 trạng thái và hàng thực phẩm gia đình có `Expiry Progress Bar` + nút chạm nhanh `Đã dùng`. |
| `ProfileHeaderCard` / `ImpactHeroCard` | Phục vụ `SB-091`: thẻ hồ sơ sinh viên `Minh Anh` và thẻ thành tựu cứu thực phẩm thực chứng (`3 phần đã nhận` · `4 món Pantry dùng kịp hạn`). |

---

## 4. CHECKLIST KHI TẠO MÀN HÌNH HOẶC CẬP NHẬT COMPONENT

1. **Tra cứu trước khi dựng:** Kiểm tra [components.csv](../tracking/components.csv) và [screen-art-direction.md](screen-art-direction.md) để xác định đúng **Archetype (`A1`–`A10`)** của màn hình sắp làm.
2. **Kiểm tra chống Boxitis:** Đếm số lượng hộp có viền trên màn hình — tuyệt đối không lồng card trong card và đảm bảo ít nhất 35% diện tích lộ nền Canvas/mặt phẳng mở.
3. **Kiểm tra chuẩn iPhone:** Đảm bảo có mặt `iOSStatusBar` đúng độ tương phản (Light/Dark) ở đỉnh và `iOSHomeIndicator` (`34pt`) ở đáy.
4. **Kiểm tra đa kích thước & nội dung tiếng Việt:** Thử chuỗi tiếng Việt dài, giá tiền dài, kiểm tra không tràn bounds ở cả 3 độ rộng (`360/375pt`, `390/393pt`, `430pt`) và kiểm tra toàn bộ vùng chạm `≥ 48×48pt`.
5. **Đồng bộ Registry & Evidence:** Sau khi sửa main component trên Figma, kiểm tra tất cả các màn hình đang chứa instance của nó, chụp lại screenshot và cập nhật [components.csv](../tracking/components.csv) + [screens.csv](../tracking/screens.csv).
