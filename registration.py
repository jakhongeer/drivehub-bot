from telegram.ext import (Updater,
                          InlineQueryHandler,
                          CallbackContext,
                          CallbackQueryHandler)
from telegram import (InlineKeyboardMarkup,
                      InlineKeyboardButton,
                      InlineQuery,
                      KeyboardButton,
                      ReplyKeyboardMarkup,
                      Update)

def choose_language(update, context):
    """Sends a message with three inline buttons attached."""
    keyboard = [[
            InlineKeyboardButton("O'zbekcha", callback_data='uz'),
            InlineKeyboardButton("Русский", callback_data='ru'),
            InlineKeyboardButton("English", callback_data='en')
    ]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Choose the langugage:', reply_markup=reply_markup)


