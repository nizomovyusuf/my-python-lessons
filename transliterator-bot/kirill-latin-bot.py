# -*- coding: utf-8 -*-
"""
КИРИЛЛ-LOTIN TELEGRAM BOT

Muallif: Nizomov Yusuf

@author: GithubDesktop\my-python-lessons
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '7161448053:AAFuCcslUlNuM0u5Enm8UPVKP7PRa9SygP0'
bot = telebot.TeleBot(TOKEN, parse_mode = None)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    answer = "Assalomu alaykum, Xush kelibsiz!"
    answer += "\nMatn kiriting:"
    bot.reply_to(message, answer)

@bot.message_handler(func = lambda  message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg)  if  msg.isascii()  else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()


