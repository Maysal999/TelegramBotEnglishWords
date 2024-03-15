import asyncio
import os
import sys

sys.path.insert(1,os.path.join(sys.path[0],'..'))


from aiogram import Bot, Dispatcher

#нужные модулы и файлы
from common.config import token
from handlers.admin.add_task import reg_router
from handlers.admin.user_group import user_group_router
from handlers.admin.drop_answer import drop_router
from handlers.admin.add_word import word1
from handlers.user_handlers.user_handlers import start
# from handlers.admin.view_content import veiw_router

# иницализация бота
bot = Bot(token=token)
dp = Dispatcher()
bot.my_admins_list = [5173312146]

#подключения на роутеры
# dp.include_router(veiw_router)\
dp.include_router(start)
dp.include_router(word1)
dp.include_router(reg_router)
dp.include_router(user_group_router)
dp.include_router(drop_router)

#функция для run
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

#run
asyncio.run(main())