""" Task-1: Search Zomato
and search for your favorite food item
from the dropdown list """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@class='sc-dBfaGr dyyfrm']").send_keys("Pizza")
sleep(5)
driver.find_element(By.XPATH,"//input[@class='sc-dBfaGr dyyfrm']").click()
dropdown=driver.find_elements(By.XPATH,"//p[@class='sc-1hez2tp-0 sc-gFXMyG jkvifB']")
dropdown[7].click()
sleep(5)
driver.close()