""" Task-3: Open demowebshop application 
Scroll to Facebook link (bottom of page)
Click and enter username and password 
Click on login """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)
# scroll to facebook link
actions=ActionChains(driver)
actions.scroll_to_element(driver.find_element(By.LINK_TEXT,"Facebook")).perform()
sleep(2)
# click on facebook link
driver.find_element(By.LINK_TEXT,"Facebook").click()
sleep(2)
driver.switch_to.window(driver.window_handles[1])
sleep(2)
driver.find_element(By.XPATH,"(//span[text()='Allow all cookies'])[2]").click()
driver.find_element(By.XPATH,"//label[@class='x78zum5 xh8yej3']//div/descendant::input").send_keys("anushka@example.com")
driver.find_element(By.XPATH,"(//label[@class='x78zum5 xh8yej3'])[2]//div/descendant::input").send_keys("123456")
driver.find_element(By.XPATH,"(//div[@class='x1c436fg'])[2]//div[1]").click()
sleep(5)
driver.quit()
