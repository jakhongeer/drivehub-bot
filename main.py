from telegram.ext import (Updater,
                          CallbackContext,
                          CommandHandler,
                          MessageHandler,)
from telegram import Update
import logging
from keys import API_TOKEN
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)


def start_command(update, context):
    context.bot.send_message(chat_id=update.effective_user.id, text="Hi r u ready to start?")




def main():
    updater=Updater(token=API_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))

    updater.start_polling()
    updater.idle()