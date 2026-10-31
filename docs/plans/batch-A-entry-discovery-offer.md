# Plan A · 36 màn — Entry, Discovery & Offer (Section 01 + 02)

Một trong hai plan chia đôi 70 màn còn lại sau batch `B-PHASE1-013`. Plan song song: [Plan B · Orders, Pantry & Account](batch-B-orders-pantry-account.md). Cả hai dựa trên bảng Interaction Map ở [Plan 2](build-100-screens-prototype.md) mục 7 và ma trận thị giác ở [screen-art-direction](../screen-art-direction.md).

Trạng thái: `READY` · Người thực hiện: _(điền tên)_ · Nhánh Git: `design/batch-A-entry-offer`.

---

## 1. Phạm vi và quyền ghi

- **Được ghi:** Section `01 · Entry & Discovery` (`69:326`) và `02 · Offer & Merchant` (`69:327`) trên page `App · All Screens` (`11:3`), gồm cả các frame đã có trong 2 section này (`SB-002, 005, 008, 013, 015, 016, 019, 022, 034, 046, 047, 049, 059`) khi cần nối lại reaction.
- **Không ghi:** Section 03 và 04 (thuộc Plan B), mọi main component đang có trên page `Components` (`11:2`), trừ component mới do chính Plan A tạo ở mục 4.
- **Registry:** chỉ sửa các dòng `SB-ID` thuộc Plan A trong [screens.csv](../../tracking/screens.csv); ghi tiến độ dưới heading riêng `## Plan A` trong [progress.md](../../tracking/progress.md).

## 2. Danh sách 36 màn

`Clone` = nhân bản frame có sẵn rồi đổi nội dung (nhanh, giữ nhất quán). `Mới` = dựng từ component. Cột "Vào từ" là các reaction cần thêm vào frame nguồn (nguồn thuộc Plan A thì tự nối; nguồn thuộc Plan B ghi ở mục 6).

### Section 01 · Entry & Discovery (24 màn) — đặt hàng ngang `y=100`, bắt đầu `x=4300`, bước `460`

