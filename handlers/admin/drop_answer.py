from aiogram import F,Router
from aiogram.types import Message

# from keyboards.admin.select_categorias import select
from data.delete_date import delete_date2
drop_router = Router()


@drop_router.message(F.text == 'Удалить задача🗑️')
async def delete_date3(message: Message):
    await message.answer(text='Введите названия задача')
    messa = message.text
    tstd = delete_date2(title=messa)
    print(tstd)
    await message.answer(text='Задача успешно удалено✅')