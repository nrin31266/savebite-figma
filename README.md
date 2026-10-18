# SaveBite

Đồ án UX/UI ứng dụng mobile tiếng Việt: Rescue Market là core, Smart Pantry là phần bổ trợ.

Bắt đầu tại [bản đồ tài liệu](docs/README.md), xem [tiến độ và bằng chứng](tracking/progress.md). Figma đích duy nhất: [SaveBite](https://www.figma.com/design/NLTv70kDZ2i3HpOnOKQCDY/Untitled).

Kiểm tra repo bằng Python 3, không cần cài dependency:

```sh
python3 scripts/validate.py
git status --short --branch
```

Chưa có app/backend để chạy. Mục tiêu dài hạn là 100 hi-fi frames và 50 màn code; trạng thái thực nằm trong registry. Prototype dùng fixture mô phỏng, không tạo giao dịch thật.

Repo GitHub: [savebite-figma · private](https://github.com/nrin31266/savebite-figma). [Mở prototype 5 màn](https://www.figma.com/proto/NLTv70kDZ2i3HpOnOKQCDY/SaveBite?page-id=2%3A2&node-id=28-2&starting-point-node-id=28%3A2&scaling=scale-down); pilot v0.3 đang chờ owner review.

Agent/client đọc [AGENTS.md](AGENTS.md); `CLAUDE.md` là symlink cùng nguồn. GitHub private được owner cho phép theo DEC-004 sau khi QA; không công khai Figma hoặc mời thành viên. Skills của dự án nằm tại `.agents/skills/`.
