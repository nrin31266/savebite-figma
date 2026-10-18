# Progress · 19/10/2026

Gate thiết kế: **AWAITING_OWNER_REVIEW**. Evidence bootstrap ghi FigmaWrite VERIFIED; pilot v0.3 technical checks PASS_WITH_LIMITS. Đây là bằng chứng lịch sử; phiên audit docs chưa reverify Figma live. DESIGN_REVIEW 5/100, BACKLOG 95/100, DONE 0/100. Baseline và owner acceptance để trống.

## Kết quả và ownership

- Đã đọc toàn bộ hai attachment và chuyển yêu cầu thành docs theo domain. 100 unique SB-IDs, 20 D-defaults, 6 flows; repo tự đọc được qua AGENTS → docs router → progress, không phụ thuộc handoff bên ngoài.
- Đã loại bản chép 3 nguồn và 10 ảnh Zia khỏi repo public; giữ tên/hash/provenance trong docs/references/README.md và source-conversion.json. Bản đầy đủ nằm ở backup private ngoài repo; docs domain đủ để tiếp tục.
- CLAUDE.md symlink tương đối tới AGENTS.md; không copy rules. Drift protocol, writer lease và checkpoints nằm ở workflow.
- Last successful batch: B-PILOT-003, fresh rebuild theo DEC-005. v0.1/v0.2 REJECTED; đã xóa đúng 5 roots cũ 5:204..5:208 và page Components cũ 5:2 do agent tạo. Page 1 được giữ nguyên.
- Lease RELEASED: Codex lead/writer; scope docs, pilot, shared tokens/components, registry; chỉ một writer, không subagent.

## Audit docs, skills và phạm vi hiện hành

- DEC-006: repo chỉ làm Figma, design system, prototype và docs/evidence. Đã bỏ stack/app implementation/API mẫu và code acceptance gates; 50/30 màn code chỉ là bối cảnh học phần.
- Làm rõ pilot đăng nhập giả định, quantity=1/slot cố định, các controls tĩnh và back từ success để review. Sửa lifecycle wording về DESIGN_REVIEW/QA_PASS/DONE; bảng components mở rộng không còn là việc bắt buộc trước pilot.
- Sửa B-ASSETS-01: pilot đã có 2 ảnh Pexels; nguồn mới cho màn sau vẫn cần manifest. Không thay business/safety/payment/navigation trên canvas.
- Skills: giữ frontend-design/ui-ux-pro-max; đã cài project-local figma-use, figma-generate-library, figma-generate-design, design-critique bằng official installer --dest. 6 SKILL.md có source/revision/hash trong manifest; không cài global. Figma trio local-only vì upstream chưa khai báo license phân phối; không commit bản nguồn này lên public.
- [Shortlist + web sources](../docs/references/agent-skills.md): đã dùng find-skills, đọc upstream, kiểm GitHub metadata và official Figma/OpenAI Docs. Chưa cài thêm MCP hoặc đổi config. Cài skills không cấp quyền Figma.
- Phiên audit này không có Figma tools trong danh sách callable; không sửa canvas, không kiểm lại screenshots/prototype/mobile. Evidence bên dưới là checkpoint pilot trước, không xác minh lại live trong đợt docs.
- Lease docs: Codex / docs, source cleanup, skills manifest / RELEASED tại checkpoint audit; không có Figma writer lease.

## Figma pilot v0.3 · evidence checkpoint trước

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
2. B-COURSE-01: source Deliverables=50 coded screens, rubric/Notes=30. Ngoài scope repo; nhóm xác nhận giảng viên khi bàn giao phần code.
3. B-RESEARCH-01: chưa có dữ liệu người dùng/merchant thật; cần research/usability evidence trước claim kết quả.
4. B-DEVICE-01: cần demo trên điện thoại và kiểm accessibility thực; prototype desktop subset chưa thay cho mobile demo.
5. B-LEGAL-01: production policy/food safety và thông tin merchant chưa review. Không chặn pilot demo; không claim food safety.

Asset pending đã được giải quyết bằng hai ảnh Pexels có manifest. Pilot-ID conflict đã giải quyết bởi DEC-001; GitHub override bởi DEC-004; quyền xóa mock cũ bởi DEC-005.

## Git checkpoint và bước tiếp theo

- Task branch: docs/figma-scope-cleanup. DEC-007 cho phép backup private, lọc lịch sử, force-push và đổi chính repo [savebite-figma](https://github.com/nrin31266/savebite-figma) thành public. Không thay Figma sharing.
- Backup private đã tạo ngoài repo, gồm workspace archive và Git bundle; bundle verify PASS. Không đưa backup hoặc đường dẫn máy cá nhân vào Git public. SHA cũ sẽ đổi sau rewrite; dùng git log để đọc checkpoint hiện tại.
- Public release: VERIFIED — GitHub trả PUBLIC, default main; anonymous API + clone PASS. Đã force-push bằng explicit force-with-lease sau scan 4 commits/141 unique blobs: không thấy credential patterns, raw reference paths hoặc source paths máy cá nhân. Main, bootstrap và cleanup đã chứa docs audit; không có PR/tags giữ các nguồn cũ.
- Audit QA: validator PASS (100 IDs, 20 defaults, 6 flows, 5 node mappings, 15 components, evidence/assets/skills hashes); canvas/mobile/usability NOT CHECKED trong phiên này. Kiểm tra links gồm progress và docs; clone public không có 3 skill local-only vẫn validate được. Validator báo riêng số skill đã kiểm hash và số optional chưa cài. Không gọi QA này là revalidation thiết kế.
- Next design batch: owner review pilot; sau acceptance mới khóa baseline và lên batch tiếp theo. Không triển khai app hoặc tự tạo tiếp 100 màn.
