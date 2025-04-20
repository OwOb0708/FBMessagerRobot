# 📬 FastAPI Messenger Webhook Bot

這是一個使用 [FastAPI](https://fastapi.tiangolo.com/) 架設的 Facebook Messenger Webhook Bot
擁有以下功能：

- 支援 Webhook 驗證
- 能夠接收與回覆使用者訊息
- 支援使用 `.env` 設定檔管理環境變數
- 可擴充的 SQLite 資料儲存功能

並結合 [ngrok](https://ngrok.com/) 作為本地端開發測試的 HTTPS 代理工具
讓本機 Web API 可被 Facebook 接收到。

---

## 📁 專案結構說明

```
fastapi-messenger-bot/
├── app/
│   ├── db/              # 資料庫邏輯 (使用 SQLite)
│   └── messenger/       # Webhook 請求處理邏輯
├── .env                 # 環境變數設定檔
└── main.py              # FastAPI 啟動主程式
```

---

## ⚙️ 技術說明

### FastAPI 是什麼？
FastAPI 是一個基於 Python 3.6+ 打造的高效能 Web API 框架
設計上強調：
- 高效能（與 Node.js 與 Go 相媲美）
- 自動生成 OpenAPI (Swagger) 文件
- 依賴型注入與資料驗證簡潔易用

### Web API 是什麼？
Web API（Web 應用程式介面）是一種透過 HTTP 協定提供資料與服務的方式
允許不同系統或平台之間進行通訊與整合

---

## 🌐 ngrok 的用途

由於 Facebook Webhook 需要公開的 HTTPS URL
而本機開發環境通常無法直接暴露於網際網路
因此使用 ngrok 建立一條從公網導向本地端的安全連線

這樣可以：
- 本地開發測試 webhook 功能
- 即時接收 Facebook 傳來的訊息

---
