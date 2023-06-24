import os

import telebot
from loguru import logger

from src.constants import keyboards
from src.utils.io import write_json

bot = telebot.TeleBot(os.environ['TEMPLATE_TBOT_TOKEN'])


class Bot:
    """Template for Telegram Bot
    """
    def __init__(self, telebot):

        self.bot = telebot

        # register handlers
        self.handlers()

        # run bot
        logger.info("Bot is running...!")
        self.bot.infinity_polling()

    def handlers(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            self.bot.reply_to(message, "Howdy, how are you doing?")

        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            write_json(message.json, 'messages')
            self.bot.send_message(
                message.chat.id, message.text,
                reply_markup=keyboards.main
            )


if __name__ == '__main__':
    logger.info('Bot started!')
    bot = Bot(bot)
