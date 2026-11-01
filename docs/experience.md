# Trải nghiệm, luồng và 100 màn

Nguồn chuẩn theo domain cho Kiến trúc Thông tin (IA), Luồng người dùng (`F-01..F-06`) và Danh mục 100 `SB-ID`. Đọc cùng [router](README.md), [ma trận định hướng thị giác 100 màn](screen-art-direction.md), [chuẩn iOS HIG](ios-guidelines.md), [visual direction](visual-direction.md) và [tiến độ](../tracking/progress.md) trước khi thay đổi.

## IA, NAVIGATION VÀ MAIN FLOWS

### Thông tin điều hướng

DEC-037–039:[final UI/native navigation checkpoint](../tracking/final-color-icons-checkpoint.md). Interrupted fresh-tab migration repaired22 callers,correct selected tab per group,canonical destinations and existing conditional Pantry entry from live190:4390.023–027 backdrop tabs stay noninteractive. Header50pt targets match fresh heart/bell/filter geometry;original callbacks retained. Scoped Present checks are recorded separately from full6-flow verification.

DEC-035:[native27 fit/device pass](../tracking/native27-device-checkpoint.md).009 keyboard307pt/CTA477;019 keyboard307pt;020 viewport410pt/keyboard307pt. Existing Gửi→010,Tìm→020 and Xong visibility callbacks retained. Shared AppBar back hit area40→44 with native glass; no route change.100 rounded/clipped roots reviewed at393×852.055 spinner changes only loading presentation,not timing or reservation outcome.

DEC-036 fresh instance replacement keeps same callbacks/020 visible-variable binding;new keyboard IDs791:8389/8498/8597. Alphabet glyphs checked enlarged and in Present020,not inferred from key-container bounds. Old keyboard instances removed;all100 current component mappings refreshed after unused-library cleanup.

Imagery/Apple27 review01/11 (DEC-032/033):009/019/020 preserve existing return handlers and020 keyboard-visible flag with genuine native27 keyboards.091/092 share a sourced stock persona portrait. Meal/context photography and218 capsule action instances reconciled; no route or SKU change in this batch. [Fresh100 default-root visual review](../tracking/vn-final-ui-checkpoint.md) delivered for owner review. This is not a full keyboard/input, persistence or business-logic test.

Cluster UI01/11 (DEC-031):[30 revised roots/100 captures](../tracking/cluster-ui-checkpoint.md).013 header login→008;075/076 overflow→089/090;095/096 header preferences→097;033 header search→019. Remove repeated footer controls.028–030 show actual food choices222pt earlier;031 offers ordered by pickup time.078 native077 context behind sheet.071 primary Orders060/secondary Explore015;092 Save→091.099 inline FAQ answers do not open cancellation or date editing.100 registry edges refreshed from visible/variable-bound live reactions; read-back does not establish full flow correctness. Existing owner exclusion of full logic testing remains.

Apple27 final UI01/11 (DEC-029/030):22 floating-nav callers;075 two Popup filters/status+storage+active.085/097 native Switch;079 Inline Calendar/Segments/Glass arrows;016 glass controls;089/095 native rows/longer fixture lists;070 order context behind cancel sheet. Scoped Pantry scroll and Splash→002 preview reset verified. [UI evidence](../tracking/apple27-e2e-checkpoint.md). Full logic deferred by owner; Present render limitation OPEN, no full flow acceptance.

Home/Pantry01/11 (`DEC-027`):005 khám phá→013;008 login thường→015,còn pending offer→034 giữ nguyên.013/015 cùng market;014 reuse cùng core layout và thêm pending strip.018 có area selection demo/header sync,GPS tùy chọn→011.077/079/080 và081/082/085/086/087 được ràUI;087 reason và095 filters cóselected states,40 choice controls sửa ở [checkpoint](../tracking/selected-states-checkpoint.md).075 trước bị từ chối; đã redesign theo hướng owner chọn tại DEC-028.014/015 có greeting nhẹ,014 pending card→062;075 hero minh hoạ/count,hai nhãn hạn riêng,storage selector vàAdd→077 giữ. [Checkpoint mới](../tracking/visual-refinement-checkpoint.md). Không full prototype PASS; Present đôi lúc thiếu static layers sau filter.

