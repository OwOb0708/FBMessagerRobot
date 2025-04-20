from fastapi import APIRouter, Request, Query
from fastapi.responses import PlainTextResponse
from app.config import settings
from app.messenger.service import handle_message, call_send_api
import json

router = APIRouter()

@router.get("/", response_class=PlainTextResponse)
async def verify(
    hub_mode: str = Query(..., alias="hub.mode"),
    hub_token: str = Query(..., alias="hub.verify_token"),
    hub_challenge: str = Query(..., alias="hub.challenge"),
):
    if hub_mode == "subscribe" and hub_token == settings.verify_token:
        return hub_challenge
    return PlainTextResponse("Forbidden", status_code=403)

@router.post("/")
async def receive_message(request: Request):
    data = await request.json()
    if data.get("object") == "page":
        for entry in data.get("entry", []):
            for event in entry.get("messaging", []):
                sender_id = event["sender"]["id"]
                if "message" in event:
                    await handle_message(sender_id, event["message"])
        return "EVENT_RECEIVED"
    return "Not a page event"


@router.get("/health")  # 測試主伺服器是否存活
def health_check():
    return {"status": "ok"}