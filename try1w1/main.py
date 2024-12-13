from aiogram import Bot, Dispatcher, types, F
import asyncio

from app.handlers import router



async def main():
    bot=Bot(token="7607580537:AAHhU2izC00xjuf8JaAU-S4eRim5sAi_8gg")
    dp=Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__== '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('бот выключен ;(')
