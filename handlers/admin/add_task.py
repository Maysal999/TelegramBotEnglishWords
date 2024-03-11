from aiogram import Router,F,Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from common.Rstate import TaskState

from data.database import AddTaskDB,GetTaskDB
from filters.chat_type import ChatTypeFilter, IsAdmin
from keyboards.admin.btn_builder import level_btn, select_categoria, option_task
from keyboards.rpbtn import main
from keyboards.admin.opros import opros

reg_router = Router()
reg_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())


categoria = None
level = None
user_id = None
content = None
photo = None
option = []


get_task_id = GetTaskDB()
add_task_db = AddTaskDB()


@reg_router.message(Command('admin'))
async def start(message: Message):
    await message.answer(text='welcome',reply_markup=main())
   
@reg_router.message(F.text == 'Добавить Задача ✏️')
async def text_title(message:Message,state: FSMContext):
    await message.answer('Введите задача')
    await state.set_state(TaskState.content)

@reg_router.message(TaskState.content,F.text)
async def text_content(message:Message,state: FSMContext):
    global content
    await state.update_data(name=message.text)
    content = message.text
    await state.set_state(TaskState.categoria)
    await message.answer('Введите вариянт - ',reply_markup = option_task())
@reg_router.message(F.text == 'Добавить вариянт ✏️')
async def text_content(message:Message, state:FSMContext):
    global option
    await message.answer('ВВедите вариянт 1 2 3 4(1- это вариянт а, 2 - это б, 3 - это в) ')
    option = message.text.split(' ')
    await state.set_state(TaskState.categoria)
    await message.answer('Выберите категория - ',reply_markup = select_categoria())

@reg_router.message(F.text )
async def text_content(message:Message, state:FSMContext):
    await state.set_state(TaskState.categoria)
    await message.answer('Выберите категория - ',reply_markup = select_categoria())

@reg_router.message(TaskState.categoria,F.text)
async def text_level(message:Message,state: FSMContext):
    global categoria
    await state.update_data(name=message.text)
    categoria = message.text
    await state.set_state(TaskState.level)
    await message.answer('Выберите уровень',reply_markup = level_btn())

@reg_router.message(TaskState.level,F.text)
async def text_level(message:Message,state: FSMContext):
    global level
    await state.update_data(name=message.text)
    level = message.text
    await message.answer('Есть фото на этом вопросе?',reply_markup=opros)
    await state.set_state(TaskState.photo)

@reg_router.message(F.text == 'No')
async def text_opros(message:Message):
    await message.answer('Succes✅',reply_markup=main())
    level_id = get_task_id.get_id_level(level=level)
    cate_id = get_task_id.get_id_categoria(title=categoria)
    task_id = get_task_id.get_id_two(content=content)
    add_task_db.add_task_with_options(level_id=level_id,cate_id=cate_id,content=content)

@reg_router.message(F.text == 'Yes')
async def text_p(message:Message,state: FSMContext,bot:Bot):
    await message.answer('отправте фото🏞️')
    await state.set_state(TaskState.photo)

@reg_router.message(TaskState.photo,F.photo)
async def text_photo(message:Message,state: FSMContext,bot:Bot):
    global photo
    await state.update_data(name=message.photo[-1].file_id)
    user_id = message.from_user.id
    photo = message.photo[-1].file_id
    await message.answer('Succes✅',reply_markup=main())
    level_id_1 = get_task_id.get_id_level(level=level)
    cate_id_1 = get_task_id.get_id_categoria(title=categoria)
    add_task_db.add_task_with_options(level_id=level_id_1,photo_id=photo,cate_id=cate_id_1,content=content)
    task_id_1 = get_task_id.get_id_two(content=content)
    for opt in option:
        add_task_db.add_options(option=opt,task_id=task_id_1)