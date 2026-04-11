""" Task-2: Open Flipkart
Search for any item
Click Search
Fetch the price of item using its name (Traversing)"""

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,"//span[@role='button']").click()
driver.find_element(By.NAME,"q").send_keys("Lipstick")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(5)
price=driver.find_element(By.XPATH,"//a[text()='SWISS BEAUTY Pure Matte Creamy Lipstick | Non-drying, H...']/../..//a[3]//div//div")   
print("Price of lipstick is: ",price.text)
sleep(5)
driver.close()