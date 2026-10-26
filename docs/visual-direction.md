# Định hướng Nghệ thuật & Ngôn ngữ Thị giác (Visual DNA)

Nguồn chuẩn cho Art Direction, Visual Hierarchy, Composition và quy tắc chống rập khuôn (anti-generic) trên toàn bộ 100 màn hình SaveBite. Đọc cùng [router](README.md), [design system](design-system.md), [iOS guidelines](ios-guidelines.md), [chiến lược asset](asset-strategy.md) và [ma trận 100 màn](screen-art-direction.md).

> **Trạng thái phê duyệt (`DEC-011`):** Toàn bộ 5 màn pilot v0.5 trên file cũ đã được xóa/nghỉ hưu. Định hướng **Art Direction v1.0 (`CONFIRMED` theo `DEC-011`)** trong tài liệu này là chuẩn bắt buộc để thiết kế mới hoàn toàn **10 màn hình đại diện Phase 1** (`SB-002`, `SB-015`, `SB-016`, `SB-019`, `SB-034`, `SB-051`, `SB-053`, `SB-056`, `SB-075`, `SB-091`) trên file Figma mới [SaveBite-V2 (`7suZz9C8oL5zV2NMxlsIVI`)](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1).

---

## 1. Bài học Phê bình từ Bản Pilot v0.5 Đã Nghỉ Hưu (Design Critique Lessons)

Dựa trên đánh giá 5 màn hình pilot v0.5 lịch sử (`SB-015`, `SB-034`, `SB-051`, `SB-053`, `SB-056` — hiện đã xóa để làm mới từ đầu trên `SaveBite-V2`):

### 1.1. Những điểm v0.5 đã làm đúng (Kế thừa sang v1.0)
- **Màu sắc thương hiệu có gốc rễ đúng ngành:** Sự kết hợp giữa xanh rừng đậm (`#004337`), nền kem ấm (`#FFFCF6`) và điểm nhấn giá cam đất (`#B34021`) tạo cảm giác thực phẩm bền vững, ấm áp, tránh được màu xanh neon công nghiệp.
- **Độ tương phản và khả năng đọc tiếng Việt:** Font `Be Vietnam Pro` hiển thị dấu tiếng Việt rõ, 13 cặp chữ/nền đều đạt chuẩn WCAG AA (`≥ 4.74:1`), không dùng chữ nhỏ màu cam nhạt trên nền sáng.
- **Tính trung thực nghiệp vụ:** Tôn trọng tuyệt đối nguyên tắc *Reserve & Pay at Pickup*, hiển thị rõ cảnh báo dị ứng `UNKNOWN` và nhãn dữ liệu mô phỏng.
- **Cấu trúc kỹ thuật Figma sạch:** Frame native editable 100%, dùng Auto Layout, biến màu/spacing và component properties không bị detach.

### 1.2. 7 vấn đề thẩm mỹ lịch sử của v0.5 bắt buộc loại bỏ hoàn toàn trên v1.0

