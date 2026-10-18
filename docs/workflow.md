# Quy trình Figma, cộng tác và QA

Nguồn chuẩn theo domain; đọc [router](README.md) và [tiến độ](../tracking/progress.md) trước khi thay đổi.

### Thứ tự ưu tiên và quản lý tài liệu lệch nhau

- **Yêu cầu môn học:** `GROUP ASSIGNMENT-UXUI.pdf` và sửa đổi có chứng cứ từ giảng viên. Khi tài liệu gốc mâu thuẫn nội bộ (ví dụ 30/50 màn code), giữ phương án bảo thủ 50 trong `docs/product.md`, ghi rõ chưa được giảng viên xác nhận.
- **Quyết định sản phẩm:** xác nhận mới nhất của người dùng/nhóm có thể kiểm chứng và ghi trong `docs/decisions.md` → trạng thái hiện hành phải được phản ánh trong `docs/product.md`/`docs/experience.md`. Nếu Decision Log và tài liệu hiện hành chưa khớp, **không tự chọn tài liệu thuận tiện**.
- **Nguồn chuẩn theo lĩnh vực:** `docs/product.md` sở hữu business scope/policy; `docs/experience.md` sở hữu flow, màn và UX state; `docs/design-system.md` sở hữu token/components; `docs/workflow.md` sở hữu Figma/agent/QA. `tracking/screens.csv` và `tracking/components.csv` giữ tình trạng thực tế và ID, không tự biến thành nguồn thay đổi requirement.
- **Figma live:** nguồn chuẩn về **những gì thực sự đang tồn tại trên canvas**; không mặc nhiên là nguồn chuẩn của yêu cầu. Nếu canvas khác docs, kiểm tra lịch sử/manual edits và đề xuất đồng bộ, **không ghi đè**. Đọc lại node thực trước khi sửa.
- **Tài liệu slide, Zia's Pizza, mockup AI và nguồn ngoài:** tài liệu tham khảo, không phải nguồn quyền lực cho nghiệp vụ.

**Giao thức khi phát hiện drift/conflict (bắt buộc):**

1. Xác định đối tượng: `REQUIREMENT`, `DECISION`, `DESIGN`, `IMPLEMENTATION`, `TRACKING`, `EXTERNAL_DOC` và ghi ngắn vào `tracking/progress.md` mục `Open conflicts` (chỉ tạo file issues riêng nếu thực sự nhiều).
2. So sánh bằng chứng nguồn, ngày duyệt, docs theo đúng chủ đề, Figma node và registry; ghi các phương án tác động tới screen IDs/components/flows.
3. **Không âm thầm sửa nhiều tài liệu cho "khớp" mà thiếu cơ sở.** Nếu khác biệt là lỗi hiển nhiên không thay đổi chính sách, có thể sửa tài liệu cùng code/registry và ghi checkpoint. Nếu ảnh hưởng phạm vi, UX flow, pricing/payment, safety, thành phần chung hoặc yêu cầu bài học: xin quyết định, ghi `docs/decisions.md`, cập nhật *tất cả tài liệu phụ thuộc trong cùng một thay đổi*, rồi QA lại màn liên quan.
4. Các việc không phụ thuộc xung đột được phép tiếp tục. Block chỉ hạng mục bị ảnh hưởng; không làm cả dự án đình trệ không cần thiết.
5. Sau quyết định, `docs/README.md` vẫn là router duy nhất; không lưu cùng một bản mô tả ở 3 nơi hoặc dùng chat history làm registry.

**Định nghĩa nhãn:** `CONFIRMED` (đề bài/đã duyệt), `DEFAULT` (giải pháp thực thi đề xuất, có thể được đổi qua decision), `FUTURE` (không tính trong MVP), `REQUIRES-REAL-DATA` (chưa có bằng chứng thực), `BLOCKED` (không thể thực hiện an toàn). Sau bootstrap, giữ nhãn ở tài liệu lĩnh vực, không yêu cầu lưu file gốc.

