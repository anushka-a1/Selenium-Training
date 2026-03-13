""" Task 1- :
Go to https://selenium.dev/
Click on "Downloads"-(link text)
Click on "Other Pages exist" -(partial link text)
fetch title """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://selenium.dev/")
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT,"Downloads").click() 
sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT,"other").click() 
sleep(5)
print(driver.title)
driver.close()
