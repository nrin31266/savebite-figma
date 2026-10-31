# Mẫu tuyển chọn cho SaveBite · 31/10/2026

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
