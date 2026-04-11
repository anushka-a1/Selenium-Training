""" Task 1 - write a selenium script to open a website and print the page title """
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.wikipedia.org/")
sleep(3)
print(driver.title)
driver.close()