import telebot
import os
from loguru import logger

bot = telebot.TeleBot(os.environ['TEMPLATE_TBOT_TOKEN'])

bot.infinity_polling()
