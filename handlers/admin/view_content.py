from aiogram import Router,F,Bot
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data.database import ViewDB
from keyboards.admin.btn_builder import view_opt

veiw_router = Router()
view_db = ViewDB()


@veiw_router.message(F.text == 'Задачи' )
async def veiw_all_list(message: Message):
    title = ''
    for i in view_db.view_two_with_photo():
        title += i
        if title==i:
            await message.answer(text=view_db(),)
