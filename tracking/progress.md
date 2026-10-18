# Progress · 19/10/2026

Gate: **AWAITING_OWNER_REVIEW**. Bootstrap PASS; FigmaWrite VERIFIED; pilot v0.3 technical checks PASS_WITH_LIMITS. DESIGN_REVIEW 5/100, BACKLOG 95/100, DONE 0/100. Baseline và owner acceptance để trống.

## Kết quả và ownership

- Đã đọc toàn bộ hai attachment và chuyển yêu cầu thành docs theo domain. 100 unique SB-IDs, 20 D-defaults, 6 flows; repo tự đọc được qua AGENTS → docs router → progress, không phụ thuộc handoff bên ngoài.
- Sources chuyển đầy đủ sang [Markdown](../docs/README.md#nguồn-đã-chuyển-thành-markdown): assignment 9 trang; Zia 25 trang + 10 hình tham khảo + persona/journey text; DOCX 803 đoạn không trống + 4 bảng. Có hash, links gốc và provenance; file nguồn ngoài repo không bị sửa/xóa. Không coi case study/dự thảo slide là nghiên cứu thật của SaveBite.
- CLAUDE.md symlink tương đối tới AGENTS.md; không copy rules. Drift protocol, writer lease và checkpoints nằm ở workflow.
- Last successful batch: B-PILOT-003, fresh rebuild theo DEC-005. v0.1/v0.2 REJECTED; đã xóa đúng 5 roots cũ 5:204..5:208 và page Components cũ 5:2 do agent tạo. Page 1 được giữ nguyên.
- Lease RELEASED: Codex lead/writer; scope docs, pilot, shared tokens/components, registry; chỉ một writer, không subagent.

## Environment, MCP và skills

- Fedora 44 KDE / Linux 6.19.10; Codex desktop, CLI available 0.150.1; Git 2.55.0, Python 3.14.7, Node 24.19.0; gh 2.97 authenticated nrin31266.
- Official Figma MCP/plugin đã có; dùng whoami, get_metadata, get_libraries, search_design_system, use_figma, screenshots/image assets. Preflight không có subscribed libraries hoặc local components/tokens; không có Code Connect/code app để reuse. Không cài trùng MCP; không đổi user config/OAuth.
- Account RIN do owner chọn: Nguyen Van Rin, team Nguyễn Văn Rin's team, tier **student**, seat **Full**, role **admin**. Access đúng file NLTv70kDZ2i3HpOnOKQCDY và native write/read đã chứng minh bằng sandbox frame 2:3/text 2:4, sau đó dọn đúng trial nodes.
- Đã dùng find-skills: `npx --yes skills find frontend-design`, `find 'mobile app design'`, `find accessibility`; đọc nguồn/metadata/content/license trước khi chọn hai skill cần dùng.
- Skills mới **project-local**: frontend-design (anthropics/skills) và ui-ux-pro-max (nextlevelbuilder). Source revision/hash ở [manifest](../.agents/skills/manifest.json). Ban đầu cài qua official installer rồi chuyển nguyên vẹn vào repo theo yêu cầu local; không giữ hai bản global. Không tạo custom SaveBite skill.
- Official skills reuse: figma-use, figma-generate-library, figma-generate-design. Brainstorming/Ponytail áp dụng scope đã duyệt; PDF/Documents dùng đọc nguồn. UI/UX Pro Max output thiên web marketing không khớp sản phẩm đã bị bỏ; quyết định visual theo docs/design-system.md.
- Context7 không cần cho canvas hiện tại. Browser có sẵn dùng để bấm prototype thật; không thêm framework hoặc tool chưa cần.

## Figma pilot v0.3

File duy nhất: [SaveBite](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=2-2). Page Pilot · Rescue Market `2:2`; Foundations `4:48`; Components mới `27:87`.

| Screen | Node trực tiếp | Screenshot |
|---|---|---|
| SB-015 · Khám phá | [28:2](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-2) | [PNG](evidence/SB-015.png) |
| SB-034 · Chi tiết ưu đãi | [28:80](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-80) | [PNG](evidence/SB-034.png) |
| SB-051 · Chọn giờ nhận | [28:118](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-118) | [PNG](evidence/SB-051.png) |
| SB-053 · Tóm tắt đặt trước | [28:167](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-167) | [PNG](evidence/SB-053.png) |
| SB-056 · Đặt trước thành công | [28:215](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-215) | [PNG](evidence/SB-056.png) |

[Prototype click-through](https://www.figma.com/proto/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?page-id=2%3A2&node-id=28-2&starting-point-node-id=28%3A2&scaling=scale-down): **VERIFIED** bằng bấm canvas thật qua 5 màn và quay về Khám phá; Back từ thành công về tóm tắt cũng đã bấm. Các Back còn lại xác minh read-back, không claim đã bấm hết.

[Overview](evidence/pilot-overview.png), [Foundations](evidence/foundations.png), [Components](evidence/components.png). 38 variables, 8 text styles; 12 component families / 15 main components, 2 variant sets, 28 instances. [Registry components](components.csv) giữ IDs 27:89..27:183 thực; SHARED 15, STABLE 0. Foundations specimen 4:49; Components specimen 29:2. Không publish library.

UI native editable, Auto Layout; ảnh raster chỉ là hai ảnh món có license/source trong manifest. Một fixture chính đi xuyên cả 5 màn, fixture phụ chỉ để so sánh ở discovery. Copy/giá/giờ/dị ứng UNKNOWN đồng bộ. QR vector và mã dự phòng có nhãn minh họa, không tạo đơn/giữ stock. Search/filter/category/favourite/tabs và offer phụ là preview tĩnh ngoài subset.

## QA và bằng chứng

- [Read-back](evidence/figma-readback.json): đúng file, đúng 5 unique screen IDs, 390×844, unlocked, Be Vietnam Pro, text styles bound, 28 instances, 9 interactions, 0 text overflow, 0 image-only screen frames, errors=[] .
- [QA evidence](evidence/qa.json): resize thật toàn bộ 5 màn ở 360 và 430 px không overflow; đã restore 390. Font stress 125% trên SB-034 được kiểm hình, giá nguyên vẹn/nội dung đọc được; đã restore styles. Đây không phải kiểm Dynamic Type trên thiết bị.
- 10 cặp text/surface thực dùng đạt ≥4.5:1 (thấp nhất 4.88); 9 connected hotspots đều ≥48×48. Giờ hết hạn có label, trạng thái chọn có dấu check, dị ứng unknown hiển thị trước confirm; không chỉ báo bằng màu.
- All final screenshots + overview/components/foundations đã xem trực tiếp. Hash PNG, assets và skills có thể kiểm lại bằng `python3 scripts/validate.py`; validator còn kiểm 100 IDs, 20 defaults, 6 flows, symlink/router, registry mapping, duplicate-ID negative self-check.
- Git whitespace check trên files dự án PASS; vendored ui-ux-pro-max có trailing spaces upstream, giữ nguyên để bảo toàn source đã pin và loại khỏi whitespace lint. Secret-pattern staged scan PASS; không có PDF/DOCX nguồn hoặc screenshot URL tạm trong commit.
- a11y_checked=false trong registry vì chưa kiểm assistive technology đầy đủ; qa_result=PASS_WITH_LIMITS, status=DESIGN_REVIEW, không QA_PASS/DONE giả.
- Chưa kiểm người dùng thật, VoiceOver/TalkBack/keyboard, Figma Mobile/thiết bị thật, toàn bộ long-content/error states, backend/auth/stock/pickup thực. Không có app để build/run hoặc video end-to-end thật.

## Open conflicts và review tiếp theo

1. Owner review thẩm mỹ/khả dụng của **v0.3**, quyết định nhận baseline hoặc nêu chỉnh sửa cụ thể; chưa rollout thêm màn.
2. B-COURSE-01: source Deliverables=50 coded screens, rubric/Notes=30. Giữ mục tiêu 50; cần xác nhận giảng viên trước nộp.
3. B-RESEARCH-01: chưa có dữ liệu người dùng/merchant thật; cần research/usability evidence trước claim kết quả.
4. B-DEVICE-01: cần demo trên điện thoại và kiểm accessibility thực; prototype desktop subset chưa thay cho mobile demo.
5. B-LEGAL-01: production policy/food safety và thông tin merchant chưa review. Không chặn pilot demo; không claim food safety.

Asset pending đã được giải quyết bằng hai ảnh Pexels có manifest. Pilot-ID conflict đã giải quyết bởi DEC-001; GitHub override bởi DEC-004; quyền xóa mock cũ bởi DEC-005.

## Git checkpoint và bước tiếp theo

- Branch task: docs/bootstrap-figma-pilot. Bootstrap checkpoint: `4aaa46c` (docs migration và registry trung thực).
- Design + QA checkpoint: `82815e3588106535f2b72bd7f5a5f8a70e87d16d`. Đã tạo và push [nrin31266/savebite-figma](https://github.com/nrin31266/savebite-figma), **private**, default branch `main`, remote `origin`. `git ls-remote` đã xác nhận `main` và `docs/bootstrap-figma-pilot` cùng SHA checkpoint này. Không có PR.
- Báo cáo xuất bản được commit tiếp sau design checkpoint; lấy SHA báo cáo mới nhất bằng `git log -1 --oneline`. Trước commit báo cáo, worktree clean và upstream đồng bộ. Báo cáo chỉ cập nhật README/router/progress; không đổi canvas hoặc bằng chứng thiết kế.
- Không sửa Git account toàn cục, không force push, không tạo PR, không đổi Figma sharing. `.gitignore` có secrets/env/cache; chỉ force-add những PNG evidence cuối được liệt kê trong QA.
- Next executable batch: chỉ owner review pilot. Sau acceptance mới khóa baseline và lên batch tiếp theo; chưa tạo 100 màn hoặc app code.
