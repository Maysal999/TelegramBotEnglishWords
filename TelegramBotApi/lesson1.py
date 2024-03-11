import telebot

from telebot import types

bot = telebot.TeleBot('6825537912:AAHtOSPF2p06HdoD1pyzVF-q5FqH4vTC4Y8')

command = ['start','help','info','func','Button']

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,text='Hello World')


# @bot.message_handler(commands=[command[1]])
# def start_message(message):
#     bot.send_message(message.chat.id,text=f'{command[0]} - это команда для запуска бота\n{command[1]} - это команда для если что-то непонятно,вызываете\n{command[2]} - это команда справочник')


@bot.message_handler(commands=[command[1]],regexp='help')
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,input_field_placeholder='Выберите команду')

    btn = types.KeyboardButton('/start')
    btn1 = types.KeyboardButton(command[1])
    btn2 = types.KeyboardButton(command[2])
    btn3 = types.KeyboardButton(command[3])

    markup.add(btn1,btn)
    markup.add(btn3,btn2)

    bot.send_message(message.chat.id,text='Hello World',reply_markup=markup)

@bot.message_handler(content_types='text')
def get_hello(message):
    if message.text.lower() == 'Hello':
        bot.reply_to(message, 'HI')
    elif message.text.lower() == 'How are you?':
        bot.reply_to(message, 'no bad')
    elif message.text.lower() == 'where are you?':
        bot.reply_to(message, 'Osh')
    else:
        bot.reply_to(message, "I don't understand you")
bot.infinity_polling()