Correction ảnh owner01/11 (`DEC-024`):019/020 dùng chung SearchField16:18,019 bỏ scroll/clipping dư để history title không bị cắt.023–026 cùng native Discovery backdrop,027 result backdrop, system bars Apple source áp7 màn. [Evidence/Present limitation](../tracking/apple-consistency-checkpoint.md):navigation/state demo đã bấm nhưng render có lúc thiếu lớp sau transition tới khi reload; không full Present PASS.

Search repair01/11 (`DEC-023`):019 Tìm→020 với query demo “bánh”;020 Xong đóng bàn phím, chạm Search mở lại.023 đổi loại ưu đãi/Reset cục bộ;027 chọn sort/Apply→021. Các thao tác này đã bấm trong IAB đã kết nối; không coi đó là query engine, lưu đủ bộ lọc hay reorder nhiều kết quả. [Checkpoint repair](../tracking/search-sort-repair-checkpoint.md), owner review pending.

Account/Impact01/11: card091→100 giữ; hotspot Back100→09148pt được kiểm Present.100 hiển thị3 đơn mẫu25K/30K/35K và90K **đã trả**, không suy ra savings/trend/CO₂. [UI checkpoint](../tracking/impact-ui-checkpoint.md); không phải dữ liệu người dùng thật.

**Root:** initial load → onboarding (lần đầu) → optional guest/login → Home.  
**Tabs:** Khám phá, Đơn của tôi, Tủ thực phẩm, Tài khoản.  
**Deep links:** offer, store, reservation, pickup code, pantry item (local links) và help.  
**Overlays:** filter, location selector, confirmation, warning, actions, add-to-favorites; không phải tất cả overlays đều là screen được đếm.

Map adoption01/11 (`DEC-022`):003/011/016/017/032/039/065/094 giữ root và các đường bấm, thay nền qua MapCanvas16:3;039/065 không vẽ tuyến chưa xác nhận,094 giữ tâm khu vực thay vì tuyên bố GPS. [Evidence](../tracking/map-adoption-checkpoint.md); Present sau thay nền chưa chạy.

Filter correction01/11 (`DEC-021`):023 có đường mở024/025/026, các Save quay023 và Apply giữ đích021; đây mới là reaction readback, chưa Present. [Checkpoint UI](../tracking/filter-ui-checkpoint.md) giữ roots và sửa hierarchy/bounds; chọn/lưu/reset/custom/tập kết quả/Back-state chưa hoàn tất.024 dùng presets30K/50K/tùy chỉnh/không giới hạn, không biểu đồ thiếu dữ liệu;026 nhắc xác minh thành phần trước khi đặt.

### Flows mục tiêu khi mở rộng sau pilot

**F-01 — Guest → rescue (PRIMARY, bắt buộc chạy end-to-end)**  
`Splash → Browse as Guest → Khám phá → Lọc dưới 50k → Detail (thông tin/dị ứng/slot) → Login (nếu cần) → Trở về cùng offer → Chọn số lượng → Chọn giờ nhận → Summary → Xác nhận giữ chỗ → Thành công → Đơn đang nhận → Mã nhận → Merchant verification simulated → Hoàn tất → Impact`.

**F-02 — Explore map/list**  
`Khám phá → Map → Tap pin → Quick preview → Offer Detail → Directions/Reserve`.

