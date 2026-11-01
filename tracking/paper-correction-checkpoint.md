# Paper correction ·01/11/2026

**AWAITING_OWNER_REVIEW.** Owner yêu cầu kiểm chỗ nên/không nên dùng giấy gấp, có bản không gấp và nền lộ sau nếp gấp phải cùng nền ngoài. Lease `codex/paper-correction` RELEASED; không commit/push. Supersede phần paper placement ở [batch trước](apple-paper-checkpoint.md), không thay đổi status bars/nghiệp vụ/reactions.

- **044:** đổi existing instance571:11115 sang `Pattern=Plain` main **577:926**, family231:458; wrapper571:11114 đổi tên Plain. Forest stage/phần ảnh/caption giữ vị trí. Không gấp góc phía sau túi đã có hình khối riêng.
- **Fold231:450:** base231:452 khoét đường chéo, layer231:453 bỏ fill xanh nhạt; vùng ngoài góc gấp trong suốt thật. Bất kỳ nền cha nào đều lộ đúng màu nền, không phải tô một tam giác kem giả. Fold chỉ giữ trong bộ mẫu; không còn dùng trên App.
- **053:** giữ Receipt edge12pt vì nội dung là biên lai; không chữ/giá nằm trên texture. **056:** gỡ đúng wrapper571:11143 và instance571:11144 vừa tạo ở batch trước: vé đã có khuyết/đường xé, không cần thêm sọc trang trí. Không sửa QR hoặc ticket main. **074:** giữ Leaf dưới ảnh,opacity0.35; không có nếp gấp và không phủ nội dung.
- Bảng mẫu231:743 có5 linked instances (Leaf/Stripe/Receipt/Plain/Fold), Auto Layout cùng kích thước; main577:926 nằm ngoài bảng review. Source vector/token bindings được reuse. Một main variant mới, registry157 entries; không token/photo mới. SVG Fold/Plain được export native vào source manifest32 brand records/hash.

Evidence: [main/app readback](evidence/paper-correction/readback.json), [final mapping + SVG export](evidence/paper-correction/final.json), [5 mẫu giấy](evidence/paper-correction/after/pattern-specimen.png), [044](evidence/paper-correction/after/SB-044.png), [053](evidence/paper-correction/after/SB-053.png), [056](evidence/paper-correction/after/SB-056.png), [074](evidence/paper-correction/after/SB-074.png), [Present044](evidence/paper-correction/runtime/present-SB-044.jpg).

PASS scoped visual review: Flat/Fold phân biệt rõ; góc ngoài Fold trùng nền card nhờ transparency, không còn tam giác sage.044 và074 capture đủ chrome;053/056 native capture vẫn có lượt thiếu status như lỗi capture trước, không chỉnh layout để che lỗi. Present044 hiển thị đủ status/ảnh/nền phẳng. Component IDs/usage sau write khớp; deleted stripe không còn parent trên canvas.

Full transition rendering,100-screen visual/contrast/mobile/usability và owner acceptance chưa kiểm lại; `prototype_verified=false`, DONE0. Giới hạn render từ batch trước vẫn OPEN. Không claim usability hoặc toàn prototype PASS từ sửa vật liệu.

Repository checks PASS: `python3 scripts/validate.py`, `git diff --check`,6 image decode,32 brand source hashes,2 exported SVG XML và4 scoped mappings.
