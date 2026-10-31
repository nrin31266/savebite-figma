# Quyết định SaveBite

20 mặc định D-001..D-020 giữ nguyên ở [product.md](product.md). Log này chỉ giữ thay đổi có nguồn duyệt.

## DEC-016 · 31/10/2026 · Correction nội dung offer và prototype context

- Nguồn: yêu cầu owner tiếp tục end-to-end, sửa nội dung sai và layout hời hợt; thực thi DEC-014/015, không thêm nghiệp vụ mới.
- Gỡ claim giờ sản xuất, khối lượng, độ tươi/an toàn và tiết kiệm chưa có dữ liệu. UNKNOWN phải rõ; UI hướng người dùng hỏi cửa hàng/kiểm nhãn, không tự tạo hướng dẫn bảo quản theo món.
- Prototype dùng bộ fixture canonical để giữ tên/merchant/giá/slot/tồn kho và lượng khi chuyển màn; thay đổi chỉ là mô phỏng local trong Figma, không tạo backend/đơn thật. Tồn kho nhánh urgency là state khác có mốc17:40, không trộn snapshot16:00.
- Khi bind text/visibility/reactions, phải kiểm read-back và Present thực theo từng nhánh. Chưa kiểm được thì giữ prototype_verified=false; không suy ra tất cả100 màn đã sửa từ vài ví dụ.
- Scope writer: App All Screens, Components/variables và registries/docs phụ thuộc; một writer trực tiếp, không agent.

## DEC-015 · 31/10/2026 · Merge checkpoint và tiếp tục design polish toàn phạm vi

- Nguồn: owner yêu cầu “commit push merge main phần này” rồi đặt goal tiếp tục tự soi/sửa theo nhóm, chụp nhiều màn, phát triển brand assets/logo/loading và có thể chọn linh vật; ưu tiên chất lượng môn UI/UX, không chỉ đủ màn.
- Cho phép commit/push/merge checkpoint hiện tại. PR#2 đã merge; không suy ra acceptance hình ảnh hoặc DONE. Phần mới làm trên nhánh `design/brand-and-screen-polish`.
- Cho phép khám phá original mascot/brand variants, thêm bớt asset có mục đích, tinh chỉnh họ màu và component kits; một writer, native editable UI, giữ nghiệp vụ và fixture. Candidate “Mầm” (túi giấy/mầm lá) là hướng do designer chọn để thử, chưa phải mascot đã được owner duyệt.
- Audit cả100 màn theo nhóm nhỏ, screenshot/read-back và Present; sửa chỗ trống thiếu ý nghĩa, hierarchy, density, typography, alignment, touch/contrast, hình/icon/source component. Không dùng contact sheet hoặc bộ màu đẹp để thay chứng cứ full-flow/content QA.
- Goal ACTIVE không giới hạn một batch; tiếp tục cho tới khi phạm vi yêu cầu được kiểm chứng. Cập nhật docs tại mốc quan trọng, không lặp sửa tài liệu sau mỗi chỉnh pixel.

## DEC-014 · 31/10/2026 · Một writer trực tiếp, dùng kit có nguồn và sửa lại bố cục

- Nguồn: owner yêu cầu tự vẽ, không giao agent, giữ họ màu hiện tại; yêu cầu tìm mẫu từ lĩnh vực khác nếu phù hợp, dùng Apple kit đã chia sẻ và shadcn preset, tăng ảnh/icon và làm lại màn cũ. Chỉ sửa docs tại các checkpoint quan trọng.
- Quyền triển khai thay đổi layout, spacing, component và brand/icon concept trong file SaveBite-V2; không phải owner acceptance cho hình mới. Không thêm backend/app hoặc tự mua kit.
- Dùng source-native Apple Search/Toggle copy từ kit owner; Figma Simple Design System Button/Input import thực; Phosphor MIT; ảnh có provenance. Điều chỉnh touch bounds/type/màu cho SaveBite, giữ nguồn và components gốc. Không đồng nhất quyền edit một file với giấy phép tái phân phối kit.
- Tham khảo Crouton/Mela cho ảnh và hierarchy, Things cho danh sách, Wallet cho vé, shadcn cho primitive; không đổi nghiệp vụ pay-at-pickup hoặc sao chép thương hiệu/screenshot làm asset sản phẩm.
- Bỏ rating/nhận xét không có dữ liệu khỏi phần UI hiển thị; dùng trạng thái chưa có đánh giá. Dữ liệu thật vẫn REQUIRES-REAL-DATA. Logo mới là concept chờ owner review.
- Native100 root đã tồn tại, vẫn có màn thiếu nội dung/interaction và chưa chạy đủ sáu flow. Giữ DONE0; checkpoint và giới hạn tại [sourced-design-checkpoint](../tracking/sourced-design-checkpoint.md).

