# Bản đồ tài liệu SaveBite

Đọc [luật agent](../AGENTS.md) rồi [tiến độ](../tracking/progress.md). Chỉ đọc domain và phụ thuộc cần thiết cho task.

| Công việc | Nguồn chuẩn | Hiện trạng / bằng chứng |
|---|---|---|
| Scope, 20 defaults, nguồn môn học, business/data policy, phạm vi Figma | [product.md](product.md) | Provenance trong tài liệu và [migration evidence](../tracking/evidence/migration.json) |
| IA, F-01..06, 100 SB-IDs, contracts pilot | [experience.md](experience.md) | [screens.csv](../tracking/screens.csv) |
| Visual direction, tokens, components và usage | [design-system.md](design-system.md) | Figma live + [components.csv](../tracking/components.csv) |
| Figma, multi-agent, MCP/skills, Git, research/a11y/QA, bàn giao thiết kế | [workflow.md](workflow.md) | [progress.md](../tracking/progress.md) |
| Quyết định mới và override đã duyệt | [decisions.md](decisions.md) | Nguồn duyệt ghi theo entry |
| Kiểm tra có thể chạy lại | [validate.py](../scripts/validate.py) | Evidence trong progress |

Khi thêm/đổi/xóa tài liệu, cập nhật router cùng thay đổi. Requirements/decisions sở hữu nghiệp vụ; Figma live sở hữu node đang tồn tại; registry chỉ theo dõi. Không đồng bộ bằng cách âm thầm ghi đè nguồn khác.

## Nguồn và tài liệu tham khảo

- [Provenance nguồn](references/README.md): nguồn học phần/dự thảo/case study; bản chép private được loại khỏi repo public.
- [Source conversion](../tracking/evidence/source-conversion.json): hash và lịch sử chuyển đổi, không yêu cầu mở file nguồn để tiếp tục.
- [Skill shortlist và hướng dẫn agent](references/agent-skills.md): kết quả find-skills, nguồn web và cách dùng đúng phạm vi.

## Skills dự án và assets

- [Skill manifest](../.agents/skills/manifest.json): 6 skill đã cài project-local; 3 skill Figma chỉ lưu local, 3 skill còn lại kèm license trong Git. Không custom SaveBite skill.
- [Asset manifest](../assets/manifest.json): nguồn, giấy phép và phạm vi ảnh minh họa/nguồn tham khảo.
- [Figma read-back](../tracking/evidence/figma-readback.json): mapping thật của 5 pilot, components và interactions.

- [QA evidence](../tracking/evidence/qa.json): widths, font stress, contrast, hit targets, prototype clicks và các giới hạn chưa kiểm.
- [Access/tools evidence](../tracking/evidence/access-and-tools.json): student/Full account, write trial và skill discovery.
