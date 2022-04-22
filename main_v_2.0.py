import config
from database import Database
import telebot

db = Database('db.db')
bot = telebot.TeleBot(config.API)
item1 = telebot.types.KeyboardButton('Поиск собеседника')
item2 = telebot.types.KeyboardButton('Остановить поиск')
item3 = telebot.types.KeyboardButton('Завершить диалог')
@bot.message_handler(commands='')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1)

    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! Добро пожаловать в анонимный чат! Нажми "Поиск собеседника".', reply_markup=markup)
    bot.send_message(message.chat.id, f'Наш чат абсолютно бесплатный и без рекламмы!')

@bot.message_handler(commands=['menu'])
def search(message):
    db.delete_queue(message.chat.id)
    db.delete_chat(message.chat.id)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1)

    bot.send_message(message.chat.id, message.from_user.first_name, reply_markup=markup)
@bot.message_handler(commands=['stop'])
def stop(message):
    chat_info = db.get_active_chat(message.chat.id)
    if chat_info != False:
        db.delete_chat(chat_info[0])
        db.delete_queue(chat_info[0])
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(item1)

        bot.send_message(chat_info[1], 'Собеседник покинул чат :(', reply_markup=markup)
        bot.send_message(message.chat.id, 'Вы вышли из чата, введите /menu для возврата в меню', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Вы не начали чат!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    # bot.send_message(message.chat.id, message.text)
    if message.chat.type == 'private':
        if message.text.lower() == 'поиск собеседника':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item2)

            chat_two = db.get_chat() # id of chat_one user

            if db.create_chat(message.chat.id, chat_two) == False:
                if message.text:
                    db.add_queue(message.chat.id)
                    bot.send_message(message.chat.id, 'Поиск собеседника...', reply_markup=markup)
                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                    markup.add(item3, item1)
            else:
                mess = 'Собеседник найден! Чтобы остановить диалог, введите /stop'
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(item3, item1)

                bot.send_message(message.chat.id, mess, reply_markup=markup)
                bot.send_message(chat_two, mess, reply_markup=markup)

        elif message.text.lower() == 'остановить поиск':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item1)

            db.delete_queue(message.chat.id)
            bot.send_message(message.chat.id, 'Поиск остановлен, напишите /menu для возврата в меню')
        elif message.text.lower() == 'завершить диалог':
            stop(message)

        else:
            try:
                chat_info = db.get_active_chat(message.chat.id)
                bot.send_message(chat_info[1], message.text)
            except:
                bot.send_message(message.chat.id, 'Вы не начали диалог!')
# @bot.message_handler()
# def check_text(message):
#     text = list(message.text)
#     if text[0] == '/':
#         pass
bot.polling(none_stop=True)