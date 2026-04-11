from core.base_api import BaseAPI
from utils.config import BASE_URL
class RegisterAPI():
    def __init__(self):
        self.base_url = BASE_URL
        self.api = BaseAPI(self.base_url)
    def register(self, payload):
        return self.api.post("/shoppers", json=payload)