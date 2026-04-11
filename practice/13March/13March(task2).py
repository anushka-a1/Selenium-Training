""" Task 2 : Using Name
--> Open Facebook
--> Enter email and password """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.NAME,"email").send_keys("N4BpD@example.com")
driver.find_element(By.NAME,"pass").send_keys("123456")
sleep(5)
driver.close()