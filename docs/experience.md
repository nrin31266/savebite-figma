# Trải nghiệm, luồng và 100 màn

Nguồn chuẩn theo domain; đọc [router](README.md) và [tiến độ](../tracking/progress.md) trước khi thay đổi.

## IA, NAVIGATION VÀ MAIN FLOWS

### Thông tin điều hướng

**Root:** initial load → onboarding (lần đầu) → optional guest/login → Home.  
**Tabs:** Khám phá, Đơn của tôi, Tủ thực phẩm, Tài khoản.  
**Deep links:** offer, store, reservation, pickup code, pantry item (local links) và help.  
**Overlays:** filter, location selector, confirmation, warning, actions, add-to-favorites; không phải tất cả overlays đều là screen được đếm.

### Flows mục tiêu khi mở rộng sau pilot

**F-01 — Guest → rescue (PRIMARY, bắt buộc chạy end-to-end)**  
`Splash → Browse as Guest → Khám phá → Lọc dưới 50k → Detail (thông tin/dị ứng/slot) → Login (nếu cần) → Trở về cùng offer → Chọn số lượng → Chọn giờ nhận → Summary → Xác nhận giữ chỗ → Thành công → Đơn đang nhận → Mã nhận → Merchant verification simulated → Hoàn tất → Impact`.

**F-02 — Explore map/list**  
`Khám phá → Map → Tap pin → Quick preview → Offer Detail → Directions/Reserve`.

**F-03 — Error and recovery**  
`Offer available → Confirm → Stock changed → Explain → Adjust quantity or choose alternatives → Confirm safely`.

**F-04 — Pickup cancellation/expiration**  
`Đơn chờ → Cancel confirmation → Cancel success` và `Đơn chờ → Gần hết giờ → Quá giờ → Help`.

**F-05 — Pantry local-first**  
`Pantry empty → Add manual item → Choose expiry → Save → Expiring soon → Notification (mock/local) → Mark used → Activity`.

**F-06 — Location denied**  
`Onboarding → Deny GPS → Select city/campus manually → Valid discovery → Enable later in settings`.

### Quy tắc backstack và transitions

- Back trên Android/iOS phải trả về trạng thái filter/search đã nhập, không reset bất ngờ.
- Modal xác nhận có cancel; destructive actions cần confirm hoặc undo khi phù hợp.
- Sau auth quay lại offer/pickup intent hợp lệ; không tự reserve hoặc mua khi chưa nhấn xác nhận.
- Deep link đến đơn/cá nhân nếu chưa đăng nhập: mở auth và điều hướng lại sau thành công.
- Màn không có dữ liệu phải cung cấp CTA có ý nghĩa. Nếu mất mạng khi đặt chỗ, không tự thông báo thành công.

---

## SCREEN INVENTORY CHUẨN — 100 HIGH-FIDELITY FRAMES

### Cách đếm nghiêm ngặt

- Mỗi `SB-xxx` là một **frame hi-fi độc lập có thể trình diễn trong Figma**, chứa một nhiệm vụ hoặc trạng thái toàn màn có lý do tồn tại.
- `Core` = screen/route hoặc bước nghiệp vụ; `State` = trạng thái toàn màn có hành vi/chỉ dẫn riêng biệt và đáng kiểm thử.
- State biến thể phải hiển thị thay đổi logic thật (stock error, permission, expiration, empty), **không được chỉ thay ảnh/màu/tiêu đề**.
- Modal nhỏ, popover, variants component, low-fi wireframes, slide PDF và ảnh mockup **không được cộng vào 100**.
- Mục tiêu triển khai **100 IDs dưới đây**, có thể thêm ngoài 100 nếu cần kiểm thử nhưng không sửa ID cũ tùy tiện; mọi thay thế ghi Decision Record và bảo toàn traceability.
- Màn P0 phải được thiết kế, QA và dùng trong prototype trước P1; P2 chỉ sau khi core đạt yêu cầu.

### Phân bố dự kiến

| Nhóm | Dải ID | Số màn | Vai trò |
|---|---|---:|---|
| A. Entry, Auth & permissions | `SB-001..012` | 12 | Entry, login, guest, permissions |
| B. Discovery, Search & location | `SB-013..033` | 21 | Rescue Market discovery |
| C. Offer, merchant & reservation | `SB-034..059` | 26 | Nội dung, trust, đặt giữ chỗ |
| D. Order status & pickup | `SB-060..073` | 14 | Nhận hàng, hủy, lỗi, lịch sử |
| E. Smart Pantry | `SB-074..090` | 17 | Quản lý đồ ăn cá nhân |
| F. Account, settings & impact | `SB-091..100` | 10 | Hỗ trợ, quyền riêng tư, tác động |
| **Tổng** | | **100** | **Consumer-facing** |

