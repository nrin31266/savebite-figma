# Mẫu tuyển chọn cho SaveBite · 31/10/2026

Cập nhật01/11: [maps.to.design chính thức](https://divriots.com/blog/introducing-maps-to-design/) được tìm thấy trong Figma quick actions, nhưng launch báo lỗi môi trường cả trước/sau restart. **Chưa import map**, không gọi output image/fill của plugin là vector native. [Map checkpoint](../../tracking/map-ui-checkpoint.md) ghi UI đã sửa độc lập và phần nguồn thật còn thiếu.

Chọn theo chức năng, giữ màu xanh–kem và Be Vietnam Pro. Đây là tham khảo thị giác/interaction, không phải nghiên cứu người dùng hay giấy phép sao chép sản phẩm khác. Không nhập screenshot đối thủ làm UI.

| Nguồn | Đã xem / lấy được | Cách dùng trong SaveBite |
|---|---|---|
| [shadcn preset của owner](https://ui.shadcn.com/create?preset=b1aIuQ2XC&item=preview) | Mở đúng preview trong browser: Luma, Stone, Blue, Raleway, Remixicon, radius large. Đã xem bảng primitives. | Tham khảo độ mềm của bề mặt, nút và nhịp chữ; giữ font/màu/icon canonical của SaveBite. Đây không phải Figma kit đã import. |
| [Crouton](https://crouton.app/) | Đã xem hình app trên trang chính: ảnh món lớn, metadata tách nhóm, danh sách ảnh nhỏ. | SB-081: ảnh minh họa + tên/lượng bên cạnh, ngày hạn nổi bật, thông tin bảo quản riêng. SB-015/034/075 tiếp tục đối chiếu theo chức năng. Không thêm recipe planner vào MVP. |
| [Things](https://culturedcode.com/things/features/) | Đã xem ảnh Today/project trên trang hãng; nhóm danh sách có thứ bậc và khoảng cách rõ. | Hướng cho SB-060/075/095: nhóm theo thời gian/trạng thái, tránh mỗi dòng thành một card lớn. Chưa coi các màn này đã được sửa xong. |
| [Too Good To Go](https://www.toogoodtogo.com/en-us/how-does-the-app-work) | Đọc mô tả flow chính thức; chưa audit ảnh app hiện hành. | Ưu tiên giờ nhận/tình trạng còn món ở Discovery và Offer. SaveBite vẫn thanh toán tại quầy; không lấy mô hình prepay hay mức tiết kiệm của đối thủ. |
| [IKEA app](https://www.ikea.com/gb/en/customer-service/mobile-apps/) | Đọc trang giới thiệu chính thức; chưa kiểm chi tiết layout app. | Nguồn bổ sung cho cách lưu/yêu thích và chuẩn bị nhận tại cửa hàng, chưa là bằng chứng visual QA. |
| [Figma Simple Design System](https://github.com/figma/sds) | Button, Input, Checkbox và **Card** import native thật. Card key `a5bde480886231526d7dd890df3779dc15b52423`, main dùng `261:5376`. | Card instance `263:4660` ở SB-081; chỉnh native slot, typography và màu. Giữ liên kết component, không detach/flatten. |
| [Apple kit owner](https://www.figma.com/design/Y8CWXWyBsyDuvniwEwmBvj/Apple-iOS-UI-Kit-Rin?node-id=128-47587) | Native clipboard copy được Search, Toggle và Keyboard; không sửa source file. | Email keyboard SB-009; Text keyboard SB-019; Search/Toggle đã dùng trong app. Không claim toàn bộ Apple library import được qua API. |
| [Phosphor](https://phosphoricons.com/) · [MIT](https://github.com/phosphor-icons/web/blob/master/LICENSE) | SVG chính thức, giữ license và SHA-256. Thêm egg/orange-slice/fish/cheese/grains/jar/snowflake. | Fruit/MeatFish/Spices category mains dùng icon nguồn mới; snowflake dùng trong SB-081. Sheet `262:845`, master IDs/source tại manifest icon. |

Các nguồn [unDraw](https://undraw.co/license), [Storyset](https://storyset.com/faqs), [Shadcnblocks](https://www.shadcnblocks.com/terms) đã kiểm điều khoản, **chưa nhập asset**. Chưa chọn hình cụ thể phù hợp hơn pool hiện có; không coi tên nguồn là deliverable đã mang vào app. Brand “Mầm” là concept vector riêng, tách provenance khỏi bộ nguồn bên ngoài.

Kết quả áp dụng và ảnh trước/sau: [brand/source checkpoint](../../tracking/brand-polish-checkpoint.md).

## Tuyển thêm theo chức năng · sourced UI/Pantry batch

| Nguồn đã kiểm | Chọn cho SaveBite | Trạng thái thực tế / giới hạn |
|---|---|---|
| [Groc · Kitstack](https://ui8.net/kitstack/products/groc--grocery-shopping-mobile-app-ui-kit) | Listing có thumbnail nền sạch, tên/lượng đi cùng ảnh, điều khiển số lượng gọn. Áp dụng nguyên tắc vào SB-075: ảnh64pt, row96pt, khoảng cách12pt; thông tin hạn vẫn bằng chữ. | Đã xem ảnh preview trong browser; đây là kit thương mại, **chưa mua/chưa nhập asset kit**. Layout Pantry được chỉnh native từ master đang có, không copy ảnh screenshot thành UI. Không lấy AI meal plan/delivery vào MVP. |
| [Airbnb · Summer Release2025](https://news.airbnb.com/product-releases/airbnb-2025-summer-release) | Ảnh món/dịch vụ làm nội dung chính; metadata yên, thứ bậc ảnh → tên → giá/điều kiện. Chọn làm hướng đối chiếu tiếp cho SB-015/034/041 và nhóm Orders. | Đã mở trang chính thức và xem hình Services/detail. **Tham khảo bố cục**, không có quyền nhập ảnh món, logo hoặc UI của Airbnb làm asset SaveBite; chưa claim áp dụng cả nhóm màn. |
| [Untitled UI · free kit](https://www.untitledui.com/free-figma-ui-kit) · [license](https://www.untitledui.com/license) | Đối chiếu spacing/label/error của form và cấu trúc settings; không chọn phong cách dashboard web cho màn iPhone. | Đã xem trang kit và đi tới luồng tải FREE; luồng tải chuyển sang checkout. **Chưa tải/nhập**, không gửi email hoặc hoàn tất checkout. Không nhầm mô tả PRO trên trang bán với nội dung bản FREE đã có. |
| [Figma SDS · Tag Toggle](https://github.com/figma/sds) | Source-native filter Off/On; override màu xanh–kem, font Be Vietnam Pro12pt, pill44pt trong vùng48pt. | **Đã import native** set `423:848`, On `423:849`, Off `423:850`;8 instances ở SB-075,4 specimen instances trên board `431:838`. Check dependency reuse `179:274`. Present đã thử Kệ khô và Ngăn đông. |
| [Pexels](https://www.pexels.com/license/) | Bổ sung ảnh cho đúng4 khoảng trống Pantry: rau, sữa chua, gạo, đậu; reuse sữa/bánh/trứng từ pool hiện có. | **4 file tải thật, hash và nguồn trong [manifest](../../assets/manifest.json)**; dùng ở thumbnails075 và ảnh theo món081. Tổng pool30 ảnh/minh họa. Ảnh là minh họa loại thực phẩm, không xác nhận bao bì/độ tươi/nhãn hiệu; candidate chờ owner review. |

[Travel App của Osman Assem](https://osmanassem.com/travel-app/) đã đọc trang tác giả và thấy preview dark/teal; không chọn làm kit chính vì lệch màu và density của SaveBite. [unDraw](https://undraw.co/illustrations) đã mở riêng Breakfast Together để xem, không tải: nhân vật không bổ sung đúng chỗ thiếu ảnh thực phẩm. Không nhập thêm chỉ vì miễn phí.

Evidence và phạm vi QA: [sourced UI/Pantry checkpoint](../../tracking/sourced-ui-pantry-checkpoint.md). Đây là tuyển nguồn và áp dụng một batch cụ thể, không phải nghiệm thu polish100 màn.
