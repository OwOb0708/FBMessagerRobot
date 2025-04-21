import requests
from datetime import datetime
from app.config import settings
from app.db.database import SessionLocal
from app.db.models import CheckinLog
from app.messenger.google_sheets import write_to_google_sheet

from zoneinfo import ZoneInfo

async def handle_message(sender_id: str, message: dict):
    
    taiwan_time = datetime.now(ZoneInfo("Asia/Taipei"))
    text = message.get("text", "")
    
    # 寫入 SQLite
    db = SessionLocal()
    try:
        log = CheckinLog(
            sender_id=sender_id,
            message_text=text,
            checkin_time=datetime.now(ZoneInfo("Asia/Taipei"))
        )
        db.add(log)
        db.commit()
    except Exception as e:
        db.rollback()
        print("DB Error:", e)
    finally:
        db.close()


    # 寫入 Google Sheet
    write_to_google_sheet(sender_id, text)
    
    # 回應結構
    response = {
        "text": f"Hi! 你打卡的時間是 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    await call_send_api(sender_id, response)

async def call_send_api(sender_id: str, response: dict):
    url = f"https://graph.facebook.com/v17.0/me/messages?access_token={settings.page_access_token}"
    payload = {
        "recipient": {"id": sender_id},
        "message": response,
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code != 200:
        print("Error:", r.text)
