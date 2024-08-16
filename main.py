#!/usr/bin/python
import asyncio
from app.handlers import bot, dp


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print("Bot started successfully")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped successfully")