### Quy tắc chất lượng không được phá

- Không biến 100 màn thành 100 bản copy/trạng thái trang trí; không lấy ảnh PNG phẳng làm UI Figma.
- Figma high-fi phải native editable text, components/instances, Auto Layout và tokens khi phù hợp; ảnh raster chỉ cho assets thật/hợp lệ.
- Không claim đã khảo sát, usability test, triển khai code, xác thực merchant, tạo node Figma hay sửa quyền nếu chưa kiểm chứng.
- Không tạo hoặc lặp core components khi chưa tìm registry/Figma; không sửa/mất thủ công những node đã có.
- Không bịa số liệu, dị ứng, an toàn thực phẩm, vị trí cửa hàng, tác động môi trường hay chứng cứ app đối thủ.
- Không buộc GPS/push; không thêm chatbot, delivery, thanh toán online hoặc merchant console vào MVP khi chưa duyệt.
- Không kết thúc batch mà bỏ cập nhật registry/checkpoint; không coi render đẹp là `DONE`.

### Bootstrap order

## FIGMA FILE ARCHITECTURE VÀ THIẾT KẾ EDITABLE

### File và project

**Dùng file được user cung cấp nếu thật sự có quyền edit**. Không tự tạo bản thay thế có tên tương tự rồi nói rằng file gốc đã được cập nhật. Nếu file thuộc sai team/Starter, agent đề xuất cách chuyển file/quyền sang Education cho người dùng duyệt.

Page Figma **đề xuất tối giản**, không tạo nhiều page chỉ vì đã dự kiến 100 màn. Agent phải audit file hiện hữu, tái sử dụng page hợp lệ, và chỉ chia khi canvas thực sự khó quản lý. Không áp số thứ tự vào tên page; ID của từng màn vẫn là `SB-xxx`.

| Page | Nội dung | Có tính vào 100 hi-fi? |
|---|---|---|
| `Foundations` | Variables, text/color styles, grid, accessibility samples | Không |
| `Components` | Reusable component sets + variants | Không |
| `Low-Fi` | Wireframes và flow thô | Không |
| `Rescue Market` | Entry/Discover/Offers/Reservation hi-fi: `SB-001..059` nếu phù hợp flow | Có |
| `Orders & Pickup` | Tracking, pickup, completion: `SB-060..073` | Có |
| `Smart Pantry` | Pantry: `SB-074..090` | Có |
| `Account & Shared` | Account/Impact: `SB-091..100`, có thể chứa entry/shared nếu group khác không phù hợp | Có |
| `Archive` | Thiết kế cũ được giữ có ghi chú khi thật sự cần | Không |

Prototype nối **trên frame gốc**, không tạo bản sao ở page khác rồi đếm hai lần. Nếu một page trở nên quá lớn hoặc có nhiều nhóm đồng chỉnh, tách theo luồng thực tế và cập nhật `docs/workflow.md` + registry. `Rescue Market` không buộc giữ một page nếu quá nặng; bảng này là gợi ý ban đầu, không phải Figma layout cố định.
### Naming conventions

- High-fi frame name: `SB-034 · Offer Detail · Available` hoặc `SB-043 · Offer Detail · Sold Out`.
- Core component: `Component/OfferCard`, variant `Status=Available, Layout=Vertical`.
- Design token: `color/brand/900`, `spacing/16`, `radius/card`, `type/body/regular`, `effect/sheet`.
- Image asset: `food_offer_bakery_01.webp` với manifest; tránh asset names kiểu `image_123 final2`.
- Prototype flow: `F01 | Guest-to-Rescue | v1`, `F05 | Pantry Local | v1`.

### Màn mẫu được duyệt mới là baseline

