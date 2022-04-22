import config
from database import Database
import telebot

db = Database('db.db')
bot = telebot.TeleBot(config.API)

@bot.message_handler(commands=['start'])
def start(message):
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = telebot.types.KeyboardButton('Поиск собеседника')
	markup.add(item1)

	bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! Добро пожаловать в анонимный чат! Нажми "Поиск собеседника".', reply_markup=markup)

@bot.message_handler(commands=['menu'])
def menu(message):
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = telebot.types.KeyboardButton('Поиск собеседника')
	markup.add(item1)

	bot.send_message(message.chat.id, message.from_user.first_name, reply_markup=markup)
@bot.message_handler(commands=['stop'])
def stop(message):
	chat_info = db.get_active_chat(message.chat.id)
	if chat_info != False:
		db.delete_chat(chat_info[0])
		markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = telebot.types.KeyboardButton('Поиск собеседника')
		markup.add(item1)

		bot.send_message(chat_info[1], 'Собеседник покинул чат :(', reply_markup=markup)
		bot.send_message(message.chat.id, 'Вы вышли из чата', reply_markup=markup)
	else:
		bot.send_message(message.chat.id, 'Вы не начали чат!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	# bot.send_message(message.chat.id, message.text)
	if message.chat.type == 'private':
		if message.text.lower() == 'поиск собеседника':
			markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = telebot.types.KeyboardButton('Остановить поиск')
			markup.add(item1)

			chat_two = db.get_chat() # id of chat_one user

			if db.create_chat(message.chat.id, chat_two) == False:
				db.add_queue(message.chat.id)
				bot.send_message(message.chat.id, 'Поиск собеседника...', reply_markup=markup)
			else:
				mess = 'Собеседник найден! Чтобы остановить диалог, введите /stop'
				markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
				item1 = telebot.types.KeyboardButton('Завершить диалог')
				# item2 = telebot.types.KeyboardButton('Поиск нового собеседника')
				markup.add(item1)

				bot.send_message(message.chat.id, mess, reply_markup=markup)
				bot.send_message(chat_two, mess, reply_markup=markup)

		elif message.text.lower() == 'остановить поиск':
			db.delete_queue(message.chat.id)
			bot.send_message(message.chat.id, 'Поиск остановлен, напишите /menu')
		elif message.text.lower() == 'завершить диалог':
			stop(message)

		else:
			try:
				chat_info = db.get_active_chat(message.chat.id)
				bot.send_message(chat_info[1], message.text)
			except:
				bot.send_message(message.chat.id, 'Вы не начали диалог!')

bot.polling(none_stop=True)