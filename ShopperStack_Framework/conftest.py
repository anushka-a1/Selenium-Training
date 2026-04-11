import pytest
from core.auth import get_auth_data
# fixture for authentication
@pytest.fixture(scope="session")
def auth_data():
    return get_auth_data()
# fixture for headers
@pytest.fixture(scope="session")
def headers(auth_data):
    return {
        "Authorization": f"Bearer {auth_data['token']}",
        "Content-Type": "application/json"
    }