## DEC-001 · 19/10/2026 · Phạm vi bootstrap pilot
- Nguồn: yêu cầu trực tiếp của Nguyễn Văn Rin và Bootstrap Prompt đính kèm trong phiên này.
- Duyệt tối đa 5 hi-fi frames: SB-015 → SB-034 → SB-051 → SB-053 → SB-056, foundations phục vụ riêng subset này và một click-through.
- Thay danh sách pilot cũ; SB-051 luôn là chọn khung giờ nhận, không đổi ID.
- Cho phép pilot trước production gate; low-fi toàn flow, nghiên cứu và video vẫn là deliverables chưa hoàn thành.
- Không tạo file Figma khác, không triển khai 100 màn, không push/tạo GitHub repo/PR/công khai/chia sẻ quyền.
- Ảnh chưa có license dùng placeholder có nhãn; success/code là demo, không đại diện stock server.
- Dừng AWAITING_OWNER_REVIEW sau QA; baseline_version để trống đến khi duyệt.
- Ảnh hưởng: 5 screen contracts, Button/OfferCard/PickupInfo/PriceBlock/PickupSlot/Nav và evidence.

## DEC-002 · 19/10/2026 · Kết nối Figma
- Người dùng chọn `RIN` qua câu hỏi trong phiên.
- MCP whoami: Nguyen Van Rin, team Nguyễn Văn Rin's team, student/Full/admin.
- Không dùng kết nối Figma khác để ghi; file đích không đổi.

## DEC-003 · 19/10/2026 · Làm lại visual pilot sau owner feedback
- Nguồn: owner đánh giá bản đầu chưa đẹp, yêu cầu cài frontend-design, dùng find-skills và cho phép chọn lại quyết định visual khi cần.
- Cài frontend-design (Anthropic) và ui-ux-pro-max (NextLevelBuilder), giữ Figma official skills cho native canvas.
- Chọn hướng food-first: ảnh bánh thật có nguồn/giấy phép, hierarchy theo món → giá → giờ nhận, giảm hộp cảnh báo kỹ thuật và khoảng trắng vô dụng; thêm cấu trúc receipt cho summary/success.
- Palette vẫn dùng cream/green/earth orange của sản phẩm; Be Vietnam Pro cho toàn UI mobile. Không dùng serif lớn/gradient hoặc thêm merchant/payment vào MVP.
- Fixture được đổi đồng bộ từ bộ 3 bánh mini thành “Bánh mì men tự nhiên” để khớp ảnh licensed. Vẫn 1 phần 25.000đ, merchant giả lập, slot 17:00–18:00, thành phần/allergens UNKNOWN.
- Ảnh Marcel Fiedler/Pexels 1079020 là ảnh minh họa demo; không đại diện merchant thật. Source/license được lưu assets/manifest.json.
- Sửa đúng 5 root node hiện có, giữ screen IDs và target file. Bản đầu không được owner chấp nhận; evidence cũ hết hiệu lực sau redraw. DONE=0; baseline chưa khóa.

## DEC-004 · 19/10/2026 · GitHub sau khi hoàn tất bootstrap và redesign
- Nguồn: yêu cầu trực tiếp mới nhất của owner: dùng gh tạo repo và upload sau khi xong toàn bộ task.
- Cho phép tạo repo GitHub `savebite-figma`, chọn private vì chưa có yêu cầu công khai, rồi push các checkpoint của task.
- Override riêng lệnh cấm push/tạo repo trong DEC-001. Không tạo PR, không mời thành viên, không public Figma hoặc đổi quyền chia sẻ.
- Chỉ push sau QA và kiểm tra files/secrets. Không ghi đè repo/remote có sẵn không thuộc task.

