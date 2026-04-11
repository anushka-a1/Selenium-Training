""" Task 1: create a function to post a request for pet
fetch id
create a function to update and delete the pet using id """

# fetch post request for pet
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
# fetch put request for pet
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
    
# delete the pet by id
def delete(id):
    response= requests.delete("https://petstore.swagger.io/v2/pet"+str(id))   
    print(response.status_code)         
    assert response.status_code == 200, "Status code mismatch, It is: "+str(response.status_code)
    print("Pet deleted, Status code is 200")

put(id)
delete(id)