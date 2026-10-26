# Chuẩn Thiết kế iPhone-Native & Hệ thống iOS (Apple HIG)

Tài liệu quy định tiêu chuẩn khung thiết bị iPhone, thành phần hệ thống (System Chrome), vùng an toàn (Safe Areas), điều hướng và mẫu tương tác iOS cho toàn bộ 100 màn hình SaveBite. Đọc cùng [router](README.md), [visual direction](visual-direction.md), [design system](design-system.md) và [chiến lược asset](asset-strategy.md).

---

## 1. Thiết bị Đích (Target Device) Đã Khóa Theo `DEC-011`

### 1.1. Chuẩn Khung Thiết bị Hiện hành (`393×852pt` — iPhone 15 Standard) vs. Pilot Cũ Đã Nghỉ Hưu

| Tiêu chí | Pilot v0.5 Cũ (`RETIRED` theo `DEC-011`) | Chuẩn Chính thức v1.0 (`CONFIRMED` theo `DEC-011`) |
|---|---|---|
| **Mẫu iPhone tham chiếu** | iPhone 13 / iPhone 14 (`390×844pt` @3x) — đã xóa/nghỉ hưu. | **iPhone 15 / iPhone 16 Standard (`393×852pt` @3x)** |
| **Đặc điểm phần cứng đầu màn** | Vẽ giả `40–44pt`, thiếu notch/Dynamic Island. | **Dynamic Island (`59pt` top safe area)** — khớp 100% với **Apple Official iOS 17 / iOS 18 Figma UI Kit**. |
| **Bottom Safe Area** | Thiếu biểu tượng Home Indicator; khoảng trống đáy `24pt` tự đặt. | **`34pt` chuẩn iOS** chứa thanh **Home Indicator (`134×5pt`)** cách đáy `8pt`. |
| **Kiểm tra co giãn (Responsive Stress)** | Kiểm ở `360×844` và `430×844`. | Kiểm ở **`375×812pt`** (iPhone SE/mini), **`393×852pt`** (chuẩn) và **`430×932pt`** (iPhone 15/16 Pro Max). |
| **Ràng buộc trong `scripts/validate.py`** | Đã nghỉ hưu cùng file cũ `NLTv70kDZ2i3HpOnOKQCDY`. | Khóa chuẩn `TARGET = '7suZz9C8oL5zV2NMxlsIVI'`, kích thước chuẩn `(393, 852)` và tập 10 màn đại diện Phase 1. |

### 1.2. Quy trình Thực thi Chuẩn iPhone 15 trên File Mới `7suZz9C8oL5zV2NMxlsIVI`
1. **Quyết định `DEC-011` đã khóa chuẩn `iPhone 15 (393×852pt, Dynamic Island)`:**
   - Mọi frame màn hình thuộc 10 màn Phase 1 (`SB-002`, `SB-015`, `SB-016`, `SB-019`, `SB-034`, `SB-051`, `SB-053`, `SB-056`, `SB-075`, `SB-091`) và 90 màn tiếp theo bắt buộc khởi tạo ở kích thước **`393×852pt`**.
   - Đặt `iOSStatusBar (Dynamic Island, 393×59pt)` ở đỉnh và `iOSHomeIndicator (393×34pt)` ở đáy mọi màn hình.
   - Sau khi ghi lên Figma bằng `use_figma`, xuất bộ ảnh `tracking/evidence/*.png` và cập nhật `tracking/evidence/figma-readback.json` + `tracking/evidence/qa.json` khớp với `scripts/validate.py`.

---

## 2. Quy chuẩn iOS System Chrome (Bắt buộc trên mọi màn hình)

Mọi màn hình từ `SB-001` đến `SB-100` phải trông như một ảnh chụp màn hình thực tế từ iPhone, tuyệt đối không để trống đỉnh/đáy màn hình như một trang web.

