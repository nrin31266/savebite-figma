# Apple kit & shadcn preflight · 31/10/2026

Owner: `codex/apple-kit-direct`. Scope: kiểm kết nối/kit, không agent phụ. File ghi duy nhất cho thiết kế: SaveBite-V2 `7suZz9C8oL5zV2NMxlsIVI`. Kit owner cung cấp chỉ đọc.

## Kết quả kiểm thật

- PASS: Figma MCP connected; identity Nguyen Van Rin, team `team::1673617987283726216`, student / Full / admin. Session `4b57a4c9-05d9-49e6-945d-35d00126140e`.
- PASS: live file target có3 pages;78 SB roots tại thời điểm đọc. Registry đang được coordinator phiên khác cập nhật từ39 lên75; không sửa CSV trong lease của họ.
- PASS: `get_libraries` xác nhận **iOS and iPadOS 26** đã subscribed, không cần cài trùng. Search trả Toggle - Switch, Date and time - Pickers, Status bar - iPhone.
- FAILED / BLOCKED_LIBRARY_IMPORT: import3 Apple assets chính thức bị từ chối `Not permitted to upsert from library`. Debug UUID `7395d99d-802e-48d4-bfe2-a24700059d1b`. Không suy diễn nguyên nhân là EULA; identity đã kiểm lại.
- PASS recovery read-back: Foundations vẫn chỉ có frame `11:59`, không Apple imports hay frame mẫu mới. Native write chưa được chứng minh; không claim đã cài/import component.
- BLOCKED_BROWSER: browser vào SaveBite hiện yêu cầu đăng nhập. Không có browser khác đã kết nối để dùng phiên đăng nhập; không đổi share settings hoặc bypass.

## Kit owner cung cấp

[Apple iOS UI Kit (Community)](https://www.figma.com/design/Y8CWXWyBsyDuvniwEwmBvj/Apple-iOS-UI-Kit--Community-).

- PASS read:18 pages, có Welcome, System Experiences, Navigation, Selection and Inputs. Welcome có iOS17/18 app examples. Tên file không tự chứng minh publisher/license chính thức.
- Status Bar set `128:42712`, key `53bd68848021d1fe0edbaf5a8d2f5debd1d55f0b`; variants Device15Pro/15ProMax, Color, Home/LockScreen. Native dimensions393×54 hoặc430×54; khác59pt top safe area SaveBite. Cần adapter layout tại screen, không tự đổi DEC-011 hay main components.
- FAILED / BLOCKED_SOURCE_IMPORT: import set theo key sang SaveBite trả `Component set ... not found`, debug UUID `8c555b4d-887e-495e-9b1b-b5575ba35e8a`. Có thể đọc source không đồng nghĩa có published-library import. Không retry lặp hoặc dựng bản nhái để claim kit đã dùng.
- License/attribution đầy đủ chưa xác minh; chưa copy assets. Hướng khả thi tiếp: owner mở file nguồn trong Figma đã đăng nhập, xác minh quyền sử dụng và copy component cần dùng sang SaveBite hoặc publish library nếu có quyền. Không tạo file đích thay thế.

## Preset và kit đối chiếu

[Preset owner](https://ui.shadcn.com/create?preset=b1aIuQ2XC&item=preview) đã đọc qua browser UI: Luma, Stone, Blue, heading/body Raleway, Remix Icon, radius Large, menu Default/Translucent, accent Subtle.

- [shadcncraft Figma](https://shadcncraft.com/figma): vendor mô tả8 styles gồmLuma và import shadcn Create URL; bảng feature có preset import trong free tier, nhưng free chỉ curated sample. Chưa tải, chưa mua, chưa kiểm import thực.
- [shadcn Figma directory](https://ui.shadcn.com/docs/figma): có free Obra Community và shadcncraft starter; các kit là community contributions. Không coi toàn bộ community kit là official hoặc license mặc định MIT.
- [Apple Design Resources](https://developer.apple.com/design/resources/) và [Figma UI kits guide](https://help.figma.com/hc/en-us/articles/24037724065943-Start-designing-with-UI-kits): nguồn kit chính thức, cách Assets → Libraries → UI kits → Add to file. Guide ghi Apple yêu cầu EULA; chưa quan sát prompt EULA trong browser nên không quy lỗi import cho nó.
- Hướng sử dụng theo owner: ưu tiên system controls/iPhone patterns, chỉ tham khảo shadcn ở primitive phù hợp. Không migration màu xanh dương/Raleway/Remix hoặc Liquid Glass toàn app khi chưa có quyết định breaking design.

## Lease & QA

**Cập nhật sau đăng nhập/restart,31/10/2026:** giới hạn import library-key phía dưới là lịch sử, không còn chặn sử dụng subset Apple. Đã copy native Toggle source `128:47034` và Search Input `128:47204` từ file owner `Y8CWXWyBsyDuvniwEwmBvj` qua clipboard Figma đang đăng nhập vào SaveBite-V2. Destination sets `158:197`/`158:210`; variants, text property và Smart Animate gốc đã read-back. Toggle được nới touch bounds64×48, giữ track51×31. Dùng5 toggle và7 search instances trên các màn app, điều chỉnh palette/type cho SaveBite. Không import toàn bộ kit, không viết vào kit nguồn, không khẳng định source-key import đã hoạt động. Xem [checkpoint hiện hành](sourced-design-checkpoint.md).

Lease `codex/apple-kit-direct`: RELEASED tại checkpoint, không có canvas mutation thành công. Plan-B/fable và coordinator vẫn ACTIVE trong progress; owner chưa xác nhận đã dừng phiên cũ. Screen continuation BLOCKED_WRITER_CONFLICT theo workflow; tiếp tục sau release/read-back mới.

- Repo validator: PASS (100 unique IDs,75 registered nodes,63 components,9 asset hashes,6 skills,DONE0).
- Screenshot/layout/contrast/prototype/mobile/owner acceptance: NOT CHECKED cho batch này vì không có output canvas mới. Native Apple import FAILED, không DONE.
- Không stage/commit/push, không cài thêm MCP/dependency hoặc sửa user config. Các thay đổi có sẵn được giữ nguyên.
