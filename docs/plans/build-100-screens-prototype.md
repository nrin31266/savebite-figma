# Plan 2 · Dựng đủ 100 màn và nối prototype chuyển màn

Kế hoạch sản xuất 90 màn còn lại trên [SaveBite-V2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1) và nối toàn bộ 100 màn thành prototype bấm được theo 6 flow `F-01..F-06`. Nguồn yêu cầu: [experience](../experience.md) (flow, 100 SB-ID, contract), [screen-art-direction](../screen-art-direction.md) (archetype, focal point, components từng màn), [visual-direction](../visual-direction.md), [ios-guidelines](../ios-guidelines.md), [design-system](../design-system.md), [asset-strategy](../asset-strategy.md), QA trong [workflow](../workflow.md).

Trạng thái: `IN_PROGRESS` theo `DEC-012` · [Plan 1](phase1-fix-sb002-sb034.md) và 30 màn cũ phải được kiểm lại, không mặc nhiên hoàn tất.

> Cập nhật31/10/2026: live inventory39/100 root, chưa coi là đã hoàn tất QA;61 màn thiếu gồm [Plan A](batch-A-entry-discovery-offer.md)36 và [Plan B](batch-B-orders-pantry-account.md)25 (9 root đã có ngoài registry cũ). Workers cô lập Section và mutation windows theo progress; audit/fix màn cũ cùng scope. Interaction Map ở mục7 vẫn là nguồn chuẩn cho reaction, không phải bằng chứng đã nối/chạy.

---

## 1. Gate mở khóa

**Cập nhật `DEC-012` (31/10/2026):** owner đã yêu cầu triển khai end-to-end, gồm audit/fix 30 màn đang có, tài nguyên dùng lại và toàn bộ phần còn thiếu. Không cần chờ duyệt Phase 1 để tiếp tục sản xuất. Đây không phải nghiệm thu thẩm mỹ: `design_baseline_version` để trống và không chuyển DONE cho tới khi có QA + owner acceptance thật.

Điều kiện thực thi vẫn bắt buộc:
1. Đọc live/reconcile màn và component trước tạo, audit/sửa lỗi trước nhân rộng; không coi 30 màn DESIGN_REVIEW là hoàn tất.
2. Xác minh quyền đọc/ghi thật, lease writer rõ, chỉ thay đổi trong scope, giữ nghiệp vụ/fixture.
3. Registry/evidence phải phản ánh kiểm tra thực; thiếu Present mode không ghi prototype_verified=true.
4. ~~Owner chọn phương án cho giới hạn prototype liên-page~~ **✅ Đã quyết (31/10/2026):** Owner chọn **Phương án A** (gộp page) → `DEC-013` đã ghi và thực thi: 4 page hi-fi gộp thành 1 page `App · All Screens` (`11:3`, 4 Section). Mọi batch từ đây dựng trực tiếp trên page `11:3`, đúng Section theo dải `SB-ID`.

### 0. ⚠️ Giới hạn đã xác nhận: Figma Plugin API không nối được prototype liên trang

Phát hiện khi thực thi Plan 1 (31/10/2026): `node.setReactionsAsync()` từ chối mọi `NODE`/`NAVIGATE` reaction có đích nằm ở page khác với nguồn — thông báo lỗi trực tiếp từ Figma: *"for NAVIGATE actions, destinations must be a different top-level frame on the same page"*. Đã thử và bị từ chối thật: `SB-015→SB-034`, `SB-016→SB-034`, `SB-019→SB-034`, `SB-034→SB-051`, `SB-015→SB-075/091`. Đây là giới hạn gốc của mô hình prototyping Figma ("prototypes are per-page"), không phải lỗi script hay có thể retry.