### Screen Registry v1 (nội dung chuẩn để agent phát sinh `screens.csv`)

| ID | Màn hình (frame) | Flow | Loại | Ưu tiên | Tiêu chí riêng biệt / nội dung bắt buộc |
|---|---|---|---|---|---|
| `SB-001` | Splash / warm start | Launch | Core | P0 | Thương hiệu, khởi động có trạng thái offline/retry |
| `SB-002` | Onboarding 1 — Giá trị cứu thực phẩm | Intro | Core | P1 | Nêu giá trị và lợi ích thực tế, có Skip |
| `SB-003` | Onboarding 2 — Tìm món gần bạn | Intro | Core | P1 | Minh họa explore, giá/địa điểm |
| `SB-004` | Onboarding 3 — Pantry giảm lãng phí | Intro | Core | P1 | Pantry là phần bổ trợ, CTA tiếp tục |
| `SB-005` | Cổng đăng nhập hoặc khám phá | Auth | Core | P0 | Browse as guest hợp lệ |
| `SB-006` | Đăng ký tài khoản | Auth | Core | P0 | Email/mật khẩu, điều khoản, validation |
| `SB-007` | Chờ xác minh email | Auth | State | P1 | Gửi lại email, đổi email |
| `SB-008` | Đăng nhập | Auth | Core | P0 | Email/mật khẩu, lỗi đăng nhập |
| `SB-009` | Quên mật khẩu | Auth | Core | P1 | Nhập email khôi phục |
| `SB-010` | Đã gửi liên kết khôi phục | Auth | State | P1 | Gửi lại, quay về login |
| `SB-011` | Giải thích quyền vị trí | Permission | Core | P0 | Từ chối có chọn khu vực thủ công |
| `SB-012` | Giải thích quyền thông báo | Permission | Core | P1 | Không ép bật; có thể bật sau |
| `SB-013` | Home — khách chưa đăng nhập | Explore | Core | P0 | Cơ chế xem món mà không cần login |
| `SB-014` | Home — người dùng đăng nhập | Explore | Core | P0 | Nội dung gần bạn, ưu đãi theo vị trí |
| `SB-015` | Khám phá — danh sách ưu đãi | Explore | Core | P0 | List với phân cấp giá/địa điểm/pickup |
| `SB-016` | Khám phá — bản đồ | Explore | Core | P0 | Pins + đồng bộ list, không ghi vị trí giả |
| `SB-017` | Xem nhanh điểm trên bản đồ | Explore | State | P1 | Bottom sheet card cho pin được chọn |
| `SB-018` | Chọn khu vực / campus | Location | Core | P0 | Khu vực thủ công và GPS tùy chọn |
| `SB-019` | Tìm kiếm — nhập từ khóa | Search | Core | P0 | Bàn phím, recent queries |
| `SB-020` | Tìm kiếm — gợi ý | Search | State | P1 | Từ khóa thực phẩm/cửa hàng |
| `SB-021` | Tìm kiếm — kết quả | Search | Core | P0 | Sort/filter hiện trạng |
| `SB-022` | Tìm kiếm — không kết quả | Search | State | P0 | Reset filter, mở rộng bán kính |
| `SB-023` | Bộ lọc tổng hợp | Filter | Core | P0 | Các group rõ: ngân sách, thời gian, loại món |
| `SB-024` | Lọc ngân sách | Filter | Core | P0 | Dưới 30K, dưới 50K, tùy chỉnh |
| `SB-025` | Lọc thời gian nhận | Filter | Core | P0 | Giờ/khung trong ngày, phù hợp giờ học |
| `SB-026` | Lọc nhu cầu ăn uống | Filter | Core | P1 | Dị ứng luôn xác minh trên detail |
| `SB-027` | Sắp xếp kết quả | Filter | Core | P1 | Gần nhất, giá thấp, nhận sớm |
| `SB-028` | Danh mục — bữa ăn | Category | Core | P1 | Listing meal category, sort |
| `SB-029` | Danh mục — bánh / tiệm bánh | Category | Core | P1 | Listing bakery category |
| `SB-030` | Danh mục — thực phẩm cửa hàng | Category | Core | P1 | Listing groceries |
| `SB-031` | Ưu đãi — đang nhận sớm | Explore | Core | P1 | Pickup window đóng sớm |
| `SB-032` | Ưu đãi — quanh trường | Explore | Core | P1 | Campus radius + pickup distance |
| `SB-033` | Đã lưu — danh sách yêu thích | Favorites | Core | P1 | Offers/merchants đã lưu |
| `SB-034` | Chi tiết offer — món cụ thể | Offer | Core | P0 | Ảnh thực, giá, khung giờ, cửa hàng, tình trạng |
| `SB-035` | Thư viện ảnh món | Offer | Core | P1 | Ảnh có chú thích, phóng to |
| `SB-036` | Thành phần & cảnh báo dị ứng | Offer | Core | P0 | Nguồn do merchant cung cấp, unknown thì ghi rõ |
| `SB-037` | Chất lượng, hạn & hướng dẫn sử dụng | Offer | Core | P0 | Không bán thực phẩm quá hạn dùng |
| `SB-038` | Chi tiết cửa hàng | Merchant | Core | P0 | Địa chỉ, giờ nhận, uy tín có căn cứ |
| `SB-039` | Bản đồ & đường tới cửa hàng | Merchant | Core | P1 | Cho phép mở app bản đồ ngoài |
| `SB-040` | Quy định nhận món tại cửa hàng | Merchant | Core | P0 | Code nhận hàng, tới đúng pickup slot |
| `SB-041` | Các offer khác của cửa hàng | Merchant | Core | P1 | Merchant-linked listing |
| `SB-042` | Đánh giá cửa hàng | Merchant | Core | P1 | Review đã xác thực, không dữ liệu giả |
| `SB-043` | Chi tiết đánh giá | Merchant | Core | P2 | Nội dung đánh giá thực và report |
| `SB-044` | Chi tiết combo / túi bất ngờ | Offer | Core | P1 | Chỉ kỳ vọng category, allergen 'không bảo đảm' rõ |
| `SB-045` | Giải thích túi bất ngờ | Offer | Core | P1 | Minh bạch điều chưa biết và rủi ro dị ứng |
| `SB-046` | Offer — hết hàng | Offer | State | P0 | Không cho đặt; gợi ý tương tự |
| `SB-047` | Offer — ngoài giờ nhận | Offer | State | P0 | Khóa CTA, thông tin giờ nhận |
| `SB-048` | Offer — gần đóng cửa | Offer | State | P1 | Cảnh báo còn ít thời gian |
| `SB-049` | Offer — có xung đột dị ứng | Offer | State | P0 | Không claim an toàn, CTA cảnh báo rõ |
| `SB-050` | Chọn số lượng | Reserve | Core | P0 | Tồn kho và giới hạn theo offer |
| `SB-051` | Chọn khung giờ nhận | Reserve | Core | P0 | Hiển thị ngày, giờ, thời gian còn lại |
| `SB-052` | Đọc lại hướng dẫn nhận | Reserve | Core | P1 | Nơi nhận, giấy tờ/code, liên hệ |
| `SB-053` | Tóm tắt đặt trước | Reserve | Core | P0 | Giá, số lượng, khung giờ, thanh toán tại quầy |
| `SB-054` | Xác nhận đặt giữ chỗ | Reserve | Core | P0 | Rõ không thu tiền online trong MVP |
| `SB-055` | Đang xử lý giữ chỗ | Reserve | State | P1 | Không double submit |
| `SB-056` | Đặt trước thành công | Reserve | State | P0 | Order ID/code và hướng dẫn nhận |
| `SB-057` | Giữ chỗ thất bại | Reserve | State | P0 | Lỗi mạng/máy chủ, retry có kiểm soát |
| `SB-058` | Tồn kho thay đổi khi xác nhận | Reserve | State | P0 | Giải thích, chọn lại số lượng/offer |
| `SB-059` | Cần đăng nhập để giữ chỗ | Reserve | State | P0 | Return to offer sau auth |
| `SB-060` | Đơn của tôi — tổng quan | Orders | Core | P0 | Đang chờ, sắp nhận, hoàn tất |
| `SB-061` | Đơn đang chờ nhận | Orders | Core | P0 | Danh sách sắp đến hạn |
| `SB-062` | Chi tiết đơn đang chờ nhận | Orders | Core | P0 | Cửa hàng, số lượng, slot, trạng thái |
| `SB-063` | Mã nhận món / QR | Pickup | Core | P0 | Backup code nếu QR không dùng được |
| `SB-064` | Hướng dẫn đưa mã cho cửa hàng | Pickup | Core | P1 | Merchant xác minh, không tự nhận thành công |
| `SB-065` | Dẫn đường tới điểm nhận | Pickup | Core | P1 | Liên kết maps an toàn |
| `SB-066` | Đơn đã sẵn sàng | Pickup | State | P1 | Không hứa merchant luôn xác nhận ready |
| `SB-067` | Sắp hết giờ nhận | Pickup | State | P0 | Thông báo khẩn nhưng không gây hoảng |
| `SB-068` | Quá giờ nhận | Pickup | State | P0 | Hết hạn theo policy, support path |
| `SB-069` | Báo cáo vấn đề khi nhận | Support | Core | P1 | Loại sự cố, bằng chứng, liên hệ |
| `SB-070` | Xác nhận hủy đơn | Orders | Core | P0 | Hiển thị policy và hậu quả |
| `SB-071` | Hủy đơn thành công | Orders | State | P1 | Xác nhận, tiếp tục khám phá |
| `SB-072` | Chi tiết đơn hoàn tất | Orders | Core | P0 | Giá thực trả, đã nhận, đánh giá |
| `SB-073` | Lịch sử đơn trống | Orders | State | P1 | Onboarding và explore CTA |
| `SB-074` | Giới thiệu Pantry | Pantry | Core | P1 | Giải thích local-first, không tự đồng bộ |
| `SB-075` | Tủ thực phẩm của tôi | Pantry | Core | P1 | Sort theo expiry, quantity, category |
| `SB-076` | Tủ trống | Pantry | State | P1 | CTA thêm thủ công, ví dụ rõ |
| `SB-077` | Thêm thực phẩm thủ công | Pantry | Core | P1 | Tên, số lượng, đơn vị, ngày hạn |
| `SB-078` | Chọn loại thực phẩm | Pantry | Core | P1 | Danh mục có icon giản lược |
| `SB-079` | Chọn ngày hạn sử dụng | Pantry | Core | P1 | Ngày 'use by' vs 'best before' |
| `SB-080` | Xác nhận thêm thực phẩm | Pantry | State | P1 | Review thông tin và edit |
| `SB-081` | Chi tiết thực phẩm | Pantry | Core | P1 | Ngày hạn, đơn vị, trạng thái, ghi chú |
| `SB-082` | Sửa thực phẩm | Pantry | Core | P1 | Chỉnh hạn và lượng không mất lịch sử |
| `SB-083` | Sắp hết hạn | Pantry | Core | P1 | Danh sách priority theo hạn |
| `SB-084` | Đã quá hạn dùng | Pantry | State | P1 | Cảnh báo, không đề xuất ăn |
| `SB-085` | Thiết lập nhắc hạn | Pantry | Core | P1 | Nhắc theo ngày, permission, timezone |
| `SB-086` | Đánh dấu đã sử dụng | Pantry | Core | P1 | Có partial usage và quantity |
| `SB-087` | Đánh dấu đã bỏ | Pantry | Core | P1 | Lý do tự chọn, không phán xét |
| `SB-088` | Gợi ý dùng thực phẩm hiện có | Pantry | Core | P2 | Gợi ý tĩnh/quy tắc, không claim AI |
| `SB-089` | Lịch sử sử dụng & bỏ thực phẩm | Pantry | Core | P2 | Minh bạch dữ liệu từ thao tác |
| `SB-090` | Tùy chọn Pantry và dữ liệu cục bộ | Pantry | Core | P1 | Export/delete và giới thiệu backup tương lai |
| `SB-091` | Tài khoản — tổng quan | Account | Core | P1 | Profile, lịch sử, hỗ trợ, cài đặt |
| `SB-092` | Chỉnh sửa hồ sơ | Account | Core | P1 | Tên hiển thị, email, xác nhận cập nhật |
| `SB-093` | Quản lý khu vực thường dùng | Account | Core | P1 | Campus/home locations, không chia sẻ công khai |
| `SB-094` | Lưu khu vực mới | Account | Core | P1 | Map selector, manual entry |
| `SB-095` | Trung tâm thông báo | Notifications | Core | P1 | Reservation, reminders, safety alerts |
| `SB-096` | Trung tâm thông báo trống | Notifications | State | P1 | Giải thích hệ thống thông báo |
| `SB-097` | Tùy chọn thông báo | Settings | Core | P1 | Push riêng cho pickup và pantry |
| `SB-098` | Quyền riêng tư & dữ liệu | Settings | Core | P1 | Xóa dữ liệu, consent, thiết bị |
| `SB-099` | Trợ giúp & câu hỏi thường gặp | Support | Core | P1 | Hủy, dị ứng, pickup, vấn đề merchant |
| `SB-100` | Tác động cá nhân | Impact | Core | P1 | Lần đã nhận, tiền tiết kiệm từ đơn hoàn tất |

