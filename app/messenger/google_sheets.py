import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import traceback

def write_to_google_sheet(sender_id: str, text: str):
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
        client = gspread.authorize(creds)

        print("開啟中...")
        sheet = client.open("打卡紀錄表").sheet1
        print("✅ 成功開啟試算表")

        # ✅ 實際寫入資料
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([now_str, sender_id, text])
        print("✅ 成功寫入 Google Sheet")

    except Exception as e:
        print("❌ Google Sheet 寫入錯誤:", repr(e))
        traceback.print_exc()
