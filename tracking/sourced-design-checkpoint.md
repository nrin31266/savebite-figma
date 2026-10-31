# Sourced kit & design correction · 31/10/2026

Status: **PARTIAL DESIGN REVIEW · end-to-end work remains IN_PROGRESS · DONE0**. Một writer `codex/direct`, không spawn agent. Scope checkpoint: native kit/assets, sửa entry/discovery/category/gallery/Pantry và reconcile inventory. Lease RELEASED tại checkpoint; chưa nghiệm thu toàn app.

## Output thực

- File duy nhất được ghi: [SaveBite-V2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=11-3). Live100 native SB roots;49 DESIGN_REVIEW,51 NEEDS_REWORK; không suy ra đủ nội dung/đẹp từ số frame. [Inventory read-back](evidence/direct/live-inventory.json); registries đã reconcile100 roots/90 component entries.13 root dựng thêm:083/084/086–090/094–099.12 root Plan-B trước đó được reconcile, không claim do writer này tạo.
- Bốn section sắp thứ tự SB-ID,5 cột; kích thước chứa đủ các root, bỏ double-offset khiến màn nằm ngoài section. Giữ IDs và dữ liệu cũ; legacy nội dung thay thế được ẩn, không reset canvas.
- [Curated UI native catalog](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=198-189): Apple Toggle/Search thực, Figma Simple Design System Button/Input và samples selection. App dùng5 Toggle/7 Search instances; Button/Input source đã được áp vào các màn sử dụng, màu/type/radius chỉnh cho SaveBite.
- Apple source file owner `Y8CWXWyBsyDuvniwEwmBvj`: copy source Toggle `128:47034`, Search `128:47204` qua clipboard browser đang đăng nhập. Destination `158:197`/`158:210`. Không viết nguồn. Library-key import Apple26 vẫn báo permission; **không** tuyên bố import toàn kit. Toggle51×31 trong touch bounds64×48, giữ Smart Animate200ms.
- [Photo Library](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=161-2):26 cell có image fill thật sau read-back, gồm25 ảnh Pexels +1 generated kraft-bag concept. Main manifest26 bản ghi có source/license/hash.13 image hashes khác nhau hiện diện trong phần hiển thị của app; số này không chứng minh mọi mapping đã QA. Ảnh bát rau/ngũ cốc1640777 được đánh context-only, không đại diện món cơm gà.
- [Icon Essentials](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=144-127):24 core Phosphor Regular giữ main IDs,4 Duotone có MIT/source/hash;3 custom vector MilkCarton/PickupPass/Pantry. [Brand concept](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=137-44): RescueMark forest/cream;5 SVG xuất native và provenance ở `assets/icons/savebite/`. Chưa owner acceptance.

## Nguồn bố cục và cách dùng