**Tác động:** Kiến trúc 4-page hiện tại (`workflow.md` §"Kiến trúc Cô lập 6 Pages", `01 Entry&Discovery` / `02 Offer&Merchant` / `03 Reserve&Orders` / `04 Pantry&Account`) khiến **toàn bộ 6 flow `F-01..F-06`** ở mục 6 bên dưới đi xuyên ít nhất 2 page — nghĩa là phần lớn bảng Interaction Map ở mục 7 **không thể nối bằng Plugin API** nếu giữ nguyên 4 page. Ví dụ F-01 một mình đã đi qua cả 4 page.

**3 phương án cho owner chọn (không tự quyết):**

| Phương án | Mô tả | Đánh đổi |
|---|---|---|
| **A. Gộp page theo flow** | Dồn các page có flow chính xuyên suốt vào cùng 1 page (ví dụ gộp 4 page hiện tại thành 1–2 page lớn hơn theo nhóm flow F-01/F-05, không theo nhóm nghiệp vụ như hiện tại) | Mất kiến trúc cô lập 50/50 cho 2 agent độc lập trong `workflow.md`; canvas 1 page rất lớn, khó quản lý thủ công |
| **B. Giữ 4 page, nối liên-page thủ công trong Figma app** | Giữ nguyên kiến trúc; mỗi page có flow starting point riêng; các điểm chuyển page (ví dụ `SB-034 → SB-051`) được owner hoặc người có quyền Editor tự kéo nối bằng tay trong Figma Desktop/web (nối liên-page **có** hỗ trợ ở UI thật của Figma, chỉ Plugin API của phiên này bị chặn) | Prototype demo cần 1 bước thủ công ngoài agent; agent không tự xác minh được các link này, phải ghi rõ "pending:cross-page" và owner tự QA |
| **C. Hybrid — gộp các cặp page có traffic cao nhất, còn lại dùng B** | Ví dụ gộp `02 Offer & Merchant` với `03 Reserve & Orders` (traffic F-01 cao nhất: offer → reservation) thành 1 page; giữ `01` và `04` riêng, nối thủ công 2 điểm còn lại (`013→034`, `056→060`) | Cân bằng, nhưng vẫn cần ít nhất 1–2 thao tác thủ công |

Plan 2 mặc định đề xuất **Phương án B** (rủi ro thấp nhất, không phá kiến trúc đã duyệt) nhưng **chờ owner xác nhận** trước khi Batch B1 bắt đầu nối dây; cho tới lúc đó, 90 màn vẫn được **thiết kế và đặt đúng page** theo kiến trúc hiện tại, chỉ hoãn bước "nối reaction liên-page".

## 2. Page, phân công và lease

- **(`DEC-013`)** Một page duy nhất `App · All Screens` (`11:3`) chứa toàn bộ 100 màn hi-fi, tổ chức bằng 4 **Section**:

| Section | Dải màn |
|---|---|
| `01 · Entry & Discovery` | `SB-001..033` |
| `02 · Offer & Merchant` | `SB-034..049`, `SB-059` |
| `03 · Reserve & Orders` | `SB-050..058`, `SB-060..073` |
| `04 · Pantry & Account` | `SB-074..100` |

- Trong mỗi section, xếp frame theo hàng ngang theo flow (cách nhau 80pt), các dải `y` khác nhau giữa 4 section để không chồng lấn (xem toạ độ hiện có trong Figma live trước khi thêm frame mới).
- Mặc định **1 agent ghi Figma**. Chỉ chia 2 agent (50/50 theo Section như [workflow](../workflow.md)) khi owner yêu cầu; vì chỉ còn 1 page, 2 agent cần tránh ghi gần như đồng thời vào vùng canvas sát nhau (rủi ro race condition), không còn ranh giới Page để cô lập tự nhiên.
- Lease ghi ở [progress](../../tracking/progress.md) mỗi batch: owner, section, SB-ID, giờ bắt đầu, giờ release.

## 3. Component cần có trước Batch 1

Đã có 29 components ([components.csv](../../tracking/components.csv)). Bổ sung theo [design-system](../design-system.md) §2.2, mỗi cái có variants và đăng ký registry trước khi dùng:

| Component | Variants chính | Dùng ở |
|---|---|---|
| `Icon/*` (Phosphor) | `Weight=Regular/Fill/Duotone` | Toàn bộ |
| `Button` | thêm `Destructive`, `Tertiary`, `State=Disabled/Loading` | `SB-046..049`, `055`, `070` |
| `StickySplitDock` | `State=Default/Urgent/Disabled` | `SB-034`, `044`, `046..049` |
| `SheetContainer` + `iOSSheetGrabber` | `Height=Compact/Medium/Large` | `SB-023..027`, `036`, `037`, `045`, `050`, `054`, `059`, `070`, `078`, `079`, `086`, `087` |
| `SegmentedControl` | 2/3 segment | `SB-016`, `033`, `060`, `025` |
| `TextField` | `Default/Focused/Filled/Error/Disabled` | `SB-006..009`, `069`, `077`, `082`, `092`, `094` |
| `FilterChip` | `Selected=True/False`, icon | `SB-019..027`, `075`, `095` |
| `EmptyState` / `ErrorRecoveryCard` | `Kind=Empty/NoResult/NetworkError/StockChanged/Expired/Cancelled` | `SB-022`, `055`, `057`, `058`, `068`, `071`, `073`, `076`, `096` |
| `PerforatedPickupPass` | `PassState=Confirmed/Ready/Completed/Expired` | `SB-056`, `062..068`, `072` |
| `QuantityStepper` | `Value`, `Max` | `SB-050`, `058` |
| `ExpiryStatusTag` / `UsageFractionSelector` / `PantryCategoryTile` | theo `Freshness`, `DateType` | `SB-074..090` |
| `iOSSwitchRow` / `iOSGroupedSection` | `On/Off` | `SB-091`, `097`, `098` |
| `NotificationRow` | `Type=Pickup/Pantry/Safety`, `Read=True/False` | `SB-095` |

## 4. Thứ tự batch

Ưu tiên P0 theo flow để F-01 chạy được sớm (workflow Phase 4: "đừng đợi màn 100 mới nối dây"). Mỗi màn: tra archetype và component ở [screen-art-direction](../screen-art-direction.md), viết contract ngắn vào [experience](../experience.md) trước khi vẽ.

| Batch | Phạm vi | SB-ID | Mục tiêu |
|---|---|---|---|
| B1 | F-01 lõi P0 | `001, 005, 008, 013, 050, 054, 055, 059, 060, 062, 063, 072, 100` | F-01 chạy end-to-end |
| B2 | Recovery P0 | `022, 046, 047, 049, 057, 058, 067, 068, 070, 071` | F-03, F-04 |
| B3 | Discovery, search, filter | `014, 017, 018, 020, 021, 023, 024, 025, 026, 027` | F-02, F-06 |
| B4 | Offer trust & merchant | `035..045, 048` | Trang offer/merchant đầy đủ |
| B5 | Entry, auth, permission | `003, 004, 006, 007, 009, 010, 011, 012` | Onboarding + auth |
| B6 | Category & favorites | `028..033` | Nhịp A3 khác nhau |
| B7 | Orders còn lại | `052, 061, 064, 065, 066, 069, 073` | Đủ nhánh Orders |
| B8 | Smart Pantry | `074, 076..090` | F-05 |
| B9 | Account & settings | `092..099` | Đủ tab Tài khoản |

Checkpoint sau B3 (~40 màn): rà gộp component trùng, nhất quán CTA/back/fixture giữa flow.

## 5. Quy ước prototype

> Mọi `Navigate`/`Move In`/`Smart Animate` dưới đây giả định nguồn và đích **cùng page**. Khi khác page, áp dụng phương án owner đã chọn ở mục 0 trước khi nối (mặc định Phương án B = để `notes` `pending:cross-page`, không tự tạo reaction).

