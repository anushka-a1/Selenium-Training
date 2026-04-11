# base file for api
import requests

class BaseAPI:

    # initializing the constructor
    def __init__(self, base_url):
        # fetching the base url
        self.base_url = base_url
        # creating the session
        self.session = requests.Session()

    def get(self, endpoint, headers=None, params=None):
        return self.session.get(f"{self.base_url}{endpoint}", headers=headers, params=params, verify=False)

    def post(self, endpoint, headers=None, json=None):
        return self.session.post(f"{self.base_url}{endpoint}", headers=headers, json=json, verify=False)

    def put(self, endpoint, headers=None, json=None):
        return self.session.put(f"{self.base_url}{endpoint}", headers=headers, json=json, verify=False)

    def patch(self, endpoint, headers=None, json=None):
        return self.session.patch(f"{self.base_url}{endpoint}", headers=headers, json=json, verify=False)

    def delete(self, endpoint, headers=None):
        return self.session.delete(f"{self.base_url}{endpoint}", headers=headers, verify=False)