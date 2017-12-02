# -*- coding: utf-8 -*-
import config
import redis
import os
import telebot
from SQLighter import SQLighter

import os


TOKEN = os.environ['TELEGRAM_TOKEN']
PORT = int(os.environ.get('PORT', '5000'))

updater = Updater(TOKEN)
# add handlers

@bot.message_handler(content_types=["text"])
def new_message(message):
    db = SQLighter(config.database_name)
    mes = db.save_row(message.chat.id, message.text)
    print(mes)
    bot.send_message(message.chat.id, mes)


updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://sql1telegram1bot.herokuapp.com/" + TOKEN)
updater.idle()

bot = telebot.TeleBot(token)

if __name__ == '__main__':
    bot.polling(none_stop=True)