## DEC-005 · 19/10/2026 · Owner yêu cầu bỏ toàn bộ mock cũ, dựng lại
- Owner tiếp tục từ chối v0.2, yêu cầu xóa các màn mock cũ và không vá bố cục đã làm.
- Cho phép xóa đúng 5 frames và page Components do agent tạo trong phiên; không xóa Page 1 hoặc nội dung người khác. Dựng lại đúng 5 SB-IDs với node IDs mới, registry sẽ theo read-back mới.
- Chọn bố cục mobile marketplace gọn: nền trắng, body charcoal, green CTA, ảnh thật, danh sách hero card + compact offer để so sánh; detail dùng ảnh lớn và pickup information dày vừa đủ. Summary tập trung terms/total, success có QR demo + mã dự phòng được ghi rõ minh họa.
- Foundations/tokens được reuse và điều chỉnh type scale/dark body cho hướng mới; không giữ canvas mock cũ như một baseline. v0.1/v0.2 đều REJECTED, DONE=0.
- Skills local frontend-design và ui-ux-pro-max đã đọc trước rebuild; official Figma skills thực thi native UI.

## DEC-006 · 19/10/2026 · Repo chỉ thực hiện Figma
- Nguồn: owner yêu cầu rà/dọn docs, bỏ nội dung không liên quan vì dự án này chỉ làm Figma.
- Scope thực thi: UX/UI, tokens/components, native editable frames, prototype và docs/QA evidence liên quan. Giữ 100 SB-IDs và gate pilot AWAITING_OWNER_REVIEW.
- Bỏ hướng dẫn triển khai app, stack, API/service code, code acceptance gates. 50/30 màn code vẫn là provenance môn học ngoài repo, không phải task agent.
- Giữ product states, fixture/safety/payment semantics cần cho thiết kế; không thay flow, canvas, IDs hoặc owner acceptance.
- Ảnh hưởng: README, AGENTS, router, product, workflow và progress.

## DEC-007 · 19/10/2026 · Công khai repo sau làm sạch lịch sử
- Nguồn: owner “rồi mở source public ra”; sau khi được báo về tài liệu private, owner chọn “Cho phép sao lưu, làm sạch lịch sử rồi mở public”.
- Cho phép sao lưu private ngoài repo, loại raw reference text/10 ảnh Zia và local source paths khỏi lịch sử, force-push các nhánh đã lọc rồi chuyển chính nrin31266/savebite-figma sang public.
- Ghi đè lựa chọn GitHub private trong DEC-004. Không thay quyền Figma, không public bản sao lưu hoặc tự cấp license cho nội dung của bên khác.
- Giữ nguyên các checkpoint thiết kế/QA ở dạng evidence lịch sử; SHA Git cũ được thay sau lọc. Kết quả thực thi ở progress.

## DEC-008 · 19/10/2026 · Cài skills trước và làm rõ docs pilot
- Nguồn: owner yêu cầu “cài các skills trước” và tinh chỉnh luật/giao diện ban đầu vừa đủ để AI và người đọc hiểu, không mơ hồ.
- Cài local bộ ba Figma và design-critique; giữ hai skill hiện có. Ưu tiên plugin khi có; không nạp trùng. Bộ ba Figma không redistrib lên Git public khi chưa có license rõ.
- Làm rõ preconditions, tương tác tĩnh, đường back và lifecycle trong docs; không coi đây là duyệt baseline hoặc cho phép tự mở rộng pilot.

## DEC-009 · 19/10/2026 · Rà context team và tinh chỉnh pilot v0.4
- Nguồn: owner yêu cầu tiếp tục task, dùng skill mới mock lại 5 màn và làm base đồng bộ, đẹp, đủ chặt cho học phần.
- Duyệt chỉnh đúng SB-015/034/051/053/056 và components phụ thuộc; giữ root IDs, fixture, 4 tabs, payment/pickup/safety semantics và gate owner review. Không rollout thêm 95 màn.
- Hướng chỉnh: nhóm thông tin theo nhiệm vụ, progress hai bước đồng bộ, callout dị ứng dùng component chung, heading success đúng kết quả, tăng hit targets và expose nội dung component cho teammate sửa bằng properties.
- Cho phép mở rộng variants Button phục vụ disabled/loading và documentation component; đây chưa là duyệt baseline hoặc chứng minh giao dịch/backend.
- Dọn context nguồn vắng mặt/logs setup sang backup private; giữ registry + evidence thiết kế và chỉ dẫn teammate khôi phục skills.

