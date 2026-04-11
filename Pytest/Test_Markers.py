# skip markers
""" import pytest
@pytest.mark.skip
def test_skip(reason="This test is skipped"):
    print("This test is skipped")
    assert False
 """
# skip if markers
""" @pytest.mark.skipif(reason="This test is skipped", condition=True)
class Test_Skip:
    def test_skip1(self):
        assert False 

    def test_skip2(self):
        assert True

    def test_skip3(self):
        assert True
 """
# parameterize markers
""" import pytest
@pytest.mark.parametrize("a,b",[(1,2),(4,5)])
def test_add(a,b):
    print(a,b)
    assert a+b == 6
 """

# example of the parameterize markers using the saucedemo website
""" import pytest
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
# giving username and password as paramters and checking multiple users
@pytest.mark.parametrize("username,password", [("standard_user","secret_sauce"),("problem_user","xyz123"),("performance_glitch_user","secret_sauce")])
def test_login(username,password):
    driver=Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    # checking if the login is successful
    assert "inventory" in driver.current_url 
    sleep(2)
    driver.quit()
 """

# fixture markers - A fixture is a function that: provides data or setup, can be reused across tests, can include teardown logic
""" import pytest """
# autouse=True means it makes a fixture run automatically for every test, without explicitly calling it.
""" @pytest.fixture(autouse=True)
def greet():
    print("Hello all")
    yield #here yeild is used to pause a function and return a value, then resume later
    print("Bye")
def test_morning(greet):
    print("Good Morning")
    assert True
def test_evening(greet):
    print("Good Evening")
    assert True
 """

# example of the fixture markers using the demowebshop website
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
import pytest
@pytest.fixture(scope="class")
def setup():
    driver=Chrome()
    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()
    yield driver #yield driver is used here to pass the WebDriver to the test AND still run cleanup after the test
    driver.close()
    sleep(2)

class Test_Register:
    def test_register(self,setup):
        driver=setup
        driver.find_element(By.ID,"gender-female").click()
        sleep(2)

    def test_firstname(self,setup):
        driver=setup
        driver.find_element(By.ID,"FirstName").send_keys("Anushka")
        sleep(2)

    def test_lastname(self,setup):
        driver=setup
        driver.find_element(By.ID,"LastName").send_keys("Chaurasia")
        sleep(2)

    def test_email(self,setup):
        driver=setup
        driver.find_element(By.ID,"Email").send_keys("anushka@example.com")
        sleep(2)

    def test_password(self,setup):
        driver=setup
        driver.find_element(By.ID,"Password").send_keys("123456")
        sleep(2)

    def test_confirmpassword(self,setup):
        driver=setup
        driver.find_element(By.ID,"ConfirmPassword").send_keys("123456")
        sleep(2)

    def test_registerbutton(self,setup):
        driver=setup
        driver.find_element(By.NAME,"register-button").click()
        sleep(2)
    