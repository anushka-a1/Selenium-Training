import pytest
from selenium import webdriver  
@pytest.fixture(scope="function")
def driver():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(5)
    yield driver 
    driver.quit()
