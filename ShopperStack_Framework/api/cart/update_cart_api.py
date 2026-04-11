from core.base_api import BaseAPI
from utils.config import BASE_URL

class UpdateCartAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.api = BaseAPI(self.base_url)

    def update_cart(self, payload, auth_data, headers, item_id):
        shopper_id = auth_data["shopper_id"]
        
        return self.api.put(f'/shoppers/{shopper_id}/carts/{item_id}', headers=headers, json=payload)