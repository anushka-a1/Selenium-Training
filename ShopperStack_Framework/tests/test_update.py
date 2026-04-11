from api.profile.update_api import UpdateAPI
from utils.read_data import read_json
# create an object for UpdateAPI
update=UpdateAPI()
# TEST for update

def test_update(auth_data, headers):
    data = read_json("test_data/profile.json")
    payload = data["update_user"]
    response = update.update(payload, auth_data, headers)
    assert response.status_code == 200
