# Apple chrome + paper ·01/11/2026

**Paper placement đã supersede:** [correction theo owner](paper-correction-checkpoint.md):044 Plain,053 Receipt,056 bỏ Stripe,074 Leaf; Fold chỉ còn trong mẫu với góc ngoài trong suốt. Status bars giữ nguyên.

**AWAITING_OWNER_REVIEW.** Owner yêu cầu áp status bar Apple trắng/đen và dùng chất liệu giấy từ sheet. Owner xác nhận chat cũ đã dừng, cho tiếp quản lease Reservation050–054/036. Lease `codex/apple-paper` RELEASED tại checkpoint; không commit/push.

## Kết quả

- Trước batch: Apple Black mới dùng019/020/023–027; các màn khác còn legacy15:2. Bốn pattern231:385/418/429/450 có trong Components nhưng không có instance trên App. Đây là nguyên nhân chưa thấy giấy trong sản phẩm, không phải thiếu asset nguồn.
- Reuse Apple Rin mains có sẵn: Black `554:1033`, White `554:1023`, source keys lần lượt `b904407d6b7f31c4518edf36aeb517e87369d2b5` và `01151055b94f3bb039cdd2ef4f51fdd061ab9287`. Đã đối chiếu kit nguồn `Y8CWXWyBsyDuvniwEwmBvj`, node128:43449/128:43575. Link205:47526 owner gửi là page Typography; status sources nằm ở System Experiences. Không vẽ lại hoặc import trùng.
- Cả100 root dùng Apple source;89 màn Black,11 màn White (001/005/034/035/036/037/046/047/050/059/063), giữ lựa chọn sáng/tối của layout hiện hành. Giữ giờ fixture17:40 ở048 và18:05 ở068; các màn còn lại16:00.393×54 trong safe area59pt, vị trí y0; root IDs, reactions và nội dung nghiệp vụ giữ nguyên.
- Readback102 status instances vì037/045 có hai status hiện hữu chồng cùng tọa độ từ trước; batch giữ IDs và đổi cùng source, không tự xóa lớp có thể phục vụ state. Legacy15:2 vẫn giữ cho hidden/reference nodes; không có status legacy hiện trên100 roots.
- **044 Fold:** instance `571:11115` trong clipped stage `571:11114`,353×260; caption chuyển cream token để đọc được trên forest. **053 Receipt:** instance `571:11122`,crop top12pt `571:11121` trên biên lai; không phủ chữ/tổng tiền. **056 Stripe:** instance `571:11144`,mép vé8pt `571:11143`,không phủ QR. **074 Leaf:** instance `571:11156` trong hero background `571:11155`,opacity0.35 dưới ảnh và nhãn.
- Không tạo master/token/ảnh mới. Registry thêm8 entries cho white source/dependencies đã tồn tại thật, tổng156; usage/mappings100 màn được reconcile. Patterns giữ native linked instances và token bindings.

## Evidence và giới hạn

[Write ledger](evidence/apple-paper/write.json), [live mappings/readback](evidence/apple-paper/inventory.json). Native: [001](evidence/apple-paper/after/SB-001.png), [015](evidence/apple-paper/after/SB-015.png), [044](evidence/apple-paper/after/SB-044.png), [053](evidence/apple-paper/after/SB-053.png), [056](evidence/apple-paper/after/SB-056.png), [074](evidence/apple-paper/after/SB-074.png). Native captures044/053/074 thiếu status dù geometry/visibility/readback đúng; không gọi các ảnh này là full render PASS.

Present trực tiếp [053](evidence/apple-paper/runtime/present-SB-053.jpg) và [044](evidence/apple-paper/runtime/present-SB-044.jpg) hiển thị đủ status Apple đen và vật liệu; [034](evidence/apple-paper/runtime/present-SB-034.jpg) hiển thị Apple trắng trên ảnh tối. Đây là kiểm hiển thị trực tiếp, không phải chạy lại transaction/full flow. Lỗi mất lớp sau transition từ checkpoint trước vẫn OPEN; chưa khẳng định nguyên nhân hoặc sửa xong.

PASS: readback100 roots/source mappings, status geometry, scoped visual material placement; `python3 scripts/validate.py`, `git diff --check`,9 saved image decode,JSON parse và checkpoint links PASS. NOT CHECKED: contrast trên mọi ảnh/state, đầy đủ100 screenshots, full6flows/mobile/Dynamic Type/usability, source redistribution license và owner acceptance. `prototype_verified=false`, DONE0.
