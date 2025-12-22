import aiosqlite

DB_PATH = "bot.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS subs (
            user_id INTEGER PRIMARY KEY,
            paid_until TEXT
        )
        """)
        await db.commit()


async def get_subscription(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute(
            "SELECT user_id, paid_until FROM subs WHERE user_id = ?",
            (user_id,)
        )
        return await cur.fetchone()
