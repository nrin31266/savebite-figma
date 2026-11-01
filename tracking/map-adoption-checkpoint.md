# Owner map adoption · 01/11/2026

DEC-022, owner yêu cầu tách phần cần dùng của map mới vào app. Một writer `codex/direct-map-adoption`; lease **RELEASED**. Không commit/push, không đổi100 roots, không owner acceptance.

- Source Components `11:2`: frame `499:7922`600×471 gồm base `499:7923`, marker vector `499:7924`, address tooltip `499:7946`. Base hash `1ae19c4d59856d2929186dd411e280ecb36ef04e`, ảnh gốc1200×942. Giữ nguyên source, pin xanh và địa chỉ470; chỉ dùng base trong app.
- Main `MapCanvas` **16:3 giữ ID**, đổi fills sang base IMAGE/FILL; legacy vector children ẩn, không xóa.8 instances trên003/011/016/017/032/039/065/094 đã đối chiếu main/hash và ẩn legacy overrides. Không thêm main: registry148; local image manifest vẫn30 vì ảnh được reuse trực tiếp bằng Figma hash, không tải bitmap mới vàoassets.
-003/011/094 resize bản đồ vừa viewport353×340/320/270;032 là crop353×124 từ nền353×277.1. Không kéo méo ảnh.016/017/039/065 giữ pin/giá/preview/CTA native; badge “Ghim mẫu · Chưa xác minh vị trí”. Status017/039 có nền opaque để chữ đường không chạy qua giờ/pin.
- Ẩn hai tuyến nét đứt `445:4961` và `442:4958`; không có route thực để vẽ trên nền thật.039/065 nhắc xác nhận địa chỉ/lối vào, không gán địa chỉ470 cho merchant.094 giữ Icon/MapPin/tâm khu vực và radius states; vòng không được coi là đo địa lý.

Evidence: [source hierarchy](evidence/map-adoption/source.json), [main write/probe](evidence/map-adoption/main-write.json), [app IDs](evidence/map-adoption/app-write.json), [readback](evidence/map-adoption/readback.json), [chrome fix](evidence/map-adoption/chrome-fix.json), [checks](evidence/map-adoption/checks.json), [overview5 màn chính](evidence/map-adoption/overview.png). Trước/sau5 màn chính và sau8 màn nằm cùng thư mục, registry link từng PNG.

PASS scoped: screenshot8 screens, crop/pin/CTA visual review,100 root IDs và8 main/hash/component mappings, legacy/path hidden, PNG decode. Probe522:846 ghi/đọc/xóa thành công. Readback call đầu quá48KB nên không trả evidence; đã thu hẹp read-only và lưu thành công, không retry canvas mutation.

NOT CHECKED: Present sau đổi nền, full8-screen/5-SKU interactions, mobile, Dynamic Type, accessibility/contrast toàn màn, usability và owner acceptance. Existing reactions chỉ được giữ/read, chưa bấm lại. Provider/license/attribution nguồn map chưa xác minh; asset candidate cho prototype, chưa duyệt công bố. Nền thật không chứng minh tọa độ merchant, cự ly, đường đi, GPS hoặc ETA.

Plugin browser lỗi trước đây không chặn reuse layer owner đã xuất. [Tài liệu hãng](https://divriots.com/blog/introducing-maps-to-design/) xác nhận export image/fill và marker có thể chỉnh; không chứng minh license của data provider trong ảnh này.
