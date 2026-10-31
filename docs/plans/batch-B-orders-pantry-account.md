# Plan B · 34 màn — Orders, Pantry & Account (Section 03 + 04)

Một trong hai plan chia đôi 70 màn còn lại sau batch `B-PHASE1-013`. Plan song song: [Plan A · Entry, Discovery & Offer](batch-A-entry-discovery-offer.md). Cả hai dựa trên bảng Interaction Map ở [Plan 2](build-100-screens-prototype.md) mục 7 và ma trận thị giác ở [screen-art-direction](../screen-art-direction.md).

Trạng thái: `PREPARED · WAITING_WRITER_WINDOW` · Người thực hiện: Plan-B/fable · Nhánh tích hợp: `design/end-to-end-quality-assets`.

**Reconcile31/10 (`DEC-012`):** live có25/50 màn thuộc Plan B.9 màn trong danh sách gốc đã tồn tại (`052,061,064,065,066,068,069,092,093`), không dựng lại. Còn25 màn thiếu (`070,071,073,074,076–090,094–099`), cùng audit/fix25 màn cũ. IDs live và giới hạn controls xem [foundation checkpoint](../../tracking/foundation-checkpoint.md); registry/workflow hiện hành override tọa độ/IDs cũ trong bảng kế hoạch.

