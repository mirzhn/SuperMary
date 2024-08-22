import telebot
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from config import (SESSION_STRING, API_ID, API_HASH, TOKEN_BOT)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
bot = telebot.TeleBot(TOKEN_BOT)