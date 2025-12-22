import asyncio
import uvicorn

from bot_app import bot, run_bot
from webhook_app import app as webhook_app
from scheduler import start_scheduler
from db import init_db

async def main():
    await init_db()
    start_scheduler(bot)

    config = uvicorn.Config(webhook_app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)

    await asyncio.gather(
        server.serve(),
        run_bot()
    )

if __name__ == "__main__":
    asyncio.run(main())
