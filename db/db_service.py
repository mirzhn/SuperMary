from models import ChatHistory, Request
from .mongo_service import MongoService as service
class DBService:
    def __init__(self, uri: str):
        self.service = service(uri)

    def set(self, object):
        self.service.set(object.__collection__, object.__dict__)

    def get(self, collection, key, value):
        doc = self.service.get(collection, {key: value})
        if collection == 'request':
            return Request(
                session_id=doc['session_id'],
                user_id=doc['user_id'],
                target=doc['target'],
                query=doc['query'], 
                request_id=doc['request_id'],
                dt=doc['dt']
        )
        elif collection == 'chat_history':
            return ChatHistory(
                request_id=doc['request_id'],
                messages=doc['messages'] 
            )
