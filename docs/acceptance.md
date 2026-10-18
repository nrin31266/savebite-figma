# Nghiệm thu thiết kế và đối chiếu học phần

Đối chiếu yêu cầu học phần ngày 19/10/2026. Đây là checklist cho nhóm, không phải chứng nhận đã hoàn thành. Repo chỉ thực hiện Figma và tài liệu thiết kế; phần code, presentation và portfolio cần nhóm theo dõi riêng.

## Hiện trạng theo tiêu chí

| Nhóm tiêu chí | Yêu cầu cần chứng minh | Hiện trạng / bước kiểm tiếp |
|---|---|---|
| UX/UI Process · 25% | Research 10%, phân tích 20 ứng dụng thật 10%, persona/journey 5% | Chưa có research/competitor matrix đã kiểm chứng. Proto-persona hiện tại là giả thuyết; cần nguồn, ngày và findings traceable. |
| Design Quality · 20% | Low-fi 5%, hi-fi UI 15%; tối thiểu 100 màn Figma | 5/100 DESIGN_REVIEW, 95 backlog, 0 DONE. Low-fi chưa được xác minh. Pilot không thay thế bài nộp hoàn chỉnh. |
| Prototype & Demo · 15% | Interaction 10%, video demo 5% | 9 hotspots của pilot đã bấm tiến/lùi. F-01 đầy đủ, video low-fi/hi-fi và demo Figma Mobile chưa hoàn thành. |
| Code Implementation · 15% | Số màn, độ khớp UI và cấu trúc code | Ngoài repo Figma. Đề bài có bất nhất Deliverables 50 / rubric 30; nhóm cần xác nhận giảng viên, không bỏ quên phần này khi tính hoàn thành học phần. |
| Presentation · 10% | Slide rõ và trình bày; cả 5 thành viên tham gia video | Ngoài phạm vi thực thi repo; dùng screenshots/evidence thật khi bàn giao. |
| Portfolio · 10% | Cấu trúc và câu chuyện quá trình thiết kế | Ngoài phạm vi thực thi repo; không kể kết quả research/usability chưa có. |
| Creativity & SDG Impact · 5% | Giải pháp có lý do, liên hệ giảm lãng phí có cơ sở | Định hướng Reserve & Pickup + Pantry đã có. Chưa có outcome/CO₂ đo thực; không tự gán số tác động. |

## Điều kiện nhận baseline pilot

- 5 SB-IDs có frame native editable trong đúng file, node/component mapping trùng registry.
- Giá 25.000đ, quantity=1, slot 17:00–18:00, merchant demo và dị ứng UNKNOWN khớp ở mọi bước; mã QR minh họa rõ.
- Nội dung và vùng chạm không bị cắt ở 360/390/430; text styles/tokens và component instances được giữ. QA không chỉ kiểm bounds của chữ.
- Toàn bộ CTA/back thuộc subset hoạt động; controls ngoài subset được ghi rõ là tĩnh. Subset chưa được gọi là F-01 end-to-end.
- Owner chấp nhận look-and-feel và usability của pilot. Trước đó baseline version/reviewed_by để trống, DONE=0.

## Khi mở rộng sau pilot

1. Hoàn thiện low-fi luồng chính và kiểm lại contracts, đặc biệt auth/return-to-offer, hết stock, hết giờ nhận và dị ứng. Ghi giả thuyết tách với findings thật.
2. Chia batch 5–8 màn theo flow/dependencies. Mỗi màn có nhiệm vụ/state riêng; overlay nhỏ, component variant và bản đổi màu không tính thành màn độc lập.
3. Reuse components/properties đã có. Nếu đổi main component, QA các màn sử dụng nó và ghi decision khi breaking.
4. Kiểm nhất quán giữa flows: 4 tabs, tên CTA, back/recovery, fixture, thông báo safety và cách trả tiền tại cửa hàng.
5. Trước nộp: inventory đủ 100 hi-fi thực chất, low-fi, prototype đầy đủ, video low-fi 1–3 phút/hi-fi 2–5 phút, demo điện thoại và sketches. Research/20 competitors/persona/journey phải có evidence phù hợp.

Mỗi tiêu chí báo **passed / failed / not checked**, kèm link evidence hoặc việc còn thiếu. Kiểm trên desktop không được thay cho thiết bị thật hoặc VoiceOver/TalkBack. QA thiết kế trong repo không chứng minh đã đạt toàn bộ điểm học phần.

## Bằng chứng hiện hành

- [Progress và blockers](../tracking/progress.md)
- [Screen registry](../tracking/screens.csv) · [Component registry](../tracking/components.csv)
- [Native read-back](../tracking/evidence/figma-readback.json) · [QA](../tracking/evidence/qa.json)
- [5 màn hiện hành](../tracking/evidence/pilot-overview.png) · [Component samples](../tracking/evidence/components.png)
