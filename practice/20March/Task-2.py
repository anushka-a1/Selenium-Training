""" Task-2: Search BMRC
and select from and to locations from the dropdown list 
and get details"""

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.bmrc.co.in/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[@class='link top-navcustom-text ']").click()
sleep(5)
# selecting the thrid option
dropdown=driver.find_element(By.XPATH,"(//select[@class='form-control select fare-selects'])[1]")
s=Select(dropdown)
s.select_by_visible_text("Halasuru")
sleep(5)
dropdown2=driver.find_element(By.XPATH,"(//select[@class='form-control select fare-selects'])[2]")
s2=Select(dropdown2)
s2.select_by_visible_text("Cubbon Park")
sleep(5)
driver.find_element(By.XPATH,"(//button)[2]").click()
sleep(5)
driver.close()