""" # single select dropdown
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("http://127.0.0.1:5500/E22_Dropdowns.html")
driver.maximize_window()
driver.implicitly_wait(5)
dropdown=driver.find_element(By.ID,"state")
s=Select(dropdown)
# printing all options
all_options=s.options
for option in all_options:
    print(option.text)
# select by visible text
# s.select_by_visible_text("West Bengal")
# sleep(2)
# select by value
# s.select_by_value("MH") #'MH' is the value of the option 
sleep(2)
# select by index
s.select_by_index(3) #indexing starts from 0
# we can select only single option here because it is single select dropdown

# multiselect dropdown
# selecting multiple options
multi_dropdown=driver.find_element(By.ID,"hobby")
drop=Select(multi_dropdown)
drop.select_by_visible_text("Dance")
drop.select_by_visible_text("Music")
sleep(2)
# deselecting multiple options
# deselect by visible text
drop.deselect_by_visible_text("Dance")
# deselect by value
# drop.deselect_by_value("music")
# deselect by index
# drop.deselect_by_index(2)
# deselect all options
drop.deselect_all()
sleep(2)
driver.close() """

# custom dropdowns example using amazon website
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes for women")
sleep(5)
dropdown=driver.find_elements(By.XPATH,"//div[@class='s-suggestion-container']")
# fetching all the names of product searched from the dropdown
for i in dropdown:
    print(i.text)
# selecting the thrid option
dropdown[2].click()
sleep(5)
