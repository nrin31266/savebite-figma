# Hệ thiết kế SaveBite

Nguồn chuẩn theo domain; đọc [router](README.md) và [tiến độ](../tracking/progress.md) trước khi thay đổi.

Hướng hiện hành là pilot **v0.5 theo DEC-010**, dựng lại từ 5 ảnh owner gửi: nền kem, xanh rừng, ảnh món ăn sáng, giá cam đất và thẻ bo tròn. v0.4 bị owner từ chối về thẩm mỹ. Bảng dưới khớp checkpoint v0.5; đọc live và registry trước khi sửa. Baseline mới vẫn chờ owner review.

## DESIGN DIRECTION — NGÔN NGỮ THỊ GIÁC CỦA APP

### Hướng đang trình review

Ấm, rõ và có nhận diện SaveBite. Theo 5 ảnh owner gửi: xanh rừng đi cùng nền kem, ảnh thực phẩm sáng, headline mạnh, giá cam đất, card mềm và icon vector nhất quán. Ảnh phải hợp món và có provenance; không thêm trang trí lấn thao tác hoặc claim tác động môi trường chưa có dữ liệu.

**Cực kỳ quan trọng:** phong cách *presentation* có tiêu đề serif lớn, nhưng **UI mobile không mang nguyên font serif khổng lồ từ slide sang**. App ưu tiên sans-serif có dấu tiếng Việt tốt, phân cấp rõ và đọc nhanh. Serif có thể dùng rất hạn chế trong campaign/header mang tính thương hiệu, không trên navigation, form, info và giá.

### Tokens hiện hành (checkpoint v0.5)

| Token | Hex | Purpose | Lưu ý |
|---|---|---|---|
| `color.brand.900` | `#004337` | Primary, CTA, brand chrome | White-on-dark contrast tốt |
| `color.brand.700` | `#2D7055` | Secondary action/brand text | Đủ tương phản với background nhạt cho chữ bình thường |
| `color.brand.100` | `#EDF3E7` | Pale backgrounds, chip selected, callouts | Không dùng chữ pale trên pale |
| `color.surface.canvas` | `#FFFCF6` | Brand canvas / marketing | Màn form có thể dùng neutral white surfaces |
| `color.surface.card` | `#FFFFFF` | White cards and sheets | Giúp app thoáng hơn slide |
| `color.accent.orange` | `#D7834B` | Graphic accent, icon highlight, badges | **KHÔNG dùng làm chữ nhỏ trên kem/trắng** vì contrast thấp |
| `color.accent.orangeText` | `#B34021` | Accessible orange/brown text | Dùng cho text trên cream |
| `color.text.primary` | `#092F29` | Headline/body high contrast | |
| `color.text.secondary` | `#606E66` | Secondary info | Đo contrast với mỗi surface khi triển khai |
| `color.border.default` | `#E8E2D8` | Dividers, controls | Không dùng divider làm tín hiệu trạng thái duy nhất |
| `color.semantic.error` | `#B42318` | Error text/icons | Đi kèm icon/label rõ |
| `color.semantic.warning` | `#9A5400` | Expiring soon | Không phán đoán food safety chỉ bằng màu |
| `color.semantic.success` | `#25603C` | Success text/icons | Dùng có label |

**Contrast v0.5:** 13 cặp chữ/nền thực dùng đạt ≥4.5:1, thấp nhất 4.74:1. Cặp màu và cách kiểm nằm trong [QA](../tracking/evidence/qa.json). Cam trang trí #D7834B không dùng làm chữ nhỏ. Leaf #80AA50 và wheat #F6D594 chỉ dùng trong icon minh họa.

### Typography, kích thước, hệ spacing