| ID | Màn | Archetype | Cách dựng | Nội dung chính | Ra tới | Vào từ |
|---|---|---|---|---|---|---|
| `SB-003` | Onboarding 2 | A1 | Clone `SB-002` (`17:2`) | Mini map + ghim `25K/30K` + huy hiệu `17:00–18:00`, PageDots 2/3 | Tiếp tục→`004`, Bỏ qua→`005` | `SB-002` Tiếp tục (`17:45`, đang tạm →`015`) |
| `SB-004` | Onboarding 3 | A1 | Clone `SB-002` | 2 thẻ độ tươi (`Sữa tươi · Còn 2 ngày`, `Rau cải · Dùng hôm nay`), CTA `Bắt đầu sử dụng` | →`011` | `003` |
| `SB-006` | Đăng ký | A2 | Clone `SB-008` (`76:678`) | 3 `TextField` (Họ tên, Email, Mật khẩu Focused) + thanh độ mạnh + điều khoản | Tạo tài khoản→`007`, Đã có tài khoản→`008` | `SB-005` Tạo tài khoản, `SB-059` Tạo tài khoản mới (`82:1024`, đang BACK) |
| `SB-007` | Chờ xác minh email | A2 | Mới | Huy hiệu phong thư, email vừa nhập, đếm ngược `00:45`, Gửi lại | Tôi đã xác minh→`014`, Đổi email→`006` | `006` |
| `SB-009` | Quên mật khẩu | A2 | Clone `SB-008` | `TextField` Focused + `iOSKeyboard` (`15:19`, y=561), nút ngay trên bàn phím | →`010` | `SB-008` text "Quên mật khẩu?" |
| `SB-010` | Đã gửi liên kết | A2 | Mới | Emblem hộp thư, hộp nhắc kiểm tra mục Spam | Quay lại đăng nhập→`008`, Thử email khác→`009` | `009` |
| `SB-011` | Quyền vị trí | A1 | Mới | Minh họa bán kính quanh trường; 2 lựa chọn ngang quyền (D-017) | Cho phép→`012`, Tự chọn khu vực→`018` | `004`; `SB-098` (Plan B, mục 6) |
| `SB-012` | Quyền thông báo | A1 | Mới | 2 banner thông báo mẫu (`Nhắc nhận bánh 16:45`, `Sữa tươi còn 1 ngày`) | Bật / Để sau→`005` | `011` |
| `SB-014` | Home đã đăng nhập | A3 | Clone `SB-015` (`17:49`) | Lời chào, thẻ nhắc đơn đang chờ, rail ngang `Đang nhận sớm` | Thẻ đơn→`062`, rail→`031`, chip Quanh trường→`032`, tim→`033`, khu vực→`018`, chuông→`095` (B) | `SB-008` Đăng nhập (`76:712`, đang tạm →`015`), `007` |
| `SB-017` | Xem nhanh pin | A4 | Clone `SB-016` (`17:187`) | Ghim `25K` phóng 1.15 màu `#B34021`, peek sheet ảnh 72pt + `Xem chi tiết` | →`034`, chạm bản đồ→`016` | `SB-016` pin `17:239` (Smart Animate) |
| `SB-018` | Chọn khu vực | A4 | Mới | Thẻ `Dùng vị trí hiện tại (tùy chọn)` + danh sách campus kèm số ưu đãi | Xác nhận→`015` | `011`, `014`, `015` (dòng khu vực trong `BrandHeader`) |
| `SB-020` | Gợi ý tìm kiếm | A5 | Clone `SB-019` (`17:282`) | Đang gõ "bánh", gợi ý chia nhóm Món / Cửa hàng | Món→`034`, Cửa hàng→`038`, phím Tìm→`021` | `SB-019` (dòng gợi ý hoặc phím) |
| `SB-021` | Kết quả tìm kiếm | A3 | Mới | `ActiveFilterStrip` + 3–4 `OfferListRow`; 1 dòng gắn cờ dị ứng, 1 dòng hết phần | →`034`, cờ dị ứng→`049`, hết phần→`046`, Sắp xếp→`027`, chip lọc→`023`, chip `Ăn chay`→`022` | `SB-019` dòng tìm gần đây; `020`; `023`; `027` |
| `SB-023` | Bộ lọc tổng hợp | A5 | Sheet 85% trên `SB-015` mờ | 3 nhóm Ngân sách / Khung giờ / Loại, footer `Đặt lại` + `Xem 8 ưu đãi` | →`021`, các nhóm→`024/025/026` | `SB-015`/`SB-013` icon lọc trong `SearchField` |
| `SB-024` | Lọc ngân sách | A5 | Sheet | Histogram giá + 3 mốc nhanh | Áp dụng→`023` | `023` |
| `SB-025` | Lọc thời gian nhận | A5 | Sheet | Segmented ngày + thẻ khung giờ theo ca học | →`023` | `023` |
| `SB-026` | Nhu cầu ăn uống | A5 | Sheet | Checkbox chế độ ăn + hộp an toàn dị ứng cố định (D-007/008) | →`023` | `023` |
| `SB-027` | Sắp xếp | A5 | Sheet thấp ~380pt | 4 tiêu chí, dòng chọn nền `#EDF3E7` | →`021` | `021` |
| `SB-028` | Danh mục bữa ăn | A3 | Mới | Category hero + ảnh `rice-bowls-5127769` (cần upload) | Offer→`034` | Tile `Bữa ăn` trên `SB-015` (`51:321`) |
| `SB-029` | Danh mục bánh | A3 | Mới | Header vàng lúa mạch, 2 `OfferCard`, banner túi bất ngờ | Offer→`034`, túi→`044` | Tile `Bánh mì` (`51:314`) |
| `SB-030` | Danh mục thực phẩm | A3 | Mới | Ảnh `produce-crates-2679261` (cần upload), mẹo lưu vào Pantry | Offer→`034`, mẹo→`074` (B) | Tile `Rau củ` (`51:328`) |
| `SB-031` | Đang nhận sớm | A3 | Mới | Header đếm ngược, dòng có thanh số phần còn lại | Dòng sắp đóng→`048`, khác→`034` | `SB-015` hero banner (`17:123`), `014` rail |
| `SB-032` | Quanh trường | A3 | Mới | Mini map strip 120pt + khoảng cách đi bộ | →`034`, mini map→`016` | `014` chip |
| `SB-033` | Yêu thích | A3 | Mới | Segmented Món/Cửa hàng + ghi chú `Lưu yêu thích không giữ chỗ` (D-018) | Còn phần→`034`, hết hôm nay→`046`, segment Cửa hàng→`038` | `SB-015` tim, `014`, `SB-047` nút Lưu yêu thích; `SB-091` dòng đã lưu (B) |

### Section 02 · Offer & Merchant (12 màn) — hàng `y=1100`, bắt đầu `x=2400`, bước `460`

