# Progress · 31/10/2026

Gate: **IN_PROGRESS · end-to-end audit/build (`DEC-012`, owner-authorized; chưa nghiệm thu baseline)** · Target Figma: [SaveBite-V2 (`7suZz9C8oL5zV2NMxlsIVI`)](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1) · Chuẩn khung: **iPhone 15 (`393×852pt`, Dynamic Island)**.

## Checkpoint brand + kit nguồn · DEC-015

- [Kết quả và việc còn lại](brand-polish-checkpoint.md), [tuyển chọn mẫu](../docs/references/curated-layouts.md).100/100 overview đã chụp/xem;15 màn chụp native riêng sau sửa và078 kiểm category. Không gọi đó là100 màn đạt QA.
- Hiện trạng registry: DESIGN_REVIEW50 + NEEDS_REWORK50, DONE0;145 component entries gồm legacy/source dependencies/candidate.31 brand SVG riêng,7 Phosphor Duotone mới; native Apple keyboards009/019 và SDS Card081 đã áp dụng.
- Entry001–012, Search019, Urgency048 và Pantry081 có correction/visual checks. Present đã kiểm consent/Privacy Back/verification và081→082; chưa đủ6 flows/a11y/mobile. PASS: validator100 IDs/145 entries/26 image hashes;71 vector hashes/XML; checkpoint links; PNG/JPEG decode; git diff whitespace. Không suy ra license/visual/whole-flow PASS từ validator.
- PR#2 phần trước đã MERGED. Phần polish ở branch `design/brand-and-screen-polish`, không tự coi đã lên main hoặc owner acceptance. Goal vẫn ACTIVE cho toàn phạm vi, ưu tiên tiếp safety037/045, context món/stock và Pantry edit082.

## Lượt thiết kế tiếp theo · ACTIVE goal

