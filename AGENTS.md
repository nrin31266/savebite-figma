# SaveBite agent rules

## Đọc và xác định phạm vi
- Repo chỉ làm Figma: UI/UX, tokens/components, prototype, docs và evidence. Không triển khai app/backend hoặc tự tạo deliverables code.
- Bắt đầu bằng `docs/README.md`, `tracking/progress.md`, rồi tài liệu domain và registry bị ảnh hưởng.
- Không cần tài liệu handoff bên ngoài repo để tiếp tục công việc. Dùng `docs/acceptance.md` để đối chiếu yêu cầu học phần; không nhầm pilot với bài nộp hoàn chỉnh.
- `docs/product.md` sở hữu nghiệp vụ; `docs/experience.md` sở hữu flow/màn.
- `docs/design-system.md` sở hữu tokens/components; `docs/workflow.md` sở hữu thực thi và QA.
- Registry giữ hiện trạng, không tự thay requirements. Figma live chứng minh node đang tồn tại.
- Giữ CONFIRMED, DEFAULT, FUTURE, REQUIRES-REAL-DATA và BLOCKED rõ ràng.
- Không bịa research, metrics, merchant, reviews, license, node IDs hoặc DONE.

## Trước khi sửa
- Đọc Git status và docs/fixtures liên quan trước khi sửa repo. Trước khi sửa canvas phải đọc Figma live; task chỉ sửa docs không cần thao tác canvas.
- Tôn trọng chỉnh sửa thủ công; không reset canvas, overwrite file hoặc xóa dữ liệu có sẵn.
- Dùng conflict protocol trong `docs/workflow.md`; ghi Open conflicts ở progress.
- Nghiệp vụ/safety/payment/navigation hoặc breaking design change cần quyết định được ghi log.
- Tiếp tục phần độc lập khi một nhánh bị chặn.

## Figma
- File đích duy nhất: `7suZz9C8oL5zV2NMxlsIVI` (`SaveBite-V2`); không tự chuyển file/team hoặc dùng lại file `NLTv70kDZ2i3HpOnOKQCDY` đã nghỉ hưu.
- Xác minh identity/team và read/write thật; nếu permission fail thì BLOCKED.
- Load figma-use trước use_figma; thêm generate-library/design cho components/screens.
- Tìm registry, canvas, variables/styles và libraries trước khi tạo; reuse trước.
- Một Figma writer mỗi vùng chung; lease ghi ở progress, giải phóng khi checkpoint.
- Không hai agent cùng sửa tokens/core components/registry/page/node.
- Native editable frames/text/instances, Auto Layout và tokens; không PNG toàn màn.
- Sau write: read-back IDs, screenshot, kiểm copy/contrast/layout/interactions.
- Khi partial mutation: reconcile ID thực trước retry; không tạo duplicate.
- IDs màn/components phải khớp registries. DONE chỉ sau QA và owner acceptance.
- Cập nhật registry và progress sau mỗi batch, không dùng chat history làm tracking.

## Repository và clients
- Branch theo `design/<module>-<scope>`, `docs/<scope>`, `fix/<scope>`.
- Commit nhỏ theo milestone; chỉ stage file thuộc task; không `git add .` khi có file lạ.
- Không reset hard, clean force, sửa lịch sử hoặc push nếu chưa được yêu cầu.
- Không commit secrets, tokens, .env thật, user config riêng tư hoặc asset không có quyền.
- `AGENTS.md` là canonical; `CLAUDE.md` symlink tương đối tới đây, không copy rules.
- Không tạo adapter client khác khi chưa dùng; không tạo custom SaveBite SKILL.md.
- Skills/MCP đã có thì reuse; skill mới cài project-local trong `.agents/skills/`, không global.
- Trước task UI đọc `.agents/skills/frontend-design/SKILL.md` và `ui-ux-pro-max/SKILL.md` khi phù hợp; source manifest đi kèm.
- Context7 dùng khi cần API/SDK phiên bản hoặc code, không bắt buộc cho canvas.
- Agent docs có thể làm worktree riêng; Figma không cô lập theo Git branch. Không tự mở nhiều agent nếu chưa được yêu cầu.
- Mọi lease phải có owner/scope và được giải phóng tại checkpoint.

## Checkpoint
- Chạy `python3 scripts/validate.py`, kiểm status, links, component mapping và evidence.
- Ghi rõ passed/failed/not checked; không claim prototype/mobile/usability chưa chạy.
- Giữ docs router hoạt động và cập nhật tài liệu domain + dependencies cùng thay đổi.
- Sau pilot: AWAITING_OWNER_REVIEW, không tự sản xuất 100 màn.
