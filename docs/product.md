# Sản phẩm, chính sách và nguồn

Nguồn chuẩn theo domain; đọc [router](README.md) và [tiến độ](../tracking/progress.md) trước khi thay đổi.

## NGUỒN GỐC, YÊU CẦU MÔN HỌC VÀ TÍNH TRUNG THỰC

### Nguồn và phạm vi hiện hành

`CONFIRMED` Theo DEC-006, repo chỉ thực hiện thiết kế Figma, prototype và docs/evidence liên quan. Các yêu cầu code, portfolio, slide/video nhóm của học phần là bối cảnh ngoài phạm vi thực thi repo; không tự khởi tạo app hoặc coi code là gate của thiết kế.

[Provenance nguồn](references/README.md) giữ tên/hash và giới hạn sử dụng. Bản chép nguồn đầy đủ được lưu private ngoài repo; tiếp tục công việc bằng docs domain hiện hành.

| Source | Dùng để quyết định | Giới hạn |
|---|---|---|
| `GROUP ASSIGNMENT-UXUI.pdf` | Deliverables, rubric, 100 hi-fi Figma screens, low-fi, prototype, videos, mobile demo, code | Có chỗ không nhất quán giữa mục bàn giao và rubric số màn code |
| `Nội dung slide chính.docx` | Tuyên ngôn sản phẩm, Rescue Market + Smart Pantry, luồng và pain points giả thuyết, hướng case study | Đoạn nghiên cứu, quote, impact, usability findings vẫn có chỗ là *đề xuất/chỗ điền* |
| `Case study slide deck - Zia's Pizza.pdf` | Cách trình bày research, wireframes, before/after, reflection | Không chép tính năng hoặc số liệu từ sản phẩm khác |
| Hội thoại chốt SaveBite | Hệ màu trầm, trình bày bằng tiếng Việt, assets thật, tránh tạo mặt người giả, ưu tiên agent tự quản lý và reusable components | Các bản slide AI tạo trước đây là **visual references**, không phải màn app đã hoàn thiện |
| Figma đích trong docs/workflow.md | Nơi lưu thiết kế | Quyền hiện hành trong tracking/progress.md; không tự tạo file thay thế |

### Đầu ra thiết kế và bối cảnh học phần

- `CONFIRMED` Ít nhất **100 hi-fi Figma frames** thực chất, có ít nhất **1 end-to-end prototype flow**.
- `CONFIRMED` Low-fi wireframes và prototype riêng về giai đoạn thiết kế (không tính nhầm low-fi vào 100 hi-fi).
- `CONFIRMED` Video low-fi khoảng 1–3 phút; video high-fi khoảng 2–5 phút; demo trên Figma Mobile.
- `CONFIRMED — ngoài phạm vi repo` Portfolio PDF/website case study, presentation và video nhóm là yêu cầu học phần; không tự sản xuất trong task Figma.
- `CONFIRMED` Phân tích ít nhất **20 ứng dụng thật**, với nguồn và ngày truy cập; không sử dụng logo đối thủ AI tự tưởng tượng.
- `CONFIRMED — ngoài phạm vi repo` Đề bài nhắc **50 màn code** ở Deliverables và **30** ở rubric/Notes. Giữ bất nhất B-COURSE-01 cho nhóm hỏi giảng viên; đây không phải backlog hoặc gate Figma.
- `CONFIRMED` Sketch ban đầu; accessibility và reflection có bằng chứng cụ thể.

**Phân biệt:** `100 Figma frames` ≠ `50 routed code screens` ≠ `23 slide thuyết trình`. Ba nhóm này có registry/tiêu chí đếm khác nhau. Mục tiêu thực tế là ít nhất 100 hi-fi frames, nhưng **đừng “đánh bóng số lượng”**.

### Đội thực hiện

1. Lê Duy Đạt
2. Lê Văn Quân
3. Đặng Ngọc Tân
4. Nguyễn Văn Rin
5. Huỳnh Thanh Thuận

Không đặt giả tên giảng viên, email, thông tin liên hệ, thống kê nhân khẩu học hoặc số liệu khảo sát.

### Bằng chứng và provenance

Cần lưu cho từng phát biểu trong portfolio: `statement`, `source_type`, `source_url/file`, `collected_at`, `verified_by`, `confidence`, `usage`. Research quote phải có mã participant ẩn danh và consent phù hợp. Bảng số liệu phải có raw data hoặc tổng hợp có thể kiểm tra. Các hình UX thử nghiệm do agent dựng minh họa phải ghi `Concept / Demo UI` trong docs/review, **không mạo nhận screenshot app vận hành thực**.

