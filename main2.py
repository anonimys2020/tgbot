try:
	import telebot
except:
	from os import system as cmd
	cmd('pip install pyTelegramBotAPI')
	cmd('clear')
	import telebot
__API = '5337741203:AAHQjuL43Mh2iNXFxEmLz6b3TcoRsvLEBaE'
bot = telebot.TeleBot(__API)

@bot.message_handler(func=lambda _: True)
def on_message(message):
	print(message.text)
	

bot.polling(none_stop=True)