| # | Vấn đề trên Pilot v0.5 (Đã nghỉ hưu) | Biểu hiện cụ thể cần tránh | Tác động đến cảm nhận sản phẩm |
|---|---|---|---|
| **1** | **Hội chứng "Boxitis" (Lạm dụng thẻ viền bo tròn)** | Trên `SB-051` và `SB-053` cũ, mọi thông tin (progress, tóm tắt món, ngày nhận, từng khung giờ, thanh toán tại quầy, dị ứng) đều bị nhốt vào các hộp full-width `radius: 24px`, viền `#E8E2D8` xếp chồng lên nhau. Trên `SB-053` cũ, thẻ `OfferSummary` còn bị lồng bên trong một thẻ trắng lớn hơn (card-in-card). | Giao diện nặng nề, giống form web/SaaS dựng tự động bằng template AI; mắt người dùng không biết đâu là tâm điểm vì hộp nào cũng có trọng lượng thị giác ngang nhau. |
| **2** | **Thiếu chuẩn iOS System Chrome thực thụ** | Thanh trạng thái (status bar) dùng chữ `16:00` bằng font `Be Vietnam Pro` màu xanh đen cùng icon sóng/pin tự vẽ thô; thiếu hoàn toàn **iOS Home Indicator** (`134×5pt`) ở đáy; trên `SB-034` cũ, ảnh món ăn bị chặn bởi một dải nền kem cứng phía trên thay vì tràn full-bleed lên đỉnh màn hình. | Mất ngay cảm giác "ảnh chụp ứng dụng iPhone thật"; trông như bản vẽ wireframe màu hoặc giao diện web mobile thu nhỏ. |
| **3** | **Lặp tiêu đề kép (Double-Header Redundancy)** | Ở `SB-051` cũ, ngay dưới thanh `AppBar` có chữ **"Đặt trước"** là tiêu đề lớn **"Bạn đến nhận lúc mấy giờ?"**. Ở `SB-053` cũ, ngay dưới **"Xác nhận"** là **"Kiểm tra đặt trước"**. Nút Back lại dùng vòng tròn viền 48×48px quá to cho mọi màn con. | Lãng phí 100–120pt chiều cao quý giá ở đầu màn hình, đẩy nội dung quan trọng xuống dưới và làm bố cục bị dồn nén. |
| **4** | **Màn hình Thành công (`SB-056`) thiếu cảm xúc và lệch bố cục** | Trên `SB-056` cũ: (1) Icon dấu tích xanh trên đỉnh quá nhỏ và nhạt nhòa; (2) Mã QR bị **căn lề trái lệch hẳn sang một bên** bên trong khung nền xanh nhạt `#EDF3E7`, để trống một khoảng vô duyên bên phải trong khi mã `DEMO-A125` ở dưới lại căn giữa; (3) Màn hình hoàn tất đơn hàng nhưng góc trên bên trái vẫn có nút `< SaveBite` như một trang form đang đi dở. | Khoảnh khắc quan trọng nhất của luồng đặt giữ chỗ (nhận vé cứu thực phẩm) bị biến thành một hộp thông tin khô khan và lỗi căn chỉnh thị giác. |
| **5** | **Trùng lặp ảnh ngay trên cùng một màn & lệch ánh sáng** | Trên `SB-015` cũ, bức ảnh bánh mì sourdough ở banner hero phía trên được **dùng lặp lại nguyên xi** ở thẻ `OfferCard` đầu tiên ngay bên dưới (cách nhau chưa đầy 50px). Trong khi đó, ảnh bánh mì sáng rực ánh nắng sớm, còn ảnh bánh sừng bò cũ bên cạnh lại chụp trong phòng tối, dính lưng ghế đen phía sau. | Lộ rõ cảm giác "mock thiếu tài nguyên"; hai thẻ sản phẩm đứng cạnh nhau nhưng không thuộc cùng một thế giới hình ảnh. |
| **6** | **Iconography tự vẽ thiếu đồng nhất** | Bộ 4 icon danh mục trên `SB-015` cũ (`Tất cả`, `Bánh mì`, `Đồ ăn sẵn`, `Rau củ`) dùng nét vẽ tự dựng rời rạc (hình rau củ giống cỏ 4 lá/đám mây, ổ bánh mì là hình bầu dục gạch 3 nét), độ dày nét và tỷ lệ lấp đầy không khớp với icon thanh điều hướng đáy. | Làm giảm độ sang trọng và tính chuyên nghiệp của toàn bộ màn hình Khám phá. |
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

## 7. Định hướng Thiết kế Chi tiết cho 10 Màn Đại diện Phase 1 (`DEC-011`)

Bảng dưới đây quy định kiến trúc thị giác bắt buộc cho **10 màn hình North-Star đại diện** trên khung **iPhone 15 (`393×852pt`, Dynamic Island)** tại file `7suZz9C8oL5zV2NMxlsIVI`:

