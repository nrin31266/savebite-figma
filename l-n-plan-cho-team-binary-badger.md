# Kế hoạch Phân công & Thực thi 100 Màn hình Figma cho 2 Designer (50/50 Split)

## 1. Bối cảnh & Bài toán Cốt lõi (Context)

Dự án **SaveBite** yêu cầu hoàn thiện **100 màn hình High-Fidelity (`SB-001`..`SB-100`)** trên một file Figma duy nhất (`NLTv70kDZ2i3HpOnOKQCDY`), tuân thủ định hướng nghệ thuật [docs/visual-direction.md](docs/visual-direction.md), chuẩn iPhone [docs/ios-guidelines.md](docs/ios-guidelines.md) và ma trận 10 Archetypes [docs/screen-art-direction.md](docs/screen-art-direction.md).

Khi chỉ có **2 thành viên trực tiếp vẽ Figma** (cùng sự hỗ trợ của Claude Code + Figma MCP), nếu chia việc sai cách sẽ gặp ngay 3 rủi ro nghiêm trọng:
1. **Đụng độ trên Figma Canvas (MCP Collision):** Theo quy tắc của `figma-use` và [AGENTS.md](AGENTS.md), Figma không có nhánh (branch) độc lập như Git. Nếu 2 người/2 agent cùng chạy script trên **cùng một Figma Page** hoặc cùng sửa page `Components` (`27:87`) một lúc, tọa độ `(x, y)` sẽ đè lên nhau và làm hỏng component instances.
2. **Đụng độ Git Registry (`screens.csv`, `components.csv`, `validate.py`):** Cả 2 cùng sửa chung 1 dòng CSV hoặc lệch mã băm trong `tracking/evidence/` sẽ gây merge conflict liên tục.
3. **Lệch gu thẩm mỹ giữa một luồng (Flow Fragmentation):** Nếu Người A vẽ màn *Tóm tắt đơn (`SB-053`)* còn Người B vẽ màn *Mã QR (`SB-063`)* mà không chung nhóm thiết kế Vé Nhận Món, giao diện sẽ bị chắp vá.

---

## 2. Nguyên tắc Chia Việc Tối ưu: "Khóa Chuẩn Chung → Tách Độc lập theo Figma Page & Cụm Archetype (50 / 50)"

### Không nên chia theo các cách sau:
- ❌ **Không chia chẵn/lẻ hoặc chia ngẫu nhiên theo số thứ tự** (`SB-001..050` và `SB-051..100` cắt ngang giữa chừng luồng Đặt chỗ `SB-050..059`).
- ❌ **Không để 2 người cùng vẽ trên 1 Page Figma** cùng lúc.
- ❌ **Không vẽ tuần tự từ `SB-001` đến `SB-100` theo số đếm**, mà phải **gom theo Cụm Bố cục (Archetype Cluster)** trong từng phân hệ: dựng 1 màn gốc (`Core`) thật chuẩn rồi sinh nhanh các màn trạng thái (`State`) cùng khung.

### Chiến lược Khuyến nghị (3 Tầng):
1. **Tầng 1 — Giai đoạn 0 (1 ngày đầu): Làm chung để khóa "Khuôn đúc" (`Foundations` + `Components` + `5 màn Pilot v1.0`)**
   - Chỉ **1 người (Designer 1 - Lead System)** giữ quyền ghi vào page `Foundations` (`4:48`) và `Components` (`27:87`) để chốt bộ core components dùng chung (Apple Status Bar, Home Indicator, BottomNav, AppBar, Button, OfferCard, PerforatedPass).
   - **Designer 2** trong lúc đó chuẩn bị sẵn 4–6 ảnh thực phẩm Pexels đã duyệt, kiểm tra `assets/manifest.json` và dựng khung вектор bản đồ `MapCanvas` + `DemoQR` + `PantryRow` ở bản nháp.
