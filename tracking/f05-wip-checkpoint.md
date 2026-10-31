# F-05 WIP · owner stop · 31/10/2026

Owner yêu cầu dừng phiên này, commit và merge main để quay lại chat cũ. Goal phiên PAUSED; mọi lease `codex/direct-polish` RELEASED. Không có writer của phiên còn hoạt động. Đây không phải nghiệm thu hoặc DONE.

## Hiện trạng để tiếp quản

- File SaveBite-V2 `7suZz9C8oL5zV2NMxlsIVI`, page `11:3`. Read-back cuối giữ100 root IDs; Pantry collection `VariableCollectionId:356:4807` có246 variables. [Inventory](evidence/f05-completion/live-inventory.json) và [state/IDs](evidence/f05-completion/state.json) ghi hiện trạng, không chứng minh QA PASS.
- Batch trước ở commit `431a503`: [checkpoint continuation](continuation-checkpoint.md), editor và7 fixture, partial/full use/disposal cùng evidence riêng. Không áp kết quả kiểm batch trước cho phần mới.
- Batch WIP thêm một slot mẫu `pantry-demo-added-milk`, form077/review080, reminder085 theo món, empty/filter/history và routing empty/populated. First-use flow bắt đầu074 (`117:3032`), tên `F05 | Pantry · first use | v2`.
- IDs bổ sung: row075 `400:4896`; editor save `400:4913`; use `400:4922`; disposal `400:4931`; reminder scroll `404:4904`, dock `404:5031`, error `404:4986`; filtered-empty `407:5013`; empty-history `407:5030`; history button076 `407:5006`; Hello Mầm instance076 `413:4923` từ master có sẵn `231:238`. Root IDs giữ nguyên, không tạo thêm component masters.
- Product/experience mô tả ý định demo một slot; chưa chứng minh nhập tự do, lưu thiết bị, bản ghi không giới hạn hoặc push OS.

## QA thực tế và lỗi mở

Present đã đi074→076→089: empty-history xuất hiện và các hàng lịch sử mẫu ẩn. Heading/caption vẫn còn copy về7 thao tác/lịch sử mẫu. [Empty](evidence/f05-completion/runtime/first-run-empty.jpg), [history trước sửa copy](evidence/f05-completion/runtime/first-run-history-before-copy-fix.jpg).

Đi076→077, chọn lượng2, mở lịch và chọn22/10/2026: date type bất ngờ thành Best before. Mở lại lịch chọn rõ Use by rồi ngày22; trở về077 thì name/category/unit bất ngờ thành “Thực phẩm của tôi”/“Khác”/“phần”. **FAIL; chưa xác định nguyên nhân và chưa sửa.** Không kết luận hover hay tọa độ là nguyên nhân.

Chưa kiểm thành công save thêm món xuyên080→075→081; chưa chạy runtime reminder/validation; chưa xác minh lối chọn ngày chưa rõ. Full F-01..F-06, mobile, a11y/usability và owner acceptance chưa hoàn tất. `prototype_verified=false`, DONE0. Canvas chứa WIP; Git merge không tương đương nghiệm thu hoặc rollback Figma.

## Tiếp tục ở chat cũ

Đọc router/progress, state/IDs và Figma live trước khi ghi; nhận lease mới. Reconcile lỗi drift form/lịch trước khi tuyên bố add/reminder hoạt động. Giữ thay đổi thủ công và source components; không tạo duplicate khi retry.