## DEC-010 · 19/10/2026 · Owner từ chối visual v0.4, chốt hướng theo ảnh tham khảo
- Nguồn: owner cung cấp 5 ảnh SaveBite và yêu cầu mock theo gu đó; đánh giá bản trước thiếu cá tính. v0.4 không được chấp nhận làm baseline.
- Hướng được phép triển khai: warm cream, forest green, typography mạnh, food photography sáng, hero/card giàu hình ảnh, icon vector có cá tính, bo tròn mềm. Giữ native editable UI và chính 5 pilot roots.
- Ảnh tham khảo không tự thay nghiệp vụ: vẫn 4 tabs, reserve/pay at pickup, dị ứng UNKNOWN và dữ liệu minh họa rõ. Không bịa ratings, giảm giá, merchant hoặc claims food-safety từ ảnh.
- Token/component changes được đồng bộ trong batch này cùng docs/registry/QA. Không rollout thêm màn ngoài pilot.

- Thực thi B-PILOT-005: giữ 5 root IDs; làm lại 5 bố cục native, 21 mains/31 instances; 40 variables, 11 text styles, 2 effect styles. BreadPhoto dùng ảnh AI minh họa sáng/ấm, lưu generation brief/hash trong manifest; ảnh không làm evidence về merchant/food safety. Reference screenshots không đưa vào public repo.
- QA: 360/390/430 bounds, detail font125, 13 cặp contrast ≥4.5 và cả 9 hotspot tiến/lùi PASS. Dừng ở AWAITING_OWNER_REVIEW, không tự nhận owner acceptance hoặc mở 95 màn còn lại.

## DEC-011 · 26/10/2026 · Nghỉ hưu Pilot v0.5, chuyển sang SaveBite-V2 (7suZz9C8oL5zV2NMxlsIVI), chốt chuẩn iPhone 15 và Phase 1 gồm 10 màn đại diện
- Nguồn: yêu cầu trực tiếp của Nguyễn Văn Rin ngày 26/10/2026 kèm liên kết file Figma mới `https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1`.
- Owner xác nhận đã xóa toàn bộ 5 màn pilot v0.5 cũ và thay thế file đích:
  1. **File Figma đích duy nhất mới:** `7suZz9C8oL5zV2NMxlsIVI` (`SaveBite-V2`). Ngừng sử dụng `NLTv70kDZ2i3HpOnOKQCDY`; toàn bộ node IDs, readback và screenshots của pilot v0.5 được đánh dấu `STALE/RETIRED` và dọn khỏi bộ bằng chứng hiện hành.
  2. **Chuẩn thiết bị iPhone (`CONFIRMED`):** Nâng cấp chính thức lên **iPhone 15 Standard (`393×852pt`, Dynamic Island `59pt` top safe area, Home Indicator `34pt` bottom safe area)** tuân thủ Apple Official iOS UI Kit và Apple HIG.
  3. **Phạm vi Phase 1 (10 màn North-Star đại diện đa Archetype):** Thiết kế mới hoàn toàn 10 màn chuẩn mực: `SB-002` (Onboarding), `SB-015` (Discovery), `SB-016` (Map), `SB-019` (Search + iOS Keyboard), `SB-034` (Offer Detail), `SB-051` (Reservation Slot), `SB-053` (Order Summary Receipt), `SB-056` (Success & Perforated QR Pass), `SB-075` (Smart Pantry), `SB-091` (Profile).
  4. **Chính sách Asset-First (`CONFIRMED`):** Loại bỏ ảnh AI tạo sinh cũ; tuyển chọn và xác minh mã băm SHA-256 cho bộ 6 ảnh thực phẩm/cửa hàng thật từ Pexels (`Pexels License`) trong `assets/manifest.json`, kết hợp hệ icon **Phosphor Icons** và font **Be Vietnam Pro / JetBrains Mono / SF Pro**.
  5. **Kế hoạch 2 Agent độc lập (50/50 Split sau khi duyệt 10 màn):** Khóa kiến trúc phân tách vùng ghi Figma theo Page (`Agent 1`: 50 màn `SB-001..049, 059` trên `01 · Entry & Discovery` và `02 · Offer & Merchant`; `Agent 2`: 50 màn `SB-050..058, 060..100` trên `03 · Reserve & Orders` và `04 · Pantry & Account`). Chưa triển khai 90 màn còn lại khi chưa có Owner Review cho 10 màn Phase 1.

