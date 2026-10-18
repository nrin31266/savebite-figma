# Quyết định SaveBite

20 mặc định D-001..D-020 giữ nguyên ở [product.md](product.md). Log này chỉ giữ thay đổi có nguồn duyệt.

## DEC-001 · 19/10/2026 · Phạm vi bootstrap pilot
- Nguồn: yêu cầu trực tiếp của Nguyễn Văn Rin và Bootstrap Prompt đính kèm trong phiên này.
- Duyệt tối đa 5 hi-fi frames: SB-015 → SB-034 → SB-051 → SB-053 → SB-056, foundations phục vụ riêng subset này và một click-through.
- Thay danh sách pilot cũ; SB-051 luôn là chọn khung giờ nhận, không đổi ID.
- Cho phép pilot trước production gate; low-fi toàn flow, nghiên cứu và video vẫn là deliverables chưa hoàn thành.
- Không tạo file Figma khác, không triển khai 100 màn, không push/tạo GitHub repo/PR/công khai/chia sẻ quyền.
- Ảnh chưa có license dùng placeholder có nhãn; success/code là demo, không đại diện stock server.
- Dừng AWAITING_OWNER_REVIEW sau QA; baseline_version để trống đến khi duyệt.
- Ảnh hưởng: 5 screen contracts, Button/OfferCard/PickupInfo/PriceBlock/PickupSlot/Nav và evidence.

## DEC-002 · 19/10/2026 · Kết nối Figma
- Người dùng chọn `RIN` qua câu hỏi trong phiên.
- MCP whoami: Nguyen Van Rin, team Nguyễn Văn Rin's team, student/Full/admin.
- Không dùng kết nối Figma khác để ghi; file đích không đổi.

## DEC-003 · 19/10/2026 · Làm lại visual pilot sau owner feedback
- Nguồn: owner đánh giá bản đầu chưa đẹp, yêu cầu cài frontend-design, dùng find-skills và cho phép chọn lại quyết định visual khi cần.
- Cài frontend-design (Anthropic) và ui-ux-pro-max (NextLevelBuilder), giữ Figma official skills cho native canvas.
- Chọn hướng food-first: ảnh bánh thật có nguồn/giấy phép, hierarchy theo món → giá → giờ nhận, giảm hộp cảnh báo kỹ thuật và khoảng trắng vô dụng; thêm cấu trúc receipt cho summary/success.
- Palette vẫn dùng cream/green/earth orange của sản phẩm; Be Vietnam Pro cho toàn UI mobile. Không dùng serif lớn/gradient hoặc thêm merchant/payment vào MVP.
- Fixture được đổi đồng bộ từ bộ 3 bánh mini thành “Bánh mì men tự nhiên” để khớp ảnh licensed. Vẫn 1 phần 25.000đ, merchant giả lập, slot 17:00–18:00, thành phần/allergens UNKNOWN.
- Ảnh Marcel Fiedler/Pexels 1079020 là ảnh minh họa demo; không đại diện merchant thật. Source/license được lưu assets/manifest.json.
- Sửa đúng 5 root node hiện có, giữ screen IDs và target file. Bản đầu không được owner chấp nhận; evidence cũ hết hiệu lực sau redraw. DONE=0; baseline chưa khóa.

## DEC-004 · 19/10/2026 · GitHub sau khi hoàn tất bootstrap và redesign
- Nguồn: yêu cầu trực tiếp mới nhất của owner: dùng gh tạo repo và upload sau khi xong toàn bộ task.
- Cho phép tạo repo GitHub `savebite-figma`, chọn private vì chưa có yêu cầu công khai, rồi push các checkpoint của task.
- Override riêng lệnh cấm push/tạo repo trong DEC-001. Không tạo PR, không mời thành viên, không public Figma hoặc đổi quyền chia sẻ.
- Chỉ push sau QA và kiểm tra files/secrets. Không ghi đè repo/remote có sẵn không thuộc task.

## DEC-005 · 19/10/2026 · Owner yêu cầu bỏ toàn bộ mock cũ, dựng lại
- Owner tiếp tục từ chối v0.2, yêu cầu xóa các màn mock cũ và không vá bố cục đã làm.
- Cho phép xóa đúng 5 frames và page Components do agent tạo trong phiên; không xóa Page 1 hoặc nội dung người khác. Dựng lại đúng 5 SB-IDs với node IDs mới, registry sẽ theo read-back mới.
- Chọn bố cục mobile marketplace gọn: nền trắng, body charcoal, green CTA, ảnh thật, danh sách hero card + compact offer để so sánh; detail dùng ảnh lớn và pickup information dày vừa đủ. Summary tập trung terms/total, success có QR demo + mã dự phòng được ghi rõ minh họa.
- Foundations/tokens được reuse và điều chỉnh type scale/dark body cho hướng mới; không giữ canvas mock cũ như một baseline. v0.1/v0.2 đều REJECTED, DONE=0.
- Skills local frontend-design và ui-ux-pro-max đã đọc trước rebuild; official Figma skills thực thi native UI.