Các PNG slide 23 trang là *narrative/visual inspiration*; không copy toàn bộ vào canvas làm thành màn UI. Chỉ sau khi người dùng duyệt 5 màn pilot, agent ghi `baseline_version` và token/component versions vào tracking. Khi một batch mới sinh, phải lấy baseline Figma thực tế, không chỉ đọc prompt chữ.

### Figma MCP & Education preflight

1. MCP tool tự xác nhận identity/team/role. Lỗi Starter của phiên cũ là lịch sử, không phải hiện trạng; xem tracking/progress.md cho bằng chứng phiên bootstrap.
2. Agent phải mở đúng file Figma và thử đọc metadata + xác minh có thể thực hiện **thao tác ghi không phá hủy** (sau khi có quyền; theo tool capability/policy), sau đó trả `fileKey`, team, status.
3. Nếu quyền không đủ: **BLOCKED**. Hỏi người dùng đăng nhập đúng tài khoản Education, bật Figma plugin/MCP phù hợp hoặc chia sẻ quyền Editor. Không tìm đường bypass.
4. Load skill Figma chuyên biệt trước khi call, nhất là `figma-use` trước mọi `use_figma`, `figma-generate-library` khi tạo component, `figma-generate-design` khi ráp màn; tuân thủ thông số/version thực tế của tool.
5. Ưu tiên write trực tiếp bằng Figma Plugin API/MCP tạo native nodes và Auto Layout; kiểm tra tính editable sau khi viết. Không gọi ảnh màn hình AI là Figma native layout.
6. Tôn trọng rate limit; nhóm thao tác hợp lý, có retry/backoff, checkpoint idempotent; không spam gọi MCP từng text node nếu có thể batch an toàn.
7. Nếu đang có thành phần trong file: audit và reuse; không xóa hay reset page gốc nếu chưa biết owner/ý nghĩa.

---

## RESEARCH, USABILITY, ACCESSIBILITY & EVIDENCE QA

### Test plan có thể tiến hành ngay

**Prototype round 1 (low-fi):** 5–8 người test dự kiến; task tìm món dưới 50k gần trường, kiểm tra pickup, tìm allergens, giữ chỗ. Test không phải mock numbers.  
**Prototype round 2 (hi-fi):** lặp nhiệm vụ sau cải thiện, thêm QR pickup và Pantry reminder.  
**Merchant interviews (khi tiếp cận được):** cách kiểm stock, cách xác nhận pickup, trách nhiệm mô tả, no-show, thời điểm bắt đầu/đóng cửa.

Mọi kết quả cần `participantId`, `consent`, `scenario`, `task`, `observed result`, `error/misclick`, `direct quote if permitted`, `severity`, `design action`, `retest result`. Không đưa outcome vào slide/report nếu chưa có real study.

### Tiêu chí accessibility

- WCAG 2.2 AA là **mục tiêu thiết kế** khi áp dụng phù hợp cho native mobile: text contrast >=4.5:1, large text >=3:1, interactive elements có hit target hợp lý và focus/hint rõ.
- Không dùng mỗi màu xanh/đỏ. `Còn 1 ngày` có text + icon + style.
- Icon-only action phải có accessible name; screen reader đọc label phù hợp và order logic.
- Form có label thực (không chỉ placeholder), mô tả validation, không mất dữ liệu khi sai.
- Giá gốc bị gạch ngang không giảm khả năng đọc giá hiện tại; giảm giá không chỉ hiện `%`.
- Đối với dị ứng và safety warnings, ngôn ngữ không mơ hồ; unknown được thông báo trước reserve.
- Font scaling/reflow/bàn phím/safe area/scrolling test thực tế.
- Không có auto-animation liên tục quan trọng; hỗ trợ reduced motion nếu code.

### User experience quality gates

