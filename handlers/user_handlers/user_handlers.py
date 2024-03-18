from aiogram import Router,F,Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
from data.database import ViewDB
from keyboards.rpbtn import main_user

start = Router()



@start.message(CommandStart())
async def main_r(message:Message):
    await message.answer('Welcome to our bot',reply_markup=main_user())


@start.message(F.text == 'Посмотреть словари 🗂️')
async def main_r(message:Message):
    db = ViewDB()
    for i in db.word_view():
            await message.answer_photo(photo=i[4],caption=f'слова - <b>{i[1]}</b>\n<b>{i[2]}</b>',parse_mode=ParseMode('HTML'))

# @start.message(F.text == 'Посмотреть Задачи ✏️')
# async def task_view_tr(message: Message):
#      db = ViewDB()
#      for i in db.view_two_without_photo():
          