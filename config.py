# file: config.py
from os import environ
from dotenv import load_dotenv

# Загрузка значений переменных окружения
load_dotenv()

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
SESSION_STRING = environ.get('SESSION_STRING')
DATABASE_URL = environ.get('DATABASE_URL')
TOKEN_BOT = environ.get('TOKEN_BOT')