- **Purpose:** người dùng hiểu màn này để làm gì trong 3–5 giây.
- **Clarity:** giá, pickup, merchant info và trạng thái xuất hiện theo đúng ưu tiên.
- **Consistency:** tiêu đề, components, CTA, pattern, alerts thống nhất.
- **Recovery:** lỗi tồn kho, offline, GPS denied, hết giờ nhận đều có cách đi tiếp.
- **Trust:** không che điều kiện quan trọng sau nhiều tương tác.
- **Evidence:** usability improvements gắn finding thật hoặc ghi là hypothesis, không bịa feedback.

---

## TRACKING, COMPONENT REGISTRY, CHECKPOINT VÀ STATE MACHINE CÔNG VIỆC

### `screens.csv` contract

Cột bắt buộc:

`id,group,title,flow,screen_type,priority,status,figma_file_key,figma_page_id,figma_node_id,design_baseline_version,component_ids,data_fixture_ids,linked_from,linked_to,prototype_verified,editable_verified,a11y_checked,qa_screenshot,qa_result,reviewed_by,updated_at,notes`

Không cập nhật status bằng suy đoán. Các cột có boolean cần thật sự được kiểm tra, không ghi `true` khi chưa chạy được Figma. `figma_node_id` cần đối chiếu tồn tại trong file hiện tại, không nhận chuỗi tự tạo.

**Lifecycle:**

`BACKLOG → SPECIFIED → READY → DESIGNING → DESIGN_REVIEW → QA_PASS → DONE`  
Ngoại lệ: `BLOCKED`, `NEEDS_REWORK`, `ARCHIVED`.

- `DESIGN_REVIEW` nghĩa là canvas có nội dung nhưng chưa được chấp nhận.
- `QA_PASS` nghĩa checklist/visual/a11y/prototype hợp lệ nhưng có thể còn chờ duyệt theo gate.
- `DONE` nghĩa cả QA, registry, evidence và điều kiện duyệt batch đạt, không còn blocker P0/P1 riêng màn.
- Khi sửa vào màn DONE, chuyển `NEEDS_REWORK` cho tới khi QA lại, không giữ DONE giả.

### `components.csv` contract

`component_key,display_name,scope,lifecycle,figma_component_id,figma_component_set_id,variants,properties,token_dependencies,usage_screen_ids,owner,version,qa_status,approved_at,deprecated_by,notes`.

Shared components phải có stable key; khi đổi Figma node ID phải update mapping và affected screens. Mọi screen khai báo `component_ids` phải resolve được (ngoại trừ local nonshared layout đã giải thích).

### `progress.md` format sau mỗi phiên

```markdown
# Progress — YYYY-MM-DD
- Current docs baseline: <git commit/version>, Figma file <verified key/team>
- Last successful batch: B-XXX
- Last successfully updated Figma node(s): ...
- Screens now: DONE x/100, QA pending y, blocked z
- Components: SHARED x, STABLE y, breaking changes pending z
- Evidence: ./tracking/evidence/...
- Active blockers / Open conflicts: ...
- User decisions required: ...
- Next executable batch: ...
- Risks / rollback instructions: ...
- Git commit: <hash if committed>
```

**Atomicity rule:** Agent không lưu `DONE` trước khi MCP ghi và kiểm tra thành công; khi lỗi giữa chừng, log `partial mutation` và node IDs có thật, không chạy lại tạo duplicate. Khi resume, reconcile live Figma theo `SB-ID` trước khi create.

### Quản lý nhiều agents

- Một **Lead Agent** quản lý docs router, batch plan, registry và quyết định; **Figma Writer Agent** duy nhất có quyền mutation trong mỗi cửa sổ tác vụ để tránh 2 agent overwrite lẫn nhau.
- Subagents có thể song song làm research, kiểm tra competitor, kiểm tra assets/license, viết screen contracts, đọc QA screenshot. Không song song sửa cùng page/component hoặc cùng registry mà không có cơ chế hợp nhất.
- Với repo, làm qua Git commits/branches theo batch; merge sau lint/spec validation. Lệnh destructive Git (`reset --hard`, xóa folder, overwrite file gốc) cần yêu cầu rõ và backup.
- Đọc lại các quyết định của người dùng ghi trong ADR; không xem prompt cũ là authority cao hơn Figma state mới.

