from playwright.sync_api import sync_playwright
import time
import os

# Lấy thông tin từ GitHub Secrets
APPLE_ID = "p.thao24122003@icloud.com"  # Thay thế bằng Apple ID của bạn
APPLE_PASSWORD = "otvi-odwz-mevo-eonv"  # Thay thế bằng Apple Password của bạn

def auto_publish():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Chạy trình duyệt ẩn
        page = browser.new_page()
        
        # 1️⃣ Truy cập Apple Podcasts Connect
        page.goto("https://podcastsconnect.apple.com/")
        time.sleep(3)

        # 2️⃣ Đăng nhập bằng tài khoản Apple
        page.fill('//input[@id="account_name_text_field"]', APPLE_ID)  # Điền Apple ID
        page.fill('//input[@id="password_text_field"]', APPLE_PASSWORD)  # Điền mật khẩu
        page.click('//button[@id="sign-in"]')  # Nhấn nút Đăng nhập
        time.sleep(5)  # Chờ 2FA nếu có
        
        # Nếu có mã 2FA, bạn cần nhập thủ công trên GitHub Actions hoặc sử dụng giải pháp OTP tự động

        # 3️⃣ Vào trang quản lý podcast
        page.goto("https://podcastsconnect.apple.com/my-podcasts/show/backlink1dpod/b50019d4-f29f-48a2-b60f-8d1bdd3e28c1")
        time.sleep(3)

        # 4️⃣ Kiểm tra nút Publish
        if page.locator('button:has-text("Publish")').is_visible():
            page.click('button:has-text("Publish")')
            print("✅ Podcast đã được publish lại!")
        else:
            print("⚡ Podcast vẫn đang hoạt động.")

        browser.close()

if __name__ == "__main__":
    auto_publish()
