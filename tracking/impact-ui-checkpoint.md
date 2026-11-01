# Account & Impact UI · 01/11/2026

Goal tổng thể UI100 màn/plugin/chart/motion vẫn ACTIVE. Batch này chỉ sửa091/100, giữ root IDs và bộ fixture3 đơn/4 Pantry; không tăng số main component. Một writer trực tiếp, lease `codex/direct-impact-ui` RELEASED tại checkpoint, không push/merge.

## Canvas đã thay đổi

-100: viewport native `461:4965`, body Auto Layout `461:4966`; hero giữ frame`85:1469`,3 phần/3 đơn **dữ liệu mẫu** và4 món Pantry. Dùng lại Mầm Celebrate master`231:314`, instance`461:4968`, không tạo thêm mascot.
- Chart`461:4984` so sánh **số tiền đã trả theo từng đơn**, không phải trend, savings hoặc CO₂.25K/30K/35K, tổng90K; track285pt, bars203.5714/244.2857/285pt bắt đầu từ0. Tên món14pt, giá14pt, ngày12pt, ảnh56pt từ pool có sẵn. Native text/rectangles/Auto Layout editable; không claim chart được import từ plugin.
- Giữ3 row IDs`85:1476/1480/1484` và label/amount IDs; ẩn các line divider cũ sau khi phát hiện chúng chiếm353pt trong horizontal flow làm info còn1pt. Methodology ngắn, nói rõ chưa có giá gốc/phương pháp CO₂.
-091:6 settings rows nới273→321pt; fix inherited SPACE_BETWEEN thành MIN để gap icon–label thực sự12pt. Labels257pt và chevron16pt, rows72pt. Reuse CaretRight`98:44`; card impact master`16:186` thêm chevron, không thêm main. Copy “Phần đã nhận tại quầy” đúng đơn vị; card đã có route100 được giữ. Back100→091 có hotspot48pt.

## QA và nguồn

[091](evidence/impact-ui/SB-091.png), [100](evidence/impact-ui/SB-100.png), [readback](evidence/impact-ui/readback.json). [Present091→100](evidence/impact-ui/runtime-impact.png), [Back100→091](evidence/impact-ui/runtime-account.png) và [cuộn tới cuối091](evidence/impact-ui/runtime-account-scroll.png) đã chạy thật. Native screenshot kiểm title/amount/date không wrap, photo/bar/mascot/copy rõ và safe area giữ nguyên. Chưa kiểm Dynamic Type, screen reader, đích đến tất cả6 menu rows hoặc toànflow; prototype_verified=false, DONE0, owner acceptance chưa có.

Đã đọc [shadcn bar charts](https://ui.shadcn.com/charts/bar) làm nguồn tham khảo chart; không nhập React/app code vào repo. Local UI/UX chart guidance: dùng bar so sánh category với direct labels; không dùng line/radar để suy ra xu hướng từ3 order mẫu.

**PlotSet:** tìm đúng [plugin chính thức](https://www.figma.com/community/plugin/1421122515439713398/plotset-charts-and-maps), bấm Save trong Figma; sau đó plugin xuất hiện trong kết quả đã lưu và chạy được bước Loading. Launch báo **“An error occurred while loading the plugin environment”**, giống maps.to.design. Chưa có chart import từ plugin, chưa đăng nhập PlotSet hoặc gửi dữ liệu tới dịch vụ. [Tài liệu hãng](https://plotset.net/integrations/figma) mô tả exportSVG editable; khả năng đó chưa xác minh thực tế ở phiên này. Không mua gói trả phí.

Tiếp tục: kiểm các nhóm Entry/Discovery/Offer còn hời hợt và motion có chủ ý; source map/plugin vẫn chưa hoạt động. Không coi hai màn này là hoàn tất goal tổng thể.
