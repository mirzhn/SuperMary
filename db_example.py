from db.db_service import DBService as db
from models import ChatHistory, Request
from config import (DATABASE_URL)
import json

mydb = db(DATABASE_URL)

my_request = Request(
    session_id="19a90a9a-c8fa-4a92-9849-93603b54f0f1", 
    user_id=112233, 
    target="bot", 
    query={"group_link": "telegram.com/group_name","period": "day"}
    )


my_chat_history = ChatHistory(
    request_id="19a90a9a-c8fa-4a92-9849-93603b54f0f1", 
    messages =  {
                    "update_id": 123456791,
                    "channel_post": {
                    "message_id": 13,
                    "chat": {
                        "id": -1001122334455,
                        "title": "Example Group",
                        "type": "supergroup"
                    },
                    "date": 1625898180,
                    "text": "First message in the group!"
                    }
                }
    )

#сохранить реквест
mydb.set(my_request)

#сохранить сообщения из телеги
mydb.set(my_chat_history)

#прочитать конкретный реквест
my_request_from_db = mydb.get('request', 'request_id', '352ce56a-607a-11ef-9362-019e4a8362b9')

#прочитать сообщения по реквесту
my_chat_history_from_db = mydb.get('chat_history', 'request_id', '19a90a9a-c8fa-4a92-9849-93603b54f0f1')