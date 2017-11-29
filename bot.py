# -*- coding: utf-8 -*-
import redis
import os
import telebot

token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']

from SQLighter import SQLighter
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def new_message(message):
    db = SQLighter(config.database_name)
    mes = db.save_row(message.chat.id, message.text)
    print(mes)
    bot.send_message(message.chat.id, mes)

if __name__ == '__main__':
    bot.polling(none_stop=True)
