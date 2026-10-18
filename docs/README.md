# Bắt đầu làm SaveBite

SaveBite là thiết kế mobile tiếng Việt: khám phá thực phẩm giá giảm → đặt trước → đến cửa hàng nhận; Smart Pantry hỗ trợ quản lý thực phẩm cá nhân. Repo chỉ làm Figma và docs/evidence thiết kế.

## Cho người mới

1. Đọc [luật agent](../AGENTS.md) và [progress](../tracking/progress.md) để biết scope đang được phép sửa.
2. Đọc [product](product.md) để hiểu đối tượng, 20 defaults, payment/pickup/safety và fixture.
3. Đọc [experience](experience.md) cho flows, 100 SB-IDs và contracts 5 màn pilot.
4. Đọc [design system](design-system.md) trước khi vẽ; xem [screens](../tracking/screens.csv) và [components](../tracking/components.csv) để tìm node thật.
5. Xem [acceptance](acceptance.md) để biết tiêu chí môn học và những phần chưa có evidence.
6. Theo [workflow](workflow.md) để kết nối, reuse, chỉnh và QA. Thiết kế hiện tại chưa được owner chấp nhận; không tự rollout thêm 95 màn.

Không cần file nguồn ngoài repo hoặc chat history để hiểu yêu cầu hiện hành. [Decisions](decisions.md) lưu thay đổi scope/nghiệp vụ đã duyệt; khi task mới thay đổi scope phải cập nhật domain tương ứng.

## Mở thiết kế và kiểm tra

- File duy nhất: [SaveBite trên Figma](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=2-2).
- [Prototype pilot](https://www.figma.com/proto/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?page-id=2%3A2&node-id=28-2&starting-point-node-id=28%3A2&scaling=scale-down) chỉ là subset 5 màn, chưa phải F-01 đầy đủ.
- [Skills và setup cho teammate](references/agent-skills.md): bộ skill cần dùng và cách khôi phục local. Cài skill không thay thế kết nối/quyền Figma.
- [Assets](../assets/manifest.json): nguồn/license/hash hai ảnh món demo.
- [Read-back](../tracking/evidence/figma-readback.json) và [QA](../tracking/evidence/qa.json) là checkpoint v0.5 đã read-back; vẫn cần đọc live trước lần sửa canvas tiếp theo.

```sh
python3 scripts/validate.py
git status --short --branch
```

Validator kiểm docs, registry và evidence trên đĩa; PASS không chứng minh canvas hiện tại hoặc kết nối Figma đang đúng.

## Quyền sở hữu thông tin

Product sở hữu nghiệp vụ; experience sở hữu flows/màn; design-system sở hữu visual/components; workflow sở hữu thực thi/QA. Registry chỉ giữ hiện trạng và mapping. Figma live chứng minh node hiện tồn tại. Không âm thầm ghi đè nguồn khác để làm chúng trông khớp nhau.
