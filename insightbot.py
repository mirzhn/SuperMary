from login import bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config import *
from util import send_text, Dialog
from telebot import types
from telegram import BotCommandScopeChat, Update

# Начало работы. Доступна кнопка "Создать отчет"
async def start(update, context):
    await context.bot.delete_my_commands(scope=BotCommandScopeChat(chat_id=update.effective_chat.id))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_create_report = types.KeyboardButton(text='🔍 Создать поиск')
    markup.add(button_create_report)
    bot.send_message(update.effective_chat.id, 'Привет! Для создания своего поиска используйте кнопку "🔍 Создать поиск"', reply_markup=markup)

async def choose_chat(update, context):
    dialog.mode = "choose_chat"
    await send_text(update, context, 'Здравствуйте, введите ссылку на чат')

async def message_processing(update, context):
    if dialog.mode == "choose_chat":
        await check_chat(update, context)

async def check_chat(update, context):
    text = update.message.text
    if text == "1":
        await send_text(update, context, 'Ссылка не действительна, убедитесь, что вы предоставили корректную ссылку')
    else:
        await choose_period(update, context)

async def choose_period(update, context):
    markup = types.InlineKeyboardMarkup()
    button_day = types.InlineKeyboardButton("День", callback_data='choose_period_День')
    button_week = types.InlineKeyboardButton("Неделя", callback_data='choose_period_Неделя')
    button_month = types.InlineKeyboardButton("Месяц", callback_data='choose_period_Месяц')
    button_back = types.InlineKeyboardButton("Назад", callback_data='back')

    markup.row(button_day, button_week)
    markup.row(button_month, button_back)

    bot.send_message(update.effective_chat.id, 'Выберете период отчета', parse_mode='html', reply_markup=markup)

async def create_report(update, context):
    query = update.callback_query.data
    await send_text(update, context, 'Вы выбрали период - ' + query[14:])
    await send_text(update, context, 'Отчет формируется, пожалуйста, подождите...')

app = ApplicationBuilder().token(TOKEN_BOT).build()
dialog = Dialog()
dialog.mode = None

def main():
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.Text(['🔍 Создать поиск']), choose_chat))

    #Для обработки сообщений пользователя
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_processing))

    #callback
    app.add_handler(CallbackQueryHandler(choose_chat, pattern="back"))
    app.add_handler(CallbackQueryHandler(create_report, pattern="choose_period_*"))
    app.add_handler(CallbackQueryHandler(choose_chat, pattern="choose_chat"))
    app.run_polling()

if __name__ == "__main__":
    main()
