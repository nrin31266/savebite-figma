# Search/filter/sort019/020/023/027 · WIP owner rejected · 01/11/2026

**LỊCH SỬ, đã supersede:** owner cho sửa tiếp; hiện trạng mới ở [repair checkpoint](search-sort-repair-checkpoint.md). Nội dung dưới ghi đúng phiên bị từ chối, không phải lệnh dừng hiện hành.

**AWAITING_OWNER_DIRECTION.** Owner yêu cầu dừng vì bố trí tệ hơn và phải dùng workflow chụp/so nhiều màn + browser đã kết nối. Writer `codex/direct-search-sort-ui` **RELEASED**. Không sửa canvas sau yêu cầu dừng, không tự rollback, không commit/push. Bốn màn giữ **NEEDS_REWORK / OWNER_REJECTED_LAYOUT_WIP**. Đây không phải checkpoint UI đạt yêu cầu.

## Canvas hiện còn gì

-019: Apple Search/Keyboard giữ native; query demo “bánh”, keyboard Tìm→020. Quick chips172.5×44 thành2 cột; history rows44pt, viewport426pt nằm trên keyboardy561; history body422pt. Đây là bố trí owner chưa chấp nhận.
-020: ba gợi ý bánh mì25K, croissant30K, túi29K; reuse nguồn ảnh/actions từ Discovery17:133/17:142/17:123, merchant chỉTiệmBánhA. Gỡ visible món/merchant không có fixture. Thêm ảnh48pt/row76pt và Cancel44pt; bố trí vẫn WIP.
-023: chevrons mở budget/time; bỏ merchant khỏi label17–18. Chọn type/Reset có hai Boolean flags, selected backgrounds/Check native; sheet527pt/y325. Budget/time/dietary/result logic cũ chưa hoàn tất.
-027: backdrop native từ021, close44pt, rows56pt/Check native,4 Boolean selected flags; sheet479pt/y373. Chọn sort mới đổi UI/state, chưa reorder danh sách nhiều kết quả.
- Collection `VariableCollectionId:530:5011` có8 Boolean prototype variables cho history/type/sort; scopes explicit ALL_SCOPES cho visibility state, không phải design tokens. Không thêm main.

## Evidence / test thật

[019/020 write IDs](evidence/search-sort-ui/search-write.json), [023/027 write IDs](evidence/search-sort-ui/sort-write.json), [targeted visual fix](evidence/search-sort-ui/visual-fix.json), [state exercise/restore](evidence/search-sort-ui/native-state-test.json). Before4 màn và native captures/state screenshots ở cùng thư mục. Registry trỏ PNG hiện trạng; ảnh không được coi là nghiệm thu.

- Native mode-value render test: history empty làm body422→310, typeSurprise và sortPrice hiển thị selected;8 values đã restore defaults. Không gọi đây là click-through test.
- Lần write đầu lỗi clone TEXT, live reconciliation xác nhận transaction rollback (không node/collection tồn dư); [readback](evidence/search-sort-ui/failed-write-reconciliation.json). Sau đó sửa helper guard và thực hiện hai batch thành công, không duplicate.
- Batch screenshot020 có lượt thiếu chrome/cancel tạm thời; single-node native capture hiển thị đủ. Endpoint URL download trả0bytes; đã thay file bằng PNG capture native hợp lệ. Không suy đoán nguyên nhân môi trường.
- **Browser hiện đã kết nối:** đúng ChatGPT in-app browser, tab editor1 và Present2 đăng nhập file đích. Đã bấm019 keyboard Tìm→020 và xác minh URL/ảnh Present; đã mở/chụp023/027 ở khung điện thoại đầy đủ. Không còn lấy403 của Playwright riêng làm blocker chung.
- Screenshot ngay sau chuyển020 có thiếu một số chrome tạm thời; screenshot sau render ổn định đủ thời gian/island/cancel. Cần lấy trạng thái ổn định khi soi Present.

## Finding sau khi owner dừng, chỉ đọc

019 quick pills thành hai cột lớn làm phần trên nặng;020 vẫn trống nhiều ở nửa dưới và chuyển sang danh sách khác nhịp với trạng thái nhập;023 lẫn chip chọn trực tiếp với disclosure mở màn con;027 các lựa chọn giãn xa và hierarchy yếu. Phải sửa theo quan sát browser/so trước-sau, không lấy bounds hoặc số state làm bằng chứng UI đẹp.

NOT CHECKED: toàn bộ hot spots, free-text input/query engine, thứ tự kết quả sau sort, kết quả sau filter, history persistence, mobile/a11y/usability và owner acceptance. Chưa cập nhật prototype_verified=true. Dữ liệu/copy sửa đúng fixture không chứng minh bố trí mới đạt yêu cầu.
