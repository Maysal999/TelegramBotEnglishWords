from aiogram import Router,F,Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from common.Rstate import AddWordState

from data.database import AddTaskDB,GetTaskDB
from filters.chat_type import ChatTypeFilter, IsAdmin
from keyboards.admin.btn_builder import select_categoria
from keyboards.rpbtn import main
word1 = Router()
word1.message.filter(ChatTypeFilter(["private"]), IsAdmin())


word = None
value = None
categoria = None


get_task_id = GetTaskDB()
add_task_db = AddTaskDB()
@word1.message(Command('admin'))
async def start(message: Message):
    await message.answer(text='welcome',reply_markup=main())
@word1.message(F.text == 'Добавить словарь 📌')
async def text_title(message:Message,state: FSMContext):
    await message.answer('Введите слова - ')
    await state.set_state(AddWordState.word)

@word1.message(AddWordState.word,F.text)
async def text_level(message:Message,state: FSMContext):
    global word
    await state.update_data(name=message.text)
    word = message.text
    await state.set_state(AddWordState.value)
    await message.answer('Введите значиние слова')

@word1.message(AddWordState.value,F.text)
async def text_level(message:Message,state: FSMContext):
    global value
    await state.update_data(name=message.text)
    value = message.text
    await state.set_state(AddWordState.categoria)
    await message.answer('Выберите категория - ',reply_markup = select_categoria())

@word1.message(AddWordState.categoria,F.text)
async def text_level(message:Message,state: FSMContext):
    global categoria
    await state.update_data(name=message.text)
    categoria = message.text
    await message.answer('отправте фото🏞️')
    await state.set_state(AddWordState.photo)
  
@word1.message(AddWordState.photo,F.photo)
async def text_photo(message:Message,state: FSMContext,bot:Bot):
    await state.update_data(name=message.photo[-1].file_id)
    photo = message.photo[-1].file_id
    add_task_db.add_words(words=word,value=value,cate_id=get_task_id.get_id_categoria(title=categoria),photo_id=photo)
