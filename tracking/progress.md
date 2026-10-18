# Progress · 19/10/2026

- Bootstrap: docs migration PASS; 100/100 IDs seeded, 20 defaults giữ tại product.md, DONE=0.
- Figma target: NLTv70kDZ2i3HpOnOKQCDY, kết nối RIN do user chọn.
- Identity verified: Nguyen Van Rin; team Nguyễn Văn Rin's team; tier student, seat Full, role admin.
- FigmaWrite=VERIFIED: sandbox frame 2:3 / text 2:4 tạo và read-back trên page 2:2; native editable, unlocked, Auto Layout.
- Canvas preflight: Page 1 (0:1) trống; local components/variables/styles rỗng. get_libraries không có subscribed; search Button/OfferCard/PickupSlot/color/spacing/body trong file rỗng. Không có Code Connect/source code trong repo trống.
- Pilot page: Pilot · Rescue Market (2:2). Trial frame 2:3 và text 2:4 đã được dọn; page được giữ. Chưa tạo 5 màn.
- Lease ACTIVE: Codex lead/writer, docs + pilot + shared tokens/components + registry; một writer, không subagent.

## Environment
- Fedora 44 KDE, Linux 6.19.10; Codex desktop session; CLI available 0.150.1.
- Git 2.55.0, Python 3.14.7, Node 24.19.0, pdftotext available.
- Figma official plugin/MCP đã có và dùng whoami/get_metadata/use_figma/get_libraries/search_design_system.
- Skills sẵn có: figma-use, figma-generate-library, figma-generate-design (đã đọc); brainstorming/Ponytail áp dụng phạm vi đã duyệt. PDF/Document skill dùng khi kiểm tra nguồn.
- Không cài thêm MCP/skills; find-skills không cần vì không thiếu capability; Context7 không cần cho canvas. Không chỉnh user config, không secrets.

## Sources và migration
- Hai attachment đã đọc toàn bộ; hash trong evidence/migration.json. Không copy handoff vào repo, không xóa file gốc ngoài repo.
- Nguồn môn học tìm thấy ngoài workspace tại Documents/Vku/4_HK1/UIUX: assignment PDF, nội dung slide DOCX và Zia PDF; đã trích và đọc text. Không claim hình/render QA của các nguồn tham khảo.
- Nội dung domain được chuyển sang docs; execution prompt cũ được thay bằng DEC-001. Chưa làm nghiên cứu/competitor audit; mọi kết quả trong slide là planned/concept.

## Open conflicts / blockers
- B-COURSE-01 REQUIREMENT: source Deliverables=50 coded screens, rubric/Notes=30; giữ 50, cần hỏi giảng viên trước nộp.
- B-RESEARCH-01: chưa có dữ liệu người dùng/merchant; chặn claim nghiên cứu.
- B-ASSETS-01: ảnh món licensed chưa có; dùng placeholder pending được duyệt cho pilot.
- B-LEGAL-01: production policy/food safety chưa review; không chặn demo.
- Danh sách pilot cũ khác mới được giải quyết bằng DEC-001, không đổi meaning SB-051.

## Next / Git
- Validate migration/router/symlink; build foundations tối thiểu rồi 5 màn và liên kết; read-back/screenshot/QA, update registries.
- Branch docs/bootstrap-figma-pilot; chưa commit, chưa push, không remote.