- **Kích thước:** mọi frame `393×852`, Device = iPhone 15, nền prototype `#1E1E1E`.
- **Push (đi sâu):** `On tap → Navigate → Move In ←`, `Ease Out 300ms`. Back = action `Back`.
- **Tab bar:** `On tap → Navigate`, `Instant`. Đích theo vai: khách (`SB-013`) → Orders `SB-073`, Pantry `SB-074`, Account `SB-005`; đã đăng nhập (`SB-014`, `015`, `016`, `060`, `061`, `075`, `076`, `091`) → `SB-015`, `SB-060`, `SB-075`, `SB-091`.
- **Sheet:** màn sheet được đếm là frame đầy đủ (vẽ màn nền mờ scrim 40% phía sau sheet), nên dùng `Navigate → Move In ↑ 300ms`, đóng = `Back`. Không dùng overlay để đếm màn.
- **Modal hoàn tất (`SB-056`, `071`):** nút `×` → `Navigate` tới `SB-015` (không `Back`).
- **Tự chuyển:** `After delay` cho Splash (1200ms), xử lý giữ chỗ (`SB-055` 800ms) và mô phỏng thời gian trôi (`SB-067` 3000ms).
- **Hotspot demo ẩn:** chỉ 3 chỗ, đặt trong vùng không có nội dung, ghi trong mô tả frame: `SB-055` (→ `057` mất mạng, → `058` tồn kho đổi) và `SB-063` (nhân viên quét mã → `072`). Lý do: Figma không có backend để rẽ nhánh kết quả thật.
- **Signature moments** theo [visual-direction](../visual-direction.md) §6: `015→034` Smart Animate 320ms (đặt tên layer ảnh trùng nhau), `050/051` Ease Out 180ms, `053→055→056` Move In ↑ + scale huy hiệu, `016↔017` Smart Animate, `075→086` Move In ↑.
- **Hotspot ≥48×48pt;** mọi màn có ít nhất 1 đường vào và 1 đường ra (không orphan).

## 6. Flow starting points

| Flow | Tên trong Figma | Bắt đầu | Chuỗi chính |
|---|---|---|---|
| F-01 | `F01 \| Guest-to-Rescue \| v1` | `SB-001` | 001 → 002 → 003 → 004 → 011 → 012 → 005 → 013 → 023 → 024 → 023 → 021 → 034 → 059 → 050 → 051 → 053 → 054 → 055 → 056 → 062 → 063 → 072 → 100 |
| F-02 | `F02 \| Map Explore \| v1` | `SB-015` | 015 → 016 → 017 → 034 → 038 → 039 |
| F-03 | `F03 \| Stock Recovery \| v1` | `SB-053` | 053 → 054 → 055 (hotspot ẩn) → 058 → 053 → 054 → 055 → 056 |
| F-04 | `F04 \| Cancel & Expire \| v1` | `SB-062` | 062 → 070 → 071 → 015; nhánh 2 bắt đầu `SB-067`: 067 → 068 → 069 |
| F-05 | `F05 \| Pantry Local \| v1` | `SB-074` | 074 → 076 → 077 → 078 → 077 → 079 → 077 → 080 → 075 → 083 → 086 → 089 |
| F-06 | `F06 \| Location Denied \| v1` | `SB-011` | 011 → 018 → 015 → 091 → 098 → 011 |

## 7. Interaction Map đủ 100 màn

`→` = Navigate (Push trừ khi ghi khác), `Back` = action Back. Đích trong ngoặc là lối ra phụ.

