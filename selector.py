import sqlite3

connect = sqlite3.connect('database.sqlite3', check_same_thread=False)
cursor = connect.cursor()


def get_id(update):
    chat_id = update.effective_chat.id
    return cursor.execute("SELECT id FROM users WHERE telegram_id = '{}'".format(chat_id)).fetchone()[0]


def lang(update):
    return cursor.execute("SELECT language FROM users WHERE id = '{}'"
                          .format(get_id(update))).fetchone()[0]
