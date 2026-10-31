# Entry & Discovery UI · 01/11/2026

Một writer trực tiếp `codex/direct-discovery-ui`; lease RELEASED tại checkpoint. Goal polish100 màn vẫn ACTIVE, không có owner acceptance hoặc DONE. Giữ100 root IDs,148 component entries và30 ảnh/minh họa; không thêm app code hoặc mua kit.

## Thay đổi trên canvas

-013/015: banner túi bánh353×112 thay hero quá cao, dùng lại minh họa nguồn`161:45`, forest/radius-md và headline22/26. Giá29.000đ, nhận18:00–19:00; sao chép đúng context/reactions từ nguồn`190:4447` tới044, thay đường031 trước đó. Category tiles82×64, content gap16;4 OfferCard instances169×246 với body HUG, giá kết thúc ở664pt, cả card kết thúc677pt trước bottom nav769pt. Main`15:160` không đổi. Filter013 sửa lệch/rộng về48×48 tại x325.
-014: giữ root`101:1924`, thêm viewport`472:5005` và body Auto Layout`472:5006`; lời chào → Search/Filter → đơn đang chờ nhận →3 món ảnh thật. Nhắc đơn giữ fixture bánh25K/17–18 độc lập với browsing context; strip`101:1959`353×86, bỏ nền trắng lồng không có ý nghĩa, thêm CaretRight instance`472:5017`. Reuse BrandHeader`474:5008`; header cũ giữ ẩn. Ba tab Orders/Pantry/Account nhận reactions từ015, gồm điều kiện Pantry empty/list đang có.
-003: mỗi pin có giờ riêng (bánh17–18, bữa ăn17:30–19); text`475:5008/5009`, minh họa vị trí được ghi rõ, không biến thành bản đồ thật.002→003→004 dùng Smart Animate220ms/Ease Out khi bấm Tiếp tục.002/004 được xem lại, không vẽ lại nội dung đang hợp lý.
-005: ghi chú quyền dùng guest tăng12/18; giữ ảnh bánh, wordmark cream và SDS controls. Không đổi gate đăng nhập khi giữ chỗ.
-013/014/015: nối khu vực→018, tim→033, chuông→095; source icon40pt giữ nguyên, thêm6 native transparent hit frames44×44 (`481:5020/5022/5024/5026/5028/5030`). Resize nested source instance không giữ44pt, nên không claim icon đã đổi kích thước.014 trước đó có tab/header hình nhưng thiếu reactions.

## Evidence và QA giới hạn

[003](evidence/entry-discovery-ui/SB-003.png), [005](evidence/entry-discovery-ui/SB-005.png), [013](evidence/entry-discovery-ui/SB-013.png), [014](evidence/entry-discovery-ui/SB-014.png), [015](evidence/entry-discovery-ui/SB-015.png). [Readback](evidence/entry-discovery-ui/final-readback.json), [navigation sau sửa](evidence/entry-discovery-ui/navigation.json), [hit areas](evidence/entry-discovery-ui/hit-areas.json). Native screenshot014 có một lần thiếu icon tab dù readback còn; [Present014](evidence/entry-discovery-ui/runtime-returning.png) và capture cuối hiển thị đủ. Không suy diễn nguyên nhân rendering.

Present đã bấm thật:005→013→044 ([giá/giờ/cảnh báo túi bánh](evidence/entry-discovery-ui/runtime-surprise.png));002→003→004 ([đích004](evidence/entry-discovery-ui/runtime-onboarding.png));014 tim→033, chuông→095 và tab Orders→060. Smart Animate chỉ được xác nhận reaction và đến đúng đích; chưa đánh giá chất lượng chuyển động bằng video hoặc Reduce Motion.

PASS scoped:7 root393×852,4 cards above nav,3 filter48pt,6 header targets44pt, main-instance mapping; repository validator và evidence decode được kiểm tại checkpoint. Chưa bấm toàn bộ CTA/filter/category/back, tất cả SKU, Pantry conditional branches ở014, mobile device, Dynamic Type, screen reader hoặc6 flow đầy đủ. `prototype_verified=false`, DONE0; cần tiếp tục Offer/Search/Orders và lỗi F05 drift cũ.

Hướng ảnh→tên→giá/điều kiện tham khảo Airbnb/Groc trong [source manifest](../docs/references/curated-layouts.md), dùng ảnh và component pool SaveBite; không nhập asset đối thủ. Apple Search và SDS controls vẫn là native source-linked. Maps.to.design/PlotSet chưa nhập được do lỗi môi trường ghi ở các checkpoint trước; batch này không thử launch lặp lại hoặc yêu cầu restart thêm.
