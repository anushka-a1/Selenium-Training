""" Task1 : Perform API Testing for the ShopperStack Swagger UI and perform the following actions:-
1. Post a request to register a user
2. Post a request to login
3. Get a request to fetch the user  """
 
import requests
#Function  to create a new Shopper Account
def register():
    payload = {
    "city": "Kota",
    "country": "India",
    "email": "kusha3444@gmail.com",
    "firstName": "Kusha",
    "gender": "FEMALE",
    "lastName": "Chaurasia",
    "password": "9879",
    "phone": 9107696561,
    "state": "Rajasthan",
    "zoneId": "ALPHA"
    }
    # Send POST request to create user
    response = requests.post("https://www.shoppersstack.com/shopping/shoppers", json=payload,verify=False) # verify = False to pass SSl certificate
    # Output API response
    print(response.text)    
    # checking the status code
    assert response.status_code==201, "Status code is not 201, It is: "+str(response.status_code)
    print("User Registered with status code 201")
    return response.json()['data']['userId'] # returning the userId 

userId = register()

# Function to authenticate the created user
def login():
    payload = {
    "email": "kusha3444@gmail.com",
    "password": "9879",
    "role": "SHOPPER"
    }
    # Send POST request to login
    response = requests.post("https://www.shoppersstack.com/shopping/users/login", json=payload,verify=False)
    # Output API response
    print(response.text)
    # Validate login success
    assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
    print("User logged in with status code 200")
    return response.json()['data']['jwtToken'] # returning the jwtToken

Token = login()

# Prepare authorization header using JWT token
headers = {
    "Authorization": "Bearer " + Token
}

# Send GET request to fetch user details
response = requests.get(f"https://www.shoppersstack.com/shopping/shoppers/{userId}",headers=headers,verify=False) 
# Output API response
print(response.text)
# Validate successful retrieval
assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
print("User fetched with status code 200")
