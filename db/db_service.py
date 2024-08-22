from models import ChatHistory, Request
from .mongo_service import MongoService as service
import json
class DBService:
    def __init__(self, uri: str):
        self.service = service(uri)

    def set(self, object):
        self.service.set(object.__collection__, object.__dict__)

    def get(self, collection, key, value):
        return self.service.get(collection, {key: value})