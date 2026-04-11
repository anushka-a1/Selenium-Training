from core.base_api import BaseAPI
from utils.config import BASE_URL

class UpdateAPI():
    def __init__(self):
        self.base_url = BASE_URL
        self.api = BaseAPI(self.base_url)
    def update(self, payload, auth_data, headers):
        # getting the auth data for fetching the shopper id
        shopper_id = auth_data["shopper_id"]
        return self.api.patch(f"/shoppers/{shopper_id}", json=payload, headers=headers)