Map UI01/11 (`DEC-017`):016→017 dùng cùng offer context;017 đổi pin cập nhật ảnh/merchant/giá/slot, CTA “Xem chi tiết món” tới034.039/065 hiện là sơ đồ minh họa, không chứng minh dẫn đường GPS/ETA;094 có state bán kính trực quan. [Batch và giới hạn QA](../tracking/map-ui-checkpoint.md); chưa F-02 end-to-end PASS.

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
| `SB-035` | Thư viện ảnh món | Offer | Core | P1 | Ảnh theo SKU, chú thích minh bạch; DEFAULT DEC-020 dùng FIT/FILL của cùng ảnh, chưa zoom/pan tự do hoặc nhiều ảnh đã xác minh |
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
| SB-075 | A8 | Smart Pantry · gian bếp nhẹ | LargeTitleBar; PantryOverviewHero88pt/Mầm64pt/count; two Apple27 Popup filters in one row; seven canonical icon rows112pt, semantic date badges and neutral Dùng/Bỏ actions; floating native BottomNav. No freshness score. DEC-030 supersedes old summary/progress. |
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

Pantry correction31/10 (DEC-016): prototype giữ trạng thái riêng cho bảy fixture canonical; chọn món nạp dữ liệu đã lưu, sửa lượng/ngày hạn/nơi cất dùng bản nháp. Lưu mới ghi về danh sách/chi tiết; quay lại không ghi nháp. Dùng một phần giữ món, dùng hết/đã bỏ gỡ khỏi danh sách đang theo dõi và tắt nhắc của món; lịch sử ghi thao tác mô phỏng, không giả lưu thiết bị hoặc gửi push thật. Ngày hạn là dữ liệu trên nhãn, không phải điểm an toàn hay khuyến nghị dùng trong48h. Nhập văn bản tự do và push thật chưa được chứng minh.

F-05 completion batch31/10: **WIP / chưa xác minh; Present QA có lỗi drift dữ liệu, xem [checkpoint](../tracking/f05-wip-checkpoint.md).** thêm một fixture từ form vào tủ với name/unit/category/date/storage đồng bộ qua080→075→081; first-run074 khởi tạo tủ trống một lần, Back của form trở về empty/populated theo state. Reminder085 chỉnh bật/tắt, trước1/2 ngày và07:30/17:30 theo giờ Việt Nam; chỉ Lưu ghi về món. Chưa có ngày hoặc đã qua ngày hạn thì không bật lịch nhắc tương lai. Dùng hết/đã bỏ tắt cờ reminder; lịch thật và permission OS nằm ngoài khả năng prototype.
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

### Quy tắc thiết kế màn từ Registry & Kết nối với 10 Screen Archetypes

**Với mỗi `SB-ID`, agent bắt buộc đối chiếu đồng thời 2 nguồn trước khi vẽ:**
1. **Contract vận hành (trong tài liệu này):** mục tiêu, entry/preconditions, content, CTA/back, states/data, edge cases, reusable components, transitions và dữ liệu cần đo khi hợp lý.
2. **Định hướng thị giác & Archetype (`A1`–`A10`) trong [screen-art-direction.md](screen-art-direction.md):** tâm điểm thị giác (1st Read), cấu trúc bố cục chống rập khuôn, loại thanh điều hướng iOS ([ios-guidelines.md](ios-guidelines.md)) và tài nguyên ảnh/icon chuẩn ([asset-strategy.md](asset-strategy.md)).

Bảng trên là **screen index nghiệp vụ**, còn [screen-art-direction.md](screen-art-direction.md) là **bản thiết kế kiến trúc thị giác cho từng màn trong 100 màn**. Mặc định ghi contract chi tiết ngay trong `docs/experience.md` theo từng đợt batch, không tự tạo 100 file `SB-XXX.md` rời rạc.

**Checklist một `SB-ID` được đếm (Technical + Aesthetic):**

