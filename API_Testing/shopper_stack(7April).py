import requests
import urllib3
#  The urllib3 library is used to disable SSL certificate verification warnings.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# The base_url variable is set to the base URL of the server's API.
base_url="https://www.shoppersstack.com/shopping"
# The session variable is set to a new requests.Session() object.
session=requests.Session()
# The payload variable is set to a dictionary containing the email, password, and role of the user.
payload={"email":"kusha3444@gmail.com","password":"9879","role":"SHOPPER"}
# The login_res variable is set to the response of a POST request to the server's login API endpoint.
login_res=session.post(f"{base_url}/users/login",json=payload,verify=False) # The verify parameter is set to False to disable SSL certificate verification.
# The if statement checks if the response status code is 200 and if the response text is not empty.
if login_res.status_code == 200 and login_res.text:
    # The data variable is set to the JSON data of the login response.
    data = login_res.json()
    # The token variable is set to the JWT token and the user_id variable is set to the user ID.
    token=data['data']['jwtToken']
    user_id=data['data']['userId']
    # The session headers are updated to include the Authorization header with a value of Bearer + token.
    session.headers.update({"Authorization":"Bearer "+token})
    # The get_res variable is set to the response of a GET request to the server's shopper API endpoint.
    get_res=session.get(f"{base_url}/shoppers/{user_id}",verify=False)
    # The get_res variable is set to the response of a GET request to the server's API endpoint for retrieving user data. The request URL is constructed using the base_url and user_id variables.
    print(get_res.text)
    print(get_res.status_code)
    print(get_res.json())
else:
    print("Login request failed or empty response")
    