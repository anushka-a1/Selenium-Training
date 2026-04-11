# traversing using XPath
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()
sleep(5)
salary=driver.find_element(By.XPATH,"//td[text()='Kierra']/..//td[5]") #traversing from child to parent node and parent to child node
department=driver.find_element(By.XPATH,"//td[text()='Kierra']/..//td[6]")
print('Salary of Kierra is',salary.text)
print('Department of Kierra is',department.text)
sleep(5)
driver.close()
 """

""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
# example of traversing 
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()
due=driver.find_element(By.XPATH,"//td[text()='Frank']/..//td[4]") 
sleep(5)
print('Due amount of Frank is',due.text)
sleep(5)
driver.close()
 """

# traversing using siblings
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()
due=driver.find_element(By.XPATH,"(//td[text()='Tim'])[1]//following-sibling::td[2]") 
sleep(2)
print('Due amount of Tim is',due.text)
sleep(5)
driver.close()
 """