import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

from db import get_subscription

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Оплатити доступ", callback_data="pay")],
        [InlineKeyboardButton(text="📅 Мій статус", callback_data="status")]
    ])


@dp.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer(
        "👋 Привіт!\n"
        "Цей бот видає доступ до закритої групи на 30 днів після оплати.",
        reply_markup=main_keyboard()
    )


@dp.callback_query(F.data == "status")
async def status_handler(callback):
    sub = await get_subscription(callback.from_user.id)

    if not sub:
        await callback.message.answer("❌ У тебе немає активної підписки.")
    else:
        await callback.message.answer(f"✅ Доступ активний до:\n{sub[1]}")


@dp.callback_query(F.data == "pay")
async def pay_handler(callback):
    await callback.message.answer(
        "💳 Оплата буде підключена на наступних кроках.\n"
        "Після оплати ти автоматично отрим