| ID | Màn | Hành động chính → Đích | Lối ra phụ |
|---|---|---|---|
| `SB-001` | Splash | After delay 1200ms → `002` | Chip `Thử lại` (offline) → `001` |
| `SB-002` | Onboarding 1 | `Tiếp tục` → `003` | `Bỏ qua` → `005` |
| `SB-003` | Onboarding 2 | `Tiếp tục` → `004` | `Bỏ qua` → `005`; vuốt lùi → Back |
| `SB-004` | Onboarding 3 | `Bắt đầu sử dụng` → `011` | Back |
| `SB-005` | Cổng đăng nhập | `Khám phá ngay` → `013` | `Đăng nhập` → `008`; `Tạo tài khoản` → `006` |
| `SB-006` | Đăng ký | `Tạo tài khoản` → `007` | `Đã có tài khoản` → `008`; Back |
| `SB-007` | Chờ xác minh email | `Tôi đã xác minh` → `014` | `Đổi địa chỉ email` → `006`; Back |
| `SB-008` | Đăng nhập | `Đăng nhập` → `014` | `Quên mật khẩu` → `009`; `Đăng ký` → `006`; Back |
| `SB-009` | Quên mật khẩu | `Gửi liên kết khôi phục` → `010` | Back |
| `SB-010` | Đã gửi liên kết | `Quay lại Đăng nhập` → `008` | `Thử email khác` → `009` |
| `SB-011` | Quyền vị trí | `Cho phép vị trí` → `012` | `Tự chọn khu vực` → `018` |
| `SB-012` | Quyền thông báo | `Bật thông báo nhắc hẹn` → `005` | `Để sau` → `005` |
| `SB-013` | Home khách | Offer nổi bật → `034` | Chip `Dưới 50K`/lọc → `023`; `SearchField` → `019`; `Đăng nhập` → `008`; chuông → `096`; tab bar (khách) |
| `SB-014` | Home đăng nhập | Offer → `034` | Thẻ đơn đang chờ → `062`; rail Đang nhận sớm → `031`; chip Quanh trường → `032`; chuông → `095`; tim → `033`; khu vực → `018`; tab bar |
| `SB-015` | Khám phá | `OfferCard` → `034` (Smart Animate) | Category → `028`/`029`/`030`; Hero → `031`; `Bản đồ` → `016`; `SearchField` → `019`; icon lọc → `023`; tim → `033`; chuông → `095`; khu vực → `018`; tab bar |
| `SB-016` | Bản đồ | Pin `25.000đ` → `017` (Smart Animate) | Segment `Danh sách` → `015`; tab bar |
| `SB-017` | Xem nhanh pin | `Xem chi tiết` → `034` | Chạm bản đồ/đóng → `016` |
| `SB-018` | Chọn khu vực | `Xác nhận` → `015` | Back |
| `SB-019` | Tìm kiếm | Phím/chip `bánh` → `020` | Từ khóa gần đây → `021`; gợi ý → `034`; `Hủy` → Back |
| `SB-020` | Gợi ý tìm kiếm | Món `Bánh mì men tự nhiên` → `034` | Cửa hàng `Tiệm Bánh A` → `038`; phím `Tìm` → `021`; `Hủy` → Back |
| `SB-021` | Kết quả tìm kiếm | Hàng 1 → `034` | Hàng có cảnh báo dị ứng → `049`; chip lọc → `023`; `Sắp xếp` → `027`; chip `Ăn chay` → `022`; Back |
| `SB-022` | Không kết quả | `Mở rộng 3 km` → `021` | `Xóa bộ lọc` → `021`; gợi ý → `034`; Back |
| `SB-023` | Bộ lọc tổng hợp | `Xem 8 ưu đãi` → `021` | Nhóm Ngân sách → `024`; Khung giờ → `025`; Nhu cầu → `026`; `×` → Back |
| `SB-024` | Lọc ngân sách | `Áp dụng` → `023` | `×` → Back |
| `SB-025` | Lọc thời gian | `Áp dụng` → `023` | `×` → Back |
| `SB-026` | Lọc nhu cầu ăn | `Áp dụng` → `023` | `×` → Back |
| `SB-027` | Sắp xếp | Chọn tiêu chí → `021` | `×` → Back |
| `SB-028` | Danh mục bữa ăn | Offer → `034` | Back |
| `SB-029` | Danh mục bánh | Offer → `034` | `Túi bánh bất ngờ` → `044`; Back |
| `SB-030` | Danh mục thực phẩm | Offer → `034` | Mẹo Pantry → `074`; Back |
| `SB-031` | Đang nhận sớm | Offer sắp đóng → `048` | Offer khác → `034`; Back |
| `SB-032` | Quanh trường | Offer → `034` | Mini map → `016`; Back |
| `SB-033` | Yêu thích | Offer còn phần → `034` | Offer hết hôm nay → `046`; segment Cửa hàng → `038`; Back |
| `SB-034` | Chi tiết offer | `Chọn giờ nhận` → `059` (khách) | Ảnh → `035`; Dị ứng → `036`; Chất lượng → `037`; Cửa hàng → `038`; Back |
| `SB-035` | Thư viện ảnh | `×` → Back | Thumbnail đổi ảnh (Smart Animate tại chỗ, không đếm màn) |
| `SB-036` | Thành phần & dị ứng | `Đã hiểu` → Back | `×` → Back |
| `SB-037` | Chất lượng & hạn | `Đã hiểu` → Back | `×` → Back |
| `SB-038` | Chi tiết cửa hàng | Offer → `034` | `Chỉ đường` → `039`; `Quy định nhận` → `040`; `Xem tất cả` → `041`; `Đánh giá` → `042`; Back |
| `SB-039` | Đường tới cửa hàng | `Mở trong Bản đồ` (tĩnh, ghi chú) | Back |
| `SB-040` | Quy định nhận món | `Đã hiểu` → Back | — |
| `SB-041` | Offer khác của tiệm | Offer → `034` | Túi bất ngờ → `044`; offer đã đóng khung → `047`; Back |
| `SB-042` | Đánh giá cửa hàng | Thẻ đánh giá → `043` | Back |
| `SB-043` | Chi tiết đánh giá | `Báo cáo` (toast tại chỗ) | Back |
| `SB-044` | Túi bất ngờ | `Chọn giờ nhận` → `050` | `Túi bất ngờ là gì?` → `045`; Back |
| `SB-045` | Giải thích túi | `Đã hiểu` → Back | `×` → Back |
| `SB-046` | Hết hàng | Ưu đãi tương tự → `034` | Back |
| `SB-047` | Ngoài giờ nhận | `Lưu vào Yêu thích` → `033` | Back |
| `SB-048` | Gần đóng cửa | `Chọn giờ nhận` → `050` | Back |
| `SB-049` | Xung đột dị ứng | Tích xác nhận + `Chọn giờ nhận` → `050` | `Xem thành phần` → `036`; Back |
| `SB-050` | Chọn số lượng | `Tiếp tục` → `051` | `×` → Back |
| `SB-051` | Chọn khung giờ | `Tiếp tục` → `053` | `Xem hướng dẫn nhận` → `052`; Back |
| `SB-052` | Hướng dẫn nhận | `Tôi đã hiểu` → `053` | Back |
| `SB-053` | Tóm tắt đặt trước | `Đặt giữ chỗ (demo)` → `054` | Back |
| `SB-054` | Xác nhận giữ chỗ | `Xác nhận giữ chỗ` → `055` | `Xem lại` → Back |
| `SB-055` | Đang xử lý | After delay 800ms → `056` | Hotspot ẩn → `057`, → `058` |
| `SB-056` | Thành công | Vé → `062` | `Xem chỉ đường` → `065`; `Về trang Khám phá` → `015`; `×` → `015` |
| `SB-057` | Giữ chỗ thất bại | `Thử giữ chỗ lại` → `055` | `Quay lại chi tiết món` → `034` |
| `SB-058` | Tồn kho thay đổi | `Điều chỉnh còn 1 phần` → `053` | Món thay thế → `034`; Back |
| `SB-059` | Cần đăng nhập | `Đăng nhập` → `050` (return-to-offer) | `Đăng ký` → `006`; `×` → Back |
| `SB-060` | Đơn của tôi | Thẻ đơn đang chờ → `062` | `Mở mã QR` → `063`; `Xem tất cả đang chờ` → `061`; đơn hoàn tất → `072`; tab bar |
| `SB-061` | Đơn đang chờ | Đơn → `062` | `Mở mã` → `063`; `Chỉ đường` → `065`; tab bar |
| `SB-062` | Chi tiết đơn chờ | `Xem mã nhận món` → `063` | `Chỉ đường` → `065`; `Hủy đặt trước` → `070`; `Báo sự cố` → `069`; Back |
| `SB-063` | Mã QR | Hotspot ẩn (nhân viên quét) → `072` | `Cách đưa mã` → `064`; `×` → Back |
| `SB-064` | Hướng dẫn đưa mã | `Đã hiểu` → Back | `Hỗ trợ` → `099` |
| `SB-065` | Dẫn đường | `Mở mã QR` → `063` | Back |
| `SB-066` | Đơn đã sẵn sàng | `Mở mã nhận món` → `063` | Back |
| `SB-067` | Sắp hết giờ | `Xem chỉ đường nhanh` → `065` | `Liên hệ hỗ trợ` → `069`; After delay 3000ms → `068` |
| `SB-068` | Quá giờ nhận | `Xem ưu đãi khác` → `015` | `Báo lý do sự cố` → `069`; `Trợ giúp` → `099` |
| `SB-069` | Báo sự cố | `Gửi báo cáo` → Back | Back |
| `SB-070` | Xác nhận hủy | `Xác nhận hủy đặt trước` → `071` | `Giữ lại đơn` → Back |
| `SB-071` | Hủy thành công | `Khám phá ưu đãi khác` → `015` | `Xem đơn của tôi` → `060` |
| `SB-072` | Đơn hoàn tất | `Xem tác động` → `100` | `Đánh giá` → `042`; `Thêm vào Tủ thực phẩm` → `080`; Back |
| `SB-073` | Lịch sử trống | `Khám phá ngay` → `013` | Offer gợi ý → `034`; tab bar (khách) |
| `SB-074` | Giới thiệu Pantry | `Bắt đầu` → `076` | tab bar (khách) |
| `SB-075` | Tủ thực phẩm | `Đã dùng` → `086` | `+ Thêm` → `077`; hàng → `081`; "2 cần dùng sớm" → `083`; "1 quá hạn" → `084`; `Gợi ý` → `088`; `Lịch sử` → `089`; `Tùy chọn` → `090`; tab bar |
| `SB-076` | Tủ trống | Chip thêm nhanh → `080` | `Thêm thủ công` → `077`; tab bar |
| `SB-077` | Thêm thủ công | `Lưu` → `080` | `Loại` → `078`; `Ngày hạn` → `079`; Back |
| `SB-078` | Chọn loại | Chọn ô → `077` | `×` → Back |
| `SB-079` | Chọn ngày hạn | `Xác nhận` → `077` | `×` → Back |
| `SB-080` | Xác nhận thêm | `Lưu vào tủ` → `075` | `Sửa lại` → `077` |
| `SB-081` | Chi tiết thực phẩm | `Đã dùng hết` → `086` | `Đã bỏ` → `087`; `Sửa` → `082`; `Nhắc hạn` → `085`; Back |
| `SB-082` | Sửa thực phẩm | `Lưu` → `081` | Back |
| `SB-083` | Sắp hết hạn | `Đã dùng` → `086` | Hàng → `081`; `Gợi ý` → `088`; Back |
| `SB-084` | Đã quá hạn | `Bỏ an toàn` → `087` | Back |
| `SB-085` | Thiết lập nhắc hạn | `Lưu` → `081` | Back |
| `SB-086` | Đánh dấu đã dùng | `Xác nhận` → `089` | `×` → Back |
| `SB-087` | Đánh dấu đã bỏ | `Xác nhận` → `075` | `×` → Back |
| `SB-088` | Gợi ý dùng | Món trong gợi ý → `081` | Back |
| `SB-089` | Lịch sử Pantry | Back → `075` | — |
| `SB-090` | Dữ liệu cục bộ | Back | `Xóa toàn bộ` (xác nhận tại chỗ, không đếm màn) |
| `SB-091` | Tài khoản | Thẻ tác động → `100` | Hồ sơ → `092`; Khu vực → `093`; Thông báo → `095`; Nhắc nhở → `097`; Quyền riêng tư → `098`; Trợ giúp → `099`; tab bar |
| `SB-092` | Sửa hồ sơ | `Lưu` → `091` | Back |
| `SB-093` | Khu vực thường dùng | `+ Thêm khu vực` → `094` | Back |
| `SB-094` | Lưu khu vực mới | `Lưu` → `093` | Back |
| `SB-095` | Thông báo | Thông báo "Đã sẵn sàng" → `066` | "Sắp hết giờ" → `067`; "Sữa còn 1 ngày" → `083`; Back |
| `SB-096` | Thông báo trống | `Cấu hình giờ nhắc` → `097` | Back |
| `SB-097` | Tùy chọn thông báo | Back | — |
| `SB-098` | Quyền riêng tư | `Quyền vị trí` → `011` | `Dữ liệu Pantry` → `090`; Back |
| `SB-099` | Trợ giúp & FAQ | `Báo sự cố cửa hàng` → `069` | Accordion mở/đóng (tại chỗ); Back |
| `SB-100` | Tác động cá nhân | Back | `Chia sẻ` (tĩnh, ghi chú) |

