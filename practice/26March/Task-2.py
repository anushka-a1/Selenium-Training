""" Task 2-Write a Selenium script in Python to open the Lenskart website,
1) open the
2) Click on Eyeglasses
3) Validate the url using assert
4) Locate the Sort By  and select the option most Viewed
5) Capture a screenshot of the webpage and save it to your local system """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='EYEGLASSES']").click()
sleep(2)
# validating the url using assert
assert "eyeglasses" in driver.current_url
# locating the Sort By dropdown and selecting the option most Viewed
dropdown=driver.find_element(By.ID,"sortByDropdown")
sleep(2)
select=Select(dropdown)
select.select_by_visible_text("Most Viewed")
# capturing a screenshot of the webpage and saving to local system
folder=os.path.join(os.getcwd(),"screenshot") 
os.makedirs(folder,exist_ok=True) 
driver.save_screenshot(f'{folder}/screenshot(Task-2).png') 
driver.quit()