### Quy tắc thiết kế màn từ Registry

**Với mỗi `SB-ID`, agent phải xác định contract vận hành trước khi vẽ:** mục tiêu, entry/preconditions, content, CTA/back, states/data, edge cases, reusable components, transitions và dữ liệu cần đo khi hợp lý. Bảng trên là **screen index**, không thay thế design contract. **Mặc định ghi contract ngay trong `docs/experience.md` hoặc mục/nhóm feature tương ứng**, chỉ tách thành `docs/screens/<feature>.md` khi nội dung thật sự dài hoặc có nhu cầu chỉnh độc lập thường xuyên. Không tự tạo 100 file `SB-XXX.md`; ID màn ổn định nằm trong registry/Figma, không là tên file docs.

**Checklist một `SB-ID` được đếm:**

1. Một node `FRAME` ở trang high-fi trong file Figma đúng, có khung mobile chuẩn và tên chứa ID.
2. Thành phần quan trọng editable, component reusable và được bind vào tokens, không flatten ảnh UI.
3. Không tràn text tiếng Việt, không thông tin demo gây hiểu nhầm, không tên/giá/địa điểm vô căn cứ được gắn là merchant thật.
4. Màn có ít nhất một đường vào/ra hoặc là state đối ứng có thể chứng minh; `orphan=true` bị chặn, trừ trang demo đặc biệt có lý do.
5. Chứng cứ QA: screenshot mới nhất + node ID + checks thực hiện + kết quả; nguồn thiết kế được ghi registry.
6. Lifecycle dùng đúng `QA_PASS`, `DESIGN_REVIEW`, `DONE` như workflow/registry. Chỉ DONE sau QA đủ phạm vi và owner acceptance; pilot PASS_WITH_LIMITS vẫn là DESIGN_REVIEW.

