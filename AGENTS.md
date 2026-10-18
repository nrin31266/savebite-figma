# SaveBite agent rules

## Đọc và xác định phạm vi
- Bắt đầu bằng `docs/README.md`, `tracking/progress.md`, rồi tài liệu domain và registry bị ảnh hưởng.
- Không cần tài liệu handoff bên ngoài repo để tiếp tục công việc.
- `docs/product.md` sở hữu nghiệp vụ; `docs/experience.md` sở hữu flow/màn.
- `docs/design-system.md` sở hữu tokens/components; `docs/workflow.md` sở hữu thực thi và QA.
- Registry giữ hiện trạng, không tự thay requirements. Figma live chứng minh node đang tồn tại.
- Giữ CONFIRMED, DEFAULT, FUTURE, REQUIRES-REAL-DATA và BLOCKED rõ ràng.
- Không bịa research, metrics, merchant, reviews, license, node IDs hoặc DONE.

## Trước khi sửa
- Đọc Git status, những caller/docs/fixtures liên quan và Figma live trước khi mutation.
- Tôn trọng chỉnh sửa thủ công; không reset canvas, overwrite file hoặc xóa dữ liệu có sẵn.
- Dùng conflict protocol trong `docs/workflow.md`; ghi Open conflicts ở progress.
- Nghiệp vụ/safety/payment/navigation hoặc breaking design change cần quyết định được ghi log.
- Tiếp tục phần độc lập khi một nhánh bị chặn.

## Figma
- File đích duy nhất: `NLTv70kDZ2i3HpOnOKQCDY`; không tự chuyển file/team.
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
- Skills/MCP đã có thì reuse; chỉ cài phần thiếu có nguồn xác minh và nhu cầu thật.
- Context7 dùng khi cần API/SDK phiên bản hoặc code, không bắt buộc cho canvas.
- Agent docs/code có thể làm worktree riêng; Figma không cô lập theo Git branch.
- Mọi lease phải có owner/scope và được giải phóng tại checkpoint.

## Checkpoint
- Chạy `python3 scripts/validate.py`, kiểm status, links, component mapping và evidence.
- Ghi rõ passed/failed/not checked; không claim prototype/mobile/usability chưa chạy.
- Giữ docs router hoạt động và cập nhật tài liệu domain + dependencies cùng thay đổi.
- Sau pilot: AWAITING_OWNER_REVIEW, không tự sản xuất 100 màn.
