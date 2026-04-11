# importing the requests module
""" import requests
# fetching get request from the url - store
response=requests.get("https://petstore.swagger.io/v2/store/inventory")
print(response.text) # to print the response text
print(response.status_code) # to print the status code
print(response.json())  # to print the response in json format
# to print the value of the key
print(response.json()['hungry'])
# to check the status code using assert
expected=300
actual=response.status_code
# if not equal then print the message")
assert expected == actual, "Status code mismatch, It is: "+str(response.status_code) # to print the status code, response is a object of class requests.Response, so we can access the status_code attribute of the object using response.status_code
 """


# fetching post request from the url - pet
""" import requests
response=requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=SOLD")
print(response.text) # to print the response text
print(response.status_code) # to print the status code
print(response.json())  # to print the response in json format
# to print the value of the key 
print(response.json()[0]['name'])
print(response.json()[0]['id'])
 """

# fetch post request for pet
""" import requests
payload = {
  "id": 1200,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Pepper",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response= requests.post("https://petstore.swagger.io/v2/pet",json=payload)
print(response.status_code) 
assert response.status_code == 200, "Status code mismatch, It is: "+str(response.status_code)
print("Status code is 200")
 """
# fetch put request for pet
""" import requests
payload = {
  "id": 100,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Beau",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response= requests.put("https://petstore.swagger.io/v2/pet",json=payload)   
print(response.status_code)         
assert response.status_code == 200, "Status code mismatch, It is: "+str(response.status_code)
print("Status code is 200")
 """

# deleting request for pet
""" import requests
response= requests.delete("https://petstore.swagger.io/v2/pet/100")   
print(response.status_code)         
assert response.status_code == 200, "Status code mismatch, It is: "+str(response.status_code)
print("Status code is 200")
 """

#performing get, post, put and delete request using function and returning the id
import requests
def post():
    payload = {
      "id": 101,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "mini",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    response= requests.post("https://petstore.swagger.io/v2/pet",json=payload)
    print(response.status_code) 
    assert response.status_code == 200, "Status code mismatch, It is: "+str(response.status_code)
    print("Pet added, Status code is 200")
    return response.json()['id']
    
id = post()

def put(id):
    payload = {
      "id": 101,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "max",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    response= requests.put("https://petstore.swagger.io/v2/pet",json=payload)
    print(response.status_code) 
    assert response.status_code == 200, "Status code mismatch, It is: "+str(response.status_code)
    print("Pet updated, Status code is 200")
    

def delete(id):
    response= requests.delete("https://petstore.swagger.io/v2/pet"+str(id))   
    print(response.status_code)         
    assert response.status_code == 200, "Status code mismatch, It is: "+str(response.status_code)
    print("Pet deleted, Status code is 200")

put(id)
delete(id)