---

## PRODUCT FOUNDATION — SAVEBITE LÀ SẢN PHẨM GÌ?

### One-liner

**SaveBite** là ứng dụng di động kết nối người tiêu dùng, đặc biệt là sinh viên và người trẻ, với thực phẩm **còn phù hợp sử dụng** đang có nguy cơ không được tiêu thụ kịp thời tại cửa hàng, giúp họ tìm — hiểu — đặt trước — đến nhận với mức giá hợp lý. **Smart Pantry** hỗ trợ theo dõi thực phẩm cá nhân để giảm quên hạn và bỏ phí tại nhà.

**Lời hứa sản phẩm:** Cứu thực phẩm. Tiết kiệm chi phí. Giảm lãng phí.  
**Giá trị trực tiếp cho người dùng:** giá dễ hiểu, gần, kịp thời gian, minh bạch, ít thao tác.  
**Giá trị rộng hơn:** tạo thêm cơ hội tiêu thụ thực phẩm còn dùng tốt và góp phần giảm lãng phí.

### Phạm vi giải pháp

- `CONFIRMED` **Rescue Market là core** (ưu tiên 70–80% UX/navigation effort): người dùng khám phá và giữ chỗ ở cửa hàng; không biến thành ứng dụng giao thức ăn thông thường.
- `CONFIRMED` **Smart Pantry là complementary**: quản lý hạn thực phẩm cá nhân trong cùng app, không tách app thứ hai.
- `DEFAULT` 100 hi-fi frames trong đồ án là **consumer-facing mobile app**, bao gồm những trạng thái nghiệp vụ cần thiết. **Merchant dashboard là FUTURE, không cộng giả vào 100 hi-fi frames**. Fixture phải biểu diễn merchant rõ ràng, không yêu cầu xây hệ thống dữ liệu hoặc merchant module.
- `FUTURE` merchant portal/app: tạo offer, quản lý tồn kho, hạn, khung nhận, xác nhận pickup, báo cáo, kiểm duyệt.
- `FUTURE` nghiệp vụ giao hàng, payment gateway, barcode scan Pantry, phê duyệt merchant qua giấy tờ, chương trình loyalty lớn, recommender AI.

### Mô hình người dùng

| Actor | Phạm vi | Quyền tối thiểu |
|---|---|---|
| Guest | Consumer app | xem feed, tìm kiếm, filter, xem chi tiết, chọn khu vực thủ công; có thể thử Pantry local nếu chưa login |
| Customer | Consumer app | lưu ưu đãi, đặt giữ chỗ, nhận code, lịch sử đơn, Pantry, thông báo, settings |
| Merchant staff | Future merchant console | quản lý offer/stock và xác nhận nhận món, không truy cập dữ liệu Pantry cá nhân |
| Merchant owner | Future merchant console | quản lý nhân viên, cửa hàng, báo cáo |
| Platform admin | Future moderation | quản trị merchant, báo cáo vi phạm, policy; không tự xem thông tin riêng tư không cần thiết |

**Persona hiện tại** (ví dụ Minh Anh, 21 tuổi) là **proto-persona để định hướng**, không được gọi là persona được khảo sát chứng thực nếu không có interview.

### Định vị không phải những gì

Không định vị là dịch vụ giao đồ ăn; không hứa mọi mặt hàng “an toàn tuyệt đối”; không bán hàng quá hạn sử dụng; không chỉ là ứng dụng giảm giá; không giả định chỉ có sinh viên dùng; không mô tả tất cả nhà hàng là đối tác đã ký kết; không coi SDG impact là số đo thật khi chưa có tracking chính xác.

---

## NHỮNG QUYẾT ĐỊNH MVP ĐÃ KHÓA TRONG SPEC (DEFAULTS)

