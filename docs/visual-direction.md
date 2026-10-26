# Định hướng Nghệ thuật & Ngôn ngữ Thị giác (Visual DNA)

Nguồn chuẩn cho Art Direction, Visual Hierarchy, Composition và quy tắc chống rập khuôn (anti-generic) trên toàn bộ 100 màn hình SaveBite. Đọc cùng [router](README.md), [design system](design-system.md), [iOS guidelines](ios-guidelines.md), [chiến lược asset](asset-strategy.md) và [ma trận 100 màn](screen-art-direction.md).

> **Trạng thái phê duyệt:** Phiên bản hiện tại trên Figma là **Pilot v0.5** (`AWAITING_OWNER_REVIEW`). Định hướng nâng cấp trong tài liệu này là **Art Direction v1.0 (`PROPOSED`)** nhằm giải quyết triệt để các hạn chế thẩm mỹ của v0.5 trước khi mở rộng 95 màn còn lại. Không tự ý sửa Figma canvas khi owner chưa duyệt quyết định chuyển đổi.

---

## 1. Đánh giá thẳng thắn hiện trạng Pilot v0.5 (Design Critique)

Dựa trên kiểm tra trực tiếp 5 màn hình pilot ([SB-015](../tracking/evidence/SB-015.png), [SB-034](../tracking/evidence/SB-034.png), [SB-051](../tracking/evidence/SB-051.png), [SB-053](../tracking/evidence/SB-053.png), [SB-056](../tracking/evidence/SB-056.png)) cùng [bộ thành phần](../tracking/evidence/components.png) và [foundations](../tracking/evidence/foundations.png):

### 1.1. Những điểm v0.5 đã làm đúng (Cần giữ lại)
- **Màu sắc thương hiệu có gốc rễ đúng ngành:** Sự kết hợp giữa xanh rừng đậm (`#004337`), nền kem ấm (`#FFFCF6`) và điểm nhấn giá cam đất (`#B34021`) tạo cảm giác thực phẩm bền vững, ấm áp, tránh được màu xanh neon công nghiệp.
- **Độ tương phản và khả năng đọc tiếng Việt:** Font `Be Vietnam Pro` hiển thị dấu tiếng Việt rõ, 13 cặp chữ/nền đều đạt chuẩn WCAG AA (`≥ 4.74:1`), không dùng chữ nhỏ màu cam nhạt trên nền sáng.
- **Tính trung thực nghiệp vụ:** Tôn trọng tuyệt đối nguyên tắc *Reserve & Pay at Pickup*, hiển thị rõ cảnh báo dị ứng `UNKNOWN` và nhãn dữ liệu mô phỏng.
- **Cấu trúc kỹ thuật Figma sạch:** Frame native editable 100%, dùng Auto Layout, biến màu/spacing và component properties không bị detach.

### 1.2. 7 vấn đề thẩm mỹ lớn khiến v0.5 chưa đạt chuẩn một ứng dụng iPhone cao cấp

