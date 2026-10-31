# Chiến lược Tài nguyên Hình ảnh, Icon & Font (Asset-First Strategy)

Tài liệu quy định chính sách tìm kiếm, tái sử dụng, kiểm duyệt bản quyền và quản lý provenance cho toàn bộ ảnh chụp, icon, minh họa, bản đồ và font chữ trên 100 màn hình SaveBite. Đọc cùng [router](README.md), [visual direction](visual-direction.md), [iOS guidelines](ios-guidelines.md), [design system](design-system.md) và [manifest tài nguyên](../assets/manifest.json).

---

## 1. Nguyên tắc Cốt lõi: Asset-First, Tuyệt đối Tránh Generate AI Lãng phí

1. **Tái sử dụng tài nguyên thực chất lượng cao trước tiên (Curated Real Assets First):**
   - Thực phẩm cứu nguy (*food rescue*) cần tạo dựng **niềm tin thị giác tức thì**. Một bức ảnh chụp thực phẩm thật dưới ánh sáng tự nhiên từ Pexels/Unsplash luôn mang lại độ chân thực, kết cấu vỏ bánh/rau củ thuyết phục hơn nhiều so với ảnh AI bóng bẩy giả tạo.
   - Các thành phần hệ thống iOS (Status Bar, Dynamic Island, Keyboard, Toggle) và bộ Icon giao diện đã có nguồn vector chuẩn công nghiệp miễn phí 100% — **nghiêm cấm dùng AI để sinh icon, sinh chữ hay vẽ khung điện thoại**.
2. **100 màn hình KHÔNG cần 100 bức ảnh khác nhau:**
   - Trong 100 màn hình của SaveBite, phần lớn là các màn trạng thái luồng đặt hàng, chọn giờ, biên lai, mã QR, quản lý hạn dùng Pantry, bản đồ và cài đặt.
   - Toàn bộ 100 màn hình chỉ cần một **Bộ sưu tập 6–8 ảnh thực phẩm & cửa hàng chuẩn (Canonical Fixture Pool)** được tuyển chọn kỹ lưỡng, đồng bộ ánh sáng ấm và gắn chặt với từng `fixture-id` xuyên suốt ứng dụng.
3. **Khi nào mới được phép dùng ảnh AI (`GENERATED_CONCEPT`):**
   - Chỉ khi thật sự không tìm được ảnh stock miễn phí hợp lệ cho một khái niệm đặc thù của dự án (ví dụ: ảnh `food-sourdough-generated-v05` đã được duyệt trong DEC-010 cho pilot, hoặc minh họa biểu tượng Túi Bất Ngờ mang màu sắc thương hiệu).
   - Mọi asset AI bắt buộc phải: (a) là ảnh đối tượng độc lập (không chứa chữ, không chứa UI giả), (b) ghi rõ `sourceType: "GENERATED_CONCEPT"` cùng `prompt` và `sha256` trong [assets/manifest.json](../assets/manifest.json), và (c) có nhãn minh họa trên giao diện để không mạo nhận là ảnh chụp từ đối tác thật.

---

## 2. Ma trận Nguồn Tài nguyên & Xác minh Bản quyền (Verified Sources Matrix)

Bảng dưới đây phân định rõ URL chính thức, giấy phép, phạm vi được phép/cấm và mức độ tương thích với Figma của từng nguồn:

