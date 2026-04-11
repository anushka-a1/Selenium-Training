from api.wishlist.add_product_api import AddProductAPI
from utils.read_data import read_json

add_product = AddProductAPI()
# create an object for AddProductAPI
# TEST for add_product

def test_add_product(auth_data, headers):
    data = read_json("test_data/wishlist.json")
    payload = data["add_product"]
    response = add_product.add_product(payload, auth_data, headers)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())
    # Accept both 201 (created) and 409 (already exists) as valid responses
    assert response.status_code in [201, 409]