| # | Vấn đề trên Pilot v0.5 | Biểu hiện cụ thể trên màn hình | Tác động đến cảm nhận sản phẩm |
|---|---|---|---|
| **1** | **Hội chứng "Boxitis" (Lạm dụng thẻ viền bo tròn)** | Trên [SB-051](../tracking/evidence/SB-051.png) và [SB-053](../tracking/evidence/SB-053.png), mọi thông tin (progress, tóm tắt món, ngày nhận, từng khung giờ, thanh toán tại quầy, dị ứng) đều bị nhốt vào các hộp full-width `radius: 24px`, viền `#E8E2D8` xếp chồng lên nhau. Trên `SB-053`, thẻ `OfferSummary` còn bị lồng bên trong một thẻ trắng lớn hơn (card-in-card). | Giao diện nặng nề, giống form web/SaaS dựng tự động bằng template AI; mắt người dùng không biết đâu là tâm điểm vì hộp nào cũng có trọng lượng thị giác ngang nhau. |
| **2** | **Thiếu chuẩn iOS System Chrome thực thụ** | Thanh trạng thái (status bar) dùng chữ `16:00` bằng font `Be Vietnam Pro` màu xanh đen cùng icon sóng/pin tự vẽ thô; thiếu hoàn toàn **iOS Home Indicator** (`134×5pt`) ở đáy cả 5 màn; trên [SB-034](../tracking/evidence/SB-034.png), ảnh món ăn bị chặn bởi một dải nền kem cứng phía trên thay vì tràn full-bleed lên đỉnh màn hình. | Mất ngay cảm giác "ảnh chụp ứng dụng iPhone thật"; trông như bản vẽ wireframe màu hoặc giao diện web mobile thu nhỏ. |
| **3** | **Lặp tiêu đề kép (Double-Header Redundancy)** | Ở [SB-051](../tracking/evidence/SB-051.png), ngay dưới thanh `AppBar` có chữ **"Đặt trước"** là tiêu đề lớn **"Bạn đến nhận lúc mấy giờ?"**. Ở [SB-053](../tracking/evidence/SB-053.png), ngay dưới **"Xác nhận"** là **"Kiểm tra đặt trước"**. Nút Back lại dùng vòng tròn viền 48×48px quá to cho mọi màn con. | Lãng phí 100–120pt chiều cao quý giá ở đầu màn hình, đẩy nội dung quan trọng xuống dưới và làm bố cục bị dồn nén. |
| **4** | **Màn hình Thành công (`SB-056`) thiếu cảm xúc và lệch bố cục** | Trên [SB-056](../tracking/evidence/SB-056.png): (1) Icon dấu tích xanh trên đỉnh quá nhỏ và nhạt nhòa; (2) Mã QR bị **căn lề trái lệch hẳn sang một bên** bên trong khung nền xanh nhạt `#EDF3E7`, để trống một khoảng vô duyên bên phải trong khi mã `DEMO-A125` ở dưới lại căn giữa; (3) Màn hình hoàn tất đơn hàng nhưng góc trên bên trái vẫn có nút `< SaveBite` như một trang form đang đi dở. | Khoảnh khắc quan trọng nhất của luồng đặt giữ chỗ (nhận vé cứu thực phẩm) bị biến thành một hộp thông tin khô khan và lỗi căn chỉnh thị giác. |
| **5** | **Trùng lặp ảnh ngay trên cùng một màn & lệch ánh sáng** | Trên [SB-015](../tracking/evidence/SB-015.png), bức ảnh bánh mì sourdough ở banner hero phía trên được **dùng lặp lại nguyên xi** ở thẻ `OfferCard` đầu tiên ngay bên dưới (cách nhau chưa đầy 50px). Trong khi đó, ảnh bánh mì sáng rực ánh nắng sớm, còn ảnh bánh sừng bò (`CroissantPhoto`) bên cạnh lại chụp trong phòng tối, dính lưng ghế đen phía sau. | Lộ rõ cảm giác "mock thiếu tài nguyên"; hai thẻ sản phẩm đứng cạnh nhau nhưng không thuộc cùng một thế giới hình ảnh. |
| **6** | **Iconography tự vẽ thiếu đồng nhất** | Bộ 4 icon danh mục trên `SB-015` (`Tất cả`, `Bánh mì`, `Đồ ăn sẵn`, `Rau củ`) dùng nét vẽ tự dựng rời rạc (hình rau củ giống cỏ 4 lá/đám mây, ổ bánh mì là hình bầu dục gạch 3 nét), độ dày nét và tỷ lệ lấp đầy không khớp với icon thanh điều hướng đáy. | Làm giảm độ sang trọng và tính chuyên nghiệp của toàn bộ màn hình Khám phá. |
| **7** | **Nhịp điệu Typography phẳng và thiếu tương phản** | Mọi con số (giá `25.000đ`, giờ `17:00–18:00`, số lượng `Còn 3 phần`, mã đơn) đều dùng cùng một kiểu xử lý với văn bản thường; thiếu số đẳng độ rộng (`tabular-nums`), thiếu sự đối lập giữa tiêu đề cảm xúc và dữ liệu giao dịch. | Khi nhân rộng lên 100 màn, các màn hình sẽ bị hòa lẫn vào nhau vì thiếu điểm nhấn thị giác đặc trưng theo từng nhiệm vụ. |

---

## 2. SaveBite Visual DNA — "Warm Editorial Rescue Market"

Để SaveBite nổi bật như một ứng dụng iOS consumer thực thụ (học hỏi nguyên tắc từ **Too Good To Go**, **Airbnb iOS**, **Wolt**, **Apple Wallet** và **Things 3** nhưng mang bản sắc Việt Nam riêng), ngôn ngữ thị giác được định nghĩa qua **4 trụ cột DNA**:

