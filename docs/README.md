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