### 2.1. Thanh trạng thái iOS (Status Bar & Dynamic Island)
- **Nguồn duy nhất được phép:** Component chính thức từ **Apple Design Resources — iOS UI Kit trên Figma Community**.
- **Cấu trúc chi tiết (`59pt` chiều cao trên iPhone 15 / `47pt` trên iPhone 14):**
  - **Bên trái:** Thời gian hệ thống dùng font `SF Pro Text Semibold 17pt`, căn giữa theo trục ngang vùng tai trái. Trong bộ màn hình SaveBite, thống nhất hiển thị **`16:00`** (khớp với đồng hồ fixture buổi chiều khi các khung giờ cứu thực phẩm `17:00–18:00` chuẩn bị mở) hoặc `9:41` chuẩn Apple nếu ở màn Onboarding/Account độc lập.
  - **Chính giữa (với target iPhone 15):** Viên thuốc **Dynamic Island** kích thước `126×37pt`, bo tròn `radius: 100pt`, màu đen tuyền `#000000`, cách mép trên `11pt`. **Quy tắc cứng:** Không biến Dynamic Island thành banner quảng cáo hay nhét nút bấm của app vào vùng này.
  - **Bên phải:** Bộ 3 biểu tượng vector chuẩn Apple gồm **Cellular Signal (4 vạch)**, **Wi-Fi**, và **Battery** (đầy hoặc 80%, không để pin đỏ yếu gây lo lắng).
- **Nghiêm cấm:**
  - Dùng font `Be Vietnam Pro` để gõ giờ `16:00` trên thanh trạng thái.
  - Tự vẽ cột sóng bằng các hình chữ nhật thô hoặc dùng ký tự Unicode/emoji (`📶`, `🔋`).
  - Đặt bất kỳ nút bấm nào (`Back`, `Favorite`, `Close`) đè lên vùng `0–54pt` của thanh trạng thái.

### 2.2. Quy tắc Tương phản Thanh trạng thái (Light vs. Dark Status Bar)

| Ngữ cảnh nền phía dưới Status Bar | Biến thể Status Bar phải dùng | Xử lý bảo vệ độ tương phản (Legibility Guard) | Màn hình áp dụng tiêu biểu |
|---|---|---|---|
| **Nền sáng:** Kem `#FFFCF6`, Trắng `#FFFFFF`, Xanh nhạt `#EDF3E7`, Bản đồ sáng `#F3EFE6` | **`Status Bar / Dark Content`** (Chữ và icon màu đen `#000000`) | Khi cuộn nội dung qua dưới Status Bar, áp dụng nền kính mờ `rgba(255, 252, 246, 0.88)` + `Background Blur 20px`. | Hầu hết các màn: `SB-015`, `SB-051`, `SB-053`, `SB-056`, `SB-060`, `SB-075`, `SB-091`... |
| **Nền tối hoặc Ảnh tràn viền (Full-Bleed Media):** Xanh rừng `#004337`, Thư viện ảnh đen, hoặc Ảnh món ăn có vùng đỉnh sẫm màu | **`Status Bar / Light Content`** (Chữ và icon màu trắng `#FFFFFF`) | Với ảnh thực phẩm sáng màu tràn viền (`SB-034`, `SB-038`), **bắt buộc** phủ một lớp gradient bảo vệ ở đỉnh ảnh (`height: 104pt`, từ `rgba(0,0,0,0.45)` ở `y=0` giảm về `rgba(0,0,0,0)` ở `y=104pt`) nếu dùng chữ trắng, HOẶC dùng biến thể `Dark Content` nếu vùng đỉnh ảnh được giữ sáng đồng nhất (đảm bảo contrast `≥ 4.5:1`). | `SB-001` (Splash xanh rừng), `SB-034` (Chi tiết món), `SB-035` (Lightbox ảnh), `SB-038` (Chi tiết cửa hàng). |
| **Khi mở iOS Modal Sheet dạng Card (Stacked Sheet)** | **`Status Bar / Light Content`** trên nền tối phía sau tấm thẻ bị thu nhỏ | Nền màn hình gốc phía sau lùi nhẹ và phủ lớp tối `rgba(0,0,0,0.4)`, đẩy chữ Status Bar thành màu trắng. | `SB-023` (Bộ lọc tổng hợp), `SB-070` (Xác nhận hủy đơn dạng sheet). |