### 2.1. Tinh thần chủ đạo: *Ấm áp như tiệm bánh chiều · Minh bạch như hóa đơn giấy · Mượt mà chuẩn iOS*
1. **Warm Daylight Food First (Thực phẩm dưới nắng chiều ấm):** Mọi màn hình thuộc luồng khám phá và chi tiết món ăn phải lấy ánh sáng tự nhiên, màu vàng vỏ bánh, màu xanh rau củ tươi và nền giấy kem ấm (`#FFFCF6`) làm cảm hứng chính. Ảnh thực phẩm không nằm lọt thỏm trong những chiếc hộp nhỏ xíu mà được ưu tiên tỷ lệ lớn, sắc nét, có nhãn thời gian nhận và số phần còn lại đè lên ảnh một cách tinh tế.
2. **Tactile Paper & Perforated Pass (Chất cảm vé giấy & biên lai thực tế):** Thay vì dùng các thẻ chữ nhật bo tròn vô hồn cho bước đặt chỗ và nhận món, SaveBite sử dụng ngôn ngữ **Vé Nhận Món (Rescue Pass / Perforated Ticket)** lấy cảm hứng từ Apple Wallet và biên lai tiệm bánh thủ công: có khía răng cưa/khuyết tròn hai bên hông vé (`ticket notch`), đường kẻ đứt nét (`dashed rule`) ngăn cách thông tin món với mã QR, và mã nhận món in bằng font monospace sắc nét.
3. **Open Canvas over Boxitis (Mặt phẳng thoáng thay vì hộp chồng hộp):** Nền kem ấm `#FFFCF6` là không gian sống chính. Các nhóm thông tin đọc hiểu (cửa hàng, khung giờ, mô tả, chính sách hủy) được đặt trực tiếp trên nền canvas, phân tách bằng **khoảng trắng có nhịp điệu (24pt–32pt)** và **đường kẻ mảnh 1pt (`#E8E2D8`)** thay vì đóng khung từng dòng vào một chiếc thẻ riêng.
4. **Dual-Mode Sub-Brand Harmony (Hai sắc thái trong cùng một hệ thống):**
   - **Rescue Market (`SB-013..073`):** Sôi động, giàu hình ảnh món ăn, tương phản mạnh giữa xanh rừng `#004337`, cam đất `#B34021` và ảnh thực phẩm ấm.
   - **Smart Pantry (`SB-074..090`):** Tĩnh lặng, ngăn nắp như một gian bếp sạch (`Calm Kitchen Inventory`) — giảm mật độ ảnh chụp, tăng sử dụng thanh tiến độ hạn dùng (`Freshness Meter`), nhãn phân loại thực phẩm tinh gọn và gam màu ngữ nghĩa theo độ tươi (`Herb Green` → `Amber Ochre` → `Terracotta Alert`).

---

## 3. Hệ thống Màu sắc & Phân tầng Bề mặt (Surface Hierarchy)

Giữ nguyên các mã màu gốc của thương hiệu đã được kiểm chứng độ tương phản ở v0.5, nhưng **quy hoạch lại vai trò phân tầng bề mặt (Surface Layering)** để chấm dứt tình trạng "mọi thứ đều là card trắng có viền":

### 3.1. Bảng phân tầng 4 cấp độ bề mặt (4-Level Surface Architecture)

| Cấp độ | Token đề xuất | Mã Hex | Vai trò bắt buộc | Quy tắc viền & đổ bóng |
|---|---|---|---|---|
| **Level 0 · Canvas** | `color.surface.canvas` | `#FFFCF6` | Nền mặc định của toàn bộ ứng dụng. Nơi đặt trực tiếp tiêu đề, đoạn văn, danh sách thông tin phẳng và dòng kẻ phân mục. | Không viền, không bóng. |
| **Level 1 · Tonal Well** | `color.surface.subtle` / `color.brand.100` | `#F4EFE6` / `#EDF3E7` | Khối nền chìm (inset grouped section) cho bộ lọc, thanh tìm kiếm, thông báo nhẹ, khung tóm tắt phụ hoặc nhóm cài đặt. | **Không dùng viền (`0px stroke`)**; tách biệt với Canvas thuần túy bằng độ chênh sắc độ nhẹ. |
| **Level 2 · Elevated Card** | `color.surface.card` | `#FFFFFF` | **Chỉ dành cho thực thể tương tác độc lập** (`OfferCard`, `ActiveOrderCard`, `RescueTicket`, `PantryUrgentCard`) hoặc bottom sheet. | Viền mảnh `1px solid #EAE3D5` HOẶC bóng ấm mềm `0 8px 24px rgba(9, 47, 41, 0.06)` (không dùng viền đậm kèm bóng gắt). |
| **Level 3 · Brand Focal** | `color.brand.900` | `#004337` | Khối tạo điểm nhấn thị giác cực mạnh: Hero Banner, trạng thái Slot đang chọn, phần đầu của Vé Nhận Món (`Pickup Pass Header`), và nút Primary CTA. | Chữ trắng `#FFFFFF` hoặc kem `#FFFCF6`; có thể điểm xuyết họa tiết lá/hạt sáng nhẹ `rgba(255,255,255,0.08)`. |

