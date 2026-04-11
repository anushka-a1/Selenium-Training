""" Task-3: Open 3 tabs with different websites
Print each tab title and url
Close all tabs except the first one """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
driver.switch_to.new_window()
driver.get("https://www.myntra.com/")
sleep(2)
driver.switch_to.new_window()
driver.get("https://www.amazon.in/")
sleep(2)
# printing title and url of facebook page
driver.switch_to.window(driver.window_handles[0])
print("Title of flipkart window is: ", driver.title)
print("URL of flipkart window is: ", driver.current_url)
sleep(3)
# printing title and url of myntra page
driver.switch_to.window(driver.window_handles[1])
print("Title of myntra window is: ", driver.title)
print("URL of myntra window is: ", driver.current_url)
sleep(3)
# printing title and url of amazon page
driver.switch_to.window(driver.window_handles[2])
print("Title of amazon window is: ", driver.title)
print("URL of amazon window is: ", driver.current_url)
# closing all tabs except the first one
sleep(2)
driver.switch_to.window(driver.window_handles[2])
driver.close()
sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.close()
sleep(2)
driver.switch_to.window(driver.window_handles[0])
driver.close()