### Decision log (ADR-lite)

Mỗi decision entry ngắn: `ID`, ngày, vấn đề, options nếu có, quyết định, lý do, screens/components impacted, nguồn hoặc người duyệt; **không tạo một file ADR cho mỗi lựa chọn nhỏ**. Phải có ADR nếu: đổi bottom navigation, thêm in-app payment, thêm merchant module vào 100 màn, thay identity colors, sửa state machine, thay policy dị ứng, thay target Figma file.

---

## SKILLS / MCP — TÌM BẰNG FIND-SKILLS, KHÔNG TẠO CUSTOM SKILL

### Chọn skill đúng, không cài tràn lan

- **Không sinh `.agents/skills/savebite-*` hoặc custom `SKILL.md` trong repo.** Quy trình đặc thù SaveBite nằm trong `AGENTS.md` + `docs/workflow.md`; các hướng dẫn domain trong `docs/` được đọc theo `docs/README.md`.
- Ưu tiên **skills chính thức/bundled của Figma plugin** nếu môi trường agent đã cung cấp; không cài bản khác gây trùng và không cho rằng package trên skills.sh giống hệt skill plugin.
- Nếu môi trường chưa có skill phù hợp, agent sử dụng **`find-skills`** từ [vercel-labs/skills](https://github.com/vercel-labs/skills) để tìm, **đọc** và chọn skill có nguồn đáng tin. Cú pháp CLI đã kiểm chứng từ tài liệu hệ sinh thái:

```bash
# Chỉ khi chưa có skill find-skills
npx skills add https://github.com/vercel-labs/skills --skill find-skills
# Search khi có nhu cầu thực tế, không tự tải hàng loạt
npx skills find figma
npx skills find design system
npx skills find accessibility
# Chỉ dùng npx skills add <repo/skill> cho mục đã kiểm tra nguồn và cần thiết
```

- Lựa chọn dựa trên nhiệm vụ, độ tin cậy repo, update/compatibility và quyền của skill. Không chạy lệnh cài gói mù, không truyền token Figma/credentials vào bất kỳ skill nào chưa được kiểm tra.

### Skill phù hợp theo giai đoạn

| Tình huống | Skill cần đọc nếu có sẵn |
|---|---|
| Chỉnh node/variables/components trên Figma qua Plugin API | `figma-use` |
| Tạo foundation, variants, reusable components | `figma-generate-library` + `figma-use` |
| Ráp màn hi-fi editable bằng design system | `figma-generate-design` + `figma-use` |
| Lập sơ đồ FigJam thật sự cần thiết | `figma-generate-diagram` |
| Đọc Figma để implement thành code | `figma-design-to-code` |
| Đồng bộ components giữa Figma và code khi đã có codebase | `figma-code-connect`, optional |

**Không custom skill**, không cài skill chỉ để có thật nhiều mục trong danh sách. Trước mỗi thao tác Figma, xem hướng dẫn MCP/skill thực tế trong phiên và tuân thủ prerequisites của tool.

### MCP tối thiểu; Context7 là tùy chọn đúng lúc

1. **Figma MCP — bắt buộc**: xác minh danh tính, đúng file/team Education, quyền Editor thật và khả năng native editable write; nếu fail đánh `FigmaWrite=BLOCKED`. Không tự tạo file thay thế và không báo đã nối thành công chỉ từ OAuth.
2. **Local files/Git — bắt buộc trong môi trường agent**: đọc/ghi repo, Git checkpoints, tránh secrets.
3. **Browser/Playwright — tùy nhu cầu**: khi cần code UI E2E, screenshot/visual regression hoặc tài liệu web; không dùng để bypass access Figma.
4. **Context7 MCP — không bắt buộc cho giai đoạn Figma canvas**. Chỉ bật/cài khi đang làm phần **code hoặc gặp nghi vấn về SDK/API theo phiên bản** (React Native/Expo/TypeScript, plugin API, testing dependencies). Ưu tiên documentation chính thức và package version đang cài; dùng Context7 để truy xuất nhanh tài liệu version-specific, không dùng nó để quyết định nghiệp vụ SaveBite hoặc thay thế skills Figma. Nếu server đã có, tái sử dụng, không thêm bản thứ hai. [Context7 docs](https://github.com/upstash/context7) cung cấp remote `https://mcp.context7.com/mcp` và setup theo client; agent kiểm tra lệnh cấu hình phù hợp, không tự nhét API key vào repo.

### Kiểm tra quyền Figma đích

Figma đích: https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/Untitled. Trạng thái thực và bằng chứng quyền nằm trong tracking/progress.md; mỗi phiên phải xác minh lại đúng tài khoản, team và thực quyền ghi trước mutation.

---

## LỘ TRÌNH THỰC HIỆN AGENT (CÓ APPROVAL GATES)

### Phase 0 — Preflight & environment (không thiết kế 100 màn)

- Check git environment, inventory current files, verify source documents.
- Verify Figma account/team/edit permissions. **Nếu fail, report blocker và không coi đã kết nối xong.**
- Detect Codex CLI/app/IDE thực tế, load skills, install missing ones from trusted source only.
- Duy trì tài liệu domain qua router, kiểm tra provenance/100 IDs, không dựng custom skill, checklist trùng hoặc scripts dư thừa.
- Bàn giao: readable Bootstrap Report, all setup steps + exact unresolved blockers.

**Gate P0:** `docs migrated and routed`, `docs self-contained`, `screen registry valid`, `Figma editor verified or clearly BLOCKED`, `no secrets in repo`.

### Phase 1 — Discovery & low-fi

- Derive JTBD/task flows and research plan; **không bịa research outcome**.
- Competitor audit 20 apps with real sources; wireframe 8–12 màn core; produce digital low-fi prototype and video checklist.
- Simulate edge-case paths before visual polish.
- Bàn giao: documented core IA, clickable low-fi skeleton, content/data contract, approved reference image direction.

**Gate P1:** primary flow đi xuyên được ở low-fi; copy không mơ hồ về payment/pickup/allergens.

### Phase 2 — Foundations + Core components

- Dựng tokens và styles; màu light, typography Vietnamese, grid, spacing, radius, accessibility samples.
- Các components core mô tả trong phần **Design System và Component Strategy** (được chuyển vào `docs/design-system.md`); kiểm tra 360/390/430 widths và dài/ngắn/empty/state.
- Ghi `figma_component_id` có thật vào registry; chụp component specimen.

**Gate P2:** owner duyệt visual baseline và các component core. Không sinh 100 frame trước gate.

### Phase 3 — 5-screen pilot

5 frame đã duyệt: `SB-015`, `SB-034`, `SB-051`, `SB-053`, `SB-056`. Có primary/secondary states, ảnh hợp lệ, accessibility, dynamic text, clear pickup. Trình người dùng duyệt **look-and-feel mobile thực**, không dựa vào slide art.

**Gate P3:** duyệt layout density, type scale, Brand colors, OfferCard, PriceBlock, PickupInfo, Nav; nếu fail, sửa 5 màn + components, không kéo sai lầm sang batch tiếp.

### Phase 4 — High-fi production

- Chia batches 5–8 frames, P0 trước; mỗi batch có screen contracts, dependency/affected components, screenshot QA và checkpoint.
- Sau 20–30 màn, review component consolidation và cross-flow consistency.
- Trước khi đủ 100 phải có primary flow prototype chạy được; đừng đợi màn 100 mới nối dây.
- Thiết kế all states thật; dữ liệu demo fixture xuyên suốt không mâu thuẫn.

**Gate P4:** `DONE >= 100` và độc lập, không duplicate/orphan/PNG UI; có audit evidence + Figma file link.

### Phase 5 — Prototype, UX tests & iteration

- Chạy ít nhất F-01 end-to-end; khuyến khích F-03 failure recovery và F-05 Pantry.
- Record usability evidence from real participants (nếu tổ chức), ưu tiên test lại sau feedback.
- Thực hiện before → finding → after dựa dữ liệu. Nếu chưa test thật, phần slide ghi là giả thuyết thiết kế, không “đã xác nhận cải thiện”.

### Phase 6 — Code UI implementation

- Ưu tiên **React Native + Expo + TypeScript** vì là stack hợp lý cho mobile UI, có đường lên app thật. Đây là `DEFAULT` định hướng, không phải yêu cầu cố định của giảng viên (Flutter hoặc HTML/CSS cũng được phép theo PDF).
- Cấu trúc `app/src/{features,components,tokens,navigation,data,services,fixtures,utils}`. `features` tách `auth`, `discover`, `offers`, `reservations`, `orders`, `pantry`, `account`.
- Shared components reflect Figma but không copy HTML mô phỏng thành production React Native. Implement loading/empty/error states và navigation theo screen IDs.
- Tách `MockRepository` và API service interfaces; chưa có backend thì phải có deterministic fixtures + mocked transitions, **không báo giao dịch thật**.
- Goal: tối thiểu 50 coded screens (ngưỡng an toàn), có kiểm tra screen-to-code mapping.

**Initial code target:** 40 màn `P0` từ registry + 10 màn cốt lõi `P1` để Pantry và Impact có code: `SB-074`, `SB-075`, `SB-076`, `SB-077`, `SB-079`, `SB-080`, `SB-084`, `SB-086`, `SB-088`, `SB-100`. Đây là lựa chọn kỹ thuật, không thay requirement; có thể thay một-một nếu đã qua ADR. Nếu một state không là route độc lập trong code, cần chứng minh bằng UI state riêng và thống nhất với cách đếm của giảng viên — **không tự khẳng định đạt 50 chỉ bằng 40 route + 10 variant**.

**Gate P6:** code chạy được, luồng chính hoạt động với mocked backend rõ ràng, không hardcode chỉ screenshot; compare design↔code trên 360/390/430, không có blocking navigation error.

### Phase 7 — Submission/portfolio

- Evidence map rubric ↔ files/URLs/recordings: Figma hi-fi, lo-fi, prototype link, two demo videos, sketch, coded UI counts, code repo, 20 competitor sources, case-study portfolio, group video.
- Presentation slide SaveBite đã tạo trước chỉ được xem là bộ minh họa ban đầu; thay phần research/test/screenshots bằng **kết quả thật** trước khi nộp.
- Không đóng dấu “100% complete” cho deliverable có review chưa chạy/permission chưa giải quyết.

---

## QA CHECKLISTS VÀ RELEASE CONDITIONS

### Per-screen QA (checklist trong `docs/workflow.md`)

```markdown
- [ ] SB-ID đúng, có một Figma FRAME thật trong đúng HIFI page.
- [ ] Từ top app bar đến CTA không bị cắt, có scrolling/safe-area phù hợp.
- [ ] Key text/editable layers; instances là components không phải PNG toàn màn.
- [ ] Colors/typography/spacing dùng tokens, không có style mới vô cớ.
- [ ] Copy tiếng Việt đúng dấu, giá/giờ/merchant fixture thống nhất.
- [ ] Primary/secondary actions có kết quả đúng; backstack không mất context.
- [ ] Error/empty/loading tương ứng có xử lý hoặc liên kết đến state phù hợp.
- [ ] Không giấu allergen/pickup terms/unknown disclosure khi cần.
- [ ] Accessibility: contrast, text scaling logic, icon labels, tap targets.
- [ ] Component reuse; không detached components vô lý.
- [ ] Screenshot mới đã review và linked in tracking.
- [ ] Figma node được read-back xác minh tồn tại và đúng loại.
- [ ] Navigation/link hợp lệ; không có orphan không được giải thích.
- [ ] Evidence và status cập nhật; chỉ DONE khi QA PASS.
```

### Batch-level QA (checklist trong `docs/workflow.md`)

- Screenshot contact sheet của batch từ Figma native frames; so sánh baseline và spacing/type scale.
- `screens.csv` và Figma nodes match 1:1 với target IDs; không duplicate/hanging links.
- All reused component IDs resolve; không branch đổi màu/variant ngẫu nhiên.
- Check language/a11y/price trust on 3 representative frames + all error states.
- Test flow transitions trong batch; không report success khi UI chỉ là static.
- Quyết định quan trọng ghi ADR. Blockers có owner và next action; batch report rõ `passed/failed/deferred`.

### Product acceptance (cuối đồ án)

| Area | Pass condition | Evidence cần có |
|---|---|---|
| 100 hi-fi screens | >=100 distinct QA-passed native Figma frames from registry; no screen-count padding | Frame inventory + screenshots + Figma links |
| Core prototype | F-01 đi từ guest/discover tới verified pickup/impact; back/recovery logic | Figma prototype demo video, link |
| Low-fi | Wireframes có rationale, low-fi flow và video 1–3m | Figma page + video |
| Design system | Tokens, components/variants chuẩn, không duplicated drift | Figma library + component registry |
| Accessibility | WCAG-inspired audit, no critical unresolved blocker | Contrast/hit target/content checks |
| 20 competitors | 20 real apps, source and observed patterns | Competitor matrix + screenshots sourced |
| Usability | Không bịa participants/metrics; nếu test thì findings traceable | Raw anonymized notes + before/after |
| Mobile demo | Figma prototype vận hành trên mobile được chứng minh | Video/photo thật, không AI mockup |
| Coded UI | Mục tiêu 50, thực sự có route/state UI chạy được | Repo, build logs, demo video, mapping |
| Portfolio & presentation | Câu chuyện xuyên suốt và phù hợp chứng cứ | PDF/website, slides, nhóm 5 người |

**STOP release nếu:** file Figma thiếu quyền, 100 ảnh raster bị tính là màn, số liệu research/test giả, prototype hỏng luồng chính, lỗi nghiêm trọng an toàn thực phẩm, duplicate/stock inconsistency trong UI, hoặc code demo không chạy được.

---


## Quy tắc hiện hành của phiên bootstrap

DEC-001 là override được duyệt của các gate pilot cũ: được tạo 5 frames subset và foundations trực tiếp phục vụ chúng sau migration/access pass. Không cần một approval mới để thực thi phạm vi này. Gate production vẫn đóng cho tới owner review. Quyền student không tự chứng minh từng tính năng: phải thử native write/read và interactions thực.

Git: branch docs/bootstrap-figma-pilot cho bootstrap; về sau design/<module>-<scope>, docs/<scope>, fix/<scope>. Lease chỉ ghi progress: owner, scope, bắt đầu và release checkpoint. Không dựng lock server. CLAUDE.md symlink tương đối tới AGENTS.md trên Linux. Không tạo adapter cho client chưa dùng.

Source requirements được kiểm tra bằng tài liệu gốc ngoài repo; provenance/hash giữ trong tracking/evidence/migration.json. Không yêu cầu đọc source attachment để tiếp tục tác vụ. Không lưu secrets hoặc cấu hình tài khoản toàn cục. Không cài tool trùng nếu official plugin đã có.

Rollback: revert commit docs khi cần; Figma chỉ sửa/xóa exact IDs do phiên này tạo sau khi đọc live, không dùng rollback Git để giả định canvas đã rollback.
