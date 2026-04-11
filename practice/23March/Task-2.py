""" Task-2: Search nike.in
and perform following actions:-
1. mouse hover and click on 'Kids'
2. scroll down and click on 'shop'
3. scroll and select any shoes and click on 'add to bag'
4. select size and add to bag """

from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.nike.in/")
driver.maximize_window()
sleep(5)
actions = ActionChains(driver)
# performing mouse hover and clicking on 'Kids'
ele1=driver.find_element(By.XPATH, "//span[text()='Kids']")
actions.move_to_element(ele1).perform()
actions.click(ele1).perform()
driver.switch_to.window(driver.window_handles[1])
# scrolling down and clicking on 'shop'
ele2=driver.find_element(By.XPATH, "//a[text()='Shop']")
actions.scroll_to_element(ele2).perform()
actions.click(ele2).perform()
sleep(5)

# scrolling down and clicking on 'shoes'
ele3=driver.find_element(By.XPATH, "//div[text()='Nike Air Max 90 SE']")
actions.scroll_to_element(ele3).perform()
actions.click(ele3).perform()
sleep(5)
driver.switch_to.window(driver.window_handles[2])
# scrolling down and clicking on 'add to bag'
ele4=driver.find_element(By.XPATH, "//button[text()='Add to Bag']")
actions.scroll_to_element(ele4).perform()
actions.click(ele4).perform()
# selecting size and clicking on 'add to bag'
ele5=driver.find_element(By.XPATH, "//label[text()='UK 6 (EU 40)']")
actions.click(ele5).perform()
actions.click(ele4).perform()
sleep(5)
driver.close()
