# Search/filter/sort019/020/023/027 · repair · 01/11/2026

**AWAITING_OWNER_REVIEW**, không DONE. Owner cho sửa lại sau rejection; lease `codex/direct-search-sort-repair` RELEASED tại checkpoint. Supersede bố trí trong [WIP bị từ chối](search-sort-wip-checkpoint.md), giữ lịch sử và source gốc. File duy nhất `7suZz9C8oL5zV2NMxlsIVI`, App page `11:3`; không tạo app code, không commit/push.

## Thay đổi có thể kiểm tra

- SB-019 `17:282`: Apple Search/Keyboard native; chip32pt trong hit44pt, một strip cuộn ngang, history48pt. Body trong viewport426pt kết thúc trước keyboardy561. Tìm mở020 với query demo “bánh”.
- SB-020 `101:2117`:3 fixture bakery có ảnh48pt, rows72pt phẳng có separator; merchant64pt chỉ Tiệm Bánh A. Apple keyboard main235:972 có Xong để đóng, chạm Search mở lại; home indicator đổi visibility để không chồng bàn phím. Không có free-text query engine.
- SB-023 `103:2173`: sheet495pt/y357. Budget/time là summary disclosure64pt; dietary56pt với lời nhắc dị ứng. SDS Tag Toggle On423:849/Off423:850 dùng4 instances543:5231/5236/5240/5245, visual44pt trong slot48pt. Local selection/reset chỉ đổi loại ưu đãi; không claim reset budget/time/dietary/kết quả. Sửa hai nhãn có raw paint trắng dù đã bind secondary token.
- SB-027 `103:2334`: sheet415pt/y437,4 sort rows52pt liên tiếp trong một nhóm, selection/check và CTA52pt. Apply mở021; chưa chứng minh reorder nhiều kết quả. Hai sheet có close44pt và bottom padding46pt.
-10 Boolean flags trong collection530:5011 (8 cũ + keyboard/home), tách prototype state khỏi tokens. Không thay source mains hoặc token definitions; giữ100 roots/148 component entries/30 local image hashes.

## Kit và evidence

Đã đọc design-critique/frontend-design/ui-ux-pro-max và figma-use/generate-design/library; tra library và thử import đúng Apple ActionSheet/Row nhưng tool báo không có quyền upsert. Không claim import thành công. Reuse Apple Search/Keyboard đã có và SDS Tag Toggle native, giữ nguồn/candidate license status.

[Search write](evidence/search-sort-repair/repairSearchWrite.json), [filter/sort write](evidence/search-sort-repair/repairFilterWrite.json), [paint fix](evidence/search-sort-repair/repairColorFix.json), [live readback](evidence/search-sort-repair/repairReadback.json), [kit import result](evidence/search-sort-repair/repairKitImport.json). [Bốn màn sau sửa](evidence/search-sort-repair/overview-after.png) là montage native Figma PNG, không gọi là browser capture.

## QA và giới hạn

- PASS scoped live readback:4 roots393×852, không sibling overlap/text overflow/paint binding drift trong phạm vi audit; không chứng minh mọi inner layout của100 màn. Legacy hidden nodes và selected absolute backgrounds được loại khỏi collision test.
- PASS browser **đúng IAB đã đăng nhập**:019 strip cuộn ngang và Tìm→020;020 Xong đóng/chạm Search mở keyboard;023 đổi loại ưu đãi và Reset về Món cụ thể. Quan sát screenshot sau render ổn định, không dựa vào AX của canvas.
- PASS browser027:chọn “Giá thấp đến cao” đổi selected/check đúng hàng, Apply→021 (`101:2161`). Đây là kiểm UI navigation, không phải reorder nhiều kết quả.
- PASS repository: `python3 scripts/validate.py` (100 IDs/148 components/30 hashes/6 skills/DONE0), `git diff --check`, checkpoint links,4 PNG decode393×852 và instance-main registry mappings. Hai nguồn font của4 màn là SF Pro/Be Vietnam Pro.
- NOT CHECKED:full search/filter/sort semantics, toàn6 flows, mobile device, Dynamic Type, usability/full a11y, provider/license và owner acceptance. `prototype_verified=false`, DONE0.
- Lỗi write opacity/clone đã đọc lại xác nhận rollback trước retry; không tạo duplicate. Batch capture có thể thiếu chrome ngay sau navigation; kiểm ảnh ổn định riêng. Không quy403 từ browser Playwright riêng thành blocker của IAB.
