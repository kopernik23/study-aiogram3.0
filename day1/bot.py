from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

import asyncio


API_TOKEN = '7182906352:AAHO1FxFHCG9PFZ_ePdKaFFYIJ6WMm2AQMw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_message(message: Message):
    await message.answer("Привет! Я БОТ!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
