# find_elements()-Used to find multiple elements on the page in the form of list.
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By 
o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)
# driver.find_element(By.TAG_NAME,'a').click() #using this first link of the page is only getting clicked
links=driver.find_elements(By.TAG_NAME,'a') #in the form of list, all links are getting stored in 'links'
print(links)
print(len(links))
# for printing the individual items of the list
for link in links:
    print(link.text)
driver.close()"""

# get attribute - fetching the value of the attribute of the element
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By 
o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)
ele=driver.find_element(By.XPATH,"//a[@class='gb_A']")
print(ele.get_attribute("aria-label")) #fetching the value through 'aria-label' attribute
driver.close()
 """