# Progress · 19/10/2026

Gate: **AWAITING_OWNER_REVIEW** · Batch **B-PILOT-005** · Pilot **v0.5**. DESIGN_REVIEW 5/100, BACKLOG 95/100, DONE 0/100. Baseline và owner acceptance chưa có.

## Phạm vi và quyền

- Repo chỉ làm Figma, UX/UI, design system, prototype và docs/evidence liên quan. [Bắt đầu cho teammate](../docs/README.md) · [Tiêu chí học phần](../docs/acceptance.md). Không cần file nguồn ngoài repo hoặc chat history để tiếp tục.
- File duy nhất: [SaveBite](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=2-2). RIN student/Full/admin đã xác minh lại; native write/read thành công. Page 1 giữ nguyên.
- Lease **RELEASED**: Codex / pilot 2:2, Components 27:87, Foundations 4:48, registry/docs/evidence / checkpoint B-PILOT-005. Một writer, không subagent.

## Thiết kế hiện hành

| Màn | Root Figma | Screenshot |
|---|---|---|
| SB-015 · Khám phá | [28:2](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-2) | [PNG](evidence/SB-015.png) |
| SB-034 · Chi tiết | [28:80](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-80) | [PNG](evidence/SB-034.png) |
| SB-051 · Giờ nhận | [28:118](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-118) | [PNG](evidence/SB-051.png) |
| SB-053 · Tóm tắt | [28:167](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-167) | [PNG](evidence/SB-053.png) |
| SB-056 · Thành công | [28:215](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?node-id=28-215) | [PNG](evidence/SB-056.png) |

- Giữ 5 root IDs; native editable và Auto Layout. [Overview](evidence/pilot-overview.png), [component samples](evidence/components.png), [Foundations v0.5](evidence/foundations.png).
- 40 variables, 11 text styles, 2 effect styles, **21 mains / 3 variant sets / 31 screen instances**; SHARED 21, STABLE 0. Progress hai bước và AllergenNotice dùng chung; Button có Disabled/Loading; properties giúp đổi nội dung không detach. Mapping trong [components.csv](components.csv).
- Fixture xuyên luồng: 1 phần bánh mì 25.000đ, nhận 17:00–18:00, merchant demo, dị ứng UNKNOWN. Đơn/mã mô phỏng; không giữ stock hoặc thu tiền thật. Search/filter/category/favourite/notification/tabs và offer phụ vẫn tĩnh.

## QA checkpoint

- **PASS** native read-back: đúng file/root IDs, 390×844, Be Vietnam Pro, text styles bound, 31 instances, 9 destinations hợp lệ, 0 UI bounds overflow. [Read-back](evidence/figma-readback.json).
- **PASS** resize 360 và 430, kiểm mọi visible child bounds + xem hình; đã restore 390. [360](evidence/pilot-360.png) · [430](evidence/pilot-430.png). Sửa floating photo controls bám responsive và category tiles chia đều ở 360.
- **PASS** font stress 125% trên 13 text nodes SB-034: đọc được giá/copy, đã restore styles. [PNG](evidence/SB-034-font125.png). Không phải Dynamic Type trên thiết bị.
- **PASS** 13 cặp chữ/nền thực dùng ≥4.5:1, thấp nhất 4.74; 9 connected hotspots ≥48×48. Selected slot 17:00–18:00 và Expired 15:00–16:00 đã assert riêng sau sửa shared default.
- **PASS** [prototype](https://www.figma.com/proto/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?page-id=2%3A2&node-id=28-2&starting-point-node-id=28%3A2&scaling=scale-down): bấm thật qua 5 màn về Khám phá và cả 4 đường Back, kiểm URL sau từng chuyển màn. Đây vẫn là subset, chưa F-01 đầy đủ.
- [QA và hashes](evidence/qa.json). `qa_result=PASS_WITH_LIMITS`, `a11y_checked=false`; không QA_PASS/DONE khi thiếu owner/device/assistive technology review.

## Context và skills cho team

- Docs router có thứ tự đọc, domain ownership và acceptance matrix; bỏ phụ thuộc vào tên file nguồn vắng mặt. Logs bootstrap/conversion/môi trường giữ private, không làm context bắt buộc. Registry và evidence thiết kế vẫn public.
- Đã dùng design-critique, frontend-design, ui-ux-pro-max và bộ ba Figma. 6 skills đủ cho scope; plugin chính thức ưu tiên khi có. [Setup teammate](../docs/references/agent-skills.md) có lệnh khôi phục 3 skill local-only, đã kiểm trên thư mục trống; nguồn/hash trong manifest.
- Figma connector đã xác minh identity/team và native write/read trong phiên này. Cấu hình máy/backup giữ ngoài repo.

## Open conflicts / chưa kiểm

1. Owner review v0.5: v0.4 đã bị từ chối về thẩm mỹ; chưa mở batch 95 màn còn lại.
2. Chưa có research/usability thật, competitor matrix 20 apps được xác minh, low-fi đầy đủ hoặc toàn bộ state matrix. Không claim đã đạt phần UX process của học phần.
3. Chưa Figma Mobile/thiết bị thật, VoiceOver/TalkBack/keyboard; cần bằng chứng trước claim các mục đó.
4. Production food-safety/merchant policy và backend nằm ngoài demo Figma; không claim an toàn hoặc giao dịch thực.

## Checkpoint tiếp theo

- Branch: design/reference-art-direction. Validator và whitespace PASS; registry/evidence trùng v0.5. Repo public vẫn giữ logs máy/nguồn private ở ngoài. SHA đọc bằng git log.
- Tiếp theo: owner review pilot, rồi hoàn thiện low-fi/contracts và chia batch theo flow trong acceptance.md. Không tự tạo 100 màn.

## B-PILOT-005 · Kết quả chỉnh visual theo reference

- Owner từ chối v0.4; DEC-010 ghi nhận yêu cầu và hướng mới. V0.5 có wordmark/leaf, banner xanh cạnh ảnh, category tile, card 2 cột, ảnh detail lớn + sheet kem, receipt và pickup ticket. 5 màn vẫn native editable; không dán reference thành ảnh UI.
- BreadPhoto dùng ảnh bánh mì AI sáng/ấm và CroissantPhoto dùng Pexels, có manifest/provenance. Không đưa 5 ảnh reference của owner vào public repo; không sao chép rating/discount/merchant/safety claims từ ảnh.
- Lease **RELEASED** tại checkpoint: Codex / pilot, Components, Foundations, registry/docs/evidence. Không có writer khác hoặc subagent.
- Bước tiếp theo là owner đánh giá thẩm mỹ v0.5; research, low-fi đầy đủ, mobile và usability vẫn chưa được kiểm. Base này không tự chứng minh đã đạt toàn bộ học phần.
