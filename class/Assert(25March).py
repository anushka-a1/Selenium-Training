# Assertion is used to verify whether the expected result matches the actual result in your test.
# validating the title of the page using Assertion
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
print(driver.title)
# assert "Google" in driver.title
expected="Google"
actual=driver.title
assert expected == actual
# checking if the title is Google Chrome
# expected="Google Chrome"
# actual=driver.title
# assert expected == actual, "Title mismatch"
# this will not execute if there is an assertion error
driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("weather")
driver.quit()
 """

# example using amazon website, click on 'Best Sellers' then validate title of the page
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"(//a[text()='Bestsellers'])[1]").click()
expected="Amazon.in Bestsellers: The most popular items on Amazon"
actual=driver.title
assert expected == actual
print(driver.title)
driver.quit()
 """

# Screenshots
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
driver.save_screenshot("screenshot.png") #it will save the screenshot in the current directory
driver.close()
 """

# saving the screenshot in a different directory - page screenshot
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
import os
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
folder=os.path.join(os.getcwd(),"screenshot") #here screenshot is the folder name
os.makedirs(folder,exist_ok=True) #it will create the folder if it doesn't exist
driver.save_screenshot(f'{folder}/screenshot.png') #it will save the screenshot in the specified directory
driver.close()
 """

# element screenshot
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
import os
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
folder=os.path.join(os.getcwd(),"screenshot")
os.makedirs(folder,exist_ok=True)
ele=driver.find_element(By.XPATH,"//textarea[@title='Search']") #it will take the screenshot of the element
ele.screenshot(f'{folder}/screenshot2.png')
driver.close()
 """

# saving the screenshots with time
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
import os
import time
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
folder=os.path.join(os.getcwd(),"screenshot")
os.makedirs(folder,exist_ok=True)
timestamp=time.strftime("%d%m%Y%H%M%S")
driver.save_screenshot(f'{folder}/screenshot{timestamp}.png')
driver.close()
 """
