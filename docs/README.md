# Bắt đầu làm SaveBite

SaveBite là thiết kế ứng dụng iPhone tiếng Việt: khám phá thực phẩm giá giảm cuối ngày → đặt giữ chỗ trước → đến cửa hàng nhận và thanh toán tại quầy; **Smart Pantry** hỗ trợ quản lý hạn dùng thực phẩm cá nhân tại nhà. Repo chỉ thực hiện Figma và tài liệu/bằng chứng thiết kế.

## Cho người mới

1. Đọc [luật agent](../AGENTS.md) và [progress](../tracking/progress.md) để nắm trạng thái gate hiện tại (`B-PHASE1-010 · FigmaWrite=BLOCKED` chờ kết nối Figma MCP vào phiên Claude Code) và phạm vi được phép sửa.
2. Đọc [product](product.md) để hiểu đối tượng người dùng, 20 quyết định mặc định (`D-001..D-020`), chính sách thanh toán tại quầy, nhận món, an toàn thực phẩm và dữ liệu fixture.
3. Đọc **Bộ 4 Tài liệu Định hướng Nghệ thuật & Chuẩn iPhone (Bắt buộc trước khi vẽ bất kỳ màn nào):**
   - [visual-direction](visual-direction.md): Phân tích các lỗi lịch sử từ pilot v0.5 (đã xóa), **Visual DNA (Warm Editorial Rescue Market)**, phân tầng 4 cấp độ bề mặt, typography và **10 quy tắc chống giao diện rập khuôn (Anti-Generic / Anti-Boxitis)**.
   - [ios-guidelines](ios-guidelines.md): Chuẩn thiết bị **iPhone 15 Standard (`393×852pt`, Dynamic Island `59pt`)** đã duyệt theo `DEC-011`, Apple Official Status Bar, Home Indicator `34pt`, Safe Areas, bàn phím và điều hướng chuẩn HIG.
   - [asset-strategy](asset-strategy.md): Chiến lược **Asset-First** (6 ảnh thực phẩm/cửa hàng thật từ Pexels, Phosphor Icons, Google Fonts, Apple UI Kit), kiểm chứng giấy phép và quy trình cập nhật `assets/manifest.json`.
   - [screen-art-direction](screen-art-direction.md): Phân loại **10 Screen Archetypes (`A1`–`A10`)** và ma trận định hướng thị giác chi tiết cho từng màn hình từ `SB-001` đến `SB-100`.
4. Đọc [experience](experience.md) cho luồng nghiệp vụ (`F-01..F-06`), danh mục 100 `SB-ID` và hợp đồng thiết kế **10 màn hình đại diện Phase 1** (`SB-002`, `SB-015`, `SB-016`, `SB-019`, `SB-034`, `SB-051`, `SB-053`, `SB-056`, `SB-075`, `SB-091`).
5. Đọc [design system](design-system.md) để nắm tokens, biến thể components và xem [screens](../tracking/screens.csv) cùng [components](../tracking/components.csv) để tra cứu trạng thái node ID thực tế.
6. Xem [acceptance](acceptance.md) để đối chiếu tiêu chí học phần và theo [workflow](workflow.md) để thực hiện quy trình 7 bước kiểm duyệt chất lượng (**Technical QA + Aesthetic QA**) cùng kế hoạch phân công **2 Agent độc lập (50/50 Page-Isolated Split)**. Không tự ý sản xuất 90 màn còn lại khi 10 màn Phase 1 chưa được owner duyệt.

**Kế hoạch hiện hành (31/10/2026):** [Plan 1 · Sửa 5 màn đầu Phase 1](plans/phase1-fix-sb002-sb034.md) → [Plan 2 · Dựng đủ 100 màn + prototype chuyển màn](plans/build-100-screens-prototype.md) (Plan 2 chỉ chạy sau owner duyệt Phase 1 và `DEC-012`).

Không cần file nguồn bên ngoài repo hoặc lịch sử chat để hiểu yêu cầu hiện hành. [Decisions](decisions.md) lưu các quyết định đã được owner phê duyệt (`DEC-001..DEC-011`).

## Mở thiết kế và kiểm tra

- File Figma đích duy nhất (`DEC-011`): [SaveBite-V2 trên Figma](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1). *(File cũ `NLTv70kDZ2i3HpOnOKQCDY` và 5 màn pilot v0.5 đã xóa/nghỉ hưu).*
- [Skills và setup cho teammate](references/agent-skills.md): bộ 6 skills dùng trong dự án, lệnh kết nối Figma MCP và lệnh khôi phục local.
- [Assets](../assets/manifest.json): nguồn Pexels, giấy phép và mã băm SHA-256 của 6 ảnh thực phẩm & cửa hàng chuẩn.
- [Read-back](../tracking/evidence/figma-readback.json) và [QA](../tracking/evidence/qa.json) lưu trạng thái xác minh kỹ thuật của file `7suZz9C8oL5zV2NMxlsIVI`; luôn phải đọc Figma live trước mỗi lần ghi canvas.

```sh
python3 scripts/validate.py
```

Validator kiểm tra tính toàn vẹn của tài liệu, liên kết nội bộ, registry và mã băm tài nguyên trên đĩa; **Technical PASS không đồng nghĩa với Aesthetic PASS** hay chứng minh kết nối Figma MCP hiện tại đang mở.

## Quyền sở hữu thông tin theo Domain

| Tài liệu | Phạm vi sở hữu chính (Canonical Ownership) |
|---|---|
| [product.md](product.md) | Nghiệp vụ, mô hình người dùng, `D-001..D-020`, state machine đơn hàng, chính sách dị ứng/an toàn và dữ liệu fixture. |
| [experience.md](experience.md) | Kiến trúc thông tin (IA), 6 luồng chính (`F-01..F-06`), danh mục gốc 100 `SB-ID` và hợp đồng vận hành 10 màn Phase 1. |
| [visual-direction.md](visual-direction.md) | Visual DNA, bài học critique từ v0.5, quy tắc bố cục chống rập khuôn (anti-boxitis), nhịp điệu thị giác và chiến lược chuyển động. |
| [ios-guidelines.md](ios-guidelines.md) | Khung thiết bị iPhone 15 (`393×852pt`), Apple HIG system chrome (Status Bar, Dynamic Island, Home Indicator), safe areas và mẫu điều hướng iOS. |
| [asset-strategy.md](asset-strategy.md) | Chính sách Asset-First, nguồn ảnh Pexels/icon Phosphor/font, xác minh bản quyền và quy tắc provenance trong `assets/manifest.json`. |
| [screen-art-direction.md](screen-art-direction.md) | 10 Screen Archetypes (`A1`–`A10`) và định hướng bố cục/điểm nhấn riêng cho từng màn trong 100 `SB-ID`. |
| [design-system.md](design-system.md) | Hệ thống Design Tokens, bảng màu, thang chữ, quy cách Component/Variant và hướng dẫn tái sử dụng trên Figma. |
| [workflow.md](workflow.md) | Quy trình thực thi Figma, quản lý lease, phân công 2 Agent (50/50 Split), 7 cổng kiểm duyệt chất lượng (Quality Gates), **Aesthetic Rubric** và nghiệm thu. |
