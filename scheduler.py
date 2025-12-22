from apscheduler.schedulers.asyncio import AsyncIOScheduler

_scheduler = None


def start_scheduler(bot):
    # Поки просто запускаємо планувальник без задач
    global _scheduler
    if _scheduler:
        return _scheduler

    _scheduler = AsyncIOScheduler(timezone="UTC")
    _scheduler.start()
    return _scheduler
