# XPath using Attribute - it is used to locate the element by its unique attribute
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
#taking the placeholder value of the element
driver.find_element(By.XPATH,"//input[@placeholder='Full Name']").send_keys("Anushka Chaurasia")
driver.find_element(By.XPATH,"//input[@placeholder='name@example.com']").send_keys("anushka@gmail.com")
driver.find_element(By.XPATH,"//textarea[@placeholder='Current Address']").send_keys("Jaipur")
driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys("Jaipur")
driver.find_element(By.XPATH,"//button[@id='submit']").click()
sleep(10)
driver.close() """

# XPath using Text - it is used to locate the element by its unique text
"""from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#taking the text value of the element
driver.find_element(By.XPATH, "//a[text()='Mobiles']").click()
driver.find_element(By.XPATH, "//a[.='Fashion']").click() #. is used to locate the element by its exact text
sleep(5)
driver.close() """

# XPath using contains attribute - This is used when you know part of the attribute value but not the full value.
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#taking the text value of the element
driver.find_element(By.XPATH, "//a[contains(@href,'deals')]").click() #contains() used to locate element using partial attribute value
driver.find_element(By.XPATH, "//a[contains(@href,'Fashion')]").click()

sleep(5)
driver.close()

# XPath using contains text - This is used when the visible text is partially known.
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#taking the text value of the element
driver.find_element(By.XPATH, "//a[contains(text(),'Deals')]").click() #contains method is used to locate the element by its partial text #contains method is used to locate the element by its partial text
sleep(5)
driver.close()
"""
# indexing - it is used to locate the element by its unique index
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, "(//a[@class='nav-a'])[2]").click()
sleep(5)
driver.close()