### 2.3. Thanh chỉ báo Home (Home Indicator & Bottom Safe Area)
- **Kích thước chuẩn:** Vùng an toàn đáy cao **`34pt`**. Bên trong chứa thanh ngang `134×5pt`, bo tròn `100pt`, nằm cách mép dưới màn hình `8pt`, căn giữa theo chiều ngang.
- **Màu sắc:** `#000000` (độ mờ `35%–80%` trên nền sáng `#FFFCF6`/`#FFFFFF`) hoặc `#FFFFFF` (độ mờ `60%–90%` trên nền tối `#004337`).
- **Quy tắc khoảng cách:**
  - Với màn có **Bottom Tab Bar**: Thanh Tab Bar cao tổng cộng **`83pt`** = `49pt` (vùng chứa 4 tab icon + chữ) + `34pt` (vùng Home Indicator bên dưới).
  - Với màn có **Sticky Bottom CTA Dock**: Khoảng cách từ đáy nút CTA (`height: 52pt`) xuống mép dưới cùng của màn hình tối thiểu là **`34pt`** (nút kết thúc ở `y = height - 34pt` hoặc `height - 38pt`, bên dưới là Home Indicator).

---

## 3. Cấu trúc Điều hướng Chuẩn iOS (Native Navigation Architecture)

### 3.1. 4 Mẫu Thanh Điều hướng Đầu trang (Top Navigation Patterns)

Không dùng một kiểu `AppBar` duy nhất cho cả 100 màn hình. Áp dụng đúng 1 trong 4 mẫu sau tùy theo cấp độ phân cấp thông tin (IA):

| Mẫu Top Bar | Chiều cao (không tính Status Bar) | Cấu trúc & Thành phần | Màn hình áp dụng |
|---|---|---|---|
| **1. Brand & Location Discovery Header** | `56pt` (+ `52pt` thanh Search bên dưới) | Trái: Wordmark `SaveBite` + cụm chọn khu vực `Đà Nẵng · Khu học xá ▾` (chạm để mở `SB-018`). Phải: Nút chuông thông báo `44×44pt` (mở `SB-095`) và nút Yêu thích `44×44pt` (mở `SB-033`). | `SB-013`, `SB-014`, `SB-015`. |
| **2. iOS Large Title Root Header** | `44pt` (compact bar) + `52pt` (Large Title) = `96pt` | Hàng trên chứa nút phụ (ví dụ `+ Thêm món`, `Lịch sử`, `Cài đặt`); hàng dưới là tiêu đề lớn `26–30pt Bold` căn trái. Khi cuộn lên, tiêu đề thu nhỏ vào giữa hàng `44pt`. | Màn gốc của các Tab: `SB-060` (Đơn của tôi), `SB-075` (Tủ thực phẩm), `SB-091` (Tài khoản), `SB-095` (Thông báo). |
| **3. Standard Push Navigation Bar** | `44pt` (hoặc `52pt` thoáng) | Trái: Nút Back chuẩn iOS (`ChevronLeft 24pt` hoặc nút tròn nhẹ `40×40pt` vùng chạm `48×48pt`). Giữa: Tiêu đề màn hình `17pt SemiBold` căn giữa. Phải: Hành động ngữ cảnh tùy chọn (`Đặt lại`, `Trợ giúp`, `Lưu`). **Không lặp lại tiêu đề H1 giống hệt ngay bên dưới.** | Luồng đặt giữ chỗ (`SB-051..054`), Chi tiết đơn (`SB-062`), Cài đặt & Hồ sơ (`SB-092..099`), Thêm/sửa Pantry (`SB-077..082`). |
| **4. Full-Bleed Media Overlay Bar** | Ảnh cao `280–320pt` tính từ `y=0` | Không có thanh nền đặc chặn đầu trang. Hai nút tròn hiệu ứng kính mờ (`40×40pt`, hit area `48×48pt`, nền `rgba(255,252,246,0.88)`, `blur(16px)`) gồm `Back` (trái) và `Yêu thích / Chia sẻ` (phải) đặt tại `y = status_bar_height + 8pt`. | `SB-034` (Chi tiết món cụ thể), `SB-038` (Chi tiết cửa hàng), `SB-044` (Chi tiết túi bất ngờ), `SB-046..049`. |

