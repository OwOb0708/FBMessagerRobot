from fastapi import FastAPI
from app.messenger.webhook import router as webhook_router

app = FastAPI(
    title="劉宇軒的後端Messenger Webhook",
    docs_url="/docs")

app.include_router(webhook_router)
