from core.base_api import BaseAPI
from utils.config import BASE_URL
class LoginAPI():
    def __init__(self):
        self.base_url = BASE_URL
        self.api = BaseAPI(self.base_url)
    def login(self, payload):
        return self.api.post("/users/login", json=payload)