### 3.2. Quy tắc Nút Quay lại (Back Action) vs. Nút Đóng (Close / Done)
- **Màn hình đi sâu theo luồng (Push Screen):** Dùng mũi tên `<` ở góc trên bên trái (`SB-034`, `SB-051`, `SB-053`, `SB-062`).
- **Màn hình Tấm trượt (Bottom Sheet / Modal):** Dùng thanh kéo `Grabber` (`36×5pt`, màu `#C8C2B8`) ở đỉnh tấm trượt kèm nút `Đóng` hoặc icon `×` (`44×44pt`) ở góc phải (`SB-023..027`, `SB-036`, `SB-037`, `SB-045`, `SB-050`).
- **Màn hình Hoàn tất Giao dịch (`SB-056` Đặt trước thành công, `SB-071` Hủy đơn thành công):** **Tuyệt đối không đặt nút `<` quay về bước form xác nhận trước đó** trên giao diện thực tế, vì đơn đã được chốt trạng thái. Sử dụng nút `×` (Đóng về màn Khám phá/Đơn hàng) hoặc các nút điều hướng rõ nghĩa ở dưới (`Xem đơn của tôi` / `Khám phá tiếp`). *(Lưu ý kỹ thuật: Nếu bài kiểm tra prototype của pilot v0.5 yêu cầu 1 hotspot quay lại để chấm điểm luồng lùi, có thể gắn vào nút phụ hoặc hành động xem lại tóm tắt đơn, nhưng không hiển thị như một thanh tiêu đề `< SaveBite` gây hiểu nhầm).*

### 3.3. Thanh Tab Đáy (iOS Bottom Tab Bar — 4 Tabs Chuẩn `D-002`)
- **4 Tab cố định:**
  1. `Khám phá` (Icon: `Compass` hoặc `Storefront`)
  2. `Đơn của tôi` (Icon: `Receipt` hoặc `ShoppingBagOpen`)
  3. `Tủ thực phẩm` (Icon: `Refrigerator` / `ArchiveBox` / `Leaf`)
  4. `Tài khoản` (Icon: `UserCircle`)
- **Trạng thái Active vs. Inactive:**
  - **Active:** Icon kiểu **Filled / Duotone** màu `#004337`, nhãn chữ `11pt SemiBold #004337` (hoặc kèm viên thuốc nền `#EDF3E7` ôm nhẹ quanh icon để tăng độ nhận diện).
  - **Inactive:** Icon kiểu **Regular Outline (`1.75pt`)** màu `#606E66`, nhãn chữ `11pt Medium #606E66`.
- **Nơi hiển thị Bottom Tab Bar:** Chỉ hiển thị trên các màn hình cấp 1 của 4 nhánh (`SB-013`, `SB-014`, `SB-015`, `SB-016`, `SB-060`, `SB-061`, `SB-073`, `SB-075`, `SB-076`, `SB-091`). **Ẩn hoàn toàn** khi người dùng đi vào Chi tiết món (`SB-034`), Đặt giữ chỗ (`SB-050..059`), Mã QR (`SB-063`), hoặc Nhập liệu biểu mẫu để nhường chỗ cho **Sticky Action Dock** hoặc **Bàn phím**.

---

## 4. Vùng Chạm, Cuộn Nội dung, Bàn phím & Tấm trượt