| ID | Quyết định đủ rõ để thiết kế | Vì sao | Ghi chú khi production |
|---|---|---|---|
| D-001 | Mobile consumer-first, tiếng Việt, UI light mode | Đúng ngữ cảnh học phần và target students | Responsive/language extension về sau |
| D-002 | Bottom navigation **Khám phá / Đơn của tôi / Tủ thực phẩm / Tài khoản** (4 tabs) | Tách đúng 4 nhiệm vụ, tránh trùng tab | Yêu thích từ header/cá nhân, không tab riêng |
| D-003 | **Guest có thể khám phá**, chỉ cần đăng nhập khi đặt giữ chỗ | Giảm friction | Có return-to-offer sau login |
| D-004 | **Reserve & Pickup, không giao hàng** | Food rescue time-sensitive, giảm operational scope | Địa điểm và pickup slot là bắt buộc |
| D-005 | **MVP không charge online**; thanh toán trực tiếp tại cửa hàng nếu cửa hàng yêu cầu, hiển thị rõ | Tránh payment/refund phức tạp mà vẫn demo luồng đặt hàng | Có payment capability trong roadmap; số tiền thanh toán ở quầy theo merchant policy |
| D-006 | Không biến giỏ hàng thành multi-merchant basket: **mỗi reservation thuộc một merchant và một offer** trong MVP | Giảm vấn đề stock, pickup, vận chuyển và checkout | Có quantity cho offer, không ghép nhiều merchant |
| D-007 | Customer thấy ảnh, mô tả, giá gốc tham chiếu (nếu merchant có căn cứ), giá rescue, số lượng còn, thời gian/địa điểm nhận, thành phần và allergens (nếu được cung cấp) | Trust before action | Không tự suy luận dị ứng từ ảnh |
| D-008 | Offer theo hai dạng: món cụ thể hoặc `surprise bag`; phải nêu rõ không bảo đảm chính xác món trong surprise bag | Cân bằng nhu cầu merchant và minh bạch | Với dị ứng nghiêm trọng, khuyến cáo không chọn khi không xác nhận thành phần |
| D-009 | Merchant là bên chịu trách nhiệm mô tả và tuân thủ quy định an toàn thực phẩm; platform hiển thị nguồn và policy rõ | Không đưa khẳng định y tế/food safety vượt dữ liệu | Cần legal/policy review trước real launch |
| D-010 | Đặt chỗ thành công chỉ khi hệ thống đã giữ số lượng trên server; không có offline-confirmed reservation | Tránh overselling | Thiết kế idempotency và atomic stock |
| D-011 | Nhận món bằng QR + code chữ/số dự phòng; merchant xác thực, không khách tự tick là đã nhận | Tạo điểm chốt trạng thái tin cậy | Mã ngắn sống theo đơn, tránh lộ public |
| D-012 | Đơn đã đặt có thể hủy trước khi pickup window bắt đầu theo demo policy | Giảm no-show; rõ ràng | Phải cấu hình merchant và hiển thị cutoff thực tế khi production |
| D-013 | Thông báo nhắc trước pickup và khi gần hết giờ; quyền push không bắt buộc | Giảm missed pickup | In-app notifications fallback |
| D-014 | Pantry là **local-first**, nhập thủ công; không tự scan barcode hoặc tự tạo món bằng AI ở MVP | Giảm lỗi dữ liệu và phụ thuộc | Đồng bộ tùy chọn sau login là FUTURE |
| D-015 | Phân biệt `hạn sử dụng` và `nên dùng trước`; item quá hạn sử dụng không được khuyến nghị ăn | An toàn và trung thực | Nguồn hạn do người dùng nhập |
| D-016 | Impact chỉ ghi **rescue đã xác nhận nhận** và **tiết kiệm ước tính có căn cứ**; không ước tính CO₂ tùy tiện | Không thổi phồng SDG | Cần methodology cho CO₂ ở future |
| D-017 | Location optional; chọn thành phố/khu vực/campus thủ công nếu không có GPS | Usability + quyền riêng tư | Radius hiển thị theo tọa độ được phép sử dụng |
| D-018 | Favorites không phải reservation, không giữ hàng | Tránh hiểu nhầm | Favorites có thể hết hàng |
| D-019 | Reviews chỉ từ đơn đã nhận được xác nhận | Trust | Moderation/report ở future |
| D-020 | Mỗi luồng phải có loading/empty/error/success/expired/permission fallback phù hợp, **không phải cứ thêm state là được tính là một màn riêng** | 100 màn chất lượng, không độn số | Mỗi frame đếm được phải có nhiệm vụ hoặc trạng thái toàn màn có ý nghĩa |