1. Một node `FRAME` ở trang high-fi trong file Figma đúng, có khung iPhone chuẩn (có `iOSStatusBar` ở đỉnh và `iOSHomeIndicator 34pt` ở đáy theo [ios-guidelines.md](ios-guidelines.md)) và tên chứa ID.
2. Đúng **Screen Archetype (`A1`–`A10`)** đã quy định trong [screen-art-direction.md](screen-art-direction.md); không vi phạm 10 quy tắc chống Boxitis trong [visual-direction.md](visual-direction.md) (không lồng card trong card, không lặp tiêu đề kép, không dùng trùng 1 ảnh ở 2 nơi trên cùng màn hình).
3. Thành phần quan trọng editable, component reusable và được bind vào tokens, không flatten ảnh UI.
4. Không tràn text tiếng Việt, không thông tin demo gây hiểu nhầm, không tên/giá/địa điểm vô căn cứ được gắn là merchant thật.
5. Màn có ít nhất một đường vào/ra hoặc là state đối ứng có thể chứng minh; `orphan=true` bị chặn, trừ trang demo đặc biệt có lý do.
6. Chứng cứ QA: screenshot mới nhất + node ID + **Technical QA PASS** + **Aesthetic Rubric PASS** (xem [workflow.md](workflow.md)); nguồn thiết kế được ghi registry.
7. Lifecycle dùng đúng `QA_PASS`, `DESIGN_REVIEW`, `DONE` như workflow/registry. Chỉ DONE sau khi đạt cả Technical QA, Aesthetic QA và owner acceptance; pilot PASS_WITH_LIMITS vẫn là DESIGN_REVIEW.

**Đề xuất delivery batches** (không nhất thiết liên tiếp ID vì ưu tiên flow):

- Pilot được duyệt cho phiên bootstrap: `SB-015` danh sách, `SB-034` chi tiết món, `SB-051` chọn khung nhận, `SB-053` tóm tắt, `SB-056` thành công mô phỏng. Đây là subset; owner review trước khi có baseline.
- Batch P0 tiếp theo: Guest/login, filters, offer transparency, pickup slots, summary, success, pickup code, expired/error/recovery.
- P1: location/search/favorites, full reservation variations, order support, Pantry core, account core.
- P2: extended reviews, richer Pantry suggestions/log; tạo đủ 100 frames thực chất.
- Việc thiết kế low-fi diễn ra trước khi khóa high-fi; agent không được vì đã có 100-frame list mà bỏ qua low-fi và prototype/video tương ứng.

---


## Contracts của 10 màn đại diện Phase 1 (`DEC-011` · `7suZz9C8oL5zV2NMxlsIVI`)

Dữ liệu chung: bộ 6 ảnh Pexels thật đã xác minh trong `assets/manifest.json` (`fixture-bakery-01`, `fixture-croissant-02`, `fixture-meal-03`, `fixture-veggie-04`, `fixture-surprise-05`, `fixture-store-01`). Đồng hồ fixture cố định `16:00` ngày `19/10/2026`, `Asia/Ho_Chi_Minh`; khung giờ nhận chính `17:00–18:00` (còn 1 giờ đến lúc mở nhận). Khung thiết bị chuẩn **iPhone 15 (`393×852pt`, Dynamic Island `59pt`, Home Indicator `34pt`)**. Không suy diễn dị ứng (`UNKNOWN` khi cửa hàng chưa khai báo).

