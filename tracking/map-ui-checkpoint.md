# Map UI checkpoint · 01/11/2026

Batch thuộc goal polish100 màn, chart/motion và kit/plugin; chưa thu hẹp goal thành5 màn. Một writer trực tiếp,100 root IDs giữ nguyên, không tạo main component mới. Lease `codex/direct-map-ui` RELEASED tại checkpoint; không push/merge, DONE0.

## Đã sửa canvas

- **016:** ẩn2 rectangle che map; toolbar353pt thay hàng464pt bị tràn;3 controls44pt. Ba pin25/30/35K reuse selection actions của Discovery; selected overlay theo current/photo. Pin88×44. Metadata price/slot dùng HUG trong row FILL, không chia đôi làm wrap.
- **017:** ảnh/tên/merchant/giá/slot theo current offer; đổi pin trong cùng frame bằng SET_VARIABLE, không tự NAVIGATE vào chính frame. AppBar/back48 về016. CTA **Xem chi tiết món** đi034 giữ context; cạnh016→017 Smart Animate220ms.
- **039:** AppBar **Vị trí cửa hàng**; một pin và tuyến nét đứt minh họa, sheet304pt. Bỏ ETA6phút/điểm xuất phát chưa có nguồn; merchant/location theo current context. CTA thật tới034 thay hover-only; sửa system chrome z-order.
- **065:** ẩn pin món khác và các rectangle che map. Một sheet304pt chứa preview, lưu ý và CTA63; bỏ chỉ dẫn tầng/cổng chưa xác nhận. Merchant/slot/ảnh theo context, AppBar/back về062. Giữ các layer ảnh và bindings, không flatten.
- **094:** source-native Primary buttons cho selected radius;3 ellipse đường kính96/152/224pt minh họa, không phải phép đo địa lý.3 Boolean vars `VariableID:447:4962/4963/4964`, giữ STRING radius-label có sẵn. Selected styles theo palette/radius/type SaveBite.

Reuse MapCanvas16:3, MapPricePin16:16, OfferListRow15:169, AppBar15:105, Apple Search158:211, SDS Primary178:371/Neutral178:374/Input179:234. Không đổi MapCanvas master hoặc xóa dữ liệu cũ. [Read-back](evidence/map-ui/readback.json) giữ roots/mains/click sources; [bounds cuối](evidence/map-ui/final-bounds.json) supersede geometry trước chỉnh44pt.

## Evidence / giới hạn

Ảnh cuối: [016](evidence/map-ui/SB-016.png), [017](evidence/map-ui/SB-017.png), [039](evidence/map-ui/SB-039.png), [065](evidence/map-ui/SB-065.png), [094](evidence/map-ui/SB-094.png). Đã chụp5 màn cùng lượt để sửa; bộ before trước restart chưa lưu bền, không claim comparison đầy đủ.

Present đã bấm:016 pin30K→017 [croissant30K/17–18](evidence/map-ui/runtime-croissant.png), tiếp tục pin35K→[meal35K/17:30–19](evidence/map-ui/runtime-meal.png).094 [500m](evidence/map-ui/runtime-radius-500.png) và [2km](evidence/map-ui/runtime-radius-2000.png) đổi nút/label/vòng. AX screenshot đôi lúc thiếu phần hình khi tương tác; ảnh browser trực tiếp cùng state500m hiển thị đầy đủ, chưa kết luận nguyên nhân.

Scoped visual: sheet không chồng/che CTA, price/slot mặc định không wrap. Chưa kiểm toàn5SKU/long text/Dynamic Type, tất cả CTA/back hoặc F-02 end-to-end; motion/reduced motion và thiết bị thật chưa kiểm. `prototype_verified=false`, chưa owner acceptance.

## Map nguồn/plugin còn thiếu

maps.to.design có trong quick actions nhưng2 lần mở trước restart và1 lần sau đều báo **“An error occurred while loading the plugin environment”**. MCP identity/read/write hoạt động. [Hướng dẫn hãng](https://divriots.com/blog/introducing-maps-to-design/) nói export image/fill; không claim plugin xuất vector native toàn bộ. Chưa có map source mới trên Foundations; đã nhờ owner thử export ở phiên Figma riêng, chưa nhận layer. Hai lần đọc Overpass tìm khu học xá trảHTTP502; không nhập dữ liệu/map nào.

Vẫn dùng sơ đồ có nhãn minh họa; route/pins không chứng minh GPS, tọa độ thật hoặc ETA. Map nguồn thật và mở bản đồ ngoài **REQUIRES-REAL-DATA / chưa hoàn tất**. Tiếp tục phần UI/chart/motion độc lập trong khi chờ môi trường/plugin hoặc layer nguồn thay đổi.