### 4.1. Kích thước Vùng chạm (Touch Targets) & Lưới Khoảng cách
- **Chuẩn Apple HIG tối thiểu:** `44×44pt` cho mọi phần tử tương tác.
- **Chuẩn QA SaveBite (`scripts/validate.py`):** Mọi hotspot được kết nối trong prototype phải đạt tối thiểu **`48×48pt`** để vượt qua cả tiêu chuẩn iOS lẫn Android/WCAG AAA. Nếu biểu tượng thị giác nhỏ hơn (ví dụ icon `20×20pt` hoặc `24×24pt`), frame bao quanh (`hit target container`) vẫn phải mở rộng đủ `48×48pt` bằng padding trong suốt.
- **Lề ngang chuẩn (Horizontal Margins):**
  - Màn hình danh sách / biểu mẫu tiêu chuẩn: **`20pt`** hai bên (`x = 20` đến `x = 373` trên màn `393pt`, hoặc `x = 20` đến `x = 370` trên màn `390pt`).
  - Màn hình lưới 2 cột ở chiều rộng hẹp (`360pt`–`375pt`): Cho phép giảm lề ngoài xuống **`16pt`** và khoảng cách giữa 2 cột (`column gap`) là **`12pt`** để mỗi thẻ luôn rộng tối thiểu `158–169pt`, không làm gãy chữ giá tiền.

### 4.2. Xử lý Bàn phím iOS (Keyboard States)
Các màn hình có trọng tâm là nhập liệu đang hoạt động (`SB-006` Đăng ký, `SB-008` Đăng nhập, `SB-019` Tìm kiếm đang gõ, `SB-020` Gợi ý tìm kiếm, `SB-077` Nhập món Pantry) cần tuân thủ:
- Trên ít nhất các màn tìm kiếm trực tiếp (`SB-019`, `SB-020`), **hiển thị bàn phím tiếng Việt / QWERTY chuẩn iOS** ở đáy màn hình (`chiều cao 291pt` bao gồm cả Home Indicator + thanh gợi ý từ `44pt` nếu có).
- Khi bàn phím mở, **nút CTA chính hoặc danh sách gợi ý phải tự động đẩy lên nằm ngay phía trên bàn phím**, tuyệt đối không để bàn phím che khuất ô đang nhập (focused input field) hoặc thông báo lỗi validation.

### 4.3. Quy tắc Cuộn (Scroll Viewport) và Thanh Đáy Cố định (Sticky Dock)
- **Phân tách lớp cố định và lớp cuộn:** Trong Figma, mỗi màn hình có nội dung dài phải tách rõ:
  1. `TopChrome` (Fixed: Status Bar + Nav Bar)
  2. `ScrollViewport` (Vertical scrolling: chứa toàn bộ nội dung chính, có `padding-bottom: 24pt` để phần tử cuối không dính sát vào thanh đáy)
  3. `BottomChrome` (Fixed: `BottomTabBar` hoặc `StickyActionDock` + `HomeIndicator`).
- **Tín hiệu cuộn (Scroll Affordance):** Khi nội dung dài vượt khung nhìn, thiết kế sao cho phần tử gần mép dưới bị lộ một phần hợp lý (peek) hoặc thanh đáy có viền mảnh `#E8E2D8` + lớp mờ nhẹ để người dùng hiểu vẫn còn nội dung bên dưới.

---

## 5. Tài nguyên Apple Chính thức & Tuân thủ Bản quyền

| Tài nguyên | Nguồn chính thức | Quy tắc sử dụng & Bản quyền trong SaveBite |
|---|---|---|
| **Apple Design Resources — iOS 17 / iOS 18 UI Kit** | [Apple Design Resources](https://developer.apple.com/design/resources/) & [Figma Community @apple](https://help.figma.com/hc/en-us/articles/24037833895831-Get-started-with-Apple-s-UI-kit) | Dùng để lấy các thành phần hệ thống chuẩn: `Status Bar`, `Dynamic Island`, `Home Indicator`, `iOS Keyboard`, `System Permission Alert` (`SB-011`, `SB-012`), `iOS Date Wheel / Calendar Picker` (`SB-079`), `Switch Toggle` (`SB-097`). |
| **Apple Human Interface Guidelines (HIG)** | [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) | Tham chiếu chuẩn cho Navigation Bars, Tab Bars, Sheets, Modality, Dynamic Type và Accessibility. |
| **Font hệ thống Apple (`SF Pro`, `SF Mono`)** | Cài đặt từ trang chính thức của Apple Developer | Chỉ dùng để hiển thị mockup giao diện iOS (Status Bar, bàn phím, hộp thoại hệ thống). **Không tải file `.ttf/.otf` từ các kho font lậu và không commit file binary font của Apple vào Git repository.** |