| ID | Màn | Archetype | Cách dựng | Nội dung chính | Ra tới | Vào từ |
|---|---|---|---|---|---|---|
| `SB-035` | Thư viện ảnh | A6 | Mới, nền `#091E1A` | Ảnh lớn + thumbnail `1/2`, chú thích nguồn | ×→Back | `SB-034` ảnh hero (`18:3`) |
| `SB-036` | Thành phần & dị ứng | A6 | Sheet | Banner `UNKNOWN`, lưới nhóm dị ứng, hướng dẫn hỏi tại quầy | Đã hiểu→Back | `SB-034` AllergenNotice (`54:375`), `SB-049` |
| `SB-037` | Chất lượng & hạn | A6 | Sheet | Dòng thời gian `Làm trong ngày → Nhận → Nên dùng trong 24h` (D-015) | →Back | Thêm link "Chất lượng & bảo quản" vào `SB-034` |
| `SB-038` | Chi tiết cửa hàng | A6 | Mới | Ảnh quầy `bakery-counter-205961` (kiểm hash, upload nếu chưa có), địa chỉ, quy định, 2 offer | Chỉ đường→`039`, Quy định→`040`, Xem tất cả→`041`, Đánh giá→`042`, offer→`034` | `SB-034` MerchantRow (`54:364`), `020`, `033` |
| `SB-039` | Đường tới cửa hàng | A4 | Clone `SB-016` | Tuyến đi bộ nét đứt `450m · 6 phút`, nút mở bản đồ ngoài (tĩnh) | Back | `038` |
| `SB-040` | Quy định nhận món | A6 | Mới | Checklist 3 bước + điều gì xảy ra khi trễ/hủy | Đã hiểu→Back | `038` |
| `SB-041` | Offer khác của tiệm | A3 | Mới | Header tiệm + 3–4 `OfferListRow` | Offer→`034`, túi→`044`, offer đã đóng→`047` | `038` |
| `SB-042` | Đánh giá cửa hàng | A6 | Mới | Tổng hợp theo 3 tiêu chí; thẻ ghi rõ `Mẫu minh họa`, không bịa sao (D-019) | Thẻ→`043` | `038`; `SB-072` (B) |
| `SB-043` | Chi tiết đánh giá | A6 | Mới | Nội dung + `Báo cáo đánh giá` | Back | `042` |
| `SB-044` | Túi bất ngờ | A6 | Mới | Minh họa túi giấy kraft bằng vector (không có ảnh hợp lệ), tem `Túi bất ngờ`, giá `29.000đ`, cảnh báo dị ứng đậm | Chọn giờ nhận→`050`, Túi bất ngờ là gì?→`045` | `029`, `041` |
| `SB-045` | Giải thích túi bất ngờ | A6 | Sheet | Sơ đồ 3 bước vì sao có túi bất ngờ | Đã hiểu→Back | `044` |
| `SB-048` | Gần đóng cửa | A6 | Clone `SB-034` | Banner cam đất `Khung nhận đóng sau 20 phút (17:40)` + pill khoảng cách | Chọn giờ nhận→`050` | `031` |

Sau khi có `021`, `031`, `033`, các màn đang thiếu lối vào (`SB-022`, `046`, `047`, `049`) sẽ có đường vào — nhớ nối.

## 3. Thứ tự batch

| Batch | Màn | Ghi chú |
|---|---|---|
| A0 | Component chung (mục 4) | Làm trước, đăng ID vào progress để Plan B dùng |
| A1 | `003, 004, 006, 007, 009, 010, 011, 012` | Onboarding + Auth |
| A2 | `014, 017, 018, 020, 021` | Mở lối vào cho `022/046/049` |
| A3 | `023, 024, 025, 026, 027` | Các sheet lọc |
| A4 | `028, 029, 030, 031, 032, 033` | Danh mục + yêu thích |
| A5 | `035, 036, 037, 038, 039, 040` | Trust + cửa hàng |
| A6 | `041, 042, 043, 044, 045, 048` | Merchant + túi bất ngờ |

Mỗi batch: dựng → chụp screenshot từng màn → tự chấm rubric → nối reaction → cập nhật `screens.csv` → commit nhỏ.

## 4. Component Plan A tạo trước (Batch A0)

Plan B cũng cần các component này; tạo xong ghi `figma_component_set_id` vào [components.csv](../../tracking/components.csv) và progress.

| Component | Variants | Dùng ở |
|---|---|---|
| `SheetContainer` | `Height=Compact/Medium/Large`, có grabber `36×5`, bo trên `28` | A: `023–027, 036, 037, 045`; B: `070, 078, 079, 086, 087` |
| `EmptyState` | Emblem 96pt + tiêu đề + mô tả, slot cho hành động | B: `073, 076, 096` (A tham chiếu `SB-022`) |
| `SegmentedControl` | 2/3 segment | A: `033`; B: `SB-060` có bản tĩnh cục bộ |
| `FilterChip` | `Selected=True/False`, có icon | `021, 023–027` |

Nếu Plan B cần trước khi A0 xong: B dựng sheet cục bộ theo mẫu `SB-050` (`83:970`) và empty theo mẫu `SB-022` (`80:809`), sau đó thay bằng instance.

