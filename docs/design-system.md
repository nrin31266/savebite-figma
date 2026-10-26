# Hệ thiết kế SaveBite (Design System & Component Architecture)

Nguồn chuẩn cho Design Tokens, Typography, Iconography và Kiến trúc Component trên Figma. Đọc cùng [router](README.md), [visual direction](visual-direction.md), [iOS guidelines](ios-guidelines.md), [chiến lược asset](asset-strategy.md) và [tiến độ](../tracking/progress.md) trước khi thay đổi.

Hiện trạng trên Figma là checkpoint **Pilot v0.5 theo DEC-010** (`AWAITING_OWNER_REVIEW`). Tài liệu này lưu trữ đầy đủ thông số v0.5 đang chạy trên canvas đồng thời quy định **Chuẩn Kiến trúc Hệ thống v1.0 (`PROPOSED`)** để loại bỏ hội chứng lạm dụng thẻ viền (*Boxitis*), bổ sung thành phần iOS System Chrome chính thức và chuẩn bị cho 100 màn hình.

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
- **Khung thiết bị & Vùng an toàn iOS (Device & Safe Areas):**
  - Baseline v0.5 hiện hành: **`390×844pt`** (kiểm tra co giãn ở `360` và `430`).
  - Đề xuất chuẩn hóa v1.0 (chờ Owner duyệt): **iPhone 15 / 16 — `393×852pt`** với **Dynamic Island (`59pt` top safe area)** và **Home Indicator (`34pt` bottom safe area)**. Xem quy định chi tiết tại [ios-guidelines.md](ios-guidelines.md).
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
- Trước khi tạo bất kỳ component mới nào, bắt buộc tra cứu [components.csv](../tracking/components.csv) và trang `Components` (`27:87`) trên Figma.
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

## 3. HIỆN TRẠNG PILOT v0.5 TRÊN FIGMA CANVAS

Dữ liệu dưới đây phản ánh chính xác trạng thái đã read-back của **Pilot v0.5** tại file `NLTv70kDZ2i3HpOnOKQCDY`:
- **Quy mô hiện có:** `40 variables`, `11 text styles`, `2 effect styles`, **`21 main components` / `3 variant sets` / `31 screen instances`** trên 5 màn hình (`SB-015`, `SB-034`, `SB-051`, `SB-053`, `SB-056`).
- **Mapping chi tiết:** Lưu tại [components.csv](../tracking/components.csv) và [board component trên Figma](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=29-2).
- **Trạng thái:** `SHARED` (chưa lên `STABLE` vì đang ở cổng `AWAITING_OWNER_REVIEW`).

### Bảng hướng dẫn sử dụng các Component Pilot hiện có

| Thành phần | Cách sử dụng đúng & Điểm cần tinh chỉnh khi lên v1.0 |
|---|---|
| `BrandHeader` | Chứa Wordmark/leaf, khu vực `Đà Nẵng · Khu học xá` và nút chuông thông báo. Chỉ dùng ở trang gốc Khám phá (`SB-013..015`). |
| `Button` | Có `Primary` (`Default`, `Disabled`, `Loading`) và `Secondary` (`Default`). Đổi nhãn qua property `Label#27:2`. |
| `OfferCard` / `OfferListRow` / `OfferSummary` | Đổi nội dung qua properties đã expose (`Title`, `Merchant`, `Price`, `Pickup`, `Availability`, `Photo`). **Không detach instance để sửa chữ.** Khi lên v1.0, `OfferSummary` trên `SB-053` sẽ tích hợp thẳng vào `UnifiedReceiptCard` để bỏ viền lồng viền. |
| `MerchantRow` / `PickupInfo` | Hiển thị tên cửa hàng/địa chỉ và khung giờ nhận. Trên `SB-034` và `SB-051` bản v1.0, ưu tiên trình bày dạng hàng phẳng có đường kẻ phân cách `1pt` thay vì đóng hộp rời rạc. |
| `PickupSlot` | 3 variants: `Available`, `Selected` (`17:00–18:00`), `Expired` (`15:00–16:00`). Giữ nguyên logic tách bạch text gợi ý theo từng state. |
| `ReservationProgress` | `Stage=Time` ở `SB-051`, `Stage=Review` ở `SB-053`. Khi lên v1.0, tích hợp gọn ngay dưới thanh điều hướng để loại bỏ tiêu đề kép. |
| `AllergenNotice` | Dùng chung ở `SB-034` và `SB-053` trước khi xác nhận đặt giữ chỗ; giữ rõ thông điệp `UNKNOWN` khi cửa hàng chưa khai báo. |
| `DemoQR` | Vector QR mẫu (`SAVEBITE-DEMO:DEMO-001:NOT-A-REAL-ORDER`). Khi lên v1.0 trên `SB-056` và `SB-063`, **bắt buộc căn giữa tuyệt đối** trong khung `PerforatedPickupPass` kèm mã `DEMO-A125` bằng font Monospace. |

---

## 4. CHECKLIST KHI TẠO MÀN HÌNH HOẶC CẬP NHẬT COMPONENT

1. **Tra cứu trước khi dựng:** Kiểm tra [components.csv](../tracking/components.csv) và [screen-art-direction.md](screen-art-direction.md) để xác định đúng **Archetype (`A1`–`A10`)** của màn hình sắp làm.
2. **Kiểm tra chống Boxitis:** Đếm số lượng hộp có viền trên màn hình — tuyệt đối không lồng card trong card và đảm bảo ít nhất 35% diện tích lộ nền Canvas/mặt phẳng mở.
3. **Kiểm tra chuẩn iPhone:** Đảm bảo có mặt `iOSStatusBar` đúng độ tương phản (Light/Dark) ở đỉnh và `iOSHomeIndicator` (`34pt`) ở đáy.
4. **Kiểm tra đa kích thước & nội dung tiếng Việt:** Thử chuỗi tiếng Việt dài, giá tiền dài, kiểm tra không tràn bounds ở cả 3 độ rộng (`360/375pt`, `390/393pt`, `430pt`) và kiểm tra toàn bộ vùng chạm `≥ 48×48pt`.
5. **Đồng bộ Registry & Evidence:** Sau khi sửa main component trên Figma, kiểm tra tất cả các màn hình đang chứa instance của nó, chụp lại screenshot và cập nhật [components.csv](../tracking/components.csv) + [screens.csv](../tracking/screens.csv).
