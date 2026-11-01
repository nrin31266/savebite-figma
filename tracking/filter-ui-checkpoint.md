# Filter UI023–026 · 01/11/2026

Owner yêu cầu kiểm tra023–026 vì còn sơ sài. File `7suZz9C8oL5zV2NMxlsIVI`, page `11:3`; một writer `codex/direct-filter-ui`, lease **RELEASED**. DEC-021; không sửa source masters/tokens, không thêm root hoặc main. Bốn màn vẫn **NEEDS_REWORK** vì logic lọc chưa hoàn chỉnh.

## Kết quả UI

| Màn | Root giữ nguyên | Thay đổi | Sheet cuối |
|---|---|---|---|
|023|`103:2173`|Group rõ, chips44pt, header/close44pt; ngân sách/giờ/nhu cầu mở024/025/026; bỏ giá gắn cứng vào tên loại ưu đãi|519pt/y333|
|024|`103:2215`|Bỏ encoding chiều cao cột không có dữ liệu; presets30K/50K/tùy chỉnh/không giới hạn theo experience. Native Check chỉ trạng thái30K mẫu; gap8 thay Space-between trong HUG|530pt/y322|
|025|`103:2256`|Bốn rows64pt, textHEIGHT/FILL, bỏ nền trắng con trên selected row, Check native ở giờ17–18|511pt/y341|
|026|`103:2297`|Rows56pt; cảnh báoHEIGHT hết tràn722pt, bỏ mãD-007 và suy diễn chung quầy gluten/trứng; nhắc xác minh thành phần trước khi đặt|541pt/y311|

Cả cụm dùng Discovery preview native từ các node đã có: BrandHeader `17:65`, Search/filter `201:4418`, CategoryStrip `17:94`, banner `17:123`; clone context tắt reactions, scrim40%. Giữ source image hash, không tạo ảnh/phẳng hóa UI. Source instances và mains tra được ở readback/registry. Header20pt Be Vietnam Pro; source buttons52pt, radius28 ở hai góc trên sheet,14 cho controls; CTA kết thúc tại806, cách đáy46pt. Không rải minh họa không liên quan vào bộ lọc.

## Evidence và giới hạn

- [Tổng quan sau sửa](evidence/filter-ui/after-overview.png), [readback](evidence/filter-ui/readback.json), [write IDs](evidence/filter-ui/write.json), [targeted fix IDs](evidence/filter-ui/fix.json), [checks](evidence/filter-ui/checks.json).
- [023 trước](evidence/filter-ui/before-SB-023.png) / [sau](evidence/filter-ui/after-SB-023.png); [024 trước](evidence/filter-ui/before-SB-024.png) / [sau](evidence/filter-ui/after-SB-024.png); [025 trước](evidence/filter-ui/before-SB-025.png) / [sau](evidence/filter-ui/after-SB-025.png); [026 trước](evidence/filter-ui/before-SB-026.png) / [sau](evidence/filter-ui/after-SB-026.png).
- PASS scoped: PNG decode, sheet bounds/bottom gap46, text horizontal bounds trong sheet, gap8 ngân sách,100 root IDs khớp registry, toàn bộ source instance mains có mapping. Chụp cả4 cùng lượt trước/sau và sửa1 lượt theo lỗi nhìn thấy.
- READBACK ONLY: closeBACK;023→024/025/026; Save024–026→023, Apply023→021. Chưa bấm được Present do browser403; không gọi đây là navigation QA PASS.
- **Chưa hoàn tất:** lựa chọn budget/slot/dietary và reset chưa có state/reactions; tùy chỉnh chưa có input; Apply chưa tính tập kết quả. Chưa chứng minh tìm món đúng nhu cầu hoặc lưu filter khi Back. Không suy diễn khả năng ăn chay/dairy-free/ít ngọt từ fixture. Hai nhãn gộp “Ăn chay / Thanh đạm”, “Ít ngọt / Nguyên cám” còn cần tách nghĩa khi triển khai filter logic.
- NOT CHECKED: keyboard, Dynamic Type, contrast/a11y toàn màn, mobile, usability,6 flows và owner acceptance. Toàn100 màn chưa hoàn chỉnh; DONE0.
