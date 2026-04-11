import openpyxl
from sheet02 import func1
import pytest
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
# giving username and password as paramters and checking multiple users
@pytest.mark.parametrize("username,password", func1())
def test_login(driver,username,password):
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    # checking if the login is successful
    assert "inventory" in driver.current_url 
    sleep(2)
    