2. **Tầng 2 — Chia 50 / 50 theo "Ranh giới Luồng + Figma Page Riêng biệt" (Tuyệt đối không đụng Page của nhau)**
   - **Designer 1 (50 màn): Phụ trách "Đầu phễu — Entry, Khám phá, Bản đồ, Tìm kiếm & Chi tiết Món/Cửa hàng" (`SB-001..049` + `SB-059`)** trên **2 Page Figma riêng**.
   - **Designer 2 (50 màn): Phụ trách "Cuối phễu — Đặt giữ chỗ, Vé QR Nhận món, Smart Pantry & Tài khoản/Impact" (`SB-050..058` + `SB-060..100`)** trên **2 Page Figma riêng**.
3. **Tầng 3 — Trong mỗi người (50 màn), vẽ theo "Cụm Khuôn Mẫu (Template/Archetype Reuse)" thay vì vẽ rời từng màn**
   - Ví dụ: Designer 1 khi đã vẽ xong màn `SB-034` (Chi tiết món), sẽ dùng chính khung đó để tạo luôn 5 màn anh em (`SB-044` Túi bất ngờ, `SB-046` Hết hàng, `SB-047` Ngoài giờ, `SB-048` Gần đóng, `SB-049` Xung đột dị ứng) trong **cùng 1 buổi** — tiết kiệm 70% thời gian mà đồng bộ 100%.

---

## 3. Bảng Phân công Chi tiết 50 / 50 Giữa 2 Người Vẽ Figma

### Kiến trúc 6 Pages trên File Figma (`NLTv70kDZ2i3HpOnOKQCDY`)

| Tên Page trên Figma | Người có quyền Ghi (Writer Lease) | Dải màn hình (`SB-ID`) | Số màn Hi-Fi |
|---|---|---|---:|
| `Foundations` (`4:48`) & `Components` (`27:87`) | **Designer 1** (Khóa trước ở Phase 0; ai cần thêm component mới phải báo trước) | Không đếm vào 100 | 0 |
| **`01 · Entry & Discovery`** | **Designer 1** (Độc quyền ghi) | `SB-001` .. `SB-033` | **33** |
| **`02 · Offer & Merchant`** | **Designer 1** (Độc quyền ghi) | `SB-034` .. `SB-049` và `SB-059` | **17** |
| **`03 · Reserve & Orders`** | **Designer 2** (Độc quyền ghi) | `SB-050` .. `SB-058` và `SB-060` .. `SB-073` | **23** |
| **`04 · Pantry & Account`** | **Designer 2** (Độc quyền ghi) | `SB-074` .. `SB-100` | **27** |
| **TỔNG CỘNG** | **Designer 1: 50 màn · Designer 2: 50 màn** | **`SB-001` .. `SB-100`** | **100** |

> *(Lưu ý: `SB-059 - Cần đăng nhập để giữ chỗ` được giao cho **Designer 1** vì đây là tấm trượt Auth Gate nối trực tiếp từ `SB-034` (Chi tiết món) về `SB-008` (Đăng nhập) do Designer 1 thiết kế, giúp chia chẵn đúng **50 màn / người** và khép kín toàn bộ giao diện Auth).*

---

### Chi tiết 50 Màn của DESIGNER 1: *"Discovery, Spatial & Showcase Lead"*
**Đặc trưng kỹ năng/công cụ:** Mạnh về bố cục hình ảnh thực phẩm, lưới thẻ đa nhịp điệu (`A3`), ảnh tràn viền (`A6`), bản đồ vector (`A4`) và các tấm trượt bộ lọc (`A5`).

1. **Cụm D1-B1 · Chi tiết Món, Túi Bất Ngờ & Các biến thể Trạng thái (10 màn — Ưu tiên P0/P1):**
   - `SB-034` (Chi tiết món cụ thể — *Pilot sẵn có, nâng lên v1.0*)
   - `SB-044` (Chi tiết túi bất ngờ), `SB-045` (Sheet giải thích túi bất ngờ)
   - `SB-046` (Hết hàng + gợi ý món tương tự), `SB-047` (Ngoài giờ nhận), `SB-048` (Gần đóng cửa), `SB-049` (Xung đột dị ứng)
   - `SB-035` (Lightbox phóng to ảnh), `SB-036` (Sheet Thành phần & Dị ứng), `SB-037` (Sheet Chất lượng & Bảo quản)
   - *Cách vẽ nhanh:* Dựng chuẩn `SB-034` trước → nhân bản khung cho `SB-044, 046..049` (6 màn cùng Archetype `A6`) → dựng 3 tấm trượt `SB-036, 037, 045`.
