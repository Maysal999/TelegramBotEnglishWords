from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove


opros = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='No'),KeyboardButton(text='Yes')]],resize_keyboard=True,input_field_placeholder='Выберите что делать')