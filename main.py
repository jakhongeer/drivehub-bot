from telegram.ext import (Updater,
                          CallbackContext,
                          CommandHandler,
                          MessageHandler,
                          ConversationHandler)
from telegram import Update
import logging
from keys import API_TOKEN
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)

# just a commit ;)


def start_command(update, context):
    context.bot.send_message(chat_id=update.effective_user.id, text="Hi r u ready to start?")


registration_conversation = ConversationHandler(
    entry_points=[CommandHandler('start', start_command)],

    states= {

    },

    fallbacks=[]

)


def main():
    updater=Updater(token=API_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(registration_conversation)

    updater.start_polling()
    updater.idle()
