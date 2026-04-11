""" Task-3: Search flipkart website
Scroll down and click on 'Myntra'
Switch back to the flipkart website
Scroll down and click on 'Cleartrip'
Switch back to the flipart website
Scroll down and click on 'Shopsy'
Fetch IDs of all the windows
Then separately fetch the ID, title and URL of each window 
and print them"""

from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,"//span[@role='button']").click()
ele1=driver.find_element(By.XPATH, "//a[text()='Myntra']")
actions = ActionChains(driver)
actions.scroll_to_element(ele1).perform()
actions.click(ele1).perform()
sleep(5)
driver.switch_to.window(driver.window_handles[0])
ele2=driver.find_element(By.XPATH, "//a[text()='Cleartrip']")
actions.scroll_to_element(ele2).perform()
actions.click(ele2).perform()
sleep(5)
driver.switch_to.window(driver.window_handles[0])
ele3=driver.find_element(By.XPATH, "//a[text()='Shopsy']")
actions.scroll_to_element(ele3).perform()
actions.click(ele3).perform()
sleep(5)


# finding the IDs of all windows
print("IDs of all windows are: ", driver.window_handles)

# fetching the IDs, title and URL of each window by switching to each window
# flipkart window
sleep(3)
driver.switch_to.window(driver.window_handles[0])
print("ID of flipkart window is: ", driver.current_window_handle)
print("Title of flipkart window is: ", driver.title)
print("URL of flipkart window is: ", driver.current_url)
# myntra window
sleep(3)
driver.switch_to.window(driver.window_handles[1])
print("ID of myntra window is: ", driver.current_window_handle)
print("Title of myntra window is: ", driver.title)
print("URL of myntra window is: ", driver.current_url)
# cleartrip window
sleep(3)
driver.switch_to.window(driver.window_handles[2])
print("ID of cleartrip window is: ", driver.current_window_handle)
print("Title of cleartrip window is: ", driver.title)
print("URL of cleartrip window is: ", driver.current_url)
# shopsy window
sleep(3)
driver.switch_to.window(driver.window_handles[3])
print("ID of shopsy window is: ", driver.current_window_handle)
print("Title of shopsy window is: ", driver.title)
print("URL of shopsy window is: ", driver.current_url)
sleep(5)
driver.quit()