2. **Cụm D1-B2 · Trang chủ, Khám phá & Danh mục Chợ Ưu Đãi (9 màn — P0/P1):**
   - `SB-015` (Khám phá danh sách — *Pilot sẵn có, nâng lên v1.0*), `SB-013` (Home Guest), `SB-014` (Home Đã đăng nhập)
   - `SB-028` (Danh mục Bữa ăn), `SB-029` (Danh mục Bánh), `SB-030` (Danh mục Rau củ/Thực phẩm), `SB-031` (Đang nhận sớm), `SB-032` (Quanh trường), `SB-033` (Đã lưu / Yêu thích)
   - *Cách vẽ nhanh:* Cùng thuộc Archetype `A3` — dùng chung `OfferCard`, `OfferListRow`, `CategoryTile` và `BottomNav`, chỉ thay đổi phần **Header đặc trưng của từng danh mục** (Countdown bar ở `031`, Mini-map ở `032`, Segmented tab ở `033`).
3. **Cụm D1-B3 · Tìm kiếm & Hệ thống Tấm trượt Bộ lọc (9 màn — P0/P1):**
   - `SB-019` (Tìm kiếm + Bàn phím iOS), `SB-020` (Gợi ý Autocomplete + Bàn phím), `SB-021` (Kết quả tìm kiếm), `SB-022` (Không kết quả + Gợi ý thay thế)
   - `SB-023` (Bộ lọc tổng hợp), `SB-024` (Lọc ngân sách), `SB-025` (Lọc thời gian nhận), `SB-026` (Lọc nhu cầu ăn uống), `SB-027` (Sắp xếp kết quả)
   - *Cách vẽ nhanh:* `SB-019..020` dùng chung khung + `iOSKeyboard`; `SB-023..027` dùng chung nền mờ của `SB-015/021` phía dưới và chỉ thay ruột tấm `ModalSheet` ở trên.
4. **Cụm D1-B4 · Bản đồ, Khu vực & Hồ sơ Cửa hàng (9 màn — P0/P1/P2):**
   - `SB-016` (Bản đồ khám phá), `SB-017` (Xem nhanh ghim trên bản đồ), `SB-018` (Chọn khu vực / Campus)
   - `SB-038` (Chi tiết cửa hàng), `SB-039` (Bản đồ đường tới cửa hàng), `SB-040` (Quy định nhận món), `SB-041` (Các offer khác của tiệm), `SB-042` (Đánh giá cửa hàng), `SB-043` (Chi tiết đánh giá)
   - *Cách vẽ nhanh:* Dựng 1 component `MapCanvas` vector ấm dùng chung cho `SB-016, 017, 039` (và chia sẻ cho Designer 2 dùng ở `SB-065, 094`).
5. **Cụm D1-B5 · Khởi động, Onboarding, Xác thực & Quyền hệ thống (13 màn — P0/P1):**
   - `SB-001` (Splash), `SB-002..004` (3 màn Onboarding), `SB-005` (Cổng Guest/Auth), `SB-011` (Quyền vị trí), `SB-012` (Quyền thông báo)
   - `SB-006` (Đăng ký), `SB-007` (Chờ xác minh email), `SB-008` (Đăng nhập), `SB-009` (Quên mật khẩu), `SB-010` (Đã gửi link), `SB-059` (Sheet Cần đăng nhập để giữ chỗ).

---

### Chi tiết 50 Màn của DESIGNER 2: *"Transaction, Pass, Pantry & Account Lead"*
**Đặc trưng kỹ năng/công cụ:** Mạnh về hệ thống hóa đơn/vé đục lỗ (`A7`), trạng thái đơn hàng, thiết kế công cụ quản lý hạn dùng Smart Pantry (`A8`) và bảng điều khiển/thống kê (`A9`).

