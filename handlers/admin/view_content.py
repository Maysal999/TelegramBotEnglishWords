# from aiogram import Router,F,Bot
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# from aiogram.fsm.context import FSMContext




# veiw_router = Router()


# @veiw_router.message(F.text == 'Посмотреть все задачи👀' )
# async def veiw_all_list(message: Message):

#     task.get_all_list_task()
#     for d in  task.data:
#         await message.answer_photo(photo=d[4], caption=f'title: {d[3]}\ncategoria: {d[5]}\ncontent: {d[1]}\n')