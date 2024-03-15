from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.database import ViewDB

def level_btn():
    button_list = ['A1','A2','B1','B2','C1','C2']
    button = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=button_list[0]),
         KeyboardButton(text=button_list[1])],
        [KeyboardButton(text=button_list[2])],
        [KeyboardButton(text=button_list[3]),
         KeyboardButton(text=button_list[4])],
        [KeyboardButton(text=button_list[5])],
        ],resize_keyboard=True,)
    return button

def remove_button():
    remove = ReplyKeyboardRemove()
    return remove

def select_categoria():
    buttons_categoria = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='математика 🔤'),
                                                       KeyboardButton(text='медицина 🧬')],
                                                       [KeyboardButton(text='IT 💻'),
                                                       KeyboardButton(text='языки 🇺🇸')]],resize_keyboard=True,one_time_keyboard=True)
    return buttons_categoria

def option_task():
    button_options = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Добавить вариянт ✏️')],
                                                   [KeyboardButton(text='Стоп ⛔')]])
    return button_options

def view_opt(content_id):
    view = ViewDB()
    button = InlineKeyboardBuilder()
    for i in view.view_options():
        for j in i[1]:
            button.row(InlineKeyboardButton(text=j))
    return button.as_markup()
# view_opt()