1. **Cụm D2-B1 · Luồng Đặt Giữ Chỗ, Biên lai & Xử lý Lỗi Tồn Kho (9 màn — Ưu tiên P0):**
   - `SB-050` (Chọn số lượng), `SB-051` (Chọn khung giờ — *Pilot sẵn có*), `SB-052` (Đọc lại hướng dẫn nhận), `SB-053` (Tóm tắt đặt trước — *Pilot sẵn có*), `SB-054` (Sheet Xác nhận giữ chỗ)
   - `SB-055` (Đang xử lý giữ chỗ), `SB-056` (Đặt trước thành công — *Pilot sẵn có*), `SB-057` (Giữ chỗ thất bại), `SB-058` (Tồn kho thay đổi khi xác nhận — `F-03`)
   - *Cách vẽ nhanh:* Toàn bộ cụm này xoay quanh `OfferSummary`, `UnifiedReceiptCard` và `PerforatedPickupPass`. Hoàn thiện cụm này là khớp nối xong nửa sau của luồng chính `F-01` và luồng lỗi `F-03`!
2. **Cụm D2-B2 · Quản lý Đơn hàng, Vé QR Nhận Món & Hủy/Quá hạn (14 màn — P0/P1):**
   - `SB-060` (Đơn của tôi — Tổng quan), `SB-061` (Đơn đang chờ nhận), `SB-062` (Chi tiết đơn chờ nhận), `SB-072` (Chi tiết đơn hoàn tất), `SB-073` (Lịch sử đơn trống)
   - `SB-063` (Mã nhận món / QR Pass), `SB-064` (Hướng dẫn đưa mã), `SB-065` (Dẫn đường tới điểm nhận), `SB-066` (Đơn đã sẵn sàng)
   - `SB-067` (Sắp hết giờ nhận), `SB-068` (Quá giờ nhận — `F-04`), `SB-069` (Báo cáo vấn đề), `SB-070` (Xác nhận hủy đơn — `F-04`), `SB-071` (Hủy đơn thành công)
   - *Cách vẽ nhanh:* `SB-062, 066, 067, 068, 072` đều là biến thể theo dòng thời gian của cùng một khung **Chi tiết Đơn / Biên lai (`A7`)**; `SB-063` kế thừa trực tiếp tấm vé QR từ `SB-056`.
3. **Cụm D2-B3 · Smart Pantry — Tủ Thực Phẩm & Nhập liệu Hạn Dùng (9 màn — P1):**
   - `SB-074` (Giới thiệu Pantry), `SB-075` (Tủ thực phẩm của tôi), `SB-076` (Tủ trống + Chip thêm mẫu 1 chạm)
   - `SB-077` (Thêm thực phẩm thủ công), `SB-078` (Sheet Chọn loại thực phẩm), `SB-079` (Sheet Chọn ngày hạn `Use by` vs `Best before`), `SB-080` (Xác nhận thêm), `SB-081` (Chi tiết thực phẩm), `SB-082` (Sửa thực phẩm)
   - *Cách vẽ nhanh:* Dựng component `PantryItemRow` (có thanh tiến độ độ tươi) và `FreshnessSummaryBanner` một lần để phủ toàn bộ nhánh Pantry (`F-05`).
4. **Cụm D2-B4 · Smart Pantry — Cảnh báo Hạn, Đánh dấu Dùng/Bỏ & Dữ liệu (8 màn — P1/P2):**
   - `SB-083` (Sắp hết hạn), `SB-084` (Đã quá hạn dùng — cảnh báo không ăn), `SB-085` (Thiết lập nhắc hạn)
   - `SB-086` (Sheet Đánh dấu đã sử dụng 100% / 50%), `SB-087` (Sheet Đánh dấu đã bỏ), `SB-088` (Gợi ý dùng thực phẩm theo quy tắc tĩnh), `SB-089` (Lịch sử sử dụng & bỏ), `SB-090` (Tùy chọn Pantry & dữ liệu cục bộ).
