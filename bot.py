# -*- coding: utf-8 -*-
import config
import redis
import os
import telebot
from SQLighter import SQLighter
from telegram.ext import Updater

token = os.environ['TELEGRAM_TOKEN']
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(token)

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def new_message(message):
    db = SQLighter(config.database_name)
    mes = db.save_row(message.chat.id, message.text)
    print(mes)
    bot.send_message(message.chat.id, mes)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=token)
updater.bot.set_webhook("https://MYAPP.herokuapp.com/" + TOKEN)
updater.idle()



