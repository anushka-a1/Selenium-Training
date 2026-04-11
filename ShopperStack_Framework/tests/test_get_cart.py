from api.cart.get_cart_api import GetCartAPI
from utils.read_data import read_json

get_cart = GetCartAPI()
# create an object for GetCartAPI
# TEST for get_cart

def test_get_cart(auth_data, headers):
    response = get_cart.get_cart(auth_data, headers)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())
    # Accept 200 (success) or 404 (cart not available)
    assert response.status_code in [200, 404]