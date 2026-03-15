# Locators - Locators are used to locate the element on the page and perform actions on it.

""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)

# Locator by ID - it is used to locate the element by its unique id
# enter values in Demoqa website and click on submit
driver.find_element(By.ID,"userName").send_keys("Anushka") 
driver.find_element(By.ID,"userEmail").send_keys("anushka@gmail.com")
driver.find_element(By.ID,"currentAddress").send_keys("Jaipur")
driver.find_element(By.ID,"permanentAddress").send_keys("Jaipur")
driver.find_element(By.ID,"submit").click() #the click method is used to click on element and return type is None
sleep(2)
driver.close() """

# example - locate the search bar for amazon website
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shirts")
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
driver.close()
 """

# Locator by Name - it is used to locate the element by its unique name
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.NAME,"field-keywords").send_keys("Shirts")
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
driver.close() """

# Locator by Class Name - it is used to locate the element by its unique class name
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
#Compound class are classes that are nested inside other classes. The compound class name should be replaced with '.'. 
driver.find_element(By.CLASS_NAME,"nav-input.nav-progressive-attribute").send_keys("Shirts") 
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
driver.close() """

# Locator by Tag Name - it is used to locate the element by its unique tag name
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.TAG_NAME,"input").send_keys("Anushka") #enters the value in first input field
driver.find_element(By.TAG_NAME,"input").send_keys("anushka@gmail.com") #enters the value in first input field only because its retrieving the first input field
driver.find_element(By.TAG_NAME,"textarea").send_keys("Jaipur") #enters the value in first text area
driver.find_element(By.TAG_NAME,"textarea").send_keys("city")
sleep(5)
driver.close() """

# Locator by Link Text - it is used to locate the element by its unique link text, used only for anchor tags
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.LINK_TEXT,"Today's Deals").click() #take the visible text of the element and click on it
sleep(5)
driver.close() """

# Locator by Partial Link Text - it is used to locate the element by its unique partial link text, used only for anchor tags
# difference between link text and partial link text is that link text is used to locate the element by its complete link text, while partial link text is used to locate the element by its partial link text only 
# link text and partial link text are space and case sensitive
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.PARTIAL_LINK_TEXT,"Today").click() #take the visible text of the element and click on it
sleep(5)
driver.close()
 """

# Locator by CSS Selector - it is used to locate the element by its unique CSS Selector
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox").send_keys("Skirts") #here #twotabsearchtextbox is the css selector which is used to locate the search bar
driver.find_element(By.CSS_SELECTOR,"#nav-search-submit-button").click()
sleep(5)
driver.close()

# Locator by CSS Selector - it is used to locate the element by its unique CSS Selector
# by class name
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
#locating the Full Name text box by its class name with help of CSS Selector
driver.find_element(By.CSS_SELECTOR,".mr-sm-2.form-control").send_keys("Anushka") #enters the value in first input field
sleep(5)
driver.close()
