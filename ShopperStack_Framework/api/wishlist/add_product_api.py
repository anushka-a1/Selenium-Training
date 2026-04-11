from core.base_api import BaseAPI
from utils.config import BASE_URL
class AddProductAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.api = BaseAPI(self.base_url)
    def add_product(self, payload, auth_data, headers):
        shopper_id = auth_data["shopper_id"]
        return self.api.post(f"/shoppers/{shopper_id}/wishlist", json=payload, headers=headers)