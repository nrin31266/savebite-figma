# SaveBite

Đồ án UX/UI ứng dụng iPhone tiếng Việt: **Rescue Market** là core, **Smart Pantry** là phần bổ trợ.

Bắt đầu tại [bản đồ tài liệu](docs/README.md), xem [tiến độ và bằng chứng](tracking/progress.md). File Figma đích duy nhất hiện hành (`DEC-011`): [SaveBite-V2](https://www.figma.com/design/7suZz9C8oL5zV2NMxlsIVI/SaveBite-V2?node-id=0-1).

Kiểm tra repo bằng Python 3, không cần cài dependency:

```sh
python3 scripts/validate.py
```

Phạm vi repo: thiết kế Figma chuẩn **iPhone 15 (`393×852pt`, Dynamic Island)**, design system, prototype và bằng chứng QA. Mục tiêu toàn đồ án là 100 hi-fi frames; giai đoạn **Phase 1 (`B-PHASE1-010`)** tập trung thiết kế mới hoàn toàn **10 màn hình North-Star đại diện** (`SB-002`, `SB-015`, `SB-016`, `SB-019`, `SB-034`, `SB-051`, `SB-053`, `SB-056`, `SB-075`, `SB-091`) trước khi mở khóa 90 màn còn lại cho 2 Agent chạy song song (50/50 split).

Repo GitHub: [savebite-figma](https://github.com/nrin31266/savebite-figma). Các màn pilot v0.5 trên file cũ đã được xóa và đánh dấu `STALE/RETIRED` theo `DEC-011`.

Agent/client đọc [AGENTS.md](AGENTS.md); `CLAUDE.md` là symlink cùng nguồn. Skills của dự án nằm tại `.agents/skills/` và bộ 6 ảnh thực phẩm Pexels đã xác minh mã băm nằm tại [assets/manifest.json](assets/manifest.json).

Cho thành viên mới: [đọc context theo thứ tự](docs/README.md#cho-người-mới), rồi xem [tiêu chí nghiệm thu](docs/acceptance.md). Không cần tài liệu nguồn ngoài repo để tiếp tục thiết kế.
