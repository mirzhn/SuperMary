from telegram import Update
from telegram.ext import ContextTypes
from telegram import Message
from telegram.constants import ParseMode

# посылает в чат текстовое сообщение
async def send_text(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str) -> Message:
    text = text.encode('utf16', errors='surrogatepass').decode('utf16')
    return await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

class Dialog:
    pass