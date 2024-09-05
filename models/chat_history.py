
class ChatHistory:
    __collection__ = 'chat_history'
    def __init__(self, request_id: str, messages: str):
        self.request_id = request_id
        self.messages = messages