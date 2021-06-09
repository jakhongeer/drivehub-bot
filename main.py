from telegram.ext import (Updater,
                          CallbackContext)
import logging
from keys import API_TOKEN
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_user.id, text="Hi R u read to start?")

def main():
    updater=Updater(token=API_TOKEN, use_context=True)
    updater.start_polling()
    updater.idle()