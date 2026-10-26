# Bắt đầu làm SaveBite

SaveBite là thiết kế ứng dụng iPhone tiếng Việt: khám phá thực phẩm giá giảm cuối ngày → đặt giữ chỗ trước → đến cửa hàng nhận và thanh toán tại quầy; **Smart Pantry** hỗ trợ quản lý hạn dùng thực phẩm cá nhân tại nhà. Repo chỉ thực hiện Figma và tài liệu/bằng chứng thiết kế.

## Cho người mới

1. Đọc [luật agent](../AGENTS.md) và [progress](../tracking/progress.md) để nắm trạng thái gate hiện tại (`AWAITING_OWNER_REVIEW`) và phạm vi được phép sửa.
2. Đọc [product](product.md) để hiểu đối tượng người dùng, 20 quyết định mặc định (`D-001..D-020`), chính sách thanh toán tại quầy, nhận món, an toàn thực phẩm và dữ liệu fixture.
3. Đọc **Bộ 4 Tài liệu Định hướng Nghệ thuật & Chuẩn iPhone (Bắt buộc trước khi vẽ bất kỳ màn nào):**
   - [visual-direction](visual-direction.md): Đánh giá thẳng thắn pilot v0.5, **Visual DNA (Warm Editorial Rescue Market)**, phân tầng bề mặt, typography và **10 quy tắc chống giao diện rập khuôn (Anti-Generic / Anti-Boxitis)**.
   - [ios-guidelines](ios-guidelines.md): Chuẩn thiết bị iPhone (`390×844` hiện hành vs đề xuất `iPhone 15 — 393×852pt Dynamic Island`), Apple Official Status Bar, Home Indicator `34pt`, Safe Areas, bàn phím và điều hướng chuẩn HIG.
   - [asset-strategy](asset-strategy.md): Chiến lược **Asset-First** (Pexels, Unsplash, Phosphor Icons, Google Fonts, Apple UI Kit), kiểm chứng giấy phép và quy trình cập nhật `assets/manifest.json`.
   - [screen-art-direction](screen-art-direction.md): Phân loại **10 Screen Archetypes (`A1`–`A10`)** và ma trận định hướng thị giác chi tiết cho từng màn hình từ `SB-001` đến `SB-100`.
4. Đọc [experience](experience.md) cho luồng nghiệp vụ (`F-01..F-06`), danh mục 100 `SB-ID` và hợp đồng dữ liệu 5 màn pilot.
5. Đọc [design system](design-system.md) để nắm tokens, biến thể components và xem [screens](../tracking/screens.csv) cùng [components](../tracking/components.csv) để tra cứu node ID thực tế.
6. Xem [acceptance](acceptance.md) để đối chiếu tiêu chí học phần và theo [workflow](workflow.md) để thực hiện quy trình 7 bước kiểm duyệt chất lượng (**Technical QA + Aesthetic QA**). Thiết kế hiện tại chưa được owner chấp nhận; không tự ý sản xuất thêm 95 màn khi chưa qua cổng duyệt.

Không cần file nguồn bên ngoài repo hoặc lịch sử chat để hiểu yêu cầu hiện hành. [Decisions](decisions.md) lưu các quyết định đã được owner phê duyệt.

## Mở thiết kế và kiểm tra

- File Figma đích duy nhất: [SaveBite trên Figma](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=2-2).
- [Prototype pilot](https://www.figma.com/proto/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?page-id=2%3A2&node-id=28-2&starting-point-node-id=28%3A2&scaling=scale-down) hiện là subset 5 màn (`SB-015 → SB-034 → SB-051 → SB-053 → SB-056`), chưa phải `F-01` đầy đủ.
- [Skills và setup cho teammate](references/agent-skills.md): bộ 6 skills dùng trong dự án và lệnh khôi phục local.
- [Assets](../assets/manifest.json): nguồn, giấy phép và mã băm SHA-256 của các ảnh thực phẩm mẫu.
- [Read-back](../tracking/evidence/figma-readback.json) và [QA](../tracking/evidence/qa.json) là dữ liệu kiểm tra kỹ thuật của checkpoint v0.5; luôn phải đọc Figma live trước lần sửa canvas tiếp theo.

```sh
python3 scripts/validate.py
git status --short --branch
```

Validator kiểm tra tính toàn vẹn của tài liệu, liên kết nội bộ, registry và mã băm evidence trên đĩa; **Technical PASS không đồng nghĩa với Aesthetic PASS** hay chứng minh kết nối Figma hiện tại đang mở.

## Quyền sở hữu thông tin theo Domain

| Tài liệu | Phạm vi sở hữu chính (Canonical Ownership) |
|---|---|
| [product.md](product.md) | Nghiệp vụ, mô hình người dùng, `D-001..D-020`, state machine đơn hàng, chính sách dị ứng/an toàn và dữ liệu fixture. |
| [experience.md](experience.md) | Kiến trúc thông tin (IA), 6 luồng chính (`F-01..F-06`), danh mục gốc 100 `SB-ID` và hợp đồng vận hành màn hình. |
| [visual-direction.md](visual-direction.md) | Visual DNA, critique thẩm mỹ, quy tắc bố cục chống rập khuôn (anti-boxitis), nhịp điệu thị giác và chiến lược chuyển động. |
| [ios-guidelines.md](ios-guidelines.md) | Khung thiết bị iPhone, Apple HIG system chrome (Status Bar, Dynamic Island, Home Indicator), safe areas và mẫu điều hướng iOS. |
| [asset-strategy.md](asset-strategy.md) | Chính sách Asset-First, nguồn ảnh/icon/font, xác minh bản quyền và quy tắc provenance trong `assets/manifest.json`. |
| [screen-art-direction.md](screen-art-direction.md) | 10 Screen Archetypes (`A1`–`A10`) và định hướng bố cục/điểm nhấn riêng cho từng màn trong 100 `SB-ID`. |
| [design-system.md](design-system.md) | Hệ thống Design Tokens, bảng màu, thang chữ, quy cách Component/Variant và hướng dẫn tái sử dụng trên Figma. |
| [workflow.md](workflow.md) | Quy trình thực thi Figma, quản lý lease, 7 cổng kiểm duyệt chất lượng (Quality Gates), **Aesthetic Rubric** và nghiệm thu. |
