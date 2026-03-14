""" Task 1 : Using ID
--> Open Amazon
--> Click on Update Location """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"nav-global-location-popover-link").click()
sleep(2)
driver.close()   
