from core.base_api import BaseAPI
from utils.config import BASE_URL
class DeleteProductAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.api = BaseAPI(self.base_url)

    def delete_product(self, auth_data, headers, item_id):
        shopper_id = auth_data["shopper_id"]
        # Try DELETE to the wishlist endpoint with itemId as query param
        return self.api.delete(f'shoppers/{shopper_id}/wishlist?itemId={item_id}', headers=headers)