- `App UI font`: **Be Vietnam Pro** (ưu tiên nếu có đầy đủ và hiển thị đúng) hoặc Inter đồng bộ toàn app; font fallback hệ thống hỗ trợ tiếng Việt.
- Type scale mobile gợi ý: Display `32/40`, H1 `26/34`, H2 `22/30`, H3 `18/26`, Body `16/24`, Secondary `14/20`, Caption `12/16`. Không ép số này nếu màn dài/đa kích thước, nhưng không để body chính dưới 14.
- Giá: card dùng H3 18/26; detail dùng Price 24/32 Bold. Chỉ hiện giá gốc/discount khi có nguồn. Thêm Hero 22/28 Bold và Wordmark 30/38 Bold; tất cả là text styles dùng chung.
- Touch target tối thiểu khoảng `44×44pt` iOS / `48×48dp` Android (hoặc quy tắc platform tương đương); khoảng cách chạm hợp lý.
- Base grid 4pt, bố cục 8pt; spacing `4, 8, 12, 16, 20, 24, 32, 48`; mobile content horizontal padding `16–20`.
- Corner radius: `8` tight, `24` controls/cards, `28` sheet; thống nhất không dùng quá nhiều mức.
- Shadow rất nhẹ và có chủ đích; card thường ưu tiên border nhạt + khoảng trắng, tránh kiểu “mọi thứ là floating card”.
- Target thiết kế **390×844 logical px** (iPhone-style frame tham chiếu) với safe-area; khả năng thích ứng 360–430w; thực hiện kiểm tra ít nhất ở 360 và 430, font scaling, bàn phím đang mở.
- Mọi giao diện content cao phải scroll được; footer CTA sticky chỉ khi có lý do, không che nội dung/safe area.

### Hệ ảnh và icon

- Ảnh món/cửa hàng phải **đại diện chính xác** cho offer demo, tránh 1 ảnh rau củ copy cho mọi món hoặc hình thực phẩm vô lý.
- Nguồn: ảnh tự chụp/được phép hoặc stock có giấy phép; lưu provenance trong `assets/manifest.json`. Pilot v0.5 dùng ảnh bánh mì AI có nhãn minh họa và ảnh croissant Pexels. Ảnh AI chỉ minh họa fixture hư cấu; không đại diện merchant, thành phần hay độ an toàn thật.
- Icon: một bộ SVG vector nhất quán (Lucide/Phosphor hoặc bộ có giấy phép phù hợp), cùng stroke và kích thước. **Không dùng emoji làm icon UI chính**.
- Đối thủ: tên thật/logo chính thức bằng nguồn có kiểm chứng; không tái tạo logo AI hoặc phỏng đoán app icon.
- Không tạo ảnh người bằng AI để gắn làm *người tham gia khảo sát thật*. Persona có thể dùng avatar minh họa rõ là conceptual, hoặc không dùng ảnh.
- Không nhét điện thoại mockup và ảnh thực phẩm vào mọi màn. Trong app, nội dung và thao tác có ưu tiên cao hơn trang trí.

### Copywriting

- Tiếng Việt tự nhiên, gọn: “Đặt trước”, “Đến nhận”, “Còn 3 phần”, “Nhận 17:00–18:00”, “Thành phần chưa được cửa hàng cung cấp”.
- Không dịch máy cứng kiểu “cứu vớt món ăn”; không quảng cáo gây áp lực “hãy cứu Trái Đất ngay”.
- Đúng VND: `25.000đ`; thông tin giá gốc chỉ hiển thị khi nguồn đáng tin. Cách tính savings không được thổi phồng.
- Giờ theo `Asia/Ho_Chi_Minh`, 24h; ngày `dd/MM/yyyy`; giữ cùng cách viết trên mọi màn.
- Nhãn `Mô phỏng/Demo` đặt trong tài liệu review và cấu hình data fixture. Ở UI trình diễn có thể dùng merchant/offer hư cấu dễ nhận biết, không in nhãn “debug”, nhưng phải **không khiến người xem hiểu có đơn hàng thật**.

---

## DESIGN SYSTEM VÀ COMPONENT STRATEGY

### Lifecycle của component

`LOCAL → CANDIDATE → SHARED → STABLE → DEPRECATED`.

- `LOCAL`: layout một màn đang thử; chưa chắc có reuse.
- `CANDIDATE`: trùng về cấu trúc/hành vi ở ≥2 màn hoặc là cross-cutting core (Button/Navigation có thể lên từ lần đầu).
- `SHARED`: đã có component Figma, variants chính, tokens, doc usage và ví dụ thực tế.
- `STABLE`: QA đạt, được dùng rộng; breaking change phải có migration plan và duyệt.
- `DEPRECATED`: có mapping thay thế và cleanup; không xóa trực tiếp khi vẫn có instance.

