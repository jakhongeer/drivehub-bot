from telegram.ext import InlineQueryHandler, callbackqueryhandler, CallbackContext, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from texts import greeting

def choose_language(update, context):
    chat_id = update.effective_chat.id
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 Ozbekcha", callback_data='uz'),
            InlineKeyboardButton("🇷🇺 Русский", callback_data='ru'),
            InlineKeyboardButton("🇬🇧 English", callback_data='en')
         ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Choose the language: ', reply_markup=reply_markup)


def button(update: Update, _: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(greeting[query.data])