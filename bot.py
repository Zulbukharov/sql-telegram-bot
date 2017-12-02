# -*- coding: utf-8 -*-
import config
import redis
import os
import telebot
from SQLighter import SQLighter

import os


TOKEN = os.environ['TELEGRAM_TOKEN']
PORT = int(os.environ.get('PORT', '5000'))

bot = telebot.TeleBot(token)

updater = bot.Updater(TOKEN)
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

