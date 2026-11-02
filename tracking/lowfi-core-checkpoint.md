# Low-fi core flows & đối chiếu ·02/11/2026 ·DEC-040

**AWAITING_OWNER_REVIEW.** [Page mới trong SaveBite-V2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=930-2).37 wireframe sản phẩm +1 frame mô phỏng cửa hàng,393×852,native editable,7 nhóm. Existing empty Low Fidelity913:9333 and100 hi-fi roots are preserved. This is retrospective schematization of the current hi-fi,not evidence of prior research.

## Đầu ra

- [PDF7 trang](review/lowfi/SaveBite-LowFi-Core-Flows.pdf):mỗi nhóm một trang,37 source hyperlinks về hi-fi gốc;SIM-01 explicitly outside customer app.
- [Wireframe registry](wireframes.csv),[native read-back/actions](review/lowfi/live-readback.json),[spec/source mappings and local components](review/lowfi/build-state.json).
- Native text/Auto Layout/components and crossed vector placeholders;zero IMAGE fills. Be Vietnam Pro only;existing spacing tokens + isolated6 grayscale roles. Five local masters931:3/5/7/11/14;no change to201 hi-fi component records.
- 36 planned canonicalSB references plus075-used to show actual used-up result,andSIM-01 to close external merchant handoff. Never counted toward100 hi-fi.

| Nhóm | Frame | Ảnh tổng quan |
|---|---:|---|
| Mở đầu/đăng nhập/vị trí |5|[01](review/lowfi/group-01.png)|
| Khám phá/tìm kiếm/lọc |6|[02](review/lowfi/group-02.png)|
| Món/an toàn/cửa hàng |4|[03](review/lowfi/group-03.png)|
| Giữ chỗ/phục hồi |6|[04](review/lowfi/group-04.png)|
| Đơn/nhận/hủy +SIM |7|[05](review/lowfi/group-05.png)|
| Tủ/ngày hạn/đã dùng |9|[06](review/lowfi/group-06.png)|
| Tài khoản/điều hướng |1|[07](review/lowfi/group-07.png)|

## Prototype và lộ trình demo1–3 phút

[Luồng01 · Đặt và nhận món](https://www.figma.com/proto/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=933-5&starting-point-node-id=933%3A5&scaling=scale-down):002→005→015→034→050→051→053→056→060→062→063. Tại063,người trình diễn nhấn phím mũi tên phải→SIM-01;chuyển vai cửa hàng,mô phỏng giao món→072. Không có nút khách tự xác nhận đã nhận.

[Luồng02 · Tủ thực phẩm](https://www.figma.com/proto/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=935-397&starting-point-node-id=935%3A397&scaling=scale-down):076→077→079→077→080→075→081→086→075-used. Added-slot Sữa tươi mới mua1hộp/Ngăn mát/Hạn sử dụng21/10;reference19/10. Trạng thái cuối0hộp tách riêng;không quay lại màn vẫn còn1hộp.

[Luồng03 · Tồn kho thay đổi](https://www.figma.com/proto/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=934-548&starting-point-node-id=934%3A548&scaling=scale-down):058→053→056. Nhánh đăng nhập059→034 giữ đúngmón;011 từ chốiGPS→018→015;062→070→071 có thể giữ lại đơn ở070.

Gợi ý video:0:00–0:15 giới thiệu phạm vi low-fi/sơ đồ hóa;0:15–1:15 luồng đặt/nhận,nhấn→ tạiQR và nói rõ tác nhân cửa hàng;1:15–2:10 Tủ/ngày hạn/đã dùng;2:10–2:40 minh họa một recovery và kết luận phạm vi. Video chưa quay.

## QA và giới hạn

- Structural PASS:38 roots,140 actual same-page navigation actions,3 starts,38/38 reachable from union of starts;zero bitmapfills,Be Vietnam Pro only,no text overflow in local Auto Layout,footers end852.37 hi-fi source mappings validated.
- Per-root exports:38 PNGs,seven overview groups;PDF7 pages/source links/fonts and final images reviewed. Fixed field-value height,static header export transform via clipping,044 first-viewport allergy warning,072 completed cancellation copy.
- Real Present:66 logged entries,38/38 roots visited;both main flows,required branches andfour tabs PASS. Every140 action destination structurally validated;not everyaction manually clicked. Registry prototype_verified is scoped to frame visitation.
- Prototype routes and verification results are finalized in [verification](review/lowfi/verification.json) and [Present route log](review/lowfi/present-routes.json). [Pickup capture](review/lowfi/present-pickup-complete.png),[Pantry used-up capture](review/lowfi/present-pantry-complete.png),[source preservation](review/lowfi/source-preservation.json). Existing Browser/Present capture can miss static layers after transitions;native per-root export is the visual source of truth. No global renderer fix claimed.
- Preset prototype:forms/date/quantity/filter/sort values are illustrative rather than a full input engine;croissant cards/history rows are visual context with no incorrect navigation to bread. Cancellation/result and empty/populated Pantry are separate scenario snapshots;no persistence/backend/QR scanning or real payment claimed.
- Full data logic,usability/screen-reader/actual-device tests and video recording NOT CHECKED. Owner acceptance pending,DONE unchanged. No app/backend code,new images,agents,commit or push in this task.