- Owner yêu cầu commit/push/merge phần có nguồn rồi tiếp tục tự audit/sửa; không giao agent. PR [#2](https://github.com/nrin31266/savebite-figma/pull/2) đã MERGED vào `main`, merge commit `bac7a8af33bc4fabdd186661380b30826000ba15`; asset commit `30c9134`, inventory/evidence commit `34bb360`. Committed-tree validator và33 vector hashes PASS. Không coi merge là owner acceptance UI.
- Branch hiện hành: `design/brand-and-screen-polish`. Lease **RELEASED tại checkpoint** owner `codex/direct-polish`: App All Screens, Components/Foundations cho brand/mascot/loading, tokens phụ thuộc, assets và registries/docs liên quan. Không writer khác hoạt động; không spawn agent.
- Nhóm audit: A001–012 Entry; B013–033 Discovery; C034–049+059 Offer; D050–058+060–073 Orders; E074–090 Pantry; F091–100 Account. Chụp contact sheets theo nhóm nhỏ để tìm lỗi rõ bằng hình; sửa chức năng/nội dung/spacing trước khi coi đủ đẹp.
- Phạm vi đầy đủ giữ nguyên: logo/brand assets/linh vật concept, loading/first-run, kit reuse, màu và contrast, layout theo chức năng, spacing/radius/wrap/alignment, content/data consistency, prototype. Các tiêu chí đạt/chưa đạt ghi checkpoint sau batch; goal vẫn ACTIVE tới khi kiểm đủ, không thu nhỏ thành vài màn showcase.
Checkpoint đã merge trước polish (`DEC-014`, lịch sử): **100/100 root native đã đăng ký** = DESIGN_REVIEW49 + NEEDS_REWORK51; BACKLOG0; DONE0. Đây là inventory, không phải100 màn hoàn chỉnh hoặc owner acceptance. Registry90 component entries; manifest26 ảnh/minh họa. Lease `codex/direct` được giải phóng tại checkpoint; lịch sử lease phía dưới giữ nguyên để truy vết.

## Checkpoint hiện hành · sourced kit & correction

- [Kết quả, nguồn, evidence và lỗi còn lại](sourced-design-checkpoint.md). [Live inventory](evidence/direct/live-inventory.json) đọc từ file đích; đã reconcile25 root trước đây chưa đăng ký, gồm13 root mới dựng trực tiếp. Bốn section được sắp theo SB-ID,5 cột, kích thước section chứa đủ màn; không đổi root IDs.
- Apple Search/Toggle copy native thành công từ kit owner; Figma Simple Design System Button/Input import thành công và dùng trên app. Không cần restart hoặc cài thêm MCP cho phần này. Apple26 library-key import vẫn không có quyền; không tuyên bố import toàn kit.
- Photo Library26 fill đã read-back;25 ảnh thật +1 generated concept. App đang dùng13 image hashes khác nhau. Có Brand/Icon Essentials/Curated UI sheets và5 SVG gốc xuất từ canvas. Chưa owner acceptance.
- Đã sửa entry/discovery,3 danh mục, gallery, merchant/surprise, Pantry entry/empty/form/confirmation, shared Pantry rows/account list;13 màn thiếu được dựng. Các màn khác vẫn cần rework và QA; không suy ra chất lượng từ đếm frame.
- Present đã đăng nhập và chạy được; kiểm thực tế một số edges (002→003,015→023,074→076→077,077→078→077, gallery thumbnail/close). Full F-01..F-06, mobile reflow, a11y/usability **NOT CHECKED**. Mọi `prototype_verified` vẫn false; log chi tiết trong checkpoint.
- Lỗi còn mở:12 root chưa có lối ra trong graph snapshot; selected-offer context qua transaction chưa đồng bộ cho mọi SKU; nhiều control/screen cũ chưa QA. Xem checkpoint để tiếp tục đúng vùng.
- `CONCURRENT-WRITER`: RESOLVED cho takeover trực tiếp; Plan-A/B đã release và owner chọn chat này. `codex/direct`: **RELEASED** tại checkpoint, scope App/Components/tokens liên quan + assets + registries/docs. Không agent mới, không commit/push; giữ nguyên dirty files có trước.

## 10 Màn Hình Đại Diện Phase 1 — Một Page Duy Nhất, Click-Through Liền Mạch (`DEC-013`)

| Màn | Archetype | Section (page `App · All Screens`, `11:3`) | Node ID & Link Trực Tiếp |
|---|---|---|---|
| `SB-002` · Onboarding 1 | `A1 · Story Entry` | `01 · Entry & Discovery` | [17:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-2) |
| `SB-015` · Khám phá | `A3 · Market Discovery` | `01 · Entry & Discovery` | [17:49](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-49) |
| `SB-016` · Bản đồ | `A4 · Spatial Map` | `01 · Entry & Discovery` | [17:187](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-187) |
| `SB-019` · Tìm kiếm | `A5 · Search + iOS Keyboard` | `01 · Entry & Discovery` | [17:282](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=17-282) |
| `SB-034` · Chi tiết offer | `A6 · Full-Bleed Showcase` | `02 · Offer & Merchant` | [18:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=18-2) |
| `SB-051` · Chọn giờ nhận | `A7 · Tactile Slot` | `03 · Reserve & Orders` | [19:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=19-2) |
| `SB-053` · Tóm tắt đặt trước | `A7 · Unified Receipt` | `03 · Reserve & Orders` | [19:69](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=19-69) |
| `SB-056` · Đặt trước thành công | `A7 · Perforated QR Pass` | `03 · Reserve & Orders` | [19:140](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=19-140) |
| `SB-075` · Tủ thực phẩm | `A8 · Calm Kitchen Pantry` | `04 · Pantry & Account` | [20:2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=20-2) |
| `SB-091` · Tài khoản | `A9 · Account & Impact Hub` | `04 · Pantry & Account` | [20:109](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=20-109) |

- **Foundations (`0:1`):** [11:59](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=11-59) (`34 variables`, `12 text styles`, `3 effect styles`).
- **Components (`11:2`):** `29 shared components` khớp 1:1 với [components.csv](components.csv).
- **Assets (`assets/manifest.json`):** 6 ảnh thực phẩm/cửa hàng thật từ Pexels, xem mục Asset expansion bên dưới cho các ảnh mới thêm.

## Batch B-PHASE1-011 (31/10/2026) — Plan 1 hoàn tất, Open conflict NAVIGATION đã đóng

- **Sửa 5 màn đầu** (`SB-002/015/016/019/034`): hết emoji làm icon, hết card-in-card ở peek sheet `SB-016`, bỏ chấm GPS giả (D-017), bản đồ lấp khoảng trống, status bar/scrim `SB-034` đúng chuẩn, hết từ mồ côi. Chi tiết lỗi/sửa từng màn ở cột `notes` trong [screens.csv](screens.csv). `CategoryTile` 3 instance và `MerchantRow`/`AllergenNotice` trên `SB-034` detach cục bộ (component gốc chưa có property Icon swap — theo dõi ở Plan 2). `MapPricePin`, `OfferCard` main component sửa trên Components page.
- **Audit 5 màn còn lại** (`SB-051/053/056/075/091`): không phát hiện vi phạm chặn; fix thêm 1 emoji lẻ (🔒 → text) trên `SB-075`, 1 emoji lẻ (📍 → vector icon) trên `SB-056`.
- **⚠️→✅ Open conflict `NAVIGATION` (phát hiện rồi đóng trong cùng batch):** Figma Plugin API chặn `NAVIGATE` reaction liên-page ("prototypes are per-page"). Owner chọn **Phương án A** (31/10/2026): *"Cái nào cùng màn, cùng chức năng thì gộp thành 1 trang để phục vụ việc nối màn"* → ghi **`DEC-013`**. Đã gộp 4 page hi-fi (`01..04`) thành **1 page `App · All Screens` (`11:3`)**, tổ chức bằng 4 Section cùng tên; xóa 3 page rỗng (`11:4/11:5/11:6`). `docs/workflow.md` đã cập nhật kiến trúc page + kế hoạch 2 agent sang Section-isolated.
- **Prototype:** reaction của 10 màn Phase 1 đã được ghi và đọc lại (Plugin API không cho chạy Present mode). **Đính chính 31/10/2026:** bản ghi trước đó viết "đã bấm thử Present mode PASS" là chưa đúng sự thật — chưa ai chạy Present mode; `prototype_verified` đặt lại `false` cho mọi dòng cho tới khi owner/người dùng chạy thật.
- **Asset expansion (xem dưới):** thêm ảnh mới vào `assets/manifest.json` để phục vụ batch 20 màn tiếp theo.

## Batch B-PHASE1-012 (31/10/2026) — Mở rộng asset pool cho 90 màn còn lại

Thêm 3 ảnh Pexels thật (biến thể góc chụp cho 3 offer đã duyệt): `bakery-rolls-2000498`, `rice-bowls-5127769`, `produce-crates-2679261` — tổng 9 ảnh, SHA-256 đã kiểm. Một ứng viên bị loại vì thấy rõ mặt người. Chưa tìm được ảnh Pexels phù hợp cho túi giấy kraft và kệ Pantry (hoãn tới batch Pantry/Túi bất ngờ). 3 ảnh mới **chưa upload lên Figma** nên các màn hiện dùng lại 4 ảnh đã có trong file.

## Batch B-PHASE1-013 (31/10/2026) — Dựng 20 màn đầu của 90 màn còn lại (Plan 2 Batch B1 + đầu B2)

Đã dựng 20 màn (tất cả `DESIGN_REVIEW`, QA kỹ thuật = screenshot + read-back; **chưa** rubric chính thức/owner review, a11y chưa kiểm):

| Section | Màn mới |
|---|---|
| `01` | `SB-001`, `005`, `008`, `013`, `022` |
| `02` | `SB-046`, `047`, `049`, `059` |
| `03` | `SB-050`, `054`, `055`, `057`, `058`, `060`, `062`, `063`, `067`, `072` |
| `04` | `SB-100` |

- Node ID từng màn: xem [screens.csv](screens.csv). Component mới: `TextField` (set `75:56`, CANDIDATE).
- **Chuỗi F-01 đã nối đầu-cuối trên Figma (reaction đọc lại, chưa chạy thật):** `001→002→(Bỏ qua)005→013→034→059→050→051→053→054→055→056→062→063→072→100`; nhánh lỗi `055⇢057/058` qua hotspot demo ẩn; `063` có hotspot ẩn mô phỏng nhân viên quét (D-011). `008→015` thay tạm cho `SB-014` (chưa dựng).
- **Chưa có đường vào (orphan có lý do):** `SB-022` (chờ `SB-021`), `046/047/049` (chờ `SB-021/031/048/033`), `067` (chờ `SB-061/095`). Lối ra tới màn chưa dựng ghi `pending` trong `notes`.
- **Hạn chế đã biết:** stepper `SB-050`, checkbox `SB-049`, segmented `SB-060` chỉ là hình tĩnh; `iOSStatusBar/HomeIndicator/AppBar/BottomNav` không có variant Theme/ActiveTab như registry từng ghi — trạng thái sáng/active làm bằng override (đã ghi drift vào [components.csv](components.csv)).
- Skill đã đọc theo yêu cầu: frontend-design, ui-ux-pro-max, design-critique, figma-use, figma-generate-design/library (không emoji, lỗi ngay cạnh trường, touch ≥44pt, copy nêu rõ hành động).

## Lease & bước tiếp theo

- **Coordinator lease (31/10/2026 15:24 +07):** `ACTIVE` · owner `lead/end-to-end` · scope docs router/decisions, tracking/screens.csv, tracking/components.csv, tracking/progress.md và tích hợp checkpoint. Không worker nào ghi trực tiếp các file chung này.
- **Asset lease:** `RELEASED` · asset-curator/fable đã trả worktree `.claude/worktrees/agent-a8fed568bde5a2ad9` với manifest26 ảnh,88SVG và checkpoint đã chỉnh. Đây là báo cáo worker, chưa lead merge/revalidate sources/hash/crop; không Figma writes. Giữ worktree để phiên tiếp quản kiểm và tích hợp, không tự coi owner acceptance.
- **Foundation lease:** `RELEASED` sau batch control/icon; lead independently reconciled 39 screen roots và 63 component entries. [Foundation checkpoint](foundation-checkpoint.md) ghi giới hạn/claims worker bị loại.
- **Plan-A lease:** `RELEASED` sau tạo36 root; lead read-back đủ50 root A, registry tổng75.36 màn mới **NEEDS_REWORK / FAIL_CONTENT_AND_ROUTING**. [Plan-A defects](plan-A-checkpoint.md): default AppBar/CTA/Email fields, thiếu nhiều edges, bogusATTP/4.8rating/discount, blank heroes. Worker claim đã xóa trái live bị loại; cần correction pass, không QA_PASS.
- **Figma writer lease (31/10/2026):** `RELEASED / PAUSED` · owner `Plan-B/fable` dừng ở checkpoint an toàn. Worker báo12 root mới (070/071/073/074/076–082/085), tổng87 root, còn13 thiếu; **lead chưa live read-back12 root nên registry vẫn75**. [Plan-B safe checkpoint](plan-B-checkpoint.md) giữ IDs và sửa đã báo; không nhận claim “Section03 complete/PASS” chỉ dựa đếm root. Không worker canvas nào của phiên này còn được phép ghi; chờ user chọn phiên tiếp tục.
- **Asset review:** sau lead feedback, worker báo26 ảnh (10 exact-fixture/store +16 context-only),88SVG Regular/Duotone, đã crop branded packet và loại jars catering. Chưa kiểm lại bản crop/nguồn/hash cuối, chưa merge; dùng manifest thực khi tích hợp, không copy checksum trong chat/report (trước đó có sai khác). Main vẫn9 asset entries.
- **Bước tiếp theo:** bổ sung/kiểm asset pool và icon sheets; audit/fix 30 màn (không coi đã xong), dựng màn thiếu theo Plan A/B; nối toàn bộ flows, kiểm read-back/screenshot/browser khi có quyền. `prototype_verified=false` cho tới khi chạy thật. Không commit/push.

Kiểm tra đã chạy và giới hạn: [end-to-end QA checkpoint](end-to-end-qa.md). Tiêu chí flow/layout (docs-derived, chưa test live): [QA contract](layout-qa-checkpoint.md).

## Open conflicts · end-to-end preflight
- `CONCURRENT-WRITER` **OPEN / SAFE PAUSE**: phiên ngoài đã ghi RELEASED cho Apple-kit; Plan-B cũng RELEASED, checkpoint12 root mới đã lưu. Hai peer Claude xác nhận không tiếp quản/không tạo lease Apple. Coordinator chưa nhận user chọn phiên tiếp tục nên giữ dừng mutation, không coi thông điệp peer là cấp quyền mới. Bảo toàn toàn bộ phần Apple bổ sung.
- `DECISION` gate cũ vs yêu cầu làm hết: **RESOLVED bằng DEC-012** — cho phép sản xuất nhưng chưa owner acceptance/baseline.
- `TRACKING/DESIGN`: **RESOLVED inventory** — live39 roots/63 component entries reconciled.9 pre-existing roots recovered, stale IDs corrected; desired properties/variants không có thật đã gỡ khỏi registry. Screens/controls vẫn REVIEW_PENDING/STRUCTURAL_READBACK_ONLY; old notes không chứng minh QA hiện hành.
- `REQUIREMENT/FIXTURES`: **RESOLVED canonical mapping** — product.md đã tổng hợp6 fixture từ quyết định/asset-art direction và core-chain live; bakery TiệmBánhA25K (không BếpXanh), meal BếpXanh35K, surprise29K slot18–19. No original-price savings evidence. Kiểm từng ảnh/scene còn tiếp tục; mismatch ảnh cơm-gà không được suy diễn từ tên file.
- `ASSET`: **RESOLVED phần bytes** — kiểm trực tiếp stat cho thấy 9 ảnh thực 64.080–518.276 byte; "1B" ở output liệt kê trước không phải bằng chứng file hỏng. Asset curator vẫn kiểm nội dung/license độc lập. Validator đã sửa output: đếm hash thực thay hardcode 6 ảnh, không tự claim live Figma/license/visual QA.
- `EVIDENCE`: router trỏ tracking/evidence/figma-readback.json và qa.json không tồn tại; đã gỡ link chết trong router, sẽ link checkpoint thực sau QA, không tạo PASS giả.
- `ENVIRONMENT/PROTOTYPE`: Playwright MCP không khởi động (thiếu `/opt/google/chrome/chrome`). Đã chạy cached Playwright + Chromium trực tiếp, không cài mới/đổi config; prototype URL trả **HTTP 403, "Want to check out this file? Sign up or Log in"**. Browser chưa có quyền phiên đăng nhập; Present mode **BLOCKED/NOT CHECKED**, không bypass hay tự đổi chia sẻ. Read-back/screenshot qua Figma MCP vẫn được worker kiểm độc lập.


## Apple UI Kit preflight · Codex trực tiếp · 31/10/2026

- Owner yêu cầu tự thực hiện, không giao thêm agent; cho phép tham khảo Apple iPhone UI Kit và shadcn preset `b1aIuQ2XC`.
- Lease `ACTIVE` · owner `codex/apple-kit-direct` · scope: một frame tham chiếu mới trên Foundations (`0:1`) và `tracking/apple-kit-checkpoint.md`; không sửa màn, tokens, core mains hoặc CSV trong writer window Plan-B/fable.
- `Open conflicts / TRACKING`: live read-back có78 screen roots; registry hiện39. Chưa reconcile toàn bộ vì coordinator/Plan-B đang giữ lease và progress thay đổi trong phiên. Đã yêu cầu owner dừng phiên vẽ cũ trước khi tiếp quản màn.
- Figma identity/session/read PASS; native write chưa kiểm. Library `iOS and iPadOS 26` đã subscribed; tìm thấy Toggle - Switch, Date and time - Pickers, Status bar - iPhone thật. Browser Figma chưa đăng nhập; MCP vẫn đọc được. Không cần cài MCP/skill trùng.

- **Apple kit checkpoint:** lease `codex/apple-kit-direct` **RELEASED**; [kết quả kiểm kit](apple-kit-checkpoint.md). Library Apple26 có sẵn nhưng native import bị từ chối; kit owner `Y8CWXWyBsyDuvniwEwmBvj` đọc được, source-key import báo not found. Không tạo canvas output; không screenshot/Present claims. BLOCKED_LIBRARY_IMPORT và BLOCKED_WRITER_CONFLICT còn mở; chưa được owner xác nhận dừng phiên cũ. Validator PASS với75 registered nodes, không phải78 live roots đã QA.


## Codex direct continuation · sau restart31/10/2026

- Owner chọn tiếp tục trong chat này: “tôi vừa khởi động lại app coi connect hết tool đò đi rồi làm”; không tạo/giao agent.
- `CONCURRENT-WRITER` RESOLVED cho tiếp quản: Plan-A/Plan-B đã RELEASED, coordinator giữ safe pause theo checkpoint. Lease `ACTIVE` · owner `codex/direct` · scope App All Screens, registry/progress và docs liên quan cho correction/build; không ghi assets đang curator sở hữu. Tokens/core mains chỉ đọc, nếu cần component variant riêng sẽ ghi scope bổ sung.
- Read-back sau restart:87 native SB roots, thiếu083/084/086–090/094–099. Apple26 subscribed nhưng import lại vẫn FAILED `Not permitted to upsert from library` (debug46104804-3512-4c1f-baf3-3d7e8cf311c8); không coi app restart là đã sửa quyền. Browser chưa có active tab; Present chưa kiểm.

- Lease mở rộng `codex/direct`: Components vùng riêng x4300,y100+ cho source-derived Apple Toggle/official Phosphor icons và reference frame; thêm token chỉ cho imported toggle nếu cần. Existing mains giữ nguyên. Chuyển asset từ worktree curator chỉ khi kiểm bytes/license/scene, không merge mù báo cáo.