**Đề xuất delivery batches** (không nhất thiết liên tiếp ID vì ưu tiên flow):

- Pilot được duyệt cho phiên bootstrap: `SB-015` danh sách, `SB-034` chi tiết món, `SB-051` chọn khung nhận, `SB-053` tóm tắt, `SB-056` thành công mô phỏng. Đây là subset; owner review trước khi có baseline.
- Batch P0 tiếp theo: Guest/login, filters, offer transparency, pickup slots, summary, success, pickup code, expired/error/recovery.
- P1: location/search/favorites, full reservation variations, order support, Pantry core, account core.
- P2: extended reviews, richer Pantry suggestions/log; tạo đủ 100 frames thực chất.
- Việc thiết kế low-fi diễn ra trước khi khóa high-fi; agent không được vì đã có 100-frame list mà bỏ qua low-fi và prototype/video tương ứng.

---


## Contracts của pilot được duyệt

Dữ liệu chung: `fixture-bakery-01`, merchant `merchant-demo-a`, offer EXACT_ITEM “Bánh mì men tự nhiên”, giá 25.000đ, 1 phần; giá gốc không có evidence nên không hiển thị. Stock 3 phần là fixture. Khu học xá và điểm nhận A hư cấu, không đại diện đối tác thật. Đồng hồ fixture cố định 16:00 ngày 19/10/2026, Asia/Ho_Chi_Minh; slot 17:00–18:00, còn 1 giờ đến lúc bắt đầu. Không suy diễn dị ứng: ingredients/allergens UNKNOWN. Ảnh AI minh họa `food-sourdough-generated-v05` có provenance trong manifest; không đại diện ảnh merchant thật. Subset bắt đầu sau khi giả định người dùng đã đăng nhập; chưa tạo auth và không dùng pilot để chứng minh guest-to-login. Số lượng cố định 1 phần, khung 17:00–18:00 được chọn sẵn; chưa kiểm khả năng đổi số lượng/khung giờ.

