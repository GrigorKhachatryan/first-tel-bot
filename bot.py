#!/usr/bin/env python
import random
import pickle

import telebot
from telebot.types import Message


TOKEN = '805207737:AAEyCqMS39E39OsSihT0l_hX_ITdyu4n00A'

bot = telebot.TeleBot(TOKEN)

USERS = set()
@bot.message_handler(commands=['start','help'])

def command_hendler(message: Message):
    bot.reply_to(message, 'это пока что не работает')

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_gigits(message: Message):
    if message.from_user.id in USERS:
        bot.reply_to(message,f"{message.from_user.first_name}, братан!")
    else:
        bot.reply_to(message, 'Покурим кальян?')
        USERS.add(message.from_user.id)



bot.polling(timeout=60)