**Đã giải quyết mâu thuẫn chính:** `Nội dung slide chính.docx` đôi lúc mô tả checkout/pay trong app. Đối với **MVP của đồ án**, `Checkout` được hiểu là **Reservation Summary → Place Reservation → Confirmation**, không khẳng định có cổng thanh toán hoạt động. Luồng thanh toán online nằm ở FUTURE, và mọi mockup cũ ghi “Payment Success” phải đổi thành trạng thái giữ chỗ/đến nhận chính xác nếu không có payment gateway.

---

## JOBS-TO-BE-DONE, SUCCESS CRITERIA VÀ NGHIÊN CỨU

### Primary JTBD

> Khi tan học, ngân sách bữa tối có giới hạn và còn ít thời gian, tôi muốn biết ngay món nào còn tốt, gần mình, giá thực phải trả và lúc nào nhận được, để quyết định nhanh và không sợ đặt xong mới biết không đến kịp.

### Secondary JTBD

> Khi mua nhiều thực phẩm về nhà, tôi muốn nhìn thấy món nào sắp hết hạn và nhận nhắc nhở đúng lúc để ưu tiên sử dụng hoặc điều chỉnh kế hoạch ăn uống.

### Product experience goals

1. **Discoverability:** tìm món theo khu vực, giá, loại món và pickup window mà không cần login trước.
2. **Trust:** thông tin món, giới hạn dữ liệu, nguồn merchant, allergens và pickup hiện diện trước CTA.
3. **Speed:** ít bước nhưng không giấu điều kiện; trở lại đúng vị trí sau lỗi và đăng nhập.
4. **Predictability:** số lượng, trạng thái đặt/nhận và thời điểm hết hạn phải giải thích được.
5. **Waste awareness:** cho người dùng thấy lợi ích được xác nhận mà không greenwash.
6. **Accessibility:** người dùng nhìn/đọc/chạm hiểu được mọi trạng thái, không dựa màu đơn lẻ.

### Research cần thu thập (không bịa)

- Khảo sát dự kiến 50–100 người dùng trẻ/sinh viên, và phỏng vấn 6–8 người (đây là kế hoạch, không phải kết quả).
- Nếu tiếp cận được, 3–5 người bán/nhân viên cửa hàng để kiểm chứng giờ nhận, tồn kho, chất lượng, trách nhiệm và no-show.
- 20 đối thủ thực từ tài liệu; audit từng app với screenshot có nguồn: pricing, transparency, map, pickup, cancellation, allergens, accessibility, loyalty, pantry.
- Usability tasks: tìm món dưới 50k, tìm pickup sau giờ học, xác minh thành phần, giữ chỗ thành công, tìm mã nhận, hủy đơn, thêm món vào Pantry và nhận nhắc hạn.
- Dữ liệu thực ghi ẩn danh, có ngày, ngữ cảnh, task success/misclick và note; không tạo testimonial giả.

### Product metrics (định nghĩa trước, không gán kết quả)

- `offer_discovery_to_detail_rate` = lượt mở detail / lượt offer impression hợp lệ.
- `reservation_completion_rate` = reservation confirmed / lượt bắt đầu tóm tắt đặt trước (phân biệt no stock, policy fail).
- `pickup_completion_rate` = verified pickups / confirmed reservations đến hạn.
- `no_show_rate` = đơn hết giờ không nhận / confirmed reservations đủ điều kiện.
- `median_time_to_find_offer` và `task_success_rate` từ usability test, không phải số liệu production.
- `pantry_expiry_reminder_engagement` và `items_marked_used` chỉ khi có event và consent thích hợp.
- `estimated_money_saved`: chỉ từ đơn đã nhận, chênh giữa giá gốc hợp lệ và giá thực trả; nếu không có giá gốc đáng tin cậy, hiển thị số lần cứu thực phẩm chứ không bịa tiền tiết kiệm.

---

## BUSINESS RULES, DATA VALIDATION VÀ TRẠNG THÁI THỰC

### Offer data contract (logical, không ép backend schema cụ thể)

`Offer` tối thiểu: `id`, `merchantId`, `title`, `offerType` (`EXACT_ITEM`/`SURPRISE_BAG`), `category`, `description`, `imageAssets`, `currency=VND`, `rescuePrice`, `originalPrice?`, `originalPriceEvidence?`, `quantityAvailable`, `maxQtyPerReservation`, `pickupWindows[]`, `location`, `ingredientsStatus`, `ingredients?`, `allergensStatus`, `allergens?`, `storageInstructions?`, `qualityDisclosure`, `merchantVerificationStatus`, `createdAt`, `updatedAt`, `status`, `version`.

