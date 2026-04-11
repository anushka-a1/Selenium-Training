from api.profile.register_api import RegisterAPI
from utils.read_data import read_json
# create an object for RegisterAPI
register=RegisterAPI()
# TEST for valid user
def test_register_valid():
    # read the test data from json file
    data = read_json("test_data/profile.json")
    # fetch the payload
    payload = data["register_valid_user"]
    response = register.register(payload)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())
    assert response.status_code in [201, 409]

# TEST for invalid user
def test_register_invalid():
    # read the test data from json file
    data = read_json("test_data/profile.json")
    # fetch the payload
    payload = data["register_invalid_user"]
    response = register.register(payload)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())
    assert response.status_code in [400, 404]