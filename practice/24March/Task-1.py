""" Task-1 Open Twitter
sign up with google """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://twitter.com/")
driver.maximize_window()
sleep(5)
# Switch to the frame
frame=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(frame)
# Click on sign up with Google
driver.find_element(By.XPATH,"//span[text()='Sign up with Google']").click()
sleep(5)
driver.quit()