| ID | Mục tiêu và entry | Nội dung / CTA / back | States và edge cases ngoài subset | Mapping / measurement |
|---|---|---|---|---|
| SB-015 | Chọn offer từ danh sách; entry pilot start, khu vực chọn tay | Giá, còn phần, merchant, giờ nhận; card → 034; 4 tabs đúng labels | Loading/empty/error/GPS fallback phải có khi mở rộng; không xin GPS trong pilot | Mapping thực: screens.csv → components.csv; impression/detail rate chưa thu |
| SB-034 | Hiểu EXACT_ITEM trước đặt; từ 015, trạng thái available demo | Mô tả món, ảnh minh họa licensed, giá, tồn, pickup, điểm nhận, unknown allergens; Đặt trước → 051; back → 015 | Sold out/expired/offline/allergy warning; không khẳng định an toàn hoặc merchant verified | Mapping thực: screens.csv → components.csv; detail-to-reserve chưa thu |
| SB-051 | Chọn slot; từ 034, giả định đã đăng nhập và quantity=1 | Ngày, slot 17–18 selected, thời điểm bắt đầu còn 1 giờ, địa điểm, hạn hủy; Tiếp tục → 053; back → 034 | Slot hết hạn/không còn chỗ phải khóa; chỉ một slot hợp lệ ở fixture | Mapping thực: screens.csv → components.csv; selection chưa thu |
| SB-053 | Kiểm tra giá/slot/terms trước confirm; từ 051 | 1×25.000đ, tổng 25.000đ, tại quầy, pickup, allergy unknown và hủy trước 17:00; Đặt trước (demo) → 056; back → 051 | Stock/price changed, retry idempotency và double submit ngoài backend subset; không charge online | Mapping thực: screens.csv → components.csv; completion chưa thu |
| SB-056 | Xem hướng dẫn và mã nhận demo; từ 053 bằng mô phỏng | Mã DEMO-A125, ID DEMO-001, nhận 17–18, 25.000đ tại quầy; Khám phá tiếp → 015; back → 053 | Mã không dùng giao dịch thật; merchant/server verification, expired và offline cache ngoài subset | Mapping thực: screens.csv → components.csv; không ghi pickup/impact thật |

