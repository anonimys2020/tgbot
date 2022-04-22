try:
	import telebot
except:
	from os import system as cmd
	cmd('pip install pyTelegramBotAPI')
	cmd('clear')
	import telebot
bot = telebot.TeleBot('5337741203:AAHQjuL43Mh2iNXFxEmLz6b3TcoRsvLEBaE')

@bot.message_handler(commands=['start'])
def start(message):
	mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>!'
	bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['me'])
def get_user_name(message):
	bot.send_message(message.chat.id, f'@{message.from_user.username}')

@bot.message_handler(commands=['clear'])
def clear(message):
	bot.send_message(message.chat.id, 'hi')

@bot.message_handler()
def get_user_text(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')

bot.polling(none_stop=True)