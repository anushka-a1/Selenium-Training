""" ## Task 1- Write a Selenium script to open a website take screenshots.
1) Open https://in.pinterest.com/
2) Take the screenshot of entire page
3) Scroll to a picture and caputure the screenshot of the picture
 """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains 
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(2)
# taking screenshot of entire page
driver.save_screenshot("screenshot1(Task-1).png")
# scroll to an element
sleep(2)
ele=driver.find_element(By.XPATH,"//img[contains(@alt,'Earthy space inspo')]")
actions=ActionChains(driver)
actions.scroll_to_element(ele).perform()
sleep(2)
# taking screenshot of an element
ele.screenshot("screenshot2(Task-1).png")
driver.close()