**Reuse-first:** trước khi tạo component, tìm trong `components.csv`, hiện trạng Figma, thư viện đang được publish/subscribed; ưu tiên chỉnh variant/properties phù hợp thay vì copy rồi detach. **Không làm base component 5 lần ở 5 màn.**

### Danh mục component tham khảo khi mở rộng

| Nhóm | Components | Minimum variants/properties |
|---|---|---|
| Core actions | `Button`, `IconButton`, `LinkButton` | Primary/secondary/tertiary/destructive; default/pressed/disabled/loading; icon slots |
| Inputs | `TextField`, `SearchField`, `Stepper`, `DatePickerInput` | Label, hint, focus, error, disabled, optional leading/trailing icon |
| Navigation | `AppTopBar`, `BottomTabBar`, `BackAction`, `SegmentedControl` | Active/inactive, guest/auth, badges, safe-area |
| Discovery | `OfferCard`, `OfferListRow`, `OfferGridCard`, `CategoryChip`, `FilterChip`, `MapPin` | Price original/rescue, availability, pickup, selected, dietary |
| Merchant | `MerchantCard`, `PickupInfo`, `StoreBadge` | Rating if verified, address, hours, pickup state |
| Pricing | `PriceBlock`, `DiscountBadge`, `QuantityControl` | Missing original price, sold-out, discount on/off |
| Communication | `Snackbar`, `Toast`, `Banner`, `InlineError`, `EmptyState`, `LoadingSkeleton`, `ConfirmationSheet` | Info/warning/error/success; accessible labels |
| Reservation | `PickupSlot`, `ReservationSummary`, `PickupCodeCard`, `OrderStatusBadge` | Available/unavailable/selected, ready/expired/complete |
| Pantry | `PantryItemRow`, `ExpiryStatusTag`, `ExpiryReminderRow` | Normal/soon/overdue/consumed/disposed |
| Trust | `AllergenList`, `FoodInformationBlock`, `MerchantDisclosure`, `PolicyLink` | Unknown disclosures, warnings, verification indicator |

### Component QA bắt buộc

- Main component và instance có tên rõ, ví dụ `OfferCard/Vertical`, không gọi `Frame 1143`.
- Auto Layout ở khu vực lặp, resizing constraints đúng; long title/long address xử lý không tràn.
- Bind shared colors/spacing/type styles qua variable/styles có thể quản lý (không hardcode hết trong 100 frame).
- Variant được kiểm soát, **không tạo 20 biến thể chỉ khác 1 icon** nếu component props giải quyết được.
- Component docs có: purpose, allowed contexts, state, content rules, a11y, do/don't, dependencies, revision.
- Screenshot QA với short/long strings, giá dài, không ảnh, sold-out, font scaling nếu có.
- Breaking change: liệt kê impacted screens, chụp screenshot trước/sau ở màn đại diện, update registry rồi mới publish.

### Không “over-engineer” hệ thống

Chỉ dựng tokens/components cần cho batch; bảng trên là danh mục gợi ý, không bắt tạo toàn bộ trước pilot. Reuse 21 main components hiện có trước khi bổ sung. Review và consolidate theo flow; Code Connect nằm ngoài phạm vi repo.

---


## Pilot v0.5 — base hiện hành cho team

Giữ 5 root frames, đổi bố cục theo DEC-010: header SaveBite có lá, banner xanh cạnh ảnh, category tile và lưới 2 cột; detail có ảnh 250px và sheet kem chồng lên; bước đặt trước dùng receipt/ticket trắng trên nền kem. Giữ 4 tabs và toàn bộ nghiệp vụ fixture. Không thêm map/pantry/order-list vào pilot chỉ vì chúng xuất hiện trong reference.

Có **40 variables, 11 text styles, 2 effect styles, 21 main components, 3 variant sets**, 31 instances trên pilot. [Registry](../tracking/components.csv) sở hữu mapping; [board component](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=29-2) có sample đủ 21 mains. SHARED chưa có nghĩa STABLE; baseline chưa được owner chấp nhận.

### Quy tắc dựng tiếp để đồng bộ