- `originalPrice` optional; **nếu thiếu evidence không show phần trăm discount**. Giá giảm không được suy từ ảnh.
- `allergensStatus`: `DECLARED` / `UNKNOWN` / `NOT_APPLICABLE` (nếu thực sự có cơ sở). Không tự biến `UNKNOWN` thành “không có dị ứng”.
- `quantityAvailable` chỉ hiển thị nếu backend trả số đáng tin; khi pending, hiển thị status và CTA phải có guard.
- `pickupWindows` dùng time zone định nghĩa rõ, giờ bắt đầu phải trước giờ kết thúc; không hiển thị giờ đã qua như available.
- `status`: `DRAFT`, `SCHEDULED`, `ACTIVE`, `SOLD_OUT`, `CLOSED`, `CANCELLED`, `EXPIRED`; frontend render theo transitions hợp lệ.
- Thời điểm `use-by`/safety do merchant khai báo và chịu trách nhiệm pháp lý; không đưa thực phẩm quá hạn dùng vào marketplace.

### Reservation contract

`Reservation`: `id`, `userId`, `offerId`, `merchantId`, `quantity`, `unitPriceSnapshot`, `totalDueAtPickup`, `pickupWindowId`, `pickupCodeId`, `state`, `stockHoldVersion`, `createdAt`, `confirmedAt?`, `pickedUpAt?`, `cancelledAt?`, `expiresAt?`, `updatedAt`, `idempotencyKey`.

`RESERVATION_STATE_MACHINE`:

`DRAFT → SUBMITTING → CONFIRMED → READY?(optional) → PICKED_UP → COMPLETED`  
`SUBMITTING → FAILED/OUT_OF_STOCK → recover`  
`CONFIRMED → CANCELLED` (theo cutoff)  
`CONFIRMED/READY → EXPIRED_NO_SHOW` (khi pickup quá hạn theo policy)  
`PICKED_UP → COMPLETED` bằng xác nhận merchant, không bằng click của customer.

**Invariant:** chưa có server confirmation thì không tạo code nhận món hợp lệ và không giảm `quantityAvailable` local như thể giao dịch thật. Server phải kiểm soát concurrency/atomic stock; retry có idempotency key để không giữ hàng đôi. Prototype được phép mô phỏng state nhưng mô tả rõ simulated trong kiểm thử.

### Price & cancellation policy

- `unitPrice` và `quantity` snapshot tại xác nhận; nếu offer đổi giá trước confirm, show warning và yêu cầu người dùng xác nhận giá mới.
- Payment: `PAY_AT_PICKUP` là lựa chọn MVP. Không hiển thị fake receipt “đã thanh toán”; reservation success chỉ xác nhận giữ chỗ.
- `Cancel`: mặc định trước pickup window bắt đầu; sau đó đưa hướng dẫn liên hệ/support. Production cần chính sách merchant rõ và khả năng audit.
- Không nêu “đã tiết kiệm X” cho đơn bị hủy/no-show; sau completion mới ghi impact.

### Pickup verification

- QR được coi là dạng trình bày `pickupCode`, không chứa dữ liệu nhạy cảm công khai; code có khả năng revoke khi hủy/hết hạn.
- Customer mở được QR offline **nếu mã đã cache hợp lệ** nhưng trạng thái xác nhận vẫn phụ thuộc merchant/server; UI phải tránh tuyên bố pickup thành công offline.
- Mã dự phòng dưới dạng text có thể đọc/chia sẻ với merchant trong lúc nhận, không dùng QR duy nhất.
- Có hướng dẫn khi cửa hàng đóng cửa sớm, không tìm thấy địa chỉ, mã không quét được, thức ăn khác mô tả, lo ngại chất lượng.

### Pantry model

`PantryItem`: `localId`, `name`, `category`, `quantity`, `unit`, `dateAdded`, `expiryDate?`, `dateType` (`USE_BY`/`BEST_BEFORE`/`UNKNOWN`), `storageLocation?`, `reminderOffsetDays`, `notes?`, `status` (`AVAILABLE`/`PARTLY_USED`/`CONSUMED`/`DISPOSED`), `lastUpdatedAt`.