Kiểm tra đường vào: mọi SB-ID ở cột "Đích" xuất hiện ít nhất một lần, trừ `SB-001` (flow start). Khi vẽ thay đổi tên CTA, sửa bảng này cùng lúc.

## 8. Cách nối dây bằng Plugin API

- Load skill `figma-use` trước mọi `use_figma`.
- Hotspot là layer đã có (button/row instance); không vẽ hình chữ nhật trong suốt trừ 3 hotspot ẩn ở mục 5.
- Mỗi batch: một script đọc bảng mục 7 của batch đó (map SB-ID → node ID từ [screens.csv](../../tracking/screens.csv)), gọi `setReactionsAsync` cho từng hotspot, rồi read-back `reactions` để đối chiếu.
- Toàn bộ 100 màn nay chung 1 page (`DEC-013`) nên `NAVIGATE` reaction luôn hợp lệ miễn đích đã tồn tại; nối dây chỉ chờ frame đích được dựng, không còn giới hạn liên-page. Đích chưa có thì ghi `pending:<SB-ID>` vào cột `notes` và nối lại ở batch sau.
- Set flow starting points (mục 6) sau B1 cho F-01, sau B2 cho F-03/F-04, sau B3 cho F-02/F-06, sau B8 cho F-05.

## 9. QA mỗi batch