### 3.2. Quy tắc sử dụng màu điểm nhấn (Accent Discipline)
- **Cam đất đậm (`#B34021` — `color.accent.orangeText`):** Dành riêng cho **Giá Rescue (`25.000đ`)** và **Nhãn khẩn cấp/sắp đóng khung giờ (`Còn 25 phút`)**. Không dùng tràn lan cho tiêu đề phụ hay icon trang trí để bảo toàn phản xạ thị giác: *nhìn thấy màu cam đất là nhìn thấy giá hời và thời gian cần hành động*.
- **Cam ấm trang trí (`#D7834B` — `color.accent.orange`):** Chỉ dùng làm mảng màu nền badge lớn, biểu đồ Pantry hoặc điểm nhấn minh họa; **tuyệt đối không dùng cho chữ nhỏ trên nền sáng**.
- **Hệ màu độ tươi cho Smart Pantry:**
  - `Tươi / Còn dài hạn (> 3 ngày)`: Nền `#EDF3E7` · Chữ/Thanh `#25603C`
  - `Sắp đến hạn (1–3 ngày)`: Nền `#FEF6EE` · Chữ/Thanh `#9A5400`
  - `Quá hạn sử dụng (Use-by passed)`: Nền `#FDF2F0` · Chữ/Thanh `#B42318` (kèm biểu tượng cảnh báo, không khuyến nghị ăn)
  - `Qua ngày nên dùng trước (Best-before passed)`: Nền `#F4EFE6` · Chữ/Thanh `#606E66` (ngôn ngữ hướng dẫn kiểm tra cảm quan thận trọng).

---

## 4. Hệ thống Typography & Nhịp điệu Chữ Tiếng Việt

### 4.1. Phân vai Font chữ (Font Pairing & Roles)

| Vai trò | Font chữ | Trọng lượng (Weights) | Phạm vi áp dụng | Lý do chọn |
|---|---|---|---|---|
| **UI & Body Chính (Canonical)** | **Be Vietnam Pro** | Regular (400), Medium (500), SemiBold (600), Bold (700) | Toàn bộ tiêu đề màn hình, nội dung, nút bấm, nhãn, danh sách, biểu mẫu. | Thiết kế chuyên biệt cho dấu tiếng Việt (`ẩ, ễ, ự`), chiều cao chữ (x-height) thoáng, hiện đại và dễ đọc ở kích thước nhỏ `12–14pt`. |
| **Editorial Accent (`PROPOSED` tùy chọn)** | **Fraunces** hoặc **Newsreader** (hoặc giữ `Be Vietnam Pro ExtraBold` tracking `-0.02em`) | SemiBold (600) / Bold (700) | **Chỉ dùng tối đa ở 3 nơi:** Tiêu đề Onboarding (`SB-001..004`), câu khẩu hiệu trong Banner Hero (`SB-013..015`), và con số tổng kết ở màn Tác động cá nhân (`SB-100`). | Tạo chất "tạp chí ẩm thực / tiệm bánh thủ công" ấm áp mà không làm rối giao diện tác vụ. **Cấm dùng trên thanh điều hướng, form, giá tiền hoặc nút bấm.** |
| **Monospace / Mã định danh** | **JetBrains Mono** hoặc **SF Mono** | Medium (500), Bold (700) | Mã nhận món dự phòng (`DEMO-A125`), mã đơn hàng (`DEMO-001`), payload QR minh họa. | Phân biệt rõ ký tự dễ nhầm (`0` vs `O`, `1` vs `I`), tạo cảm giác vé điện tử / biên lai xác thực đáng tin cậy. |
| **iOS System Chrome** | **SF Pro Text / SF Pro Display** | Semibold (600), Regular (400) | Đồng hồ thanh trạng thái iOS (`16:00`), bàn phím hệ thống iOS, hộp thoại quyền hệ thống (Permission Alert). | Bắt buộc để phần khung hệ thống trông giống iPhone thật 100%. |

