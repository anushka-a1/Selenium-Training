# Implicit Wait- Implicit wait tells Selenium to wait for a certain amount of time while searching for elements.
# If the element appears before the time ends, Selenium continues immediately.
# If the element does not appear before the time ends, Selenium throws an exception.
""" from os import wait
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.find_element(By.TAG_NAME,"button").click()
driver.implicitly_wait(10)
t=driver.find_element(By.XPATH,"//div[@id='finish']//h4")
print(t.text)
# The reason nothing is printed is that the element already exists in the DOM, but its text appears later after the loading finishes. 
# implicitly_wait() only waits for element presence, not for text to appear.
 """
# example of implicit wait on decathlon
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.decathlon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//img[@src='https://contents.mediadecathlon.com/s1371134/k$314e5f23e193aab04dceff5d9bcbdee4/defaut.jpg?format=auto&quality=70&f=2520x0']").click()
driver.find_element(By.XPATH,"//img[@alt='Beanies & Neck Warmers']").click()
 """

# Explicit Wait- Explicit wait is used to wait for a specific condition before continuing. It is more flexible than implicit wait.
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.find_element(By.TAG_NAME,"button").click()
wait=WebDriverWait(driver,10)  #create a wait object 
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='finish']//h4")))
t=driver.find_element(By.XPATH,"//div[@id='finish']//h4")
print(t.text)
"""

