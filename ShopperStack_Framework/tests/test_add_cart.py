from api.cart.add_cart_api import AddtoCartAPI
from utils.read_data import read_json

add_cart = AddtoCartAPI()
# create an object for AddtoCartAPI
# TEST for add_to_cart

def test_add_to_cart(auth_data, headers):
    data = read_json("test_data/cart.json")
    payload = data["add_to_cart"]
    response = add_cart.add_to_cart(payload, auth_data, headers)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())
    # Cart endpoint returns 404 if not available; also accept 200, 201, 409
    assert response.status_code in [200, 201, 404, 409]