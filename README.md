# Telegram TikTok Live/Die Checker

Bot Telegram kiểm tra tình trạng tài khoản TikTok (live / banned / error).

## Cách chạy nhanh (Python 3.10+)
1) Tạo bot và lấy token từ @BotFather.
2) Tạo file `.env` hoặc export biến môi trường:
   ```bash
   export BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
   ```
3) Cài đặt thư viện:
   ```bash
   pip install -r requirements.txt
   ```
4) Chạy bot:
   ```bash
   BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN python bot.py
   ```

## Cách dùng
- `/check username1 username2 @username3` — kiểm nhanh vài username.
- Gửi *file .txt* (mỗi dòng 1 username) để kiểm tra hàng loạt. Bot sẽ trả về 3 file `*_live.txt`, `*_banned.txt`, `*_error.txt`.

> Lưu ý: Giới hạn song song tối đa 5 để giảm rủi ro 429 từ TikTok. Nếu kiểm tra nhiều, hãy chia nhỏ danh sách.