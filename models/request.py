
import uuid
from datetime import datetime

class Request:
    __collection__ = 'request'
    def __init__(self, session_id: str, user_id: str, target: str, query: str, request_id: str = str(uuid.uuid1()), dt: datetime = datetime.now()):
        self.session_id = session_id
        self.user_id = user_id
        self.target = target
        self.query = query
        self.request_id = request_id
        self.dt = dt