**Đọc trước khi làm:** mục 5 "Quy ước chung" trong [Plan A](batch-A-entry-discovery-offer.md#5-quy-ước-chung-áp-dụng-cho-cả-plan-a-và-b) — có bảng ID component, imageHash và 9 lỗi đã gặp khi dựng 30 màn đầu. Plan B tuân thủ y nguyên.

---

## 1. Phạm vi và quyền ghi

- **Được ghi:** Section `03 · Reserve & Orders` (`69:328`) và `04 · Pantry & Account` (`69:329`) trên page `App · All Screens` (`11:3`), gồm cả các frame đã có trong 2 section này (`SB-050–058, 060, 062, 063, 067, 072, 075, 091, 100`) khi cần nối lại reaction.
- **Không ghi:** Section 01 và 02 (thuộc Plan A), main component đang có trên page `Components` (`11:2`), trừ component mới do chính Plan B tạo ở mục 4.
- **Registry:** chỉ sửa các dòng `SB-ID` thuộc Plan B trong [screens.csv](../../tracking/screens.csv); ghi tiến độ dưới heading riêng `## Plan B` trong [progress.md](../../tracking/progress.md).

## 2. Danh sách 34 màn

`Clone` = nhân bản frame có sẵn rồi đổi nội dung. `Mới` = dựng từ component. Cột "Vào từ" là reaction cần thêm vào frame nguồn (nguồn thuộc Plan A ghi ở mục 6).

### Section 03 · Reserve & Orders (10 màn) — hàng `y=2100`, bắt đầu `x=6080`, bước `460`

| ID | Màn | Archetype | Cách dựng | Nội dung chính | Ra tới | Vào từ |
|---|---|---|---|---|---|---|
| `SB-052` | Đọc lại hướng dẫn nhận | A7 | Clone `SB-051` (`19:2`) | Checklist 3 điều kiện: đến đúng `17:00–18:00`, trả `25.000đ` tại quầy, hủy trước `17:00` | Tôi đã hiểu→`053` | Thêm link "Xem hướng dẫn nhận" trên `SB-051` |
| `SB-061` | Đơn đang chờ nhận | A9 | Clone `SB-060` (`84:1217`) | Danh sách theo độ khẩn, timeline `16:00 → 17:00 → 18:00` | Đơn→`062`, Mở mã→`063`, Chỉ đường→`065`, tab bar | Link "Xem tất cả đang chờ" trên `SB-060` |
| `SB-064` | Hướng dẫn đưa mã | A7 | Mới | 3 bước tại quầy + cách đọc `DEMO-A125` khi máy quét lỗi; nhấn mạnh cửa hàng xác nhận (D-011) | Đã hiểu→Back, Hỗ trợ→`099` | Link "Cách đưa mã" trên `SB-063` |
| `SB-065` | Dẫn đường tới điểm nhận | A4 | Clone `SB-016` (`17:187`) — chỉ copy, đặt trong Section 03 | Tuyến đi bộ + banner `17:00–18:00 · DEMO-A125` ở đỉnh | Mở mã QR→`063`, Back | `SB-056` Xem chỉ đường (`19:235`), `SB-062` Chỉ đường, `SB-067` Chỉ đường, `061` |
| `SB-066` | Đơn đã sẵn sàng | A7 | Clone `SB-062` (`84:1290`) | Banner xanh `Phần bánh đã được đóng gói tại quầy` + pass trạng thái Ready | Mở mã→`063` | `095` |
| `SB-068` | Quá giờ nhận | A10 | Clone `SB-067` (`85:1342`) | Trạng thái `EXPIRED_NO_SHOW`, giải thích chính sách, không tính impact | Xem ưu đãi khác→`015`, Báo lý do→`069`, Trợ giúp→`099` | `SB-067` After delay 3s |
| `SB-069` | Báo sự cố khi nhận | A9 | Mới | Radio lý do (đóng cửa sớm, mã không quét được, món khác mô tả, nghi ngờ chất lượng/dị ứng) + ô ghi chú | Gửi→Back | `SB-062` Báo sự cố (`84:1355`), `SB-067` Hỗ trợ (`85:1383`), `068`, `099` |
| `SB-070` | Xác nhận hủy đơn | A7 | Sheet trên `SB-062` mờ | `Hủy miễn phí trước 17:00`, chip lý do, nút đỏ `#B42318` + `Giữ lại đơn` | Xác nhận hủy→`071`, Giữ lại→Back | `SB-062` text Hủy (`84:1354`) |
| `SB-071` | Hủy đơn thành công | A10 | Mới (theo `EmptyState`) | `Đã hủy DEMO-001 · Phần bánh đã được mở lại`, không nợ phí | Khám phá→`015`, Xem đơn→`060` | `070` |
| `SB-073` | Lịch sử đơn trống | A10 | Mới, tab root | `EmptyState` + dải 2 ưu đãi gợi ý + `BottomNav` (tab Đơn active) | Khám phá→`013`, ưu đãi→`034` | `SB-013` tab Đơn (Plan A, mục 6) |

### Section 04 · Pantry & Account (24 màn) — hàng `y=3100`, bắt đầu `x=1480`, bước `460`

| ID | Màn | Archetype | Cách dựng | Nội dung chính | Ra tới | Vào từ |
|---|---|---|---|---|---|---|
| `SB-074` | Giới thiệu Pantry | A1 | Mới | Minh họa kệ bếp vector + huy hiệu `Lưu cục bộ trên máy · Không cần đăng nhập` (D-014) | Bắt đầu→`076` | `SB-013` tab Pantry, `SB-030` (Plan A) |
| `SB-076` | Tủ trống | A10 | Mới | `EmptyState` kệ trống + 3 chip thêm nhanh + `BottomNav` (tab Pantry) | Chip→`080`, Thêm thủ công→`077` | `074` |
| `SB-077` | Thêm thủ công | A8 | Mới | `TextField` tên, chip đơn vị, segmented nơi bảo quản, trigger ngày hạn | Loại→`078`, Ngày hạn→`079`, Lưu→`080` | `SB-075` nút `+ Thêm món`, `076` |
| `SB-078` | Chọn loại thực phẩm | A5 | Sheet | 8 ô danh mục pastel + gợi ý nơi bảo quản | Chọn→`077` | `077` |
| `SB-079` | Chọn ngày hạn | A5 | Sheet | Toggle `Hạn sử dụng` vs `Nên dùng trước` (D-015), chip `+2 ngày/+5/+1 tuần/Chưa rõ`, lưới lịch | Xác nhận→`077` | `077` |
| `SB-080` | Xác nhận thêm | A8 | Mới | Thẻ xem trước `Sữa tươi · 1 hộp · Ngăn mát · HSD 21/10` + giờ nhắc | Lưu vào tủ→`075`, Sửa lại→`077` | `077`, `076`, `SB-072` nút Thêm vào Tủ (`85:1442`) |
| `SB-081` | Chi tiết thực phẩm | A8 | Mới | Vòng/thanh độ tươi lớn, metadata, dock 3 hành động | Đã dùng hết→`086`, Đã bỏ→`087`, Sửa→`082`, Nhắc hạn→`085` | `SB-075` các `PantryItemRow`, `083`, `088` |
| `SB-082` | Sửa thực phẩm | A8 | Clone `077` | Còn `1/2 hộp`, đổi nơi bảo quản, chú thích lần sửa trước | Lưu→`081` | `081` |
| `SB-083` | Sắp hết hạn | A8 | Mới | Danh sách ưu tiên 24–48h nền `#FEF6EE` | Dòng→`081`, Đã dùng→`086`, Gợi ý→`088` | `SB-075` banner "2 cần dùng sớm", `095` |
| `SB-084` | Đã quá hạn dùng | A8 | Mới | Hộp đỏ `Không khuyến nghị sử dụng`; tách Use-by vs Best-before | Bỏ an toàn→`087` | `SB-075` "1 quá hạn" |
| `SB-085` | Thiết lập nhắc hạn | A5 | Mới | Mốc nhắc, giờ `07:30/17:30`, múi giờ `Asia/Ho_Chi_Minh`, fallback khi tắt quyền | Lưu→`081` | `081` |
| `SB-086` | Đánh dấu đã dùng | A8 | Sheet | Chọn `1/4 · 1/2 · Hết`, lời khích lệ nhẹ, hủy nhắc | Xác nhận→`089` | `SB-075` nút Đã dùng, `081`, `083` |
| `SB-087` | Đánh dấu đã bỏ | A8 | Sheet | Lý do không phán xét | Xác nhận→`075` | `081`, `084` |
| `SB-088` | Gợi ý dùng thực phẩm | A8 | Mới | Thẻ kết hợp theo quy tắc, ghi rõ **không phải AI**, không gợi ý món quá hạn | Món→`081` | `SB-075`, `083` |
| `SB-089` | Lịch sử Pantry | A8 | Mới | Tóm tắt tuần + log thao tác | Back | `086`, `SB-075` |
| `SB-090` | Dữ liệu cục bộ | A8 | Mới | Dung lượng, Xuất JSON/CSV, Xóa toàn bộ, ghi chú sao lưu `FUTURE` | Back | `SB-075`, `098` |
| `SB-092` | Sửa hồ sơ | A2 | Mới | Avatar chữ `MA`, 3 `TextField`, toast đã lưu | Lưu→`091` | `SB-091` thẻ hồ sơ (`20:130`) |
| `SB-093` | Khu vực thường dùng | A9 | Mới | 2 thẻ vị trí đã lưu + cam kết không chia sẻ | + Thêm→`094` | `SB-091` dòng Khu vực (`20:147`) |
| `SB-094` | Lưu khu vực mới | A4 | Clone `SB-016` | Ghim tâm cố định + vòng bán kính `500m/1km/2km` + ô tên | Lưu→`093` | `093` |
| `SB-095` | Trung tâm thông báo | A9 | Mới | Lọc Tất cả / Đơn / Pantry; dòng chưa đọc nền `#EDF3E7` | Sẵn sàng→`066`, Sắp hết giờ→`SB-067`, Sữa còn 1 ngày→`083` | `SB-091`; `SB-014`, `SB-015` chuông (Plan A) |
| `SB-096` | Thông báo trống | A10 | Mới | `EmptyState` chuông nghỉ + cam kết không spam | Cấu hình giờ nhắc→`097` | `SB-013` chuông (Plan A) |
| `SB-097` | Tùy chọn thông báo | A9 | Mới | 5 `iOSSwitchRow` chia 2 nhóm Pickup / Pantry + giờ yên lặng | Back | `SB-091` dòng Nhắc lịch (`20:150`), `096` |
| `SB-098` | Quyền riêng tư & dữ liệu | A9 | Mới | Trạng thái quyền vị trí (đang chọn tay), dữ liệu Pantry cục bộ, xuất/xóa | Quyền vị trí→`011` (A), Dữ liệu Pantry→`090` | `SB-091` dòng Dữ liệu (`20:158`) |
| `SB-099` | Trợ giúp & FAQ | A9 | Mới | Ô tìm, 4 chủ đề, accordion 1 mục mở sẵn | Báo sự cố cửa hàng→`069` | `SB-091` dòng Trợ giúp (`20:164`), `064`, `068` |

Sau batch này `SB-067` có lối vào (`095`), đóng nốt màn đang thiếu đường vào thuộc Plan B.

## 3. Thứ tự batch

Các màn không cần `SheetContainer`/`EmptyState` làm trước, để không phải chờ Batch A0 của Plan A.

| Batch | Màn | Ghi chú |
|---|---|---|
| B0 | Component mục 4 | `iOSSwitchRow`, `NotificationRow`, `PantryCategoryTile` |
| B1 | `052, 061, 064, 065, 066, 068, 069` | Orders, không cần sheet |
| B2 | `092, 093, 094, 095, 097, 098, 099` | Account |
| B3 | `074, 077, 080, 081, 082, 083, 084, 085` | Pantry core |
| B4 | `070, 071, 073, 076, 096` | Cần `SheetContainer`/`EmptyState` (hoặc bản cục bộ theo mẫu `SB-050`/`SB-022`) |
| B5 | `078, 079, 086, 087, 088, 089, 090` | Sheet Pantry + log |

Mỗi batch: dựng → screenshot từng màn → tự chấm rubric → nối reaction → cập nhật `screens.csv` → commit nhỏ.

## 4. Component Plan B tạo

| Component | Variants | Dùng ở |
|---|---|---|
| `iOSSwitchRow` | `On=True/False`, nhãn + mô tả | `097` (sau này có thể dùng ở `085`) |
| `NotificationRow` | `Type=Pickup/Pantry/Safety`, `Read=True/False` | `095` |
| `PantryCategoryTile` | 8 loại, icon vector, nền pastel | `078` |

Dùng `SheetContainer`, `EmptyState`, `SegmentedControl`, `FilterChip` do Plan A tạo (ID sẽ có trong progress/components.csv). Pantry đã có `PantryItemRow` (`16:171`), `FreshnessSummaryBanner` (`16:161`).

## 5. Lưu ý riêng cho Plan B

- `BottomNav` không có variant tab active: đặt tab active bằng override (nền `#EDF3E7`, bo 14, chữ SemiBold `#004337`, icon `#004337`), các tab còn lại `#606E66`. `SB-060` là mẫu đã làm đúng.
- `SB-065`, `SB-094` clone từ `SB-016` nằm ở Section 01: chỉ **đọc và clone**, rồi `appendChild` bản clone vào Section 03/04 — không sửa frame gốc.
- Pantry (`074–090`) không dùng `OfferCard`, không giá tiền (luật 9 visual-direction); phân biệt rõ `Hạn sử dụng` / `Nên dùng trước`.
- `SB-097` cần nút gạt kiểu iOS thật; `SB-098` không dùng thuật ngữ kỹ thuật mập mờ.

## 6. Liên kết chéo với Plan A

Quy tắc: **chủ của frame nguồn nối reaction**. Nếu đích chưa dựng → ghi `pending:SB-xxx` trong `notes`, nối ở lượt nối chéo cuối (một người làm, sau khi cả hai plan xong).

| Nguồn (Plan B) | Đích (Plan A) |
|---|---|
| `SB-098` Quyền vị trí | `SB-011` |
| `SB-072` Đánh giá (`85:1439`) | `SB-042` |
| `SB-091` dòng Ưu đãi đã lưu (`20:153`) | `SB-033` |

Plan A sẽ nối sang Plan B: `SB-013` → `073 / 074 / 096`, `SB-014`/`SB-015` chuông → `095`, `SB-030` → `074`.