QR vector ở pilot chỉ mã hóa SAVEBITE-DEMO:DEMO-001:NOT-A-REAL-ORDER, có nhãn minh họa và mã DEMO-A125; không dùng nhận món thật. Thiết kế mã nhận cho flow đầy đủ thuộc SB-063 ở batch sau; triển khai xác thực backend nằm ngoài repo. Prototype subset bỏ qua SB-050/052/054/055 để kiểm tra liên kết công cụ, không thay flow F-01 đầy đủ. Các controls ngoài đường pilot chưa mô phỏng đầy đủ và phải được nói rõ trong báo cáo QA.

Fixture phụ fixture-croissant-02 chỉ nằm ở SB-015: bánh sừng bò, 30.000đ, còn 2 phần, nhận 17:00–18:00, cùng merchant giả lập. Không liên kết sang detail của offer khác; ngoài đường click-through pilot.

### Ranh giới tương tác của pilot

Chuỗi đang review: `SB-015 → SB-034 → SB-051 → SB-053 → SB-056 → SB-015`. Đây là click-through đặt trước mô phỏng; F-01 đầy đủ chưa hoàn thành. Các CTA/back nằm trong bảng contract phía trên; search/filter/category/favourite/notification/tabs và offer phụ đang tĩnh.

Back từ SB-056 về SB-053 là đường review prototype, không chứng minh đơn thật có thể chỉnh sau xác nhận. Cả 9 hotspots tiến/lùi đã bấm trong prototype v0.5 và kiểm URL sau mỗi chuyển màn. Mapping node/component phải đọc registry + evidence trước khi sửa canvas.

Khi mở rộng, định nghĩa auth, stock/error và post-confirm navigation trước khi tạo màn; không suy diễn hành vi production từ đường back của pilot. Controls ngoài subset được ghi rõ trong tài liệu review, không claim đã hoạt động. Copy safety, giá và slot phải khớp product.md/fixture; thay hành vi nghiệp vụ cần decision.

### Quy tắc mở rộng từ pilot

Mỗi màn mới phải có contract trước khi vẽ: mục tiêu, entry, fixture, CTA/back, states và cách kiểm. Reuse component bằng properties/variants; không đổi nghĩa của SB-ID hoặc nhân bản màn để đủ số lượng. Một batch 5–8 màn chỉ bắt đầu sau khi owner chấp nhận baseline pilot. Dữ liệu của cùng offer/đơn phải khớp ở discovery → detail → summary → pickup.
