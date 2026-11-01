# Selected states ·01/11/2026

**Historical selected-state batch; AWAITING_OWNER_REVIEW for selectors,075 in this batch REJECTED by owner.** Current075 superseded by [approved-direction implementation](visual-refinement-checkpoint.md), awaiting review. Lease `codex/home-pantry` RELEASED. Không commit/push hoặc DONE. Owner yêu cầu làm lượt Mầm/carrot,Home greeting/order card,075 và semantic labels/spacing **sau** batch này; lượt mới ở bước brainstorming,không tự coi thiết kế075 đã được chấp nhận.

## Hiện trạng

-100 root IDs giữ nguyên,registry157 entries; không master/icon/photo mới trong batch này. Main PantryItemRow16:171 đã có native `CategoryIcon#583:0`,8 fixture rows và081 dùng glyph theo nhóm thay ảnh. Source pantry assets vẫn giữ trong manifest; ảnh context074 không phải yêu cầu người dùng chụp món.
-087: bốn nhãn căn trái,x52 trong row353pt; native row là vùng bấm,source buttons cũ ẩn. Inactive cream+border/default,selected forest+cream+check.4 flags `598:8149..8152`;3 callers đi tới disposal reset flags để không giữ màu món trước.095:Tất cả/Đơn hàng/Tủ thực phẩm có3 flags `598:8229..8231`,chỉ một active; nhóm thông báo và caption giữ logic cũ.
- Audit bổ sung40 choices ở018(area),024(budget),025(pickup),026(dietary),027(sort),069(incident),070(cancel reason),077(quantity),078(category),079(date type),082(quantity). IDs/flags/original-action counts ở [choice ledger](evidence/home-pantry/choice-ledger.json). Dietary toggle độc lập; các nhóm còn lại exclusive. Ngày hạn giữ48pt hit cells;date type được sync khi mở từ add/edit. Category selected flags được set trước NAV về form.
- Những group đã có selected bindings ở077/082(storage),085(reminder),086(fractions),094(radius) giữ logic và được đưa inactive về cream/border thay nhiều nền sage.051 chỉ một slot còn nhận được tô active;slot đã đóng vẫn không có action,không mở lại giờ đã qua.023 SDS Tag Toggle On/Off và các nav đã có trạng thái rõ được giữ.
- Row added400:4896 đã sửa override:353×96,content277,label211,date277; native readback có thật. Runtime check cuối chưa kết luận vì prototype đi về onboarding ngoài dự kiến; không nhận save-list rendering PASS.
- Choice cards có8pt gap;024/025/026/027 sheets vẫn neo đáy852. Fonts/icons/tokens reuse; không bịa UI-kit import hoặc thêm backend/query engine.

##075 và research

Đã tham khảo màn Kitchen/inventory trong hero của [KitchenPal chính thức](https://kitchenpalapp.com/en/) và [Apple HIG segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls). Reference lấy nguyên tắc tách title/action,storage scope,list; không copy branding/ảnh sản phẩm hoặc áp estimated expiry/barcode vào SaveBite. Hai gallery image alt trên website không khớp ảnh thực,không dùng chúng làm bằng chứng inventory. Không lưu asset tham khảo có quyền tái phân phối chưa rõ vào repo.

075 live hiện có header606:8185,Add44pt606:8188;16:161 overview ưu tiên một số rồi hai số inline;20:33 storage selector4 phần,counters vàfilter bindings cũ giữ nguyên. [Snapshot bị owner từ chối](evidence/home-pantry/selection/after/SB-075-owner-rejected.png). Owner yêu cầu làm lại theo hướng trang chính giàu chất lượng hơn;không đánh dấu visual PASS/acceptance cho075.

## QA có bằng chứng

- PASS readback: [100-root mappings +40 choice audit](evidence/home-pantry/selection/live-final.json),không text overflow trong content hiện hoặc variable-controlled;40 hit areas≥44pt;defaults exclusive hợp lệ,Dietary none default. Registry/screens được reconcile từ live,không dùng IDs trong chat tự suy diễn.
- Native reviewed: [018](evidence/home-pantry/selection/after/SB-018.png),[077](evidence/home-pantry/selection/after/SB-077.png),[078](evidence/home-pantry/selection/after/SB-078.png),[079](evidence/home-pantry/selection/after/SB-079.png),[024](evidence/home-pantry/selection/after/SB-024.png),[025](evidence/home-pantry/selection/after/SB-025.png),[026](evidence/home-pantry/selection/after/SB-026.png),[027](evidence/home-pantry/selection/after/SB-027.png),[051](evidence/home-pantry/selection/after/SB-051.png),[069](evidence/home-pantry/selection/after/SB-069.png),[070](evidence/home-pantry/selection/after/SB-070.png). Source capture có lượt thiếu status/button paints;không coi đó là full render PASS.
- Present:005→013 và005→008→015 cùng market;018 chọn Ký túc xá→015 đổi header;077→079 chọn22→077→080 giữ milk/category/Use by/date22;095 Orders/Pantry đổi active và lọc đúng nhóm.026 [hai active độc lập](evidence/home-pantry/selection/runtime/dietary-multi.jpg),[toggle off riêng](evidence/home-pantry/selection/runtime/dietary-toggle-off-render-open.jpg) thay đúng trạng thái.
- **OPEN render:** một số lượt đổi state làm capture thiếu các static layers (87 reason,95 Pantry,026 toggle-off),có lượt ổn sau chờ,có lượt vẫn thiếu. Không khẳng định nguyên nhân hoặc đã sửa lỗi engine. Renderer failure khác với readback/selection values,không gộp thành prototype PASS.
- **NOT CHECKED/limits:** full6flows/mobile/Dynamic Type/usability/all-state contrast;custom budget chưa nhập số tự do,filter groups chưa có query engine,multi-result sorting/report submit/backend chưa triển khai. Category glyph mapping fixtures đúng vàswap configurable;đổi nhóm bất kỳ tự sync icon chưa chứng minh. F05 reminder/disposal/empty branches chưa đủ QA. `prototype_verified=false`,DONE0.

## Lượt tiếp theo owner đã yêu cầu

Dùng brainstorming chốt hướng trước khi sửa: Mầm Kitchen/carrot không che mắt/miệng và đuôi đúng;Home signed-in có lời chào nhẹ,order pending card làm lại;075 làm lại;rà semantic labels/màu/padding/radius toàn app. Cho phép reuse/import kit Apple Rin và kit phù hợp,kể cả edit/add/delete component sau live usage/reference audit. Không xóa main còn dùng hoặc biến quyền sửa thành owner acceptance.