| ID | Archetype | Mục tiêu & Entry | Nội dung, Components & CTA/Back |
|---|---|---|---|
| `SB-002` | `A1` | Onboarding 1 — Truyền tải giá trị cứu thực phẩm giàu cảm xúc | Micro-UI Card Collage (`fixture-bakery-01` `25.000đ` + badge `Cứu món ngon cuối ngày`), Display `30/36 Bold`, `PageDots (1/3)`, nút `Tiếp tục` (`Button/Primary`) và `Bỏ qua` (`Button/Secondary`). |
| `SB-015` | `A3` | Khám phá — Trang chợ ưu đãi đa nhịp điệu | `BrandHeader` (`Đà Nẵng · Khu học xá`), Apple Search + Filter48pt,4 CategoryTile, promo túi bánh (`fixture-surprise-05`29K/18–19→044), lưới2 OfferCard169×246 (bánh25K & croissant30K, giờ17–18 hiển thị trước nav),1 OfferListRow (meal35K/17:30–19), BottomNav. DEFAULT theo DEC-019, chưa owner acceptance. |
| `SB-016` | `A4` | Bản đồ — Khám phá không gian trực quan quanh trường | `MapCanvas` vector ấm toàn màn hình, `MapPricePin` (`25.000đ` Selected `#B34021`, `30.000đ`, `35.000đ` Default `#004337`), thanh `SearchField` nổi kính mờ, thẻ xem nhanh `OfferListRow` ở đáy + `BottomNav`. |
| `SB-019` | `A5` | Tìm kiếm — Trải nghiệm iPhone-native với bàn phím thật | `SearchField` (Focused), chip từ khóa gần đây (`bánh mì men tự nhiên`, `cơm chiều dưới 35k`), lối tắt theo ca học (`Dưới 30.000đ`, `Nhận 17:00–18:00`), `iOSKeyboard` (`393×291pt`) + `iOSHomeIndicator`. |
| `SB-034` | `A6` | Chi tiết offer — Món cụ thể ấn tượng, mặt phẳng mở | Ảnh `food-sourdough-461060` full-bleed `393×300pt` (`y=0`) + `MediaOverlayBar`, tấm nội dung `#FFFCF6` bo góc `28pt`, giá `25.000đ` + `Còn 3 phần`, `MerchantRow` & `PickupInfo` ngăn cách bằng đường kẻ `1pt`, `AllergenNotice (UNKNOWN)`, đáy là Split Sticky Dock (`25.000đ · Trả tại quầy` + `Button/Primary` `Chọn giờ nhận`). |
| `SB-051` | `A7` | Chọn khung giờ nhận — Tương tác tinh tế, không lặp tiêu đề | `AppBar` (`Chọn giờ nhận`) + `ReservationProgress (Bước 1/2)`, dải `OfferSummary` gọn, `PickupSlot` (`17:00–18:00` Selected `#004337` vs `15:00–16:00` Expired), `MerchantRow` phẳng, điều khoản hủy trước `17:00` + `Button/Primary` (`Tiếp tục`). |
| `SB-053` | `A7` | Tóm tắt đặt trước — Biên lai giấy đứt nét đáng tin cậy | `AppBar` (`Kiểm tra đặt trước`) + `ReservationProgress (Bước 2/2)`, `UnifiedReceiptCard` (tích hợp `OfferSummary` + đường đứt nét + bảng tính tiền `1 phần × 25.000đ`, `Phí đặt giữ chỗ: 0đ`, `Cần thanh toán tại quầy: 25.000đ` — không card-in-card), `AllergenNotice (UNKNOWN)` + `Button/Primary` (`Đặt giữ chỗ (demo)`). |
| `SB-056` | `A7` | Đặt trước thành công — Vé nhận món đục lỗ & QR căn giữa | `AppBar` (nút đóng `×`), Celebration Header (`Đã giữ 1 phần cho bạn!`), `PerforatedPickupPass` có khuyết bán nguyệt `16pt` hai bên hông, `DemoQR` căn giữa tuyệt đối trên nền trắng, mã `SB-A125` Monospace `22pt Bold`, `Button/Secondary` (`Xem chỉ đường`) + `Button/Primary` (`Về trang Khám phá`). |
| `SB-075` | `A8` | Smart Pantry — Thẩm mỹ gian bếp ngăn nắp, khác biệt chợ | `LargeTitleBar` (`Tủ thực phẩm`), `FreshnessSummaryBanner` (`2 cần dùng sớm · 4 còn hạn tốt · 1 quá hạn`), chip lọc ngăn lưu trữ, 4 hàng `PantryItemRow` có `Expiry Progress Bar` (phân biệt `Hạn sử dụng` vs `Nên dùng trước`) và nút `Đã dùng`, `BottomNav`. |
| `SB-091` | `A9` | Tài khoản — Quản lý hồ sơ & tác động thực chứng | `LargeTitleBar` (`Tài khoản`), `ProfileHeaderCard` (`Minh Anh · Khu học xá ĐH Đà Nẵng`), `ImpactHeroCard` (`3 đơn đã nhận · 4 món Pantry dùng kịp hạn` theo `D-016`), bảng cài đặt iOS Inset Grouped List trên nền `#F4EFE6`, `BottomNav`. |
