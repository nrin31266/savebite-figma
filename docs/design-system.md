# Hệ thiết kế SaveBite

Nguồn chuẩn theo domain; đọc [router](README.md) và [tiến độ](../tracking/progress.md) trước khi thay đổi.

## DESIGN DIRECTION — NGÔN NGỮ THỊ GIÁC CỦA APP

### Phong cách được chốt

Sạch, thật, hiện đại, gần gũi, có độ ấm, ít trang trí, tin cậy. Tham khảo **vibe của các slide SaveBite phiên bản kem–xanh thông–cam đất đã được người dùng chọn**: ảnh thực phẩm đời thực, bố cục thoáng, độ tương phản rõ, accent cam có tiết chế. Không dùng hình người AI không tự nhiên, ánh sáng “quá hoàn hảo” và những đồ họa greenwashing.

**Cực kỳ quan trọng:** phong cách *presentation* có tiêu đề serif lớn, nhưng **UI mobile không mang nguyên font serif khổng lồ từ slide sang**. App ưu tiên sans-serif có dấu tiếng Việt tốt, phân cấp rõ và đọc nhanh. Serif có thể dùng rất hạn chế trong campaign/header mang tính thương hiệu, không trên navigation, form, info và giá.

### Tokens nền tảng (DEFAULT — cần kiểm tra tương phản trên Figma sau khi áp dụng)

| Token | Hex | Purpose | Lưu ý |
|---|---|---|---|
| `color.brand.900` | `#143E32` | Primary, CTA, headline, app chrome | White-on-dark contrast tốt |
| `color.brand.700` | `#33745A` | Secondary action/brand text | Đủ tương phản với background nhạt cho chữ bình thường |
| `color.brand.100` | `#E8EFE6` | Pale backgrounds, chip selected, callouts | Không dùng chữ pale trên pale |
| `color.surface.canvas` | `#F8F6F0` | Brand canvas / marketing | Màn form có thể dùng neutral white surfaces |
| `color.surface.card` | `#FFFFFF` | White cards and sheets | Giúp app thoáng hơn slide |
| `color.accent.orange` | `#D7834B` | Graphic accent, icon highlight, badges | **KHÔNG dùng làm chữ nhỏ trên kem/trắng** vì contrast thấp |
| `color.accent.orangeText` | `#894E2E` | Accessible orange/brown text | Dùng cho text trên cream |
| `color.text.primary` | `#143E32` | Headline/body high contrast | |
| `color.text.secondary` | `#526C60` | Secondary info | Đo contrast với mỗi surface khi triển khai |
| `color.border.default` | `#D9E2D9` | Dividers, controls | Không dùng divider làm tín hiệu trạng thái duy nhất |
| `color.semantic.error` | `#B42318` | Error text/icons | Đi kèm icon/label rõ |
| `color.semantic.warning` | `#9A5400` | Expiring soon | Không phán đoán food safety chỉ bằng màu |
| `color.semantic.success` | `#25603C` | Success text/icons | Dùng có label |

**Kiểm tra sơ bộ:** `#143E32` trên `#F8F6F0` ~11:1; `#33745A` trên `#F8F6F0` ~5.1:1; `#D7834B` trên `#F8F6F0` ~2.7:1 nên không phù hợp cho body text. Đây là tỷ lệ tính toán từ bảng màu, agent vẫn phải test các tổ hợp foreground/background thực tế.

### Typography, kích thước, hệ spacing

- `App UI font`: **Be Vietnam Pro** (ưu tiên nếu có đầy đủ và hiển thị đúng) hoặc Inter đồng bộ toàn app; font fallback hệ thống hỗ trợ tiếng Việt.
- Type scale mobile gợi ý: Display `32/40`, H1 `28/36`, H2 `24/32`, H3 `20/28`, Body `16/24`, Secondary `14/20`, Caption `12/16`. Không ép số này nếu màn dài/đa kích thước, nhưng không để body chính dưới 14.
- Giá/rescue price có type treatment dễ quét mắt, thường `20–24sp` tùy card/detail; giá gốc gạch ngang, giá thực trả quan trọng hơn phần trăm giảm.
- Touch target tối thiểu khoảng `44×44pt` iOS / `48×48dp` Android (hoặc quy tắc platform tương đương); khoảng cách chạm hợp lý.
- Base grid 4pt, bố cục 8pt; spacing `4, 8, 12, 16, 24, 32, 40, 48`; mobile content horizontal padding `16–20`.
- Corner radius: `8` tight, `12` controls, `16` cards, `24` modal/sheet; thống nhất không dùng quá nhiều mức.
- Shadow rất nhẹ và có chủ đích; card thường ưu tiên border nhạt + khoảng trắng, tránh kiểu “mọi thứ là floating card”.
- Target thiết kế **390×844 logical px** (iPhone-style frame tham chiếu) với safe-area; khả năng thích ứng 360–430w; thực hiện kiểm tra ít nhất ở 360 và 430, font scaling, bàn phím đang mở.
- Mọi giao diện content cao phải scroll được; footer CTA sticky chỉ khi có lý do, không che nội dung/safe area.

### Hệ ảnh và icon

- Ảnh món/cửa hàng phải **đại diện chính xác** cho offer demo, tránh 1 ảnh rau củ copy cho mọi món hoặc hình thực phẩm vô lý.
- Nguồn: ảnh nhóm tự chụp, merchant được phép, hoặc ảnh hợp lệ có giấy phép; lưu URL, tác giả, license, attribution, ngày, quyền dùng vào `assets/manifest.json`.
- Icon: một bộ SVG vector nhất quán (Lucide/Phosphor hoặc bộ có giấy phép phù hợp), cùng stroke và kích thước. **Không dùng emoji làm icon UI chính**.
- Đối thủ: tên thật/logo chính thức bằng nguồn có kiểm chứng; không tái tạo logo AI hoặc phỏng đoán app icon.
- Không tạo ảnh người bằng AI để gắn làm *người tham gia khảo sát thật*. Persona có thể dùng avatar minh họa rõ là conceptual, hoặc không dùng ảnh.
- Không nhét điện thoại mockup và ảnh thực phẩm vào mọi màn. Trong app, nội dung và thao tác có ưu tiên cao hơn trang trí.

### Copywriting

- Tiếng Việt tự nhiên, gọn: “Đặt trước”, “Đến nhận”, “Còn 3 phần”, “Nhận 17:00–18:00”, “Thành phần chưa được cửa hàng cung cấp”.
- Không dịch máy cứng kiểu “cứu vớt món ăn”; không quảng cáo gây áp lực “hãy cứu Trái Đất ngay”.
- Đúng VND: `25.000đ`; thông tin giá gốc chỉ hiển thị khi nguồn đáng tin. Cách tính savings không được thổi phồng.
- Giờ theo `Asia/Ho_Chi_Minh`, 24h; ngày `dd/MM/yyyy`; dùng format locale chuẩn trong code.
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

### Các component nền tảng nên xuất hiện trước pilot

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

Không thiết kế toàn bộ 100 component trước khi nhìn thấy màn. Dựng Foundations + khoảng 15–25 component nền tảng, sau đó mở rộng component theo flow; review và consolidate sau mỗi 10–15 màn. Về sau có thể code-connect, nhưng **Code Connect không bắt buộc trước pilot**, và không phải lúc nào Figma Education cũng có cùng capability như các gói khác.

---

