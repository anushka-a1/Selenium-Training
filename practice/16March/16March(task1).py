""" Task-1: Open Amazon
Search for Mobiles
Click Search
Fetch the price of mobile using its name (Traversing)"""

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(5)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Samsung").click()
sleep(5)
price=driver.find_element(By.XPATH,"//span[text()='Samsung Galaxy M07 Mobile (Black, 4GB RAM, 64GB Storage) | MediaTek Helio G99 | AnTuTu 624K | IP54| 50MP Camera | 7.6mm Slim | 5000mAh Battery | 25W Fast Charging | 6 Gen OS Upgrades | Without Charger']/../../../..//div[3]//div[1]//div[1]//div[1]//div[1]//div[1]//span[2]//span[2]")
print("Price of mobile is: ",price.text)
sleep(5)
driver.close()