5. **Cụm D2-B5 · Tài khoản, Khu vực Lưu, Thông báo, Cài đặt & Tác động Cá nhân (10 màn — P1):**
   - `SB-091` (Tài khoản tổng quan), `SB-092` (Chỉnh sửa hồ sơ), `SB-093` (Quản lý khu vực thường dùng), `SB-094` (Lưu khu vực mới)
   - `SB-095` (Trung tâm thông báo), `SB-096` (Thông báo trống), `SB-097` (Tùy chọn thông báo iOS Switch), `SB-098` (Quyền riêng tư & dữ liệu), `SB-099` (Trợ giúp & FAQ), `SB-100` (Tác động cá nhân — điểm kết thúc `F-01`).

---

## 4. Lộ trình Chạy Song Song theo Tuần / Ca Làm Việc (Không ai phải chờ ai)

```text
GIAI ĐOẠN 0 (Chung) ──► Chốt iPhone Frame + Core Components + Nâng cấp 5 màn Pilot v1.0
       │
       ├──► DESIGNER 1 (Pages 01 & 02 - 50 màn)                DESIGNER 2 (Pages 03 & 04 - 50 màn)
       │    ├─ Đợt 1 (P0): SB-034..037, 044..049 (10 màn)      ├─ Đợt 1 (P0): SB-050..058 (9 màn Đặt chỗ)
       │    ├─ Đợt 2 (P0): SB-013..015, 028..033 (9 màn)       ├─ Đợt 2 (P0): SB-060..068, 070..073 (14 màn Đơn/QR)
       │    ├─ Đợt 3 (P0): SB-019..027 (9 màn Search/Filter)   ├─ Đợt 3 (P1): SB-074..082 (9 màn Pantry Core)
       │    ├─ Đợt 4 (P1): SB-016..018, 038..043 (9 màn Map)   ├─ Đợt 4 (P1): SB-083..090 (8 màn Pantry States)
       │    └─ Đợt 5 (P0/P1): SB-001..012, 059 (13 màn Auth)   └─ Đợt 5 (P1): SB-091..100 (10 màn Account/Impact)
       │
       └──► GIAI ĐOẠN KẾT NỐI PROTOTYPE (Nối 4 điểm giao nhau giữa D1 & D2 cho F-01..F-06)
```

### Chỉ có đúng 4 điểm nối dây Prototype giữa Designer 1 và Designer 2:
Nhờ chia khéo theo ranh giới luồng, 2 người làm việc độc lập 95% thời gian và chỉ cần nối dây qua lại ở **4 nút giao (Handoff Nodes)** sau:
1. **`SB-034` (D1) → `SB-050` / `SB-051` (D2):** Nút `Chọn giờ nhận` trên màn Chi tiết món của D1 trỏ sang màn Chọn số lượng/giờ nhận của D2.
2. **`SB-056` / `SB-071` (D2) → `SB-015` / `SB-060` (D1/D2):** Nút `Khám phá tiếp` trên màn Thành công của D2 trỏ về màn Khám phá `SB-015` của D1.
3. **`SB-034` (D1) → `SB-059` (D1) → `SB-008` (D1) → `SB-051` (D2):** Luồng khách chưa đăng nhập bấm đặt chỗ (`F-01` Guest-to-Auth) nằm gọn bên phía D1 rồi mới chuyển sang `SB-051` của D2.
4. **Thanh `BottomNav` (4 Tabs):**
   - Tab 1 (`Khám phá`) → `SB-015` (D1)
   - Tab 2 (`Đơn của tôi`) → `SB-060` (D2)
   - Tab 3 (`Tủ thực phẩm`) → `SB-075` (D2)
   - Tab 4 (`Tài khoản`) → `SB-091` (D2)

---

## 5. Quy tắc Chống Xung Đột Git & Figma MCP cho 2 Người

1. **Quy tắc Figma Page Lease (Tuyệt đối tuân thủ):**
   - Mỗi lần gọi Claude Code (`use_figma`), câu lệnh đầu tiên trong script luôn là `await figma.setCurrentPageAsync(targetPage)`.
   - **Designer 1** chỉ gọi `setCurrentPageAsync` vào Page `01 · Entry & Discovery` và `02 · Offer & Merchant`.
   - **Designer 2** chỉ gọi `setCurrentPageAsync` vào Page `03 · Reserve & Orders` và `04 · Pantry & Account`.
   - Khi một người cần thêm mới hoặc sửa một `Main Component` trên page `Components` (`27:87`), phải nhắn người kia tạm dừng 5 phút, thực hiện xong và ghi nhận vào `tracking/components.csv`.
