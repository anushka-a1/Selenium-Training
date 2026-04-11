from api.profile.login_api import LoginAPI
from utils.read_data import read_json
login=LoginAPI()
# create an object for LoginAPI
# TEST for valid user
def test_login_valid():
    # read the test data from json file
    data = read_json("test_data/profile.json")
    # fetch the payload
    payload = data["login_valid_user"]
    response = login.login(payload)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())
    assert response.status_code == 200

# TEST for invalid user
def test_login_invalid():
    # read the test data from json file
    data = read_json("test_data/profile.json")
    # fetch the payload
    payload = data["login_invalid_user"]
    response = login.login(payload)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())
    assert response.status_code in [400, 401]