- Thiết kế MVP: offline/local-first, nhập thủ công; không cần ảnh camera/scan barcode.
- Khi `expiryDate` thiếu, không suy đoán, hiển thị “Chưa có ngày hạn”.
- Khi `USE_BY` đã qua ngày, chỉ hướng dẫn xử lý an toàn và kiểm tra nhãn nhà sản xuất; **không khuyến nghị sử dụng thực phẩm đã quá hạn dùng**.
- Khi `BEST_BEFORE` đã qua, UI cần dùng ngôn ngữ thận trọng và không quyết định thay người dùng về an toàn.
- Reminder scheduling: timezone đúng, tôn trọng quyền permission và user preferences; không spam push, có clear/dismiss, hủy notification khi consumed/disposed.
- “Gợi ý dùng” chỉ dựa trên item có sẵn theo quy tắc đơn giản và safety checks; không cần gọi LLM.

### Privacy, security và compliance nền tảng

- Chỉ xin GPS khi có lý do trong flow; cho phép chọn khu vực thủ công.
- Đơn có địa điểm nhận công khai của merchant; vị trí chính xác của khách không công khai cho merchant ngoài phạm vi cần thiết.
- Không upload hình Pantry cá nhân/biểu đồ tiêu dùng cá nhân vô căn cứ.
- Không đưa mật khẩu, token, khóa MCP/API vào Git, screenshots hoặc prompt; `.env` private + example chỉ với placeholders.
- Xóa account/data và export pantry có hành vi/mô tả rõ; các khẳng định retention/legal sẽ quyết định khi chọn backend và điều kiện triển khai thực.
- Không fake nhãn “đã xác minh”, đánh giá 5 sao và thương hiệu/địa chỉ thật trong production; demo fixtures phải tách và kiểm soát.
- Trước public launch, làm legal/food safety review theo thị trường mục tiêu; tài liệu này không phải tư vấn pháp lý.

---

## CONTENT, DEMO DATA VÀ ASSET PROVENANCE

### Fixture policy

Có thể dùng dữ liệu ví dụ cho prototype để trình diễn, **nhưng không được nhận là giá/tồn kho/cửa hàng thật**. Dữ liệu mẫu đề xuất trên màn demo:

- Campus/khu vực: thành phố Đà Nẵng; chọn campus thủ công hoặc vị trí giả định, không khẳng định quan hệ đối tác.
- Merchant demo: `Tiệm Bánh A`, `Căng tin B`, `Quầy Rau C` hoặc thương hiệu hư cấu tránh mạo danh doanh nghiệp hiện hữu.
- Offer demo: `Túi bánh cuối ngày` giá 25.000đ, pickup 17:00–18:00; `Combo rau củ` 30.000đ, pickup 16:00–17:30. Đây là **fixture**, không phải dữ liệu khảo sát/production. Giá/khung giờ chỉ nên được dùng nhất quán xuyên suốt prototype.
- Không lẫn cùng một offer với nhiều mức giá, tên merchant hay pickup hours ở các frame liên tiếp.
- Bộ fixture phải có danh sách IDs ổn định; mỗi frame mapping tới cùng fixture khi tương ứng cùng đối tượng.

### Manifest ảnh

Mỗi asset: `assetId`, `kind`, `filePath`, `sourceUrl`, `license`, `attribution`, `downloadDate`, `usageScope`, `merchantId?`, `offerId?`, `altText`, `approved`. AI assets nếu dùng cho concept minh họa cần ghi `sourceType=GENERATED_CONCEPT`, không được dựng “chân dung người tham gia khảo sát” như người có thật.

### Competitor evidence

Danh sách 20 ứng dụng gợi ý đã có trong `Nội dung slide chính.docx`: Too Good To Go, Karma, ResQ Club, Flashfood, Phenix, Foodsi, Munch, Yindii, Goodie Bag, Gander, LastBite, FoodHero, Cheaf, Bene Bono, treatsure, Surplus Indonesia, FoodObox, OLIO, HopHopFood, Food Rescue Hero. Agent phải xác minh **sự tồn tại, nguồn hiện hành và screenshots** trước khi cho vào matrix/charts; nếu app ngừng hoạt động hoặc không có nguồn đáng tin, ghi sự thật và đề xuất thay thế có căn cứ.

Bảng đối thủ bắt buộc có `App / Model / Current availability / Official source / Access date / Screens observed / Strengths / Weaknesses / Learning for SaveBite`. Không cần code clone 20 app và không dùng app icons trong product UI SaveBite.

---

