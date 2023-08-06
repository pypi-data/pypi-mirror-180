from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TWITTER_BOT_API_TOKEN: str = "5805830954:AAEx4YgU-ZzmKojD4Xv0cyB6CrAsakjdg04"
CHANNEL_ID: int = -1001863320905

bot = Bot(token=TWITTER_BOT_API_TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)

message: str = """
• 17:30-17:40 (10m): Network 🚫
• 17:30-17:50 (20m): Electricity ✅
• 17:40-17:50 (10m): Network ✅
"""


async def send_message_to_channel() -> None:
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=message,
        disable_notification=False,
    )


if __name__ == '__main__':
    executor.start(dispatcher, send_message_to_channel())