| Hạng mục | Nguồn chính thức | Giấy phép (License) & Điều kiện | Đánh giá chất lượng & Tương thích Figma | Khi nào ưu tiên / Khi nào KHÔNG dùng | Trạng thái |
|---|---|---|---|---|---|
| **Ảnh thực phẩm & cửa hàng (Ưu tiên #1)** | **Pexels** (`https://www.pexels.com`) · [Giấy phép Pexels](https://www.pexels.com/license/) | Miễn phí cho mục đích thương mại & phi thương mại; cho phép cắt cúp/chỉnh màu. Không được bán lại ảnh gốc hoặc ngụ ý nhân vật/thương hiệu trong ảnh bảo trợ cho app. | Ảnh độ phân giải rất cao, nhiều góc chụp 3/4 và flat-lay ẩm thực tự nhiên; kéo thả trực tiếp vào Figma Image Fill (`FILL` / `CROP`). | **Ưu tiên số 1** cho mọi món ăn trong `OfferCard`, `OfferDetail`, `Category` và `Banner`. **Không dùng** ảnh có logo chuỗi cửa hàng thật hoặc khuôn mặt người rõ nét. | `VERIFIED SOURCE` (Đang dùng trong repo) |
| **Ảnh thực phẩm & cửa hàng (Ưu tiên #2)** | **Unsplash** (`https://unsplash.com`) · [Giấy phép Unsplash](https://unsplash.com/license) | Miễn phí sử dụng, chỉnh sửa trong mockup/sản phẩm; khuyến khích ghi công tác giả (`Attribution`) trong `assets/manifest.json`. | Chất lượng nhiếp ảnh editorial xuất sắc, tông màu ấm áp, rất hợp phong cách *Warm Editorial Rescue Market*. | **Ưu tiên số 2** khi Pexels thiếu món ăn kiểu Á / Việt Nam (cơm hộp, bánh mì, rau củ chợ). **Không dùng** gói *Unsplash+* (có phí/hạn chế). | `VERIFIED SOURCE` |
| **Hệ thống Icon chính (Canonical Icon Set)** | **Phosphor Icons** (`https://phosphoricons.com`) · [GitHub MIT](https://github.com/phosphor-icons/core) | **MIT License** — tự do sử dụng, chỉnh sửa, nhúng vào Figma và code mà không bị ràng buộc bản quyền. | Xuất sắc cho iOS: có 6 độ dày đồng bộ (`Thin`, `Light`, `Regular`, `Bold`, `Fill`, `Duotone`) trên khung `24×24pt` chuẩn; đầy đủ icon ẩm thực, tủ lạnh, biên lai, QR. | **Ưu tiên tuyệt đối** cho toàn bộ 100 màn hình: dùng `Regular` cho trạng thái thường, `Fill`/`Duotone` cho tab đang chọn và danh mục thực phẩm. | `VERIFIED SOURCE` (Đề xuất chuẩn hóa v1.0) |
| **Hệ thống Icon phụ / Tương thích** | **Lucide Icons** (`https://lucide.dev`) · [Giấy phép ISC](https://lucide.dev/license) | **ISC License** (tương đương MIT) — hoàn toàn miễn phí và mở. | Nét mảnh `2px` bo đầu tròn sạch sẽ, gọn gàng cho các biểu tượng điều hướng cơ bản (`ChevronLeft`, `Search`, `SlidersHorizontal`, `Check`). | Dùng cho các icon điều khiển cơ bản nếu đã có sẵn trong component; **không trộn lẫn** icon cùng loại của hai bộ trên cùng một thanh công cụ. | `VERIFIED SOURCE` |
| **Công cụ tra cứu Icon** | **Iconify** (`https://iconify.design`) · [Figma Plugin](https://www.figma.com/community/plugin/735098390272716381/iconify) | Công cụ tổng hợp; **bản quyền phụ thuộc vào từng bộ icon con bên trong** (chỉ lọc lấy `ph:` Phosphor hoặc `lucide:` Lucide). | Tiện lợi để chèn SVG vector trực tiếp vào Figma. | Chỉ dùng làm **công cụ tìm kiếm** các bộ đã duyệt (`ph`, `lucide`, `tabler`). **Cấm** lấy ngẫu nhiên icon từ các bộ không rõ license hoặc khác nét vẽ. | `VERIFIED TOOL` |
| **Font chữ Giao diện & Biên lai** | **Google Fonts** (`https://fonts.google.com`): `Be Vietnam Pro`, `Fraunces`, `JetBrains Mono` | **SIL Open Font License 1.1 (OFL-1.1)** — miễn phí 100% cho thiết kế, nhúng ứng dụng và phân phối. | Có sẵn mặc định trên Figma Cloud & Desktop; hỗ trợ tiếng Việt đầy đủ 100% dấu kép. | Dùng xuyên suốt toàn bộ nội dung SaveBite. **Không dùng** các font chỉ hỗ trợ bảng mã Latin cơ bản gây lỗi dấu tiếng Việt. | `CONFIRMED` (`Be Vietnam Pro`) |
| **Thành phần Hệ thống iPhone** | **Apple Design Resources** (`https://developer.apple.com/design/resources/`) · [Hướng dẫn Figma Apple UI Kit](https://help.figma.com/hc/en-us/articles/24037833895831-Get-started-with-Apple-s-UI-kit) | Bản quyền Apple Inc. — cấp phép sử dụng để thiết kế mockup/prototype cho các ứng dụng chạy trên hệ điều hành iOS/iPadOS. | Chuẩn xác tuyệt đối tới từng pixel cho `Status Bar`, `Dynamic Island`, `Home Indicator`, `Keyboard`, `System Alert`. | **Bắt buộc** dùng cho lớp vỏ hệ thống iOS. **Cấm** trích xuất icon hệ thống Apple để làm logo thương hiệu hoặc dùng ngoài ngữ cảnh mockup iOS. | `VERIFIED SOURCE` |

---

## 3. Bộ 9 Tài nguyên Ảnh Thực phẩm & Cửa hàng Chuẩn Đã Xác minh (`CONFIRMED` trong `assets/manifest.json`)

Theo `DEC-011`, toàn bộ ảnh AI tạo sinh và ảnh tối của bản pilot cũ đã được loại bỏ. Kho lưu trữ hiện có **9 file ảnh chụp thật từ Pexels (`Pexels License`)** — 6 ảnh gốc (pilot) + 3 ảnh thay thế/biến thể bổ sung 31/10/2026 để tránh lặp ảnh khi batch 90 màn cần nhiều điểm nhấn hơn cho cùng 1 fixture — đã được kiểm duyệt thị giác (ánh sáng tự nhiên ấm `5000K–5800K`, chủ thể rõ, không dính logo thương hiệu hay mặt người) và kiểm tra mã băm SHA-256 tự động qua `scripts/validate.py`:

| Mã Fixture | `assetId` & File trong repo | Nguồn & Giấy phép | Tên món & Cửa hàng hư cấu | Màn hình sử dụng tiêu biểu |
|---|---|---|---|---|
| **`fixture-bakery-01`** | `food-sourdough-461060` · [bread-sourdough-pexels-461060.jpg](../assets/food/bread-sourdough-pexels-461060.jpg) | Pixabay / Pexels (`Pexels License`) | **Bánh mì men tự nhiên** · *Tiệm Bánh A (demo)* · `25.000đ` (Còn 3 phần) · Nhận `17:00–18:00` | `SB-002` (Onboarding Hero Card), `SB-015` (Card 1), `SB-016` (Pin `25K`), `SB-034` (Full-bleed Hero), `SB-051`, `SB-053`, `SB-056`. |
| **`fixture-croissant-02`** | `food-croissant-3892469` · [croissant-warm-pexels-3892469.jpg](../assets/food/croissant-warm-pexels-3892469.jpg) | Elkhamisi / Pexels (`Pexels License`) | **Bánh sừng bò bơ Pháp** · *Tiệm Bánh A (demo)* · `30.000đ` (Còn 2 phần) · Nhận `17:00–18:00` | `SB-015` (Card 2 — ánh sáng gỗ ấm đồng bộ với Card 1), `SB-016` (Pin `30K`), `SB-029`, `SB-041`, `SB-046` (Gợi ý thay thế). |
| **`fixture-meal-03`** | `food-meal-1640777` · [rice-veggie-bowl-pexels-1640777.jpg](../assets/food/rice-veggie-bowl-pexels-1640777.jpg) | Ella Olsson / Pexels (`Pexels License`) | **Cơm gà áp chảo & rau củ** · *Bếp Xanh Campus (demo)* · `35.000đ` (Còn 4 phần) · Nhận `17:30–19:00` | `SB-013`, `SB-014`, `SB-015` (`OfferListRow`), `SB-016` (Pin `35K`), `SB-019..021`, `SB-028`, `SB-031`, `SB-032`. |
| **`fixture-veggie-04`** | `food-veggie-2255935` · [fresh-produce-pexels-2255935.jpg](../assets/food/fresh-produce-pexels-2255935.jpg) | Wendy Wei / Pexels (`Pexels License`) | **Combo rau củ tươi trong ngày** · *Quầy Rau C (demo)* · `30.000đ` (Còn 5 phần) · Nhận `16:00–17:30` | **Banner Hero của `SB-015`** (chống trùng ảnh với Card 1!), `SB-030` (Danh mục Rau củ), `SB-033` (Yêu thích). |
| **`fixture-surprise-05`** | `food-sourdough-sliced-1775043` · [bread-sliced-pexels-1775043.jpg](../assets/food/bread-sliced-pexels-1775043.jpg) | Marianna OLE / Pexels (`Pexels License`) | **Túi bánh bất ngờ cuối ngày** (`SURPRISE_BAG`) · *Tiệm Bánh A (demo)* · `29.000đ` (Còn 2 túi) · Nhận `18:00–19:00` | `SB-035` (Ảnh thứ 2 trong thư viện món bánh), `SB-044` (Chi tiết túi bất ngờ), `SB-045` (Giải thích túi bất ngờ). |
| **`fixture-store-01`** | `store-bakery-205961` · [bakery-counter-pexels-205961.jpg](../assets/food/bakery-counter-pexels-205961.jpg) | Igor Ovsyannykov / Pexels (`Pexels License`) | **Không gian quầy Tiệm Bánh A** · *Điểm A, Khu học xá (demo)* · Mở nhận `16:00–19:00` | `SB-038` (Chi tiết cửa hàng), `SB-040` (Quy định nhận món), `SB-042` (Đánh giá cửa hàng). |
| `fixture-bakery-01` (ảnh thay thế) | `food-bakeryrolls-2000498` · [bakery-rolls-pexels-2000498.jpg](../assets/food/bakery-rolls-pexels-2000498.jpg) | Cats Coming / Pexels (`Pexels License`) | **Ổ bánh mì nhỏ trong giỏ đan** — cùng offer `Bánh mì men tự nhiên` · *Tiệm Bánh A (demo)*, góc chụp khác để tránh lặp ảnh | Dùng khi 1 màn cần 2 điểm nhấn bánh (vd. featured banner + card) |
| `fixture-meal-03` (ảnh thay thế) | `food-ricebowls-5127769` · [rice-bowls-pexels-5127769.jpg](../assets/food/rice-bowls-pexels-5127769.jpg) | Sirikul R / Pexels (`Pexels License`) | **Hai phần cơm gà chụp từ trên xuống** — cùng offer `Cơm gà áp chảo & rau củ` · *Bếp Xanh Campus (demo)*, góc top-down khác | Dùng cho danh mục `SB-028` hoặc banner khi cần tránh lặp ảnh với `OfferListRow` |
| `fixture-veggie-04` (ảnh thay thế) | `food-producecrates-2679261` · [produce-crates-pexels-2679261.jpg](../assets/food/produce-crates-pexels-2679261.jpg) | Mark Stebnicki / Pexels (`Pexels License`) | **Thùng dưa & cà chua bi tại quầy nông sản** — cùng offer `Combo rau củ tươi trong ngày` · *Quầy Rau C (demo)* | Dùng cho `SB-030` (Danh mục Rau củ) hoặc banner khi cần tránh lặp ảnh |

---

## 4. Quy tắc Tuyển chọn Ảnh, Icon, Minh họa & Bản đồ

### 4.1. Tiêu chuẩn Chọn & Xử lý Ảnh Thực phẩm (Photography Direction)
1. **Nhiệt độ màu & Ánh sáng (Warm Daylight Consistency):**
   - Chỉ chọn ảnh có ánh sáng tự nhiên ban ngày hoặc nắng chiều ấm (`5000K–5800K`).
   - **Loại bỏ ngay:** Ảnh chụp dưới đèn huỳnh quang xanh lạnh, ảnh đánh flash gắt vào đĩa nhựa bóng, ảnh nền đen tối tăm kiểu nhà hàng fine-dining ban đêm, hoặc ảnh bị ám màu tím/xanh dương.
2. **Bố cục & Tỷ lệ cắt (Crop-Safe Framing):**
   - Chủ thể món ăn phải chiếm **65%–80% diện tích trung tâm** để khi tái sử dụng ở 3 tỷ lệ chuẩn không bị mất phần ngon nhất của món:
     - `16:10` hoặc `4:3` tràn viền cho màn Chi tiết (`SB-034`, `SB-038`).
     - `4:3` ngang cho thẻ lưới 2 cột (`OfferCard` trên `SB-015`).
     - `1:1` vuông (`56×56pt` hoặc `64×64pt`, bo góc `10pt`) cho dòng tóm tắt đơn hàng (`OfferSummary` trên `SB-051..056`, `OfferListRow`).
3. **Tính trung thực với tên món:**
   - Món tên gì thì ảnh phải đúng món đó. Không dùng ảnh pizza hay hamburger phương Tây để minh họa cho món ăn sinh viên Đà Nẵng nếu tiêu đề ghi là cơm hoặc rau củ.

### 4.2. Tiêu chuẩn Hệ thống Icon (Iconography Rules)
1. **Một gia đình Icon duy nhất:** Chuẩn hóa toàn bộ icon giao diện về **Phosphor Icons** (hoặc **Lucide Icons** cho các mũi tên điều hướng cơ bản).
2. **Bản đồ thay thế các Icon tự vẽ trên Pilot v0.5:**
   - Danh mục `Tất cả` → Phosphor `SquaresFour` (Fill khi chọn / Regular khi không chọn)
   - Danh mục `Bánh mì` → Phosphor `Bread` hoặc `Croissant`
   - Danh mục `Đồ ăn sẵn` → Phosphor `BowlFood` hoặc `CookingPot`
   - Danh mục `Rau củ` → Phosphor `Carrot` hoặc `Plant`
   - Tab `Khám phá` → Phosphor `Compass` hoặc `Storefront`
   - Tab `Đơn của tôi` → Phosphor `Receipt` hoặc `ShoppingBagOpen`
   - Tab `Tủ thực phẩm` → Phosphor `ArchiveBox` / `Package` / `ThermometerCold`
   - Tab `Tài khoản` → Phosphor `UserCircle`
3. **4 kích thước Token cố định:**
   - `16×16pt` (`stroke 1.5pt`): Icon đi kèm dòng metadata nhỏ (đồng hồ giờ nhận, địa điểm, chiếc lá dị ứng).
   - `20×20pt` (`stroke 1.75pt`): Icon trong ô tìm kiếm, nút phụ, dòng danh sách cài đặt.
   - `24×24pt` (`stroke 1.75pt–2pt`): Icon trên thanh điều hướng `AppBar`, nút lọc `Filter`, và `BottomTabBar`.
   - `32×32pt` (`Duotone`): Icon trong ô danh mục (`CategoryTile`) và huy hiệu trạng thái rỗng/lỗi (`EmptyState`, `ErrorState`).

### 4.3. Tiêu chuẩn Minh họa, Bản đồ & Mã QR (Illustrations, Maps & QR)
1. **Minh họa Trạng thái (Spot Badges thay vì Tranh AI toàn màn):**
   - Với các màn Onboarding (`SB-002..004`), Empty State (`SB-022`, `SB-073`, `SB-076`, `SB-096`) và Error/Expired (`SB-046`, `SB-057`, `SB-068`), **không chèn hình vẽ AI nhiều chi tiết lệch tông**.
   - Thay vào đó, sử dụng **Composed Vector Spot Badges** (`72×72pt` hoặc `96×96pt`): kết hợp các hình học mềm nền `#EDF3E7` / `#FEF6EE` với icon Phosphor `Duotone` cỡ lớn màu `#004337` / `#B34021` cùng các thẻ UI thu nhỏ (micro-UI illustration). Cách này vừa sang trọng kiểu iOS hiện đại (như Airbnb/Stripe/Linear), vừa 100% vector native trên Figma.
2. **Bản đồ Vector Tùy biến (`SB-016`, `SB-017`, `SB-039`, `SB-065`, `SB-094`):**
   - Không chụp ảnh màn hình Google Maps có dính chữ bản quyền hay giao diện rối mắt.
   - Dựng một **Component `MapCanvas` bằng Vector Native trên Figma** với bảng màu ấm đồng bộ thương hiệu: nền đất `#F3EFE6`, công viên cây xanh `#E2ECE4`, mặt nước sông Hàn/biển `#CFE2E0`, đường chính `#FFFFFF` viền `#E5DEC9`, và đặt các ghim giá `MapPin` (`25K`, `30K`) nổi bật phía trên.
3. **Mã QR Nhận món (`DemoQR` trên `SB-056`, `SB-063`):**
   - Tái sử dụng component vector `DemoQR` (`27:183`) đã có trong file Figma (mã hóa chuỗi `SAVEBITE-DEMO:DEMO-001:NOT-A-REAL-ORDER`), luôn đặt trên nền trắng `#FFFFFF` có vùng đệm an toàn (`quiet zone ≥ 16pt` bốn phía) và căn giữa tuyệt đối trong khung vé.

---

## 5. Quy trình Cập nhật `assets/manifest.json` & Kiểm tra Validator

Bất kỳ khi nào thêm hoặc thay thế một file ảnh trong thư mục `assets/` (khi thực hiện batch thiết kế), bắt buộc tuân thủ quy trình 4 bước sau để không làm gãy `python3 scripts/validate.py`:

1. **Đặt tên file rõ nghĩa theo chuẩn:** `assets/food/<ten-mon>-<source-id>.<jpg|png|webp>` (ví dụ: `assets/food/rice-bowl-pexels-1640777.jpg`).
2. **Tính mã băm SHA-256 thực tế của file trên đĩa:**
   ```bash
   sha256sum assets/food/<ten-file>
   ```
3. **Khai báo đầy đủ các trường bắt buộc vào [assets/manifest.json](../assets/manifest.json):**
   - `assetId`: định danh duy nhất (ví dụ `"food-meal-1640777"`).
   - `kind`: `"FOOD_PHOTO"`, `"STORE_PHOTO"`, hoặc `"FOOD_ILLUSTRATION"`.
   - `filePath`: đường dẫn tương đối từ gốc repo (`"assets/food/..."`).
   - `sourceUrl`: URL trang gốc của bức ảnh trên Pexels/Unsplash (hoặc `null` kèm `sourceType: "GENERATED_CONCEPT"` và `prompt` nếu là ảnh AI).
   - `license` & `licenseUrl`: tên giấy phép và đường dẫn điều khoản.
   - `attribution`: tên tác giả / nguồn.
   - `downloadDate`: ngày tải (`YYYY-MM-DD`).
   - `usageScope`: ghi rõ `"Fictional demo offer only; no real merchant endorsement or food safety claim"`.
   - `merchantId` & `offerId`: khớp với fixture trong [product.md](product.md) và [experience.md](experience.md).
   - `altText`: mô tả tiếng Việt rõ ràng phục vụ accessibility.
   - `approved`: `true` sau khi kiểm tra không dính watermark/logo thật.
   - `sha256`: chuỗi 64 ký tự hex trùng khớp tuyệt đối với kết quả lệnh `sha256sum`.
4. **Chạy trình kiểm tra tự động:**
   ```bash
   python3 scripts/validate.py
   ```
   *(Lưu ý: `scripts/validate.py` dòng 67–69 sẽ đọc toàn bộ `assets/manifest.json` và đối chiếu `hashlib.sha256` của từng file trên đĩa; thiếu file hoặc sai lệch 1 byte cũng sẽ báo lỗi `Asset drift`).*