## DEC-012 · 31/10/2026 · Cho phép triển khai end-to-end, không đồng nghĩa nghiệm thu baseline
- Nguồn: owner yêu cầu "coi làm hết luôn các cái còn lại", nhấn mạnh 30 màn cũ chưa đủ/chưa kiểm kỹ, chấp thuận phương án asset sheets → audit/fix → phần còn thiếu và xác nhận "làm end to end".
- Cho phép thực thi toàn bộ 100 SB-ID theo docs/plans, sửa 30 màn đã có, bổ sung ảnh thật có giấy phép, icon SVG/spot badges và sheet dùng lại; dùng workers theo lease cô lập, fable chủ đạo, worker Sonnet 4.6 khi cần.
- Override điều kiện phải chờ duyệt Phase 1 mới được sản xuất tiếp trong DEC-011/Plan 2. Đây là **authorization triển khai**, không phải owner acceptance; design_baseline_version vẫn trống, DONE=0 cho tới khi QA và owner duyệt thực sự.
- Giữ file đích, native editable UI, 4 tabs, reserve/pay-at-pickup, safety/fixture và toàn bộ 100 ID. Mượn nguyên tắc bố cục có nguồn, không sao chép branding, bịa nghiên cứu/metrics hay tự thêm món/merchant mới.
- Ảnh/minh họa có thể được gom contact sheet rồi crop để xử lý, nhưng UI/control/icon phải native vector/components; không dùng ảnh phẳng thay màn. Icon canonical vẫn Phosphor, custom chỉ mở rộng có chủ đích và ghi nguồn/license.
- Cho phép pool ảnh đa dạng theo nhu cầu sử dụng thay cho giới hạn 6–8 ảnh; mỗi ảnh phải kiểm nội dung, source/license/hash và ánh xạ fixture đúng. Không cài tool mới nếu bộ hiện tại đủ.
- Không tự commit/push hoặc đổi quyền chia sẻ. Kết thúc ở AWAITING_OWNER_REVIEW; test không thực hiện được ghi NOT CHECKED/BLOCKED.
- Ảnh hưởng: docs router, Plan 2 gates, workflow, asset strategy, screens/components registries và checkpoint QA.

## DEC-013 · 31/10/2026 · Gộp 4 page hi-fi thành 1 page "App · All Screens" để prototype liên-flow hoạt động
- Nguồn: yêu cầu trực tiếp của owner ("Cái nào cùng màn, cùng chức năng thì gộp thành 1 trang để phục vụ việc nối màn"), trả lời cho Open conflict `NAVIGATION` ghi ở `tracking/progress.md` (31/10/2026) — Figma Plugin API chặn mọi `NAVIGATE` reaction có đích khác page nguồn ("prototypes are per-page"), phát hiện khi thực thi Plan 1.
- Chọn **Phương án A** trong 3 phương án đã đề xuất ở `docs/plans/build-100-screens-prototype.md` mục 0: gộp toàn bộ page hi-fi đếm vào 100 màn (`01 Entry & Discovery`, `02 Offer & Merchant`, `03 Reserve & Orders`, `04 Pantry & Account`) thành **một page duy nhất `App · All Screens`** (giữ node id `11:3`, đổi tên), tổ chức lại bằng 4 **Section** Figma (không phải page) mang đúng tên 4 nhóm cũ để giữ tính tổ chức trực quan. `Foundations` (`0:1`), `Components` (`11:2`) giữ nguyên, không gộp.
- Thực thi ngay trong phiên: chuyển 10 node frame Phase 1 hiện có sang page `11:3`/4 section tương ứng (giữ nguyên node ID, chỉ đổi `x`/`y` để tránh chồng lấn và đổi `parent`), xóa 3 page rỗng còn lại (`11:4`, `11:5`, `11:6`). Nối lại 6 hotspot từng bị chặn liên-page (`SB-015→034`, `SB-015 tab→075/091`, `SB-016 peek→034`, `SB-019 gợi ý→034`, `SB-034→051`) cộng thêm vòng lặp pilot `051→053→056→015` và tab `Pantry/Account→Khám phá` — toàn bộ 10 màn Phase 1 giờ là một prototype click-through liền mạch.
- Hệ quả tới `docs/workflow.md`: bảng "Kiến trúc Cô lập 6 Pages" và kế hoạch 50/50 theo Page (`DEC-011` mục 5) **không còn áp dụng theo Page**; thay bằng lease/phân công theo **Section** trên cùng 1 page (owner cập nhật bảng trong cùng batch docs này). Không đổi phạm vi 100 `SB-ID`, không đổi fixture/nghiệp vụ.
- Ảnh hưởng registry: `tracking/screens.csv` cột `figma_page_id` của 10 màn Phase 1 đổi từ `11:3/11:4/11:5/11:6` thành `11:3` (duy nhất); `figma_node_id` giữ nguyên.
