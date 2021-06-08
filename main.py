from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          ConversationHandler,
                          CallbackQueryHandler)
from registration import request_language
import time
import logging
from keys import API_TOKEN
from registration import request_language, button
from constants import *
from selector import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


def start_command(update, context):
    chat_id = update.effective_chat.id

    result = cursor.execute(
        "SELECT telegram_id, first_name, last_name from users WHERE telegram_id = '{}'"
            .format(chat_id)).fetchall()
    print(result)
    if len(result) == 0:
        cursor.execute("INSERT INTO users(telegram_id, first_name, last_name) VALUES ('{}', '{}', '{}')"
                       .format(chat_id, update.effective_user.first_name, update.effective_user.last_name))
        connect.commit()
        request_language(update, context)
        return REGISTRATION
    else:
        print('user exists')
        # return MAIN_MENU

        # UPDATE users SET password = '{}' WHERE telegram_id = '{}'.format(password, chat_id)
        # connect.commit()
    # context.bot.send_message(chat_id=chat_id, text="Hi dude! Are u ready to build great project!")
    # time.sleep(0.5)
    # choose_language(update, context)


def main():
    updater = Updater(token=API_TOKEN)
    dp = updater.dispatcher

    registration_conversation = ConversationHandler(
        entry_points=[CallbackQueryHandler(callback=button)],
        states={

        },

        fallbacks=[

        ],
        map_to_parent={

        }
    )

    main_conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', start_command)
        ],

        states={
            REGISTRATION: [
                registration_conversation
            ],
        },

        fallbacks=[]

    )

    dp.add_handler(main_conversation)

    updater.start_polling()
    updater.idle()
