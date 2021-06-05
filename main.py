from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          CallbackQueryHandler)
import time
import logging
from keys import API_TOKEN
from registration import choose_language, button
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

def start_command(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hi dude! Are u ready to build great project!")
    time.sleep(0.5)
    choose_language(update, context)


def main():
    updater = Updater(token=API_TOKEN)
    dp = updater.dispatcher
    start_handler = CommandHandler('start', start_command)
    dp.add_handler(start_handler)
    dp.add_handler(CommandHandler('lang', choose_language))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()