1. 7 gates trong [workflow](../workflow.md) cho từng màn, rubric 8 tiêu chí không còn Red Flag.
2. Contact sheet batch (screenshot), so art direction và frame Phase 1 đã audit; không gọi là baseline được duyệt cho tới owner acceptance (`DEC-012`).
3. Bấm thử toàn bộ hotspot của batch trong Present mode; chỉ ghi `prototype_verified=true` cho màn đã bấm thật.
4. Cập nhật [screens.csv](../../tracking/screens.csv): `figma_page_id`, `figma_node_id`, `component_ids`, `linked_from`, `linked_to`, `editable_verified`, `qa_result`; components mới vào [components.csv](../../tracking/components.csv).
5. `python3 scripts/validate.py` PASS; commit nhỏ theo nhánh `design/<module>-<scope>`; cập nhật [progress](../../tracking/progress.md) và release lease.

## 10. Định nghĩa hoàn tất

- 100 frame native `393×852` khớp 1:1 registry, không duplicate, không PNG toàn màn, không orphan.
- 6 flow starting points chạy được từ đầu tới cuối; F-01 đi trọn guest → impact.
- Mọi màn `State` có hành động cứu vãn (luật 10).
- Các màn chỉ chuyển `DONE` sau owner review; trước đó dừng ở `QA_PASS` / `AWAITING_OWNER_REVIEW`.
