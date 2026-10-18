# SaveBite

Đồ án UX/UI ứng dụng mobile tiếng Việt: Rescue Market là core, Smart Pantry là phần bổ trợ.

Bắt đầu tại [bản đồ tài liệu](docs/README.md), xem [tiến độ và bằng chứng](tracking/progress.md). Figma đích duy nhất: [SaveBite](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/Untitled).

Kiểm tra repo bằng Python 3, không cần cài dependency:

```sh
python3 scripts/validate.py
git status --short --branch
```

Chưa có app/backend để chạy. Mục tiêu dài hạn là 100 hi-fi frames và 50 màn code; trạng thái thực nằm trong registry. Prototype dùng fixture mô phỏng, không tạo giao dịch thật.

Agent/client đọc [AGENTS.md](AGENTS.md); `CLAUDE.md` là symlink cùng nguồn. Không push hoặc công khai nội dung trong phiên bootstrap.
