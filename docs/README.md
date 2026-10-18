# Bản đồ tài liệu SaveBite

Đọc [luật agent](../AGENTS.md) rồi [tiến độ](../tracking/progress.md). Chỉ đọc domain và phụ thuộc cần thiết cho task.

| Công việc | Nguồn chuẩn | Hiện trạng / bằng chứng |
|---|---|---|
| Scope, 20 defaults, nguồn môn học, business/data policy, roadmap app | [product.md](product.md) | Provenance trong tài liệu và [migration evidence](../tracking/evidence/migration.json) |
| IA, F-01..06, 100 SB-IDs, contracts pilot | [experience.md](experience.md) | [screens.csv](../tracking/screens.csv) |
| Visual direction, tokens, components và usage | [design-system.md](design-system.md) | Figma live + [components.csv](../tracking/components.csv) |
| Figma, multi-agent, MCP/skills, Git, research/a11y/QA, code handoff | [workflow.md](workflow.md) | [progress.md](../tracking/progress.md) |
| Quyết định mới và override đã duyệt | [decisions.md](decisions.md) | Nguồn duyệt ghi theo entry |
| Kiểm tra có thể chạy lại | [validate.py](../scripts/validate.py) | Evidence trong progress |

Khi thêm/đổi/xóa tài liệu, cập nhật router cùng thay đổi. Requirements/decisions sở hữu nghiệp vụ; Figma live sở hữu node đang tồn tại; registry chỉ theo dõi. Không đồng bộ bằng cách âm thầm ghi đè nguồn khác.

## Nguồn đã chuyển thành Markdown

Không cần mở PDF/DOCX để đọc nội dung. Chỉ đọc các bản nguồn khi tra provenance hoặc giải quyết conflict; không copy lại policy từ nguồn sang nhiều domain.

| Nguồn | Markdown đầy đủ | Cách dùng |
|---|---|---|
| Đề bài UX/UI | [course-assignment.md](references/course-assignment.md) | 9 trang text, links gốc; yêu cầu học phần và mâu thuẫn 50/30 |
| Nội dung slide SaveBite | [savebite-slide-content.md](references/savebite-slide-content.md) | 803 đoạn không trống, 4 bảng, 23 mục slide; là dự thảo, không evidence nghiên cứu |
| Case study Zia’s Pizza | [zia-pizza-case-study.md](references/zia-pizza-case-study.md) | 25 trang text, links và hình persona/journey/wireframes; tham khảo phương pháp |
| Kiểm chứng conversion | [source-conversion.json](../tracking/evidence/source-conversion.json) | Hash gốc, số trang/đoạn/bảng, nội dung hình và phạm vi sử dụng |

## Skills dự án và assets

- [Skill manifest](../.agents/skills/manifest.json): frontend-design và ui-ux-pro-max được cài local trong repo; third-party upstream, không custom SaveBite skill.
- [Asset manifest](../assets/manifest.json): nguồn, giấy phép và phạm vi ảnh minh họa/nguồn tham khảo.
- [Figma read-back](../tracking/evidence/figma-readback.json): mapping thật của 5 pilot, components và interactions.

- [QA evidence](../tracking/evidence/qa.json): widths, font stress, contrast, hit targets, prototype clicks và các giới hạn chưa kiểm.
- [Access/tools evidence](../tracking/evidence/access-and-tools.json): student/Full account, write trial và skill discovery.
