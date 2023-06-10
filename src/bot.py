import telebot
import os
from loguru import logger


class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['TEMPLATE_TBOT_TOKEN'])
        self.send_welcome = self.bot.message_handler(
            commands=['start', 'help']
        )(self.send_welcome)
        self.echo_all = self.bot.message_handler(
            func=lambda message: True
        )(self.echo_all)

    def run(self):
        logger.info("Bot is running...!")
        self.bot.infinity_polling()

    def send_welcome(self, message):
        self.bot.reply_to(message, "Howdy, how are you doing?")

    def echo_all(self, message):
        self.bot.reply_to(message, message.text)


if __name__ == '__main__':
    logger.info('Bot started!')
    bot = Bot()
    bot.run()
