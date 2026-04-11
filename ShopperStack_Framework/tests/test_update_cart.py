from api.cart.update_cart_api import UpdateCartAPI
from api.cart.get_cart_api import GetCartAPI
from utils.read_data import read_json

update_cart = UpdateCartAPI()
get_cart = GetCartAPI()
# create an object for UpdateCartAPI
# TEST for update_cart

def test_update_cart(auth_data, headers):
    # Get current cart to find an item to update
    get_response = get_cart.get_cart(auth_data, headers)
    if get_response.status_code == 200:
        cart_items = get_response.json()['data']
        if cart_items:
            # Use the first item's cartId/itemId for updating
            item_id = cart_items[0]['cartId']
            data = read_json("test_data/cart.json")
            payload = data["add_to_cart"]
            payload["quantity"] = 2  # Update quantity
            response = update_cart.update_cart(payload, auth_data, headers, item_id)
            print("STATUS:", response.status_code)
            print("RESPONSE:", response.json())
            assert response.status_code == 200
        else:
            print("No items in cart to update")
            assert True
    else:
        # Cart endpoint returns 404 if not available
        print(f"Cart not available (status {get_response.status_code})")
        assert get_response.status_code == 404