| Nguồn | Đã tham khảo / cách áp dụng |
|---|---|
| [Crouton](https://crouton.app/) | Website và ảnh product nhìn trực tiếp qua browser: ảnh món rõ, thông tin định lượng gọn. Áp vào category/gallery; không copy branding hoặc product screenshot vào app. |
| [Mela](https://mela.recipes/) | Đọc mô tả native recipe viewer/cook mode từ nguồn gốc. Ảnh source fetch timeout; không claim visual audit screenshot Mela. Tham khảo nội dung tập trung theo tác vụ. |
| [Things](https://culturedcode.com/things/features/) | Tham khảo tổ chức danh sách/nhóm. Pantry dùng hàng nhẹ, label ngày rõ, hành động cạnh món; account dùng grouped list. |
| [Apple Wallet](https://www.apple.com/wallet/) | Tham khảo pass hierarchy: giờ, món, QR/mã dự phòng và thanh toán tại quầy. Không thêm chức năng Wallet integration vào requirements. |
| [shadcn preset owner chọn](https://ui.shadcn.com/create?preset=b1aIuQ2XC&item=preview) | Tham khảo primitives và hierarchy. Giữ forest/cream/Be Vietnam Pro/Fraunces; không migrate Blue/Raleway/Remix. Obra Community đã xem; không claim Luma Pro miễn phí hoặc MIT. |

## Correction có ảnh và read-back

- Entry/brand001–005: sửa CTA, skip, copy và brand concept. Discovery013/015 có dedicated scroll, ảnh editorial khác ảnh listing, search Apple + filter48pt riêng.014 giảm duplicate/sai copy, giữ active-order strip.
- Category028/029/030 có ảnh, headline và nội dung riêng; bỏ ba meal rows trùng nhau ở028 và meal sai nhóm ở030. Bakery hai SKU đúng25K/30K; produce dùng tên fixture,30K/slot16:00–17:30. Listing/selected-offer routing toàn app chưa hoàn tất.
- Gallery035 trước trống ảnh; nay2 ảnh sourced, thumbnail đổi ảnh bằng biến, close về034. Gỡ claim “ảnh thực tế chụp tại quầy”. Merchant038 có ảnh source; surprise044 có minh họa túi đóng kín và copy không cam kết thành phần.
- Reviews042/043: bỏ visible rating4.8/120 lượt và lời nhận xét dựng; dùng empty states trung thực. Legacy bị ẩn để bảo toàn, không được tái sử dụng làm dữ liệu thật.
- Pantry075 có7 fixture tương ứng summary và storage counts; semantic date rows, scroll và item actions.074/076 là intro/empty đúng chức năng, không còn marketplace empty-search copy.077/080 dùng source Input/Button, category/date/storage bindings; không chứng minh nhập/lưu dữ liệu thật.
- QA thực phát hiện picker078: main HUG62pt và hàng48pt làm tile đè. Sửa8 master168×112 fixed Auto Layout,4 hàng112pt, header/close48pt và handle căn giữa.079 sửa header/close, dock nằm trên home safe area,31 selected-day variables; chọn22 chuyển highlight và trả ngày về form/confirmation.
-056 giữ native pass/QR, sửa checklist và hai hành động “Chỉ đường”/“Xem đơn của tôi”, close48pt.091 sửa grouped settings labels/spacing và scroll. Các sửa này không đồng nghĩa toàn màn đã qua rubric.

## Verification

- **PASS, phạm vi hẹp:** read-back100 root IDs/mappings;26 photo fills; native Apple variants/reactions; source Button/Input identity; gallery2 ảnh; source tile168×112 và picker row geometry; validator repo100 IDs/100 registered nodes/90 entries/26 hashes/6 skills/DONE0.
- **Present thật, viewport393×852:**002→003;015 filter→023;074→076→077;077→078 chọn Sữa & trứng→077;077 date→079 chọn22/10→077 hiển thị22/10→080 hiển thị22/10;035 thumbnail2 đổi sang ảnh bánh cắt lát, close→034;097 Apple Toggle đầu tiên chuyển On→Off. Đây là các thao tác app trong prototype, không dùng Next frame toolbar để nhận là flow pass. Đã reset viewport sau kiểm.
- Browser evidence: [gallery đổi ảnh](evidence/direct/gallery-second-browser.jpg), [ngày22/10 trên confirmation](evidence/direct/pantry-date-browser.jpg), [Apple Toggle Off](evidence/direct/apple-toggle-browser.jpg). Native render sau sửa: [category picker](evidence/direct/117-3166-sourced.png), [calendar](evidence/direct/117-3213-sourced.png), [form](evidence/direct/117-3124-sourced.png). Search app đã bỏ opacity0.5 từ source để giữ màu chữ secondary đúng token; không coi đây là audit contrast toàn100 màn.
- **NOT CHECKED:** full F-01..F-06, mọi error/cancellation branch, all100 screenshots,375/430pt reflow, real iPhone, assistive technology, usability và owner acceptance. `prototype_verified=false` vẫn giữ cho mọi màn vì chưa hoàn tất hợp đồng toàn màn/flow.
- **PARTIAL VISUAL REVIEW:** [ảnh ghép](evidence/direct/sourced-design-preview.jpg), [Discovery](evidence/direct/17-49-sourced.png), [Bakery](evidence/direct/104-2329-sourced.png), [Pantry intro](evidence/direct/117-3032-sourced.png), [gallery](evidence/direct/106-2630-sourced.png), [kit catalog](evidence/direct/198-189-sourced.png). Một số capture từng hiển thị chrome cắt, capture sau/riêng status đầy đủ; chưa chứng minh hết các safe-area lỗi cũ. 077/080 còn cần kiểm scroll/copy dài. Snapshot ảnh form có thể trước tinh chỉnh visibility cuối; không dùng làm pixel acceptance.

## Công việc còn lại, không che bằng số frame

1. Graph snapshot còn12 root chưa có outgoing navigation:031/032/033/039/041/047/049/064/069/092/093/100. Thêm back/action đúng semantics và kiểm incoming orphans theo Interaction Map.
2. Mọi SKU phải giữ đúng tên/giá/ảnh/merchant/slot/số lượng qua034/050–059/order/pass; hiện nhiều nhánh cũ vẫn về bread mặc định. Các listing031/032/033/041 còn duplicate/default content. Không claim đặt món khác đã end-to-end.
3. Pantry form/confirmation phản ánh ngày đã chọn, nhưng sau Save075 vẫn là snapshot7 fixture; cần mô hình demo inventory thống nhất và test dùng một phần/bỏ/lịch sử. Field text còn là prototype prefill, không nhận là editable text input hoạt động thật. Storage selection mới chưa chạy toàn bộ nhánh.
4. Quantity/checkbox/filter/notification/data-export/delete và các control cũ chưa được kiểm hết. Không claim thực hiện authentication, OS permission, gửi báo cáo hoặc lưu thiết bị.
5. Chạy sáu flow, chụp các màn còn thiếu, sửa bố cục/copy/contrast theo evidence rồi mới nâng QA/owner gate. Không tự DONE hoặc tuyên bố “100 màn đã đẹp”.

Giữ nguyên các dirty files/worktrees có trước; không stage/commit/push, không cài client/MCP trùng và không mua kit.
