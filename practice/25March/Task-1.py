""" Task-1: go to saucedemo.com
give username and password,
if login fails,take screenshot
if it logins, then use assertion to validate """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
sleep(5)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
sleep(2)
ele=driver.find_element(By.ID,"password").send_keys("secret_sauce")
sleep(2)
driver.find_element(By.ID,"login-button").click()
# using try and except to check if login is successful
try:
    # using assertion
    assert "inventory" in driver.current_url
    print("Login is successful")
except:
    print("Login is not successful")
    # taking screenshot if login is not successful
    driver.save_screenshot("screenshot1.png")
driver.close()