- Canvas kem #FFFCF6; headline xanh #004337; body #092F29; chữ phụ #606E66. Dùng cam #B34021 cho giá, không dùng đồng thời nhiều accent tranh sự chú ý.
- Padding màn 20px; gap 8/12/16px theo độ liên quan. Card trắng radius 24, border #E8E2D8, shadow effect/card nhẹ. Không đóng mọi câu chữ vào một card riêng.
- Ảnh món ăn là trọng tâm ở khám phá/chi tiết; checkout ưu tiên giá, giờ, điểm nhận và policy. Dùng BreadPhoto/CroissantPhoto instances; không lấy ảnh UI toàn màn làm background.
- Horizontal rows chứa text phải hug chiều cao; các tile chia đều chiều rộng. Search co FILL bên cạnh filter 48px. Header/CTA có target ≥48px; footer button cao 52px, safe-area dưới 24px.
- Nội dung dài phải cuộn trong Scroll viewport, footer đứng riêng. Ở 390px, summary hiển thị dị ứng UNKNOWN và điều kiện hủy trước CTA; ở 360px phải cuộn được tới cuối.
- Font Be Vietnam Pro; dùng đúng text styles thay vì chỉnh cỡ tùy hứng. Giữ hierarchy ít cấp: heading 26, section 22, body 14–16, metadata 12. Không lấy khung điện thoại hoặc Dynamic Island trong reference làm nội dung app.

| Thành phần | Cách team dùng |
|---|---|
| BrandHeader | Wordmark/leaf, khu vực demo và thông báo preview. Dùng ở trang chính; không bịa badge unread hoặc liên kết notification chưa mô phỏng. |
| Button | Primary/Secondary ở Default; Primary thêm Disabled/Loading. Label đổi qua property ở Default/Disabled; Loading có nhãn và vòng chờ tĩnh riêng. Đây là state mẫu, chưa có request backend/animation. |
| OfferCard / OfferListRow / OfferSummary | Đổi nội dung bằng properties đã expose; OfferCard có Photo instance-swap và Title/Merchant/Price/Pickup/Availability. Ảnh/giá/tồn/giờ phải cùng fixture. Không detach để sửa copy. |
| MerchantRow / PickupInfo | Properties Merchant/Address và Label/Time. Dùng thông tin hư cấu có nhãn demo khi chưa có merchant thật. |
| PickupSlot | Available/Selected dùng Time; hint theo state. Expired sample 15:00–16:00, Selected 17:00–18:00. Không chia sẻ default hint giữa các state trái nghĩa. |
| ReservationProgress | Stage Time ở SB-051, Review ở SB-053; chỉ báo tiến độ, không phải nút điều hướng. |
| AllergenNotice | Dùng chung ở detail/summary trước confirm; Title/Body editable, giữ nghĩa UNKNOWN. |

Fixture chính: fixture-bakery-01, Tiệm Bánh A (demo), Bánh mì men tự nhiên, 1 phần 25.000đ, còn 3 phần; giờ mẫu 16:00 ngày 19/10/2026, nhận 17:00–18:00. Fixture phụ: bánh sừng bò 30.000đ, còn 2 phần. Không có giá gốc/discount đã xác minh. Demo QR giữ payload SAVEBITE-DEMO:DEMO-001:NOT-A-REAL-ORDER và mã DEMO-A125; không dùng giao dịch thật.

## Checklist khi team tạo màn hoặc đổi component

- Từ registry tìm node/instance phù hợp; đọc live trước sửa. Thay text qua properties, đổi state qua variants.
- Dùng tokens/styles hiện hữu. Component mới chỉ thêm khi component hiện tại không biểu diễn được nhiệm vụ; ghi mục đích và mapping.
- Kiểm 360/390/430, nội dung tiếng Việt và vùng chạm. Kiểm toàn bộ node bounds, vì kiểm text riêng sẽ bỏ sót icon/filter bị cắt.
- Với layout hay copy mới dài hơn mẫu: thử chuỗi dài, giá dài và state thiếu dữ liệu trước khi gọi SHARED. Các trường hợp chưa thử phải ghi NOT CHECKED.
- Sau đổi main component, xem mọi màn dùng nó; không chỉ nhìn specimen. Cập nhật registry/evidence rồi trình review.