### 4.2. Thang chữ (Type Scale) và Quy tắc Số học (`Tabular Numerals`)

| Style Token | Kích thước / Dòng (`pt`) | Weight | Letter Spacing | Quy tắc bắt buộc |
|---|---|---|---|---|
| `type.display.hero` | `30 / 36` | Bold (700) | `-0.02em` | Dùng cho Onboarding, Impact số lớn hoặc tiêu đề thành công. Không quá 2 dòng. |
| `type.title.large` | `26 / 32` | Bold (700) | `-0.015em` | iOS Large Title ở màn gốc của Tab (`Đơn của tôi`, `Tủ thực phẩm`, `Tài khoản`) hoặc tên món trên `SB-034`. |
| `type.title.section` | `20 / 26` | SemiBold (600) | `-0.01em` | Tiêu đề khu vực (`Ưu đãi hôm nay`, `Cần dùng sớm`). |
| `type.title.card` | `16 / 22` | SemiBold (600) | `0` | Tên món ăn trên `OfferCard`, tên cửa hàng, tiêu đề hàng. Tối đa 2 dòng (`line-clamp: 2`). |
| `type.price.hero` | `24 / 30` | Bold (700) | `-0.01em` | Giá Rescue trên màn Chi tiết & Tổng thanh toán. Bắt buộc bật `tabular-nums`. |
| `type.price.card` | `18 / 24` | Bold (700) | `-0.01em` | Giá Rescue trên thẻ ưu đãi. Đi kèm giá gốc gạch ngang `13/18 Regular #606E66` (khi có căn cứ). |
| `type.body.default` | `15 / 22` | Regular (400) | `0` | Mô tả món ăn, hướng dẫn nhận hàng, nội dung thông báo. |
| `type.body.medium` | `15 / 22` | Medium (500) | `0` | Nhãn trường thông tin, dòng tóm tắt biên lai, mục cài đặt. |
| `type.caption.meta` | `13 / 18` | Medium (500) | `0` | Khung giờ nhận (`17:00–18:00`), khoảng cách (`0.8 km`), tên cửa hàng phụ. |
| `type.badge.micro` | `12 / 16` | SemiBold (600) | `+0.01em` | Badge trạng thái (`Còn 3 phần`, `Còn 1 ngày`, `Ảnh minh họa`). Không dùng `ALL CAPS` dài. |
| `type.code.ticket` | `22 / 28` | Bold (700) | `+0.08em` | Mã nhận hàng `DEMO-A125` trên vé QR (`SB-056`, `SB-063`). |

---

## 5. 10 Quy tắc Bố cục Chống Rập Khuôn (Anti-Generic & Anti-Boxitis Laws)

Mọi thiết kế viên và agent khi sửa hoặc tạo mới bất kỳ màn hình nào trong 100 màn phải tuân thủ **10 luật cứng** sau:

1. **Luật "Tối đa 1 lớp thẻ" (Zero Nested Cards):** Không bao giờ đặt một thẻ có viền/nền trắng nằm lọt bên trong một thẻ có viền/nền trắng khác. Nếu một khối biên lai (`SB-053`) cần hiển thị món ăn + giờ nhận + bảng giá, tất cả phải nằm chung trong **một khung biên lai duy nhất** và ngăn cách các phần bằng đường kẻ ngang `1px #E8E2D8` hoặc đường đứt nét `dashed`.
2. **Luật "35% Mặt phẳng mở" (Open Canvas Ratio):** Trên mọi màn hình (trừ màn bản đồ hoặc ảnh toàn màn), ít nhất **35% diện tích vùng nội dung** phải để lộ nền Canvas `#FFFCF6` hoặc mặt phẳng liên tục, không bị chia vụn thành các hộp chữ nhật đóng kín.
3. **Luật "Cấm tiêu đề kép" (No Double Headers):** Nếu thanh điều hướng trên cùng đã có tiêu đề màn hình (ví dụ `Chọn giờ nhận` hoặc `Kiểm tra đặt trước`), phần nội dung bên dưới đi thẳng vào bước tiến độ và dữ liệu — **không lặp lại một dòng H1 khổng lồ có cùng ý nghĩa ngay bên dưới**.
4. **Luật "Phân cấp độ bo góc" (Corner Radius Hierarchy):**
   - `28pt`: Đáy tấm trượt (Bottom Sheet) và mặt phẳng nội dung đè lên ảnh Hero (`SB-034`).
   - `20pt`: Thẻ thực phẩm chính (`OfferCard`), Vé nhận món (`RescueTicket`), Banner Hero.
   - `14pt`: Ô chọn khung giờ (`PickupSlot`), ô nhập liệu (`TextField`), khối cảnh báo (`AllergenNotice`), nhóm cài đặt.
   - `8pt`: Nhãn nhỏ (Tag/Badge), ảnh thu nhỏ (`56×56pt` hoặc `64×64pt`) nằm trong dòng tóm tắt.
   - `999pt (Pill)`: Nút CTA chính, chip lọc (`FilterChip`), thanh tiến độ.