2. **Quy tắc Chia Vùng trong `tracking/screens.csv` (Tránh Git Merge Conflict):**
   - `screens.csv` được sắp xếp cố định từ `SB-001` (dòng 2) đến `SB-100` (dòng 101).
   - **Designer 1** chỉ sửa các dòng `SB-001..049` và `SB-059`.
   - **Designer 2** chỉ sửa các dòng `SB-050..058` và `SB-060..100`.
   - Mỗi người làm trên nhánh Git riêng theo từng đợt (`design/d1-batch1-offer`, `design/d2-batch1-reserve`), chạy `python3 scripts/validate.py` PASS rồi merge vào `main` sau mỗi đợt 8–10 màn.
3. **Lưu ý về `scripts/validate.py` khi bắt đầu mở rộng ngoài 5 màn Pilot:**
   - Hiện tại dòng 39 của [scripts/validate.py](scripts/validate.py#L39) đang có câu lệnh bảo vệ giai đoạn pilot: `assert set(live) == PILOT, 'Pilot scope changed'`.
   - Ngay khi Owner duyệt xong 5 màn Pilot để mở khóa sản xuất 95 màn còn lại, cần cập nhật dòng này trong `scripts/validate.py` từ `assert set(live) == PILOT` thành `assert PILOT.issubset(live)` để cho phép thêm các màn hình mới vào `figma-readback.json`.

---

## 6. Phối hợp với 3 Thành viên Còn lại trong Nhóm 5 Người

Theo [docs/product.md](docs/product.md#L15-L21), nhóm có 5 thành viên (Đạt, Quân, Tân, Rin, Thuận). Để 2 người vẽ Figma đạt tốc độ và chất lượng thẩm mỹ cao nhất, 3 thành viên còn lại đảm nhận các phần việc không đụng vào Hi-Fi Canvas nhưng quyết định **65% tổng điểm học phần** (theo [docs/acceptance.md](docs/acceptance.md)):
- **Thành viên 3 (UX Research & Competitor Audit — 25% điểm):** Thực hiện bảng phân tích 20 ứng dụng đối thủ thực tế kèm ảnh chụp màn hình có nguồn, hoàn thiện khảo sát/phỏng vấn và Persona/Journey map.
- **Thành viên 4 (Low-Fi Wireframes, Assets Curation & QA Tester — 20% điểm):** Dựng page `Low-Fi` (8–12 màn cốt lõi + quay video low-fi 1–3 phút), tuyển chọn sẵn ảnh thực phẩm Pexels đúng ánh sáng ấm cho Designer 1 & 2, và bấm kiểm tra từng màn theo **Aesthetic Rubric 8 tiêu chí** ([docs/workflow.md](docs/workflow.md)).
- **Thành viên 5 (Frontend Demo, Presentation & Portfolio — 35% điểm):** Chuẩn bị khung code demo ứng dụng từ các màn đã duyệt, dựng kịch bản video demo hi-fi 2–5 phút trên điện thoại thật và biên tập Portfolio/Slide thuyết trình.

---

## 7. Các File sẽ Cập nhật (Sau khi bạn Duyệt Plan này)

Nếu bạn đồng ý với kế hoạch phân chia 50/50 này, bước thực thi tiếp theo sẽ ghi chính thức bảng phân công **2-Designer Execution Plan (D1 vs D2, 10 Batches, Page Isolation & Handoff Protocol)** vào:
- [docs/workflow.md](docs/workflow.md): Bổ sung mục **Kế hoạch Phân công 2 Figma Designers (50/50 Page-Isolated Split & 10-Batch Roadmap)** để cả nhóm và các phiên Claude Code tiếp theo lấy làm chuẩn vận hành.
- Kiểm tra lại bằng `python3 scripts/validate.py`.
