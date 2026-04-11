# Keyboard Actions- example of using Enter key
""" from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
ele = driver.find_element(By.ID, "twotabsearchtextbox")
ele.send_keys("Mobiles")
ele.send_keys(Keys.ENTER)
driver.implicitly_wait(5)
driver.close()
 """

# copy-paste using keyboard
""" from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID, "userName").send_keys("Anushka")
driver.find_element(By.ID, "userEmail").send_keys("anushka@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Jaipur")
# copying the current address in the permanent address field
driver.find_element(By.ID, "currentAddress").send_keys(Keys.CONTROL + "a") # ctrl + a is used to select the text
driver.find_element(By.ID, "currentAddress").send_keys(Keys.CONTROL + "c") # ctrl + c is used to copy the text
driver.find_element(By.ID, "permanentAddress").send_keys(Keys.CONTROL + "v") # ctrl + v is used to paste the text
driver.find_element(By.ID, "submit").click()
driver.implicitly_wait(5)
driver.close()
 """

# Mouse Actions using ActionChains class
""" from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
driver.implicitly_wait(5)
# performing normal click to test
# driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[2]").click()
# driver.implicitly_wait(2)
# driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[1]").click()
# driver.implicitly_wait(2)
# driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]").click()
# driver.implicitly_wait(2) 
# only single clicked work
# storing the elements in variables
double_click=driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[1]")
right_click=driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[2]")
single_click=driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]")
# now using action chains to perform these actions
# Step-1: create an object of ActionChains class
actions = ActionChains(driver)
# Step-2: storing the actions in the object
sleep(2)
actions.double_click(double_click).perform()
sleep(2)
actions.context_click(right_click).perform()
sleep(2)
actions.click(single_click).perform()
sleep(2)
# Step-3: perform the actions
actions.perform()
driver.implicitly_wait(5)
driver.close()
 """

# Scroll Actions - scroll to element - Scroll to element means moving the webpage until a specific element becomes visible on the screen so Selenium can interact with it.
""" from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
ele = driver.find_element(By.XPATH, "(//div[@class='a-section feed-carousel-viewport'])[3]//a//img[1]")
# clicking element
click = driver.find_element(By.XPATH, "(//div[@class='a-section feed-carousel-viewport'])[3]//a//img[1]")
actions = ActionChains(driver)
actions.scroll_to_element(ele).perform()
actions.click(click).perform()
driver.implicitly_wait(5)
driver.close()
 """
# scroll by amount- Scroll by amount means moving the page by a fixed number of pixels (instead of scrolling to a specific element).
""" from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://amazon.in/")
driver.maximize_window()
sleep(5)
actions = ActionChains(driver)
# single scroll
actions.scroll_by_amount(0,400).perform()
actions.scroll_by_amount(0,400).perform()
sleep(5)
driver.close()
 """

# scroll by origin - Scroll by origin means scrolling relative to a specific starting point (origin) instead of the whole page.
""" from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://amazon.in/")
driver.maximize_window()
sleep(5)
actions = ActionChains(driver)
ele=driver.find_element(By.XPATH, "(//div[@class='a-section feed-carousel-viewport'])[3]//a//img[1]")
# the element is the starting point and from that point it gets scrolled down to the defined amount
origin=ScrollOrigin.from_element(ele)
actions.scroll_from_origin(origin,0,400).perform()
sleep(5)
driver.close() """

# move to element -move_to_element() is used in Selenium ActionChains to move the mouse cursor to a specific element, mainly for hover actions. (mouse hover action)
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://amazon.in/")
driver.maximize_window()
sleep(5)
actions = ActionChains(driver)
ele=driver.find_element(By.XPATH, "(//div[@class='a-section feed-carousel-viewport'])[3]//a//img[1]")
actions.move_to_element(ele).perform()
sleep(5)
 

# using click_and_hold() to click and hold an element
""" from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,"//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
actions = ActionChains(driver)
ele1=driver.find_element(By.XPATH, "//input[@id='userName']")
ele1.send_keys("anushka")
ele=driver.find_element(By.XPATH, "(//input[@type='password'])")
ele.send_keys("anushka")
ele2=driver.find_element(By.XPATH, "(//img[@class='ng-star-inserted'])[1]")
sleep(5)
# actions.click_and_hold(ele).perform()
# sleep(5)
actions.click_and_hold(ele2).perform()
sleep(5)
# release
actions.click_and_hold(ele2).pause(8).release().perform()
sleep(5) 
driver.close()
 """

# drag and drop
""" from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
sleep(5)
drag=driver.find_element(By.XPATH,"//div[@id='draggable']")
drop=driver.find_element(By.XPATH,"//div[@id='droppable']")
actions = ActionChains(driver)
actions.drag_and_drop(drag,drop).perform()
sleep(5)
driver.close() """

# tab/ window handling
""" from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(5)
# manually 3 or 4 tabs
# fetch the IDs of all tabs
print("before current window handle: ",driver.current_window_handle)
print("before driver title:",driver.title)
# opening new tabs
sleep(5)
driver.switch_to.new_window()
driver.get("https://www.amazon.in/")
print("after driver title:",driver.title)
print("after current window handle: ",driver.current_window_handle)
print(driver.window_handles)
sleep(5)
# switch the tabs
driver.switch_to.window(driver.window_handles[0])
sleep(5)
driver.close()
 """