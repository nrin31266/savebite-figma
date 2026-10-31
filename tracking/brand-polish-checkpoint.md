# Brand & sourced-layout polish · 31/10/2026

Owner-authorized theo DEC-014/015, một writer `codex/direct-polish`, không giao agent. PR [#2](https://github.com/nrin31266/savebite-figma/pull/2) đã merge phần trước vào main; phần checkpoint này ở branch `design/brand-and-screen-polish`. **Goal vẫn ACTIVE; DONE0; chưa owner acceptance.**

## Nguồn và inventory

- [Tuyển chọn mẫu theo chức năng](../docs/references/curated-layouts.md): preview shadcn Luma, Crouton và Things đã xem trực quan; Too Good To Go/IKEA mới đọc mô tả chính thức. Phân biệt tham khảo với asset import thật.
- 100 root live giữ IDs. Registry **145 component entries**, bao gồm legacy/candidate và dependencies; không phải145 component độc lập đã đạt QA. [Live usage](evidence/polish/live-usage.json) tính cả trạng thái visibility có binding, bỏ legacy hidden không có binding. `BACK`/conditional actions không thể suy ra đầy đủ từ cột linked_to.
- [31 original brand SVG](../assets/brand/mam/sources.json):8 Mầm poses,3 BagMark tones,4 patterns,2 wordmarks,6 stickers,8 activity states. Board [231:554](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=231-554); [ảnh board](evidence/polish/after/brand-suite.png). Wordmark vẫn editable text trên canvas; SVG export outline chữ để portable. Concept chưa owner duyệt.
-7 Phosphor Duotone nguồn mới, native masters `262:817/821/825/829/833/837/841`, board [262:845](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=262-845). [Sheet](evidence/polish/after/pantry-icon-sheet.png), [category picker](evidence/polish/after/SB-078.png). Original SVG/MIT/hash trong `assets/icons/phosphor/sources.json`; không claim tự vẽ các glyph này.
- Apple Keyboard remote set `235:651`, Email main `235:788`, Text main `235:972`; app instances `100:1885`/`17:345`. Source paste đã vào board rồi được reparent về Components; không copy lặp. Keys giữ nguồn và dependencies, localize dấu cách/Gửi/Tìm.
- SDS Card set `261:5371`, main `261:5376`; instance `263:4660` ở SB-081. Source-native instance/slot còn nguyên; override text, fills, ảnh và kiểu chữ cho app.

## Đã sửa và kiểm trực quan

- Entry001–012: mark/wordmark mới; Splash activity thay nút tap giả; Onboarding004 có minh họa Pantry; sửa Skip alignment; Email007/010 có hướng dẫn đúng thay countdown/CTA chỉ đường;011 có chọn khu vực thủ công,012 bỏ claim mọi cửa hàng nhắc60 phút. Login không báo lỗi mật khẩu ngay khi vừa vào. Email fixture thống nhất `minhanh@example.com`.
-006 checkbox ban đầu tắt; native SDS control atom + label hai dòng, CTA disabled khi chưa xác nhận. Liên kết “Điều cần biết”→099 và “Quyền riêng tư”→098; Back hai màn này dùng native BACK.005 bỏ câu tự động đồng ý điều khoản khi chỉ xem món.
-019 dùng Apple Text Keyboard native; bỏ ký tự cursor `|`, outline vuông thừa và số gợi ý không khớp nội dung.
-048 thêm ảnh bánh nguồn, sửa merchant wrap, bỏ emoji, mốc demo17:40 đúng “còn20 phút” và giữ disclosure UNKNOWN. **Stock/time sang bước số lượng chưa đồng bộ toàn flow.**
-081 bỏ freshness progress suy đoán; ảnh sữa có nhãn minh họa, ngày21/10/2026, còn2 ngày theo mốc19/10,1 hộp/ngăn mát/ghi chú trống. Thêm Sửa→082, giữ đã dùng→086/đã bỏ→087. [Ảnh cuối081](evidence/polish/after/SB-081.png).082 vẫn sơ sài và chưa giữ dữ liệu sửa xuyên màn.
- [Entry001–005](evidence/polish/after/review-1.jpg), [Entry006–010](evidence/polish/after/review-2.jpg), [011/012/019/048/081](evidence/polish/after/review-3.jpg): native screenshot, sau sửa screenshot lại vùng thay đổi. Không dùng section crop cũ làm chứng cứ phiên bản cuối.

## Audit và verification

- Overview **100/100 đã chụp và xem** qua10 contact sheets trong `evidence/polish/`; không đồng nghĩa100 màn đọc được ở mức từng glyph. [Capture method](evidence/polish/capture-method.json):17 individual exports +83 section crops; padding40px mỗi cạnh đã đo/chỉnh.15 màn thay đổi được native screenshot full393×852, thêm078 để kiểm category. Screenshot MCP một số lần timeout; native `node.screenshot()` và Present là fallback thật, không tạo PASS từ timeout.
- Present393×852 đã bấm:006 chưa tick→CTA không chuyển; tick→enabled→007;007 đổi email→006;Privacy→098→Back006 giữ tick. Evidence [enabled](evidence/polish/after/consent-enabled.jpg), [verification edge](evidence/polish/after/email-verified-edge.jpg), [privacy return](evidence/polish/after/privacy-return.jpg).081 Sửa→082 đã bấm thật [edge](evidence/polish/after/SB-082-edge.jpg).
- Contrast pair arithmetic checked: forest/cream11.04, forest/wheat5.78, forest/paper8.17, secondary/cream5.23, secondary/sage4.74, terracotta/cream5.58. Chưa kiểm mọi scrim/ảnh/control disabled hoặc accessibility trên thiết bị thật.
- Activity có6 timed CHANGE_TO edges `.35s`/Smart Animate`.22s`,2 Static variants. Chưa chứng minh motion/reduced-motion bằng playback đầy đủ. Prototype whole-flow/a11y/mobile chưa PASS; `prototype_verified=false`.

Repository checks: `python3 scripts/validate.py` PASS (100 IDs,145 entries,26 image hashes,DONE0);71 SVG source hashes/XML PASS; local checkpoint links và evidence decode PASS; `git diff --check` PASS. Lease writer được giải phóng tại checkpoint, goal vẫn ACTIVE.

## Việc còn lại của goal đầy đủ

| Nhóm | Phát hiện cần xử lý tiếp |
|---|---|
| A001–012 | First-run vs returning demo history; auth return-intent khi đặt; keyboard Return và permission branches cần chạy Present. |
| B013–033 | Pin/preview giá không khớp017; invented merchants/counts018/020; danh sách021/031–033 lặp; selected SKU chưa theo xuyên flow. |
| C034–049+059 |037 có giờ sản xuất/khuyến nghị24h không có nguồn;045 có claim giá/chất lượng;041 trộn merchant; cần sửa nội dung trước mỹ thuật. |
| D050–073 | Quantity/stock/time context, stepper/filter, cancel reason và navigation states; pass/offline/retry phải chạy flow thật. |
| E074–090 |082 edit đủ trường;085 reminder sheet;086/087 selected state;075 snapshot sau lưu chưa phản ánh form; export/delete còn thiếu states. |
| F091–100 |092 toast trước action;093 links;095 grouping;096 empty asset;100 exit; privacy/export confirmation còn kiểm. |

Tiếp tục audit theo nhóm, dùng ảnh/kit phục vụ chức năng; không trải linh vật lên QR hoặc thông tin an toàn. Không coi overview, inventory hay merge là nghiệm thu thiết kế.
