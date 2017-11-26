import config
import telebot
from SQLighter import SQLighter

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def new_message(message):
    db = SQLighter(config.database_name)
    mes = db.save_row(message.chat.id, message.text)
    print(mes)
    bot.send_message(message.chat.id, mes)

if __name__ == '__main__':
    bot.polling(none_stop=True)
