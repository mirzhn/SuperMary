from pymongo import MongoClient

class MongoService:
    def __init__(self, uri: str):
        self.uri = uri
        self.client = MongoClient(self.uri)
        self.db = self.client.get_default_database()

    def has_access_to_db(self):
        try:
            with MongoClient(self.uri) as client:
                client.admin.command('ping')
            return True
        except:
            return False
        
    def set(self, collection, document):
        collection = self.db[collection]
        result = collection.insert_one(document)
        return result.inserted_id
    
    def get(self, collection, query=None):
        collection = self.db[collection]
        documents = collection.find(query)
        result = list(documents)
        return result
    

