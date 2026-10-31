# Sourced UI & Pantry imagery · 31/10/2026

Owner yêu cầu tìm mẫu/component/asset đẹp từ lĩnh vực phù hợp, tự thiết kế trực tiếp, không agent khác. Giữ palette xanh–kem. File đích duy nhất `7suZz9C8oL5zV2NMxlsIVI`;100 root IDs giữ nguyên, DONE0. Không sửa logic form/reminder WIP của phiên trước.

## Đã đưa vào thiết kế

-4 ảnh Pexels có nguồn/hash: rau`5709305`, sữa chua`10809259`, gạo`31555430`, đậu`768089`; manifest tổng30 entries. Native asset nodes trên Foundations: rau`423:856`, yogurt`423:855`, rice`423:854`, peas`423:857`, nằm trong board`161:2`. `approved=false` chờ owner review; ảnh minh họa loại món, không xác nhận sản phẩm/bao bì/độ tươi.
- SB-075:7 thumbnail64×64, giữ7 row IDs và master`16:171`, slot`424:838`; row96pt, gap12pt, typography tên14/21 và ngày12/18. Quick action12pt với66×48 target. Khắc phục label summary quá hẹp bằng FILL và padding8. Món thêm bằng form giữ fallback thay vì giả định ảnh sữa.
- SDS Tag Toggle set`423:848`, mains On`423:849`/Off`423:850`, source key`aa708ea694a7f3d928fc7311848243d5aef8c3e6`.8 instances trong075;4 specimen instances tại [board nguồn](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=431-838). Giữ parent reactions/visibility; font12, pill44 trong touch area48. Remote Check`179:274` reuse.
- SB-081:6 selected-photo surfaces thay icon bằng ảnh đúng loại; giữ variable visibility và root. Sữa tiếp tục dùng ảnh cũ. Card/CTA native nguồn vẫn giữ liên kết.
- [Source manifest theo chức năng](../docs/references/curated-layouts.md): đã xem Groc và Airbnb chính thức; Untitled UI chỉ xem/free-checkout chưa tải; Travel/unDraw không chọn. Không mua kit hoặc claim toàn bộ Apple kit import.

## Kiểm tra và giới hạn

- PASS read-back:100 roots,7 row instance mains/bindings/reactions và ảnh;8 Tag Toggle skins,6 detail photo hashes. [JSON](evidence/sourced-ui-pantry/readback.json); [bounds cuối sau chỉnh quick action12pt](evidence/sourced-ui-pantry/final-row-bounds.json) supersede text bounds trong read-back trước đó.
- PASS scoped visual: [SB-075](evidence/sourced-ui-pantry/SB-075.png), [native Tag Toggle specimen](evidence/sourced-ui-pantry/tag-toggle.png). Ảnh giữ ở layer fill; text/controls vẫn editable. Chưa kiểm Dynamic Type hoặc contrast mọi trạng thái.
- PASS thao tác Present: [Kệ khô](evidence/sourced-ui-pantry/runtime-dry.png) lọc bánh/gạo; chọn [Gạo](evidence/sourced-ui-pantry/runtime-rice.png) hiển thị ảnh gạo, Best before15/11/2026, Kệ khô. [Ngăn đông](evidence/sourced-ui-pantry/runtime-frozen.png) lọc đậu; chọn [Đậu Hà Lan](evidence/sourced-ui-pantry/runtime-peas.png) hiển thị ảnh đậu, Use by28/10/2026, Ngăn đông. Không suy diễn thành F-05 PASS.
- Known limitation: ảnh minh họa sữa chua trong bát/gạo trong bát/đậu tươi không mô tả bao bì hộp/túi hay xác nhận đông lạnh. Caption081 và usageScope nêu minh họa; không dùng làm bằng chứng safety.
- Chưa kiểm: chọn/detail toàn7 món, edit/save/add/reminder sau đổi UI; lỗi drift date/name/category/unit của checkpoint F05 vẫn OPEN. Toàn100 màn, full6flows, mobile/usability/owner acceptance vẫn chưa PASS; prototype_verified giữfalse.

Lease `codex/direct-sourced-ui` RELEASED tại checkpoint. Repository validator/whitespace/evidence decode kết quả ghi ở progress; không push/merge batch này.