## 5. Quy ước chung (áp dụng cho cả Plan A và B)

Đọc trước: [AGENTS.md](../../AGENTS.md), [visual-direction](../visual-direction.md), [ios-guidelines](../ios-guidelines.md), skill `figma-use` + `figma-generate-design` trong `.agents/skills/`.

**Tham chiếu có sẵn trong file**

| Loại | ID / giá trị |
|---|---|
| Status bar / Home indicator / Keyboard | `15:2` / `15:17` / `15:19` |
| AppBar (prop `Title#15:0`) / LargeTitleBar / BottomNav | `15:105` / `15:111` / `15:122` |
| Button Primary (`Label#15:2`) / Secondary (`Label#15:3`) | `15:149` / `15:151` |
| OfferCard / OfferListRow / OfferSummary | `15:160` / `15:169` / `16:63` |
| UnifiedReceiptCard / PerforatedPickupPass / DemoQR | `16:76` / `16:124` / `16:100` |
| PantryItemRow / FreshnessSummaryBanner / ImpactHeroCard | `16:171` / `16:161` / `16:186` |
| TextField (set, Default/Focused/Error) | `75:56` (`75:44` / `75:49` / `75:55`) |
| imageHash bánh mì | `9229b77514748e00389f6abfc707a40b608001b2` |
| imageHash croissant | `30db81ade08ff0f66f092d125db83365ba0452af` |
| imageHash cơm gà | `966da3684f0cf0ffd0e29805dc1a75c1db016fcc` |
| imageHash rau củ | `1611a0e8ff6902c46b991a55b9576a1067feaec5` |

**Những lỗi đã gặp — tránh lặp lại**

1. Mỗi lần gọi `use_figma` là **nguyên tử**: lỗi ở đâu thì toàn bộ thay đổi của lần gọi đó bị hoàn tác → chia script vừa phải, chạy lại cả đoạn khi lỗi.
2. Không `appendChild` node mới vào bên trong instance, không sửa hình học (`vectorPaths`) hay vị trí con của instance → detach có ghi lý do, hoặc đặt node ngoài instance.
3. Frame auto-layout bỏ qua `x/y` của con → dùng `insertChild` đúng thứ tự, hoặc `layoutPositioning = 'ABSOLUTE'` cho lớp phủ.
4. Ảnh: dùng `imageHash` của ảnh **đã có trong Figma**; SHA-256 của file trong repo không dùng được. Ảnh mới phải upload trước (`upload_assets`), rồi ghi hash vào progress.
5. Component status bar/app bar/bottom nav **không có** variant Theme/ActiveTab: chế độ sáng làm bằng override màu chữ/icon trắng; tab active = nền `#EDF3E7`, bo 14, chữ SemiBold `#004337` (xem hàm mẫu trong lịch sử SB-060).
6. Text property phải dùng đúng khóa có hậu tố (`Title#15:0`, `Label#15:2`); `setProperties` sai khóa trong `try/catch` sẽ âm thầm không đổi gì.
7. Path SVG cho `vectorPaths`: tách khoảng trắng đầy đủ (`M 4 6 L 10 12`), không dùng lệnh rút gọn; icon nhanh nhất là `figma.createNodeFromSvg`.
8. Sau khi clone một frame, xóa reaction cũ (`setReactionsAsync([])` cho mọi node con) rồi mới nối lại.
9. Không emoji, không mặt người, không bịa giá gốc/đánh giá/dị ứng; dữ liệu theo fixture trong [product](../product.md).

**Định nghĩa xong một màn:** frame `393×852` có tên `SB-xxx · …` trong đúng Section; screenshot đã xem; không vi phạm rubric (emoji, card-in-card, từ mồ côi, lề 20pt); reaction đã nối và đọc lại; dòng `screens.csv` đã cập nhật (`status=DESIGN_REVIEW`, `prototype_verified=false` cho tới khi có người chạy Present mode thật). DONE chỉ sau khi owner duyệt.

## 6. Liên kết chéo với Plan B

Quy tắc: **chủ của frame nguồn nối reaction**. Nếu đích thuộc plan kia mà chưa dựng → ghi `pending:SB-xxx` vào `notes`, nối ở lượt nối chéo cuối cùng (một người làm, sau khi cả hai plan xong).

| Nguồn (Plan A) | Đích (Plan B) |
|---|---|
| `SB-013` tab Đơn của tôi / Tủ thực phẩm / chuông | `SB-073` / `SB-074` / `SB-096` |
| `SB-014` chuông, `SB-015` chuông | `SB-095` |
| `SB-030` mẹo Pantry | `SB-074` |

Plan B sẽ nối về Plan A: `SB-098 → SB-011`, `SB-072 → SB-042`, `SB-091 → SB-033`.