| Màn hình | Archetype | Tâm điểm thị giác (Focal Point) & Quy cách Thiết kế v1.0 |
|---|---|---|
| **`SB-002` · Onboarding 1** | `A1 · Brand & Story Entry` | (1) Nền `#FFFCF6` thoáng; 55% không gian trên là **Editorial Micro-UI Card Collage** trên vòm tròn `#EDF3E7` kết hợp ảnh bánh mì `food-sourdough-461060` + thẻ giá `25.000đ · Nhận 17:00–18:00` nghiêng nhẹ sống động; (2) Tiêu đề Display `30/36 Bold` giàu cảm xúc (*"Cứu món ngon cuối ngày, nhẹ ví mỗi chiều tan học"*); (3) Đáy gồm `PageDots (1/3)`, nút `Tiếp tục` (`#004337`) và nút `Bỏ qua` góc trên phải. |
| **`SB-015` · Khám phá** | `A3 · Editorial Market Discovery` | (1) `BrandHeader` (`Đà Nẵng · Khu học xá ▾`) + `SearchTrigger`; (2) 4 `CategoryTile` dùng **Phosphor Icons Duotone** (`Tất cả`, `Bánh mì`, `Bữa ăn`, `Rau củ`); (3) **Featured Hero Banner** nền `#004337` kết hợp ảnh nông sản `food-veggie-2255935` (không trùng ảnh Card 1!) và nhãn `"Khung giờ vàng 16:00–18:00"`; (4) Lưới 2 cột `OfferCard` (`Bánh mì men tự nhiên 25.000đ` — `food-sourdough-461060` & `Bánh sừng bò bơ Pháp 30.000đ` — `food-croissant-3892469`) + 1 hàng ngang `OfferListRow` (`Cơm gà áp chảo & rau củ 35.000đ` — `food-meal-1640777`); (5) `BottomNav` (`83pt`) + `iOSHomeIndicator`. |
| **`SB-016` · Bản đồ** | `A4 · Spatial Map Explorer` | (1) Bản đồ vector tùy biến `MapCanvas` tông ấm (`#F3EFE6` đất, `#E2ECE4` công viên, `#CFE2E0` sông Hàn, `#FFFFFF` đường lớn) chiếm trọn màn hình quanh Khu học xá Đà Nẵng; (2) Các **Ghim Giá `MapPricePin`** (`25.000đ` đang active màu cam đất `#B34021`, `30.000đ`, `35.000đ` màu `#004337`); (3) Thanh tìm kiếm + chuyển đổi `Danh sách / Bản đồ` kính mờ nổi ở trên; (4) Thẻ xem nhanh `MapPeekCard` (`Bánh mì men tự nhiên · 450m · Nhận 17:00–18:00`) trượt nhẹ phía trên `BottomNav`. |
| **`SB-019` · Tìm kiếm** | `A5 · Search & Input Configurator` | (1) Thanh `SearchField` đang focus (viền `#004337 2pt`, con trỏ nhấp nháy, nút `Hủy` bên phải); (2) Cụm **Tìm kiếm gần đây** dạng chip gọn (`bánh mì men tự nhiên`, `cơm chiều dưới 35k`, `rau củ tươi`) + **Lối tắt theo khung giờ & ngân sách** (`Dưới 30.000đ`, `Nhận ngay 17:00–18:00`, `Cách trường < 500m`); (3) Đáy màn hình hiển thị **Bàn phím iOS QWERTY Tiếng Việt chuẩn (`291pt`)** kèm thanh gợi ý từ và `iOSHomeIndicator`. |
| **`SB-034` · Chi tiết món** | `A6 · Immersive Offer Showcase` | (1) Ảnh `food-sourdough-461060` tràn **full-bleed** lên sát đỉnh màn hình (`393×300pt`, `y=0`) dưới `iOSStatusBar (Light)` kèm lớp scrim bảo vệ và 2 nút kính mờ `Back` / `Heart`; (2) Tấm nội dung `#FFFCF6` bo góc `28pt` đè lên ảnh; (3) Tiêu đề + Giá `25.000đ` + Badge `Còn 3 phần`; thông tin `Tiệm Bánh A` và khung giờ `17:00–18:00` trình bày dạng hàng phẳng ngăn cách bằng đường kẻ mảnh `1pt #E8E2D8`; hộp ấm riêng cho `AllergenNotice (UNKNOWN)`; (4) Đáy màn hình là **Sticky Split Dock** (Trái: `25.000đ · Trả tại quầy` / Phải: Nút `Chọn giờ nhận →`). |
| **`SB-051` · Chọn giờ nhận** | `A7 · High-Trust Transactional` | (1) `PushNavBar` (`Chọn giờ nhận`) + `ReservationProgress (Bước 1/2)` tích hợp gọn (không lặp tiêu đề kép); (2) Dải tóm tắt món gọn (`OfferCompactStrip`: ảnh vuông `56×56pt` + `Bánh mì men tự nhiên · 1 phần · 25.000đ`); (3) Thẻ khung giờ **`17:00–18:00 · Đang mở`** nền xanh rừng `#004337` chữ trắng (kèm badge `"Còn 1 giờ nữa bắt đầu"`) đối lập rõ với khung **`15:00–16:00 · Đã qua giờ`** bị khóa; (4) Địa chỉ nhận phẳng + điều khoản hủy trước `17:00` + Sticky CTA `Tiếp tục`. |
| **`SB-053` · Tóm tắt đặt trước** | `A7 · Unified Rescue Receipt` | (1) `PushNavBar` (`Kiểm tra đặt trước`) + `ReservationProgress (Bước 2/2)`; (2) **Một tờ Biên Lai Đặt Giữ Chỗ (`UnifiedReceiptCard`) duy nhất** (tuyệt đối không lồng card trong card): phần đầu là món + `Tiệm Bánh A` + khung giờ `17:00–18:00`, ngăn cách bằng đường đứt nét (`dashed rule`) và 2 khuyết vé nhẹ với bảng tính tiền (`1 phần × 25.000đ`, `Phí đặt giữ chỗ: 0đ`, `Cần thanh toán tại quầy: 25.000đ`); (3) `AllergenNotice (UNKNOWN)` bên dưới biên lai + Sticky CTA `Đặt giữ chỗ (demo)`. |
| **`SB-056` · Đặt trước thành công** | `A7 · Perforated Pickup Pass` | (1) Bỏ nút `<` quay lui sai logic, dùng nút đóng `×` góc phải; (2) **Celebration Header** giàu cảm xúc (Huy hiệu tích xanh rừng `#004337` + tiêu đề `"Đã giữ 1 phần cho bạn!"` + phụ đề `"Hẹn gặp bạn tại Tiệm Bánh A lúc 17:00–18:00"`); (3) **Vé Nhận Món Đục Lỗ (`PerforatedPickupPass`)** với 2 khuyết bán nguyệt `16pt` hai bên hông, **mã `DemoQR` căn giữa tuyệt đối** trong khung trắng chuẩn quét, mã dự phòng `DEMO-A125` bằng font `JetBrains Mono Bold 22pt` ngay bên dưới; (4) Hai nút hành động: `Xem chỉ đường` (Secondary) và `Về trang Khám phá` (Primary). |
| **`SB-075` · Smart Pantry** | `A8 · Calm Kitchen Inventory` | (1) `LargeTitleBar` (`Tủ thực phẩm` + nút `+ Thêm món`); (2) **Thanh Tổng quan Độ tươi (`FreshnessSummaryBanner`)**: `2 cần dùng sớm (48h)` · `4 còn hạn tốt` · `1 quá hạn`; (3) Dải chip vị trí lưu trữ (`Tất cả (7)`, `Ngăn mát (4)`, `Kệ khô (3)`); (4) Danh sách `PantryItemRow` mang thẩm mỹ gian bếp ngăn nắp (không có giá tiền/nút mua): mỗi hàng có icon danh mục pastel, nhãn phân biệt rõ `Hạn sử dụng (Use by)` vs `Nên dùng trước (Best before)`, **Thanh tiến độ hạn dùng (`Expiry Progress Bar`)** theo màu ngữ nghĩa (`#9A5400` sắp hết hạn, `#25603C` còn tươi, `#B42318` quá hạn không khuyến nghị ăn) và nút chạm nhanh `Đã dùng`; (5) `BottomNav` (Tab 3 active). |
| **`SB-091` · Tài khoản** | `A9 · Hub & Impact Dashboard` | (1) `LargeTitleBar` (`Tài khoản`); (2) **Thẻ Hồ sơ Sinh viên (`ProfileHeaderCard`)**: Avatar chữ cái `MA` (`Minh Anh · Khu học xá ĐH Đà Nẵng`) + huy hiệu khu vực ưu tiên; (3) **Thẻ Điểm nhấn Tác động Thực chứng (`ImpactSummaryCard` nền `#004337`)**: hiển thị `"3 phần thực phẩm đã nhận thành công"` và `"4 món trong Pantry dùng kịp hạn"` (tuân thủ `D-016`, không bịa số kg CO₂); (4) Danh sách cài đặt kiểu **iOS Inset Grouped List** trên nền `#F4EFE6` (`Khu vực thường dùng`, `Nhắc lịch nhận & hạn Pantry`, `Quyền riêng tư & dữ liệu cục bộ`, `Trợ giúp & Chính sách an toàn thực phẩm`); (5) `BottomNav` (Tab 4 active). |
