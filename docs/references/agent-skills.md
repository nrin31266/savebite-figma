# Skill shortlist và cách giao việc

Rà ngày 19/10/2026 bằng `find-skills`: `npx --yes skills find figma` và `npx --yes skills find 'design critique'`. Đã đọc SKILL.md upstream và kiểm tra GitHub source/license. Số installs/stars là snapshot, không chứng minh chất lượng hoặc quyền tool trong phiên.

| Ứng cử viên | Nguồn / installs | Đánh giá cho SaveBite |
|---|---|---|
| `figma-use` | [Figma](https://skills.sh/figma/mcp-server-guide/figma-use), 8.6K | Ưu tiên cho native read/write; chỉ dùng khi tool tương ứng có trong phiên |
| `figma-generate-library` | [Figma](https://skills.sh/figma/mcp-server-guide/figma-generate-library), 4.2K | Tokens/components, đi cùng figma-use; không tự dựng cả library khi chỉ sửa một component |
| `figma-generate-design` | [Figma](https://skills.sh/figma/mcp-server-guide/figma-generate-design), 5.7K | Ráp màn từ system hiện hữu, đi cùng figma-use |
| `design-critique` | [Anthropic](https://skills.sh/anthropics/knowledge-work-plugins/design-critique), 5.1K | Ứng cử viên bổ sung khi cần review hierarchy, flow và usability; nhận xét là đánh giá thiết kế, không thay nghiên cứu thật |
| `frontend-design` | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design), đã cài local | Giữ để review visual direction; nhiều ví dụ thiên web nên phải theo brief mobile |
| `ui-ux-pro-max` | [NextLevelBuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), đã cài local | Tra patterns/UX có chọn lọc; không tự sinh landing page hay đổi design-system canonical |

GitHub snapshot: Figma guide 2,086 stars; Anthropic knowledge-work-plugins 30,134; Anthropic skills 181,960; UI/UX Pro Max 137,175. Hai skill local có license riêng Apache-2.0 và MIT trong thư mục tương ứng. GitHub API không khai báo license cấp repo cho Figma guide; ưu tiên reuse qua plugin chính thức, không suy diễn quyền sao chép cả repo.

Đề xuất: bộ ba Figma phục vụ canvas, hai skill local dùng có chọn lọc; design-critique dùng khi có task review. Theo yêu cầu owner đã cài thêm 4 skill: bộ ba Figma và design-critique, tất cả project-local. Bộ ba Figma được ignore khỏi Git public vì chưa có license phân phối cấp repo; manifest vẫn pin source/revision/hash. Bản clone public có thể cài chúng bằng official installer với --dest .agents/skills. design-critique giữ kèm Apache-2.0 LICENSE. Nếu cài, destination là `.agents/skills/`, pin source/revision/hash vào manifest; không dùng `-g`. Không chọn implement-design, Code Connect, React/Expo hoặc browser automation chỉ vì installs cao.

Lệnh tương đương để cài skill review trên một bản clone mới:

```sh
npx skills add anthropics/knowledge-work-plugins --skill design-critique
```

## Giao việc rõ, không lặp toàn bộ spec

Task nên nêu: kết quả cần có → SB-IDs/node IDs → phần được thay đổi → fixture → kiểm tra nghiệm thu. Ví dụ: “Review copy SB-034 và SB-053 theo product.md; ghi điểm chưa rõ và đề xuất sửa; chưa sửa canvas. Kiểm giá/slot/allergens thống nhất.”

- Giữ luật bền vững trong AGENTS; domain requirements trong docs; trạng thái/nodes trong registry và progress. Đây là cách áp dụng [OpenAI Docs về AGENTS.md](https://developers.openai.com/codex/guides/agents-md/).
- Chỉ nạp skill khi task cần; [OpenAI Docs về skills](https://developers.openai.com/codex/skills/) mô tả cơ chế đọc metadata trước và nạp hướng dẫn khi sử dụng.
- [Figma write-to-canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/) xác nhận native nodes cần MCP/client hỗ trợ và quyền edit. Tài liệu hoặc evidence cũ không chứng minh phiên hiện tại có quyền.
- Trước sửa: đọc live + tìm/reuse. Sau sửa: read-back IDs + xem screenshot + kiểm click thuộc scope. Giới hạn batch theo yêu cầu, không tự tạo thêm màn để “hoàn thiện”. Đây là áp dụng [Figma library skill](https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-library/SKILL.md).
- Docs-only: kiểm nội dung/links/registry; không bắt buộc gọi Figma, không claim kiểm canvas. Task canvas bị thiếu tool thì ghi BLOCKED riêng phần canvas và tiếp tục phần docs độc lập.
