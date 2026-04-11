"""Task 2: Write a Selenium script to open a website and print the current URL. """
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.wikipedia.org/")
sleep(2)
print(driver.current_url)
driver.close()