from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler)
import logging
from keys import API_TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

def start_command(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hi dude! Are u ready to build great project!")

def main():
    updater = Updater(token=API_TOKEN)
    dp = updater.dispatcher
    start_handler = CommandHandler('start', start_command)
    dp.add_handler(start_handler)

    updater.start_polling()

