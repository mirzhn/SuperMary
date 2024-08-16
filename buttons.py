from telebot import types

user_dictionaries = {} # Словарь для хранения экземпляров класса WordDictionary для каждого пользователя

btn_createsearch = types.KeyboardButton("🔍 Создать поиск")
btn_delsearch = types.KeyboardButton("📝 Редактировать поиск")
btn_editsearch = types.KeyboardButton("❌ Удалить поиск")
btn_addword = types.KeyboardButton("📝 Добавить слово")
btn_addchat = types.KeyboardButton("📝 Добавить чат")
btn_delword = types.KeyboardButton("❌ Удалить слово")
btn_delchat = types.KeyboardButton("❌ Удалить чат")
btn_help = types.KeyboardButton("☝ Помощь!")
btn_back = types.KeyboardButton('Назад')

markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
#markup_start.row(btn_crtsearch)
markup_start.row(btn_createsearch, btn_delsearch)
markup_start.row(btn_editsearch, btn_help)

markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
markup_back.row(btn_back)

mark_intosearch = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
mark_intosearch.row(btn_addchat, btn_addword)
mark_intosearch.row(btn_delchat, btn_delword)
mark_intosearch.row(btn_back)

states = {}

# Константы состояний
STATE_ADD_WORDS = 'Add words'
STATE_ADD_CHATS = 'Add chats'
STATE_ADD_SEARCH = 'Create Search'
STATE_DEL_SEARCH = 'Delete Search'
STATE_DEL_CHATS = 'Delete Chat'
STATE_DEL_WORDS = 'Delete Word'


help_text_ru = """
Приветствую вас здесь!

Вот несколько советов, которые помогут вам правильно настроить ваш Поиск:

------

При добавлении чата для Поиска, необходимо добавить ссылку на чат, например, https://t.me/yurydud

------

Чтобы не добавлять множество слов с разными окончаниями, можно использовать только часть слова. Например, добавление слова "расклад" перешлет вам сообщения, содержащие слова: "раскладка", "раскладной", "раскладываемая" и т.д.

------

Если вы хотите, чтобы в тексте сообщения было найдено сразу несколько слов, то их можно перечислить через запятую при добавлении. Например, "BMW, 2024" будет искать сообщения, которые одновременно содержат слова "BMW" и "2024".

"""

def add_words(message, bot): 
    user = message.from_user.id
    states[user] = STATE_ADD_WORDS
    bot.send_message(user, '❓ Введите слово для Поиска', reply_markup=markup_back)

def add_chats(message, bot): 
    user = message.from_user.id
    states[user] = STATE_ADD_CHATS
    bot.send_message(user, '❓ Введите чат для Поиска', reply_markup=markup_back)
