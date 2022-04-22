# try:
import sqlite3
import telebot
import config
# from os import system as cmd
# except:
# 	from os import system as cmd
# 	cmd('pip install sqlite3')
# 	cmd('clear')
# 	import sqlite3
bot = telebot.TeleBot(config.API)
class Database:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

        # self.cursor.execute("CREATE TABLE IF NOT EXISTS chats(id INTEGER PRIMARY KEY AUTOINCREMENT, chat_1 VARCHAR(255) NOT NULL, chat_2 VARCHAR(255) NOT NULL);")
        # self.cursor.execute("CREATE TABLE IF NOT EXISTS queue(id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id VARCHAR (255) NOT NULL);")


    def add_queue(self, chat_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `queue` (`chat_id`) VALUES (?)", (chat_id,))

    def delete_queue(self, chat_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM `queue` WHERE `chat_id` = ?", (chat_id,))

    def delete_chat(self, id_chat):
        # print(id_chat)
        with self.connection:
            return self.cursor.execute("DELETE FROM `chats` WHERE `chat_1` = ?", (id_chat,))
    def get_chat(self):
        with self.connection:
            chat = self.cursor.execute("SELECT * FROM `queue`", ()).fetchmany(1)
            if(bool(len(chat))):
                for row in chat:
                    return row[1]
            else:
                return False
    def create_chat(self, chat_one, chat_two):
        with self.connection:
            if chat_two != 0:
                # Создание чата
                self.cursor.execute("DELETE FROM `queue` WHERE `chat_id` = ? ", (chat_two,))
                self.cursor.execute("INSERT INTO `chats` (`chat_1`, `chat_2`) VALUES (?,?);", (chat_one, chat_two,))
                return True
            else:
                # В очередь
                return False
    def get_active_chat(self, chat_id):
        chat_info = ''
        with self.connection:
            chat = self.cursor.execute("SELECT * FROM `chats` WHERE `chat_1` = ?", (chat_id,))
            id_chat = 0
            for row in chat:
                # print(row)
                id_chat = row[0]
                chat_info = [row[1], row[2]]
            # print(id_chat, chat_info, chat_id)
            if id_chat == 0:
                chat = self.cursor.execute("SELECT * FROM `chats` WHERE `chat_2` = ?", (chat_id,))
                # print(chat_id)
                for row in chat:
                    id_chat = row[0]
                    chat_info = [row[0], row[1]]
                if chat_id == 0:
                    return False
                else:
                    return chat_info
            else:
                return chat_info
class Connect:
    def __init__(self, database_file, sql=None, value=None):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        if sql and value:
            try:
                with self.connection:
                    return self.cursor.execute(sql, value)
            except:
                pass