from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"ok": True, "service": "tg-access-bot"}


@app.post("/payment/webhook")
async def payment_webhook():
    # Поки тестовий webhook. Пізніше підключимо платіжку.
    return {"ok": True}
