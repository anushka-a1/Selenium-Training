""" Task-2: Open Demo Web Shop website
Click on Apparels and Shoes
and handle the all three dropdowns """

import select
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)
# clicking on Apparels and Shoes
driver.find_element(By.PARTIAL_LINK_TEXT,"Apparel").click()
sleep(2)
# selecting the option from the first dropdown
dropdown1=driver.find_element(By.XPATH,"//select[@id='products-orderby']")
select1=Select(dropdown1)
select1.select_by_visible_text("Price: Low to High")
sleep(2)
# selecting the option from the second dropdown
dropdown2=driver.find_element(By.XPATH,"//select[@id='products-pagesize']")
select2=Select(dropdown2)
select2.select_by_index(2)
sleep(2)
# selecting the option from the third dropdown
dropdown3=driver.find_element(By.XPATH,"//select[@id='products-viewmode']")
select3=Select(dropdown3)
select3.select_by_visible_text("List")
sleep(2)
driver.close()