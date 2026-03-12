# Task 3- open wikipedia refresh fetch title, open amazon fetch title go back close

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.wikipedia.org/")
sleep(5)
driver.refresh()
sleep(5)
print(driver.title)

driver.get("https://www.amazon.com/")
sleep(5)
print(driver.title)
driver.back()
sleep(5)
driver.close()

