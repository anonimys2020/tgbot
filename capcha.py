# =====================================================
# Если Вы добавляете в готового бота - это Вам не нужно.
import telebot
import random
from telebot import types
import config
from database import Connect
Connect('db.db')

bot = telebot.TeleBot(config.API)
# =====================================================
captcha_list = ["яблоко", "арбуз", "банан", "виноград", "морковь",
                "кукуруза"]  # это название всех элементов с капчи, можете поставить что угодно
# ================
cp1 = ""  # смайлики в капче.
cp2 = ""
cp3 = ""
cp4 = ""
cp5 = ""
cp6 = ""
# ================
completecaptcga = []


# вместо 999 вставьте ID, у которого никогда не будет требовать капчу!

@bot.message_handler(commands=["start"])
def start_captcha(message):
    ms = message.chat.id
    if ms in completecaptcga:
        bot.send_message(message.chat.id, 'Вы уже прошли проверку')  # если юзер прошел проверку, тут уже вашего бота вставлять
    else:
        # Это внутреняя клавиатура, которая содержит в себе символы, на которые нажимает человек.
        keyboard = types.InlineKeyboardMarkup()
        cpt1 = types.InlineKeyboardButton(text=cp1, callback_data="cpt1")
        cpt2 = types.InlineKeyboardButton(text=cp2, callback_data="cpt2")
        cpt3 = types.InlineKeyboardButton(text=cp3, callback_data="cpt3")
        keyboard.add(cpt1, cpt2, cpt3)
        cpt1 = types.InlineKeyboardButton(text=cp4, callback_data="cpt4")
        cpt2 = types.InlineKeyboardButton(text=cp5, callback_data="cpt5")
        cpt3 = types.InlineKeyboardButton(text=cp6, callback_data="cpt6")
        keyboard.add(cpt1, cpt2, cpt3)
        markdown = """
        *bold text*
        _italic text_
        [text](URL)
        """
        global emoji
        emoji = random.choice(captcha_list)
        global dostup
        dostup = 0
        # само сообщение с капчей.
        bot.send_message(message.chat.id,
                         'Чтобы продолжить пользоваться ботом, выберите на клавиатуре' + '*' + emoji + '*',
                         parse_mode="Markdown", reply_markup=keyboard)


# тут проверки, верно ли нажал человек. Изменять только текст, остальное не трогать!
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "cpt1":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[0:1]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=' Проверка пройдена успешно!')
                    completecaptcga.append(call.message.chat.id)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы нажали не на тот символ!')
        if call.data == "cpt2":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[1:2]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=' Проверка пройдена успешно!')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы нажали не на тот символ!')
        if call.data == "cpt3":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[2:3]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=' Проверка пройдена успешно!')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы нажали не на тот символ!')
        if call.data == "cpt4":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[3:4]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=' Проверка пройдена успешно!')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы нажали не на тот символ!')
        if call.data == "cpt5":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[4:5]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=' Проверка пройдена успешно!')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы нажали не на тот символ!')
        if call.data == "cpt6":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[5:6]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=' Проверка пройдена успешно!')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы нажали не на тот символ!')


bot.polling()
# =====================================================
# Если Вы добавляете в готового бота - это Вам не нужно.
class Bot:
    def __init__(self, bot, message, completecaptcga=list):

# =====================================================
        self.captcha_list = ["яблоко", "арбуз", "банан", "виноград", "морковь", "кукуруза"]  # это название всех элементов с капчи, можете поставить что угодно

        self.cp1 = ""  # смайлики в капче.
        self.cp2 = ""
        self.cp3 = ""
        self.cp4 = ""
        self.cp5 = ""
        self.cp6 = ""

        self.completecaptcga = completecaptcga



        self.ms = message.chat.id
        if self.ms in self.completecaptcga:
            bot.send_message(message.chat.id, 'Вы уже прошли проверку')  # если юзер прошел проверку, тут уже вашего бота вставлять
        else:
            # Это внутреняя клавиатура, которая содержит в себе символы, на которые нажимает человек.
            keyboard = types.InlineKeyboardMarkup()
            cpt1 = types.InlineKeyboardButton(text=cp1, callback_data="cpt1")
            cpt2 = types.InlineKeyboardButton(text=cp2, callback_data="cpt2")
            cpt3 = types.InlineKeyboardButton(text=cp3, callback_data="cpt3")
            keyboard.add(cpt1, cpt2, cpt3)
            cpt1 = types.InlineKeyboardButton(text=cp4, callback_data="cpt4")
            cpt2 = types.InlineKeyboardButton(text=cp5, callback_data="cpt5")
            cpt3 = types.InlineKeyboardButton(text=cp6, callback_data="cpt6")
            keyboard.add(cpt1, cpt2, cpt3)
            markdown = """
            *bold text*
            _italic text_
            [text](URL)
            """
            self.emoji = random.choice(self.captcha_list)
            self.dostup = 0
            # само сообщение с капчей.
            bot.send_message(message.chat.id, 'Чтобы продолжить пользоваться ботом, выберите на клавиатуре' + '*' + self.emoji + '*', parse_mode="Markdown", reply_markup=keyboard)


        # тут проверки, верно ли нажал человек. Изменять только текст, остальное не трогать!
        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.message:
                if call.data == "cpt1":
                    ms = call.message.chat.id
                    if ms in completecaptcga:
                        bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                    else:
                        check = captcha_list[0:1]
                        check = check[0]
                        if emoji == check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text=' Проверка пройдена успешно!')
                            completecaptcga.append(call.message.chat.id)
                        else:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text='Вы нажали не на тот символ!')
                if call.data == "cpt2":
                    ms = call.message.chat.id
                    if ms in completecaptcga:
                        bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                    else:
                        check = captcha_list[1:2]
                        check = check[0]
                        if emoji == check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text=' Проверка пройдена успешно!')
                            completecaptcga.append(call.message.chat.id)
                        if emoji != check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text='Вы нажали не на тот символ!')
                if call.data == "cpt3":
                    ms = call.message.chat.id
                    if ms in completecaptcga:
                        bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                    else:
                        check = captcha_list[2:3]
                        check = check[0]
                        if emoji == check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text=' Проверка пройдена успешно!')
                            completecaptcga.append(call.message.chat.id)
                        if emoji != check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text='Вы нажали не на тот символ!')
                if call.data == "cpt4":
                    ms = call.message.chat.id
                    if ms in completecaptcga:
                        bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                    else:
                        check = captcha_list[3:4]
                        check = check[0]
                        if emoji == check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text=' Проверка пройдена успешно!')
                            completecaptcga.append(call.message.chat.id)
                        if emoji != check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text='Вы нажали не на тот символ!')
                if call.data == "cpt5":
                    ms = call.message.chat.id
                    if ms in completecaptcga:
                        bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                    else:
                        check = captcha_list[4:5]
                        check = check[0]
                        if emoji == check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text=' Проверка пройдена успешно!')
                            completecaptcga.append(call.message.chat.id)
                        if emoji != check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text='Вы нажали не на тот символ!')
                if call.data == "cpt6":
                    ms = call.message.chat.id
                    if ms in completecaptcga:
                        bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                    else:
                        check = captcha_list[5:6]
                        check = check[0]
                        if emoji == check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text=' Проверка пройдена успешно!')
                            completecaptcga.append(call.message.chat.id)
                        if emoji != check:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text='Вы нажали не на тот символ!')