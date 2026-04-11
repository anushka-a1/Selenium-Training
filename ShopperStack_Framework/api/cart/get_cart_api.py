from core.base_api import BaseAPI
from utils.config import BASE_URL
class GetCartAPI():
    def __init__(self):
        self.base_url = BASE_URL
        self.api = BaseAPI(self.base_url)

    def get_cart(self, auth_data, headers):
        shopper_id = auth_data["shopper_id"]
        return self.api.get(f"/shoppers/{shopper_id}/cart", headers=headers)