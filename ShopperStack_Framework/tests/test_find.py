from api.profile.find_api import FindAPI
# create an object for FindAPI
find=FindAPI()
# TEST for find

def test_find(auth_data, headers):
    response = find.find(auth_data, headers)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())
    assert response.status_code == 200