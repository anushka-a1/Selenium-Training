from core.base_api import BaseAPI
from utils.config import BASE_URL

class DeleteCartAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.api = BaseAPI(self.base_url)

    def delete_cart(self, auth_data, headers, product_id):
        shopper_id = auth_data["shopper_id"]
        return self.api.delete(f'/shoppers/{shopper_id}/carts/{product_id}', headers=headers)