5. **Luật "Không lặp ảnh trên cùng một khung nhìn":** Một màn hình không bao giờ được hiển thị cùng một file ảnh thực phẩm ở 2 vị trí khác nhau (ví dụ: nếu `OfferCard` đầu tiên của `SB-015` là ảnh bánh mì sourdough, thì Banner Hero phía trên phải dùng ảnh tổ hợp nông sản/rau củ tươi hoặc bố cục typography + minh họa thực vật).
6. **Luật "Bất đối xứng có chủ đích trong Khám phá" (Editorial Rhythm):** Danh sách khám phá (`SB-013`, `SB-014`, `SB-015`, `SB-028..032`) không được chỉ là một lưới đều tăm tắp từ trên xuống dưới. Phải kết hợp nhịp điệu: **1 khối Featured / Đang nhận sớm (ngang hoặc lớn)** → **Lưới 2 cột so sánh nhanh** → **Danh sách ngang theo tiệm hoặc khoảng cách**.
7. **Luật "Biên lai & Vé đục lỗ cho Giao dịch" (Perforated Ticket Motif):** Các màn hình `SB-053` (Tóm tắt), `SB-056` (Thành công), `SB-062` (Chi tiết đơn), `SB-063` (Mã QR) phải sử dụng hình thái **Vé Cứu Thực Phẩm (Rescue Pass)** có hai khuyết bán nguyệt (`16pt`) ở hai cạnh bên ngay tại đường ranh giới với vùng mã QR, mã QR căn giữa tuyệt đối trên nền trắng sạch, bên dưới là mã chữ-số monospace cỡ lớn dễ đọc tại quầy.
8. **Luật "Túi bất ngờ khác biệt tức thì với Món cụ thể":**
   - *Món cụ thể (`SB-034`):* Ảnh chụp cận cảnh món ăn thật chiếm 35% chiều cao màn hình.
   - *Túi bất ngờ (`SB-044`, `SB-045`):* Sử dụng thiết kế **Mystery Kraft Bag Hero** (hình ảnh túi giấy/hộp quà thực phẩm kèm con dấu `"Túi bất ngờ · Giá trị ước tính"` và dải tag các nhóm món có thể xuất hiện như `Bánh ngọt`, `Bánh mặn`, `Bánh mì nguyên cám`) để người dùng không bao giờ nhầm lẫn rằng họ đang đặt một món cố định.
9. **Luật "Smart Pantry mang thẩm mỹ Gian bếp ngăn nắp":** Các màn Pantry (`SB-074..090`) không dùng lại `OfferCard` của chợ ưu đãi. Pantry sử dụng **Thẻ Hạn Dùng Ngang (Freshness Row)** với thanh chỉ báo thời gian còn lại (`Expiry Progress Bar`), nhãn phân biệt rõ `Hạn sử dụng (Use by)` và `Nên dùng trước (Best before)`, cùng thao tác trượt/chạm nhanh để đánh dấu `Đã dùng` mà không mang cảm giác mua bán.
10. **Luật "Trạng thái rỗng và lỗi là điểm hướng dẫn, không phải trang cụt":** Không màn hình `State` nào được phép chỉ có một icon nhỏ + 1 câu thông báo giữa màn hình trắng. Mọi màn lỗi/hết hàng/trống (`SB-022`, `SB-046..049`, `SB-057..058`, `SB-067..068`, `SB-073`, `SB-076`, `SB-096`) phải có: (1) Minh họa ngữ nghĩa rõ ràng, (2) Giải thích nguyên nhân cụ thể không đổ lỗi cho người dùng, và (3) Khối hành động cứu vãn trực tiếp trên màn hình (ví dụ: danh sách 2 ưu đãi tương tự còn hàng ngay bên dưới thông báo hết hàng của `SB-046`).

---

