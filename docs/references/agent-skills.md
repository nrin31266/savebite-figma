# Skills và setup cho team

Rà ngày 19/10/2026 bằng `find-skills`: `npx --yes skills find figma` và `npx --yes skills find 'design critique'`. Đã đọc SKILL.md upstream và kiểm tra GitHub source/license. Bộ đã cài được dùng theo nhiệm vụ; metadata không chứng minh quyền tool trong phiên.

| Skill | Nguồn | Dùng cho SaveBite |
|---|---|---|
| `figma-use` | [Figma](https://skills.sh/figma/mcp-server-guide/figma-use) | Ưu tiên cho native read/write; chỉ dùng khi tool tương ứng có trong phiên |
| `figma-generate-library` | [Figma](https://skills.sh/figma/mcp-server-guide/figma-generate-library) | Tokens/components, đi cùng figma-use; không tự dựng cả library khi chỉ sửa một component |
| `figma-generate-design` | [Figma](https://skills.sh/figma/mcp-server-guide/figma-generate-design) | Ráp màn từ system hiện hữu, đi cùng figma-use |
| `design-critique` | [Anthropic](https://skills.sh/anthropics/knowledge-work-plugins/design-critique) | Đã cài để review hierarchy, flow và usability; nhận xét là đánh giá thiết kế, không thay nghiên cứu thật |
| `frontend-design` | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design), đã cài local | Giữ để review visual direction; nhiều ví dụ thiên web nên phải theo brief mobile |
| `ui-ux-pro-max` | [NextLevelBuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), đã cài local | Tra patterns/UX có chọn lọc; không tự sinh landing page hay đổi design-system canonical |

Bộ 6 skill hiện tại đủ cho task Figma: 3 skill canvas, 2 skill visual/UX và 1 skill critique. Chưa cần thêm code, Code Connect hoặc MCP trùng. Bộ ba Figma chỉ cài local vì upstream không khai báo license phân phối; manifest pin source/revision/hash. Design-critique giữ Apache-2.0 LICENSE, frontend-design và ui-ux-pro-max giữ license riêng.

## Giao việc rõ, không lặp toàn bộ spec

Task nên nêu: kết quả cần có → SB-IDs/node IDs → phần được thay đổi → fixture → kiểm tra nghiệm thu. Ví dụ: “Review copy SB-034 và SB-053 theo product.md; ghi điểm chưa rõ và đề xuất sửa; chưa sửa canvas. Kiểm giá/slot/allergens thống nhất.”

- Giữ luật bền vững trong AGENTS; domain requirements trong docs; trạng thái/nodes trong registry và progress. Đây là cách áp dụng [OpenAI Docs về AGENTS.md](https://developers.openai.com/codex/guides/agents-md/).
- Chỉ nạp skill khi task cần; [OpenAI Docs về skills](https://developers.openai.com/codex/skills/) mô tả cơ chế đọc metadata trước và nạp hướng dẫn khi sử dụng.
- [Figma write-to-canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/) xác nhận native nodes cần MCP/client hỗ trợ và quyền edit. Tài liệu hoặc evidence cũ không chứng minh phiên hiện tại có quyền.
- Trước sửa: đọc live + tìm/reuse. Sau sửa: read-back IDs + xem screenshot + kiểm click thuộc scope. Giới hạn batch theo yêu cầu, không tự tạo thêm màn để “hoàn thiện”. Đây là áp dụng [Figma library skill](https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-library/SKILL.md).
- Docs-only: kiểm nội dung/links/registry; không bắt buộc gọi Figma, không claim kiểm canvas. Task canvas bị thiếu tool thì ghi BLOCKED riêng phần canvas và tiếp tục phần docs độc lập.

## Máy teammate mới

Bản clone đã chứa frontend-design, ui-ux-pro-max và design-critique. Bộ ba Figma dùng plugin chính thức nếu đã được cung cấp. Nếu thiếu skill trong môi trường, cần Node/npm cho lệnh npx. Từ repo root chạy project-local; không dùng -g:

```sh
npx skills add https://github.com/figma/mcp-server-guide/tree/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5 --skill figma-use figma-generate-library figma-generate-design --agent codex --copy -y
python3 scripts/validate.py
```

Sau đó kiểm skill được discover, kết nối Figma trong đúng tài khoản và xác minh read/write trên file đích trước sửa canvas. Manifest pin source/hash; không cài thêm MCP trùng. Các placeholder design tool trong design-critique được hiểu là Figma; chưa có nguồn user feedback nối sẵn, không bịa dữ liệu này.

Lệnh khôi phục trên đã chạy thử trong thư mục trống: cài được đúng 3 SKILL.md vào .agents/skills, không ghi global. Reuse plugin chính thức khi môi trường đã cung cấp cùng skills; không nạp trùng bản plugin và bản local.
