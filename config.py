from telebot import types
API = "xxxxxx:xxxxxxxxx"
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Поиск собеседника')
item2 = types.KeyboardButton('Остановить поиск')
item3 = types.KeyboardButton('Завершить диалог')