## 6. Chiến lược Chuyển động & Tương tác Cao cấp (Selective Motion & Micro-interactions)

Vì mục tiêu cuối cùng là một prototype Figma và bản demo ứng dụng mượt mà, **không rải hiệu ứng đều khắp 100 màn hình**, mà tập trung ngân sách tương tác vào **5 điểm chạm tạo cảm xúc mạnh nhất (Signature Moments)**:

| Điểm chạm (Signature Moment) | Màn hình áp dụng | Hành vi tương tác & Chuyển động (Figma Smart Animate / Demo) | Nơi giữ tĩnh / đơn giản để đối lập |
|---|---|---|---|
| **1. Mở Chi tiết Món từ Khám phá (Hero Card Expand)** | `SB-015` → `SB-034` | Ảnh món ăn từ `OfferCard` mở rộng mượt lên phần Hero đầu trang `SB-034`, tấm thông tin nền kem trượt nhẹ từ dưới lên (`Spring: mass 1, stiffness 300, damping 28`, ~`320ms`). | Chuyển tab dưới đáy (`BottomNav`) đổi tức thì (`Instant` hoặc `Dissolve 120ms`), không trượt ngang gây chóng mặt. |
| **2. Chọn Khung giờ & Số lượng (Tactile Slot Selection)** | `SB-050`, `SB-051` | Khi chạm chọn khung giờ `17:00–18:00`, nền ô chuyển sang xanh rừng `#004337`, icon đồng hồ đổi thành dấu tích tròn trắng, thanh tổng tiền ở đáy cập nhật ngay lập tức (`Ease Out 180ms`). | Các dòng thông tin địa chỉ và điều khoản hủy giữ nguyên vị trí tĩnh, không nhấp nháy. |
| **3. Chốt giữ chỗ → Phát hành Vé Nhận Món (Ticket Issuance Reveal)** | `SB-053` → `SB-055` → `SB-056` | Nút CTA chuyển sang trạng thái `Đang giữ chỗ...` (`SB-055`), sau đó Vé Nhận Món (`SB-056`) trượt lên như một tấm vé vừa in xong kèm huy hiệu xác nhận xanh lá nở nhẹ (`Scale 0.85 → 1.0`, `Spring 350ms`). | Mã QR và mã chữ `DEMO-A125` hiển thị tĩnh tuyệt đối, độ tương phản tối đa để nhân viên quét mã không bị lóa. |
| **4. Bản đồ & Tấm trượt Xem nhanh (Map Pin → Peek Sheet)** | `SB-016` ↔ `SB-017` | Chạm vào ghim giá (`25K`) trên bản đồ làm ghim phóng nhẹ lên (`1.15x`) và đổi sang màu cam đất `#B34021`, đồng thời tấm thẻ xem nhanh (`SB-017`) trượt từ dưới đáy lên mà không làm mất ngữ cảnh bản đồ. | Nền bản đồ không tự xoay hoặc zoom giật cục khi chỉ đổi giữa hai ghim gần nhau. |
| **5. Đánh dấu "Đã dùng" trong Tủ thực phẩm (Pantry Check-off)** | `SB-075` → `SB-086` | Chạm nút `Đã dùng` làm thanh hạn dùng rút gọn, hiện phản hồi xác nhận ấm áp ("Đã dùng kịp thời 1 hộp sữa · Giảm 1 món bỏ phí") trước khi cập nhật danh sách. | Các màn Cài đặt, Chính sách, FAQ (`SB-097..099`) dùng chuyển trang Push iOS tiêu chuẩn, gọn và nhanh. |

> **Quy tắc Accessibility cho Motion:** Mọi trạng thái kết thúc của animation phải đầy đủ thông tin khi xem tĩnh. Khi bật chế độ `Reduce Motion` trên iOS, thay toàn bộ chuyển động `Slide/Spring` bằng `Cross-dissolve ≤ 150ms` hoặc chuyển tức thì.

---

## 7. Kế hoạch Nâng cấp 5 Màn Pilot (Từ v0.5 lên v1.0 khi Owner duyệt)

Bảng dưới đây tóm tắt thay đổi cụ thể cho 5 màn hình pilot để biến chúng thành chuẩn mực (North Star Baseline) trước khi nhân rộng ra 95 màn còn lại:

