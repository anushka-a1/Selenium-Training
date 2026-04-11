""" Task2- get attributes of all links in amazon page"""
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By 
o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
links=driver.find_elements(By.XPATH,'//a[@class="nav-a  "]')
print(links)
for link in links:
    print(link.get_attribute("text"))
driver.close()
