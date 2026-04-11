""" Task-2: Open Zomato
and click on Login
and click on Sign in with Google"""

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/delivery")
driver.maximize_window()
sleep(5)
# Click on Login
driver.find_element(By.XPATH,"//a[text()='Log in']").click()
sleep(3)
# Switch to the first frame
frame1=driver.find_element(By.XPATH,"//iframe[contains(@id,'auth')]")
driver.switch_to.frame(frame1)
sleep(3)
# Switch to the second frame
frame2=driver.find_element(By.XPATH,"(//iframe[@title='Sign in with Google Button'])[1]")
driver.switch_to.frame(frame2)
sleep(3)
# Click on Sign in with Google
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
sleep(5)
driver.quit()