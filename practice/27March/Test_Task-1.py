""" Task-1: open demo web shop website
click on register
and fill the form using separate test functions """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)
# creating a function to test if clicking on register button works
def test_register():
    driver.find_element(By.LINK_TEXT,"Register").click()
    sleep(2)
# creating a function to fill the form
# creating a function to test if clicking on gender button works
def test_gender():
    driver.find_element(By.ID,"gender-female").click()
    sleep(2)
# creating a function to test if filling the first name works
def test_first_name():
    driver.find_element(By.ID,"FirstName").send_keys("Anushka")
    sleep(2)
# creating a function to test if filling the last name works
def test_last_name():
    driver.find_element(By.ID,"LastName").send_keys("Chaurasia")
    sleep(2)
# creating a function to test if filling the email works
def test_email():
    driver.find_element(By.ID,"Email").send_keys("anushka@example.com")
    sleep(2)
# creating a function to test if filling the password works
def test_password():
    driver.find_element(By.ID,"Password").send_keys("123456")
    sleep(2)
# creating a function to test if filling the confirm password works
def test_confirm_password():
    driver.find_element(By.ID,"ConfirmPassword").send_keys("123456")
    sleep(2)
# creating a function to test if clicking on register button works
def test_register_button():
    driver.find_element(By.NAME,"register-button").click()
    sleep(2)
driver.close()