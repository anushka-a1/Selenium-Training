from api.wishlist.get_product_api import GetProductAPI
from utils.read_data import read_json

get_product = GetProductAPI()
# create an object for GetProductAPI
# TEST for get_product

def test_get_product(auth_data, headers):
    response = get_product.get_product(auth_data, headers)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())
    assert response.status_code == 200