| Màn hình | Vấn đề ở v0.5 | Thiết kế lại ở v1.0 (`PROPOSED`) |
|---|---|---|
| **`SB-015` · Khám phá** | Ảnh bánh mì ở Hero trùng với Card 1; icon danh mục tự vẽ thô; ảnh croissant tối; thiếu Home Indicator. | (1) Thay ảnh trong Banner Hero bằng ảnh tổ hợp nông sản/bánh tươi khác hoặc bố cục Hero Editorial có nhãn `"Khung giờ vàng 17:00–18:00"`; (2) Thay toàn bộ icon danh mục & tab bar bằng bộ **Phosphor Icons** chuẩn (Duotone cho active, Regular cho inactive); (3) Thêm badge `"Còn 3 phần"` và `"17:00–18:00"` gọn gàng trên góc ảnh `OfferCard`; (4) Bổ sung chuẩn iOS Status Bar + Home Indicator `34pt`. |
| **`SB-034` · Chi tiết món** | Dải kem chặn trên đỉnh ảnh; các khối cửa hàng, giờ nhận, dị ứng đều đóng hộp riêng lẻ. | (1) Cho ảnh `BreadPhoto` tràn **full-bleed** lên sát đỉnh màn hình (`y=0`) dưới Status Bar (có lớp phủ gradient nhẹ bảo vệ chữ giờ/pin và 2 nút tròn kính mờ `Back` / `Heart`); (2) Tấm nội dung bo góc `28pt` đè lên ảnh; (3) Gộp thông tin Cửa hàng + Giờ nhận vào một danh sách phẳng ngăn cách bằng đường kẻ mảnh `1px`, giữ hộp nền ấm riêng cho `AllergenNotice`; (4) Đáy màn hình dùng **Split Sticky Dock** (Trái: `25.000đ · Trả tại quầy` / Phải: Nút `Chọn giờ nhận →`). |
| **`SB-051` · Chọn giờ nhận** | Tiêu đề kép ("Đặt trước" + "Bạn đến nhận lúc mấy giờ?"); 5 hộp bo tròn `radius-24` xếp chồng lên nhau. | (1) Bỏ tiêu đề thừa trên AppBar, dùng thanh tiến độ 2 bước tích hợp ngay trên đầu; (2) Thu gọn `OfferSummary` thành một dải ngang mảnh (`compact strip`) gắn liền với thông tin cửa hàng; (3) Thiết kế các ô `PickupSlot` như những tấm thẻ thời gian có chỉ báo trạng thái rõ ràng (`Đang mở · Còn 1 giờ nữa bắt đầu` vs `Đã đóng khung 15:00–16:00`); (4) Đưa điều khoản hủy xuống ngay trên thanh CTA cố định kèm Home Indicator. |
| **`SB-053` · Tóm tắt đặt trước** | Thẻ lồng trong thẻ (card-in-card); 3 hộp lớn tranh chấp thị giác; tiêu đề kép. | (1) Chuyển toàn bộ phần tóm tắt thành **một tờ Biên Lai Đặt Giữ Chỗ (Unified Rescue Receipt)** duy nhất trên nền kem: phần đầu là món + cửa hàng + khung giờ, ngăn cách bằng đường đứt nét (`dashed line`) với bảng tính tiền (`1 phần: 25.000đ`, `Phí đặt trước: 0đ`, `Cần thanh toán tại quầy: 25.000đ`); (2) Tích hợp nhãn `"Thanh toán trực tiếp tại cửa hàng"` ngay trong chân biên lai; (3) Đặt `AllergenNotice` gọn bên dưới trước nút xác nhận. |
| **`SB-056` · Đặt trước thành công** | QR bị lệch trái trong hộp xanh; icon tích quá nhỏ; có nút `< SaveBite` sai logic hoàn tất. | (1) Bỏ nút `<` quay lui ở góc trái, thay bằng nút đóng `×` hoặc hoàn tất về trang chủ; (2) Tạo **Header xác nhận giàu cảm xúc** (Huy hiệu tích xanh rừng `#004337` nổi bật + tiêu đề `"Đã giữ 1 phần cho bạn!"` + phụ đề `"Hẹn gặp bạn tại Tiệm Bánh A lúc 17:00–18:00"`); (3) Thiết kế **Vé Nhận Món (Perforated Pickup Pass)** với khuyết tròn hai bên hông, **mã QR căn giữa tuyệt đối** trong khung trắng chuẩn quét, mã dự phòng `DEMO-A125` bằng font Monospace lớn ở ngay dưới, kèm 2 nút hành động: `Xem đường đi` (Secondary) và `Về trang Khám phá` (Primary). |
