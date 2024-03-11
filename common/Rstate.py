from aiogram.fsm.state import State,StatesGroup


class TaskState(StatesGroup):
    title = State()
    content = State()
    photo = State()
    level = State()
    categoria = State()