## PHẠM VI HƯỚNG PHÁT TRIỂN — KHÔNG TỰ TRỘN VÀO 100 MÀN

`FUTURE-MERCHANT`: Merchant onboarding → Store verification → Dashboard → Create/Update Offer → Upload true images/ingredients/allergens → Configure stock/pickup slots → Orders → Scan/Enter Pickup Code → Confirm Handover → Incident Report → Analytics.  
`FUTURE-ADMIN`: Moderation of merchants/reviews, food safety incidents, consent/data requests, audit logs.  
`FUTURE-PAYMENTS`: Online payments, refunds, dispute resolution, retry, chargeback and merchant payouts.  
`FUTURE-PANTRY`: Barcode extraction, receipts import, cloud sync, household sharing, richer recipes with credible safety constraints.  
`FUTURE-GROWTH`: Recommendations, multi-language, broader cities/regions, impact analysis and partner reporting.

Việc **không thiết kế merchant trong 100 frame bản consumer MVP** là quyết định scope có chủ đích, không có nghĩa kiến trúc tương lai không hỗ trợ merchant. Nếu giảng viên yêu cầu nhiều actor, dùng ADR phê duyệt để dành một nhóm frame mới (không xóa 100 ID lịch sử tùy tiện).

---

## OPEN RISKS, DECISION LOG VÀ VẤN ĐỀ ĐÃ GIẢI QUYẾT

### Resolved defaults để agent không hỏi lại

- 100 hi-fi consumer app frames, 4 tabs, guest browse; merchant portal FUTURE.
- Rescue Market core, Smart Pantry complement; không delivery.
- Pay at pickup; online payment FUTURE.
- Pantry manual local-first; barcode/AI FUTURE.
- UI mobile sans-serif, slide design là reference không là design system nguyên bản.
- 100 frames distinct, error/state chỉ đếm nếu là frame thật và có ý nghĩa.
- Code UI ngoài phạm vi repo; bất nhất 50/30 của học phần giữ trong B-COURSE-01.
- Brand color trầm, ảnh thật, tiếng Việt, không fake people/test/impact.

### Blockers không được tự bịa cách vượt

| ID | Tình trạng | Cách giải quyết | Ảnh hưởng |
|---|---|---|---|
| `B-FIGMA-01` | RESOLVED trong phiên 19/10/2026: RIN student/Full/admin, native sandbox write/read pass | Reverify mỗi phiên; bằng chứng hiện hành trong tracking/progress.md | Không còn chặn pilot |
| `B-COURSE-01` | PDF ghi 50 màn code ở Deliverables nhưng 30 ở rubric | Nhóm xác nhận giảng viên khi làm phần học phần ngoài repo | Không chặn thiết kế |
| `B-RESEARCH-01` | Chưa có dữ liệu khảo sát/merchant interviews được xác minh trong tài liệu | Lập research plan; không tạo số liệu/quote giả | Chặn claim nghiên cứu, không chặn wireframes giả thuyết |
| `B-ASSETS-01` | RESOLVED cho pilot: hai ảnh Pexels có source/license/hash; các màn mới chưa được bao phủ | Dùng manifest; tìm nguồn hợp lệ khi có nhu cầu asset mới | Không chặn pilot; không giả đối tác |
| `B-LEGAL-01` | Chính sách food safety, xử lý đơn và thanh toán thật chưa được tư vấn/duyệt | Prototype mô phỏng bảo thủ, legal review trước launch | Chặn production launch, không chặn prototype |

### Khi nào agent phải xin duyệt chủ dự án

1. Thay target file/team/plan Figma hoặc tạo file khác thay thế.
2. Chuyển từ 100 màn consumer sang merchant/admin hoặc đổi nhóm tính năng lớn.
3. Đổi bottom navigation, state machine đặt trước, chính sách payment/pickup, giá hoặc safety semantics.
4. Thay hệ màu/font và component family đã được duyệt pilot.
5. Xóa hàng loạt frame, detach/migrate core components, cập nhật mâu thuẫn với research thật.
6. Đăng nội dung công khai, gửi email, đặt hàng, thanh toán, kết nối dịch vụ mang chi phí hoặc thu thập dữ liệu người dùng thật.

Mọi quyết định nhỏ về spacing, crop ảnh hợp lệ, copy ngắn gọn, thêm states lỗi đúng phạm vi, tái sử dụng components có thể tự xử lý và ghi log — **không cần hỏi liên tục**.

---

