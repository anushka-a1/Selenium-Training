""" Task 3-Write a script to:
1) navigate to amazon
2) search a product through send_keys BUT dont click on search icon
3) Wait for the suggestions to appear
4) Click on 4th suggestion
5) Click on Sort By and click on newest
6) Click on free shipping check box
7) wait for first product and return the name=price
 """

import select
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Lip tint")
# waiting for the suggestions to appear
wait=WebDriverWait(driver,10)
dropdown=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='s-suggestion-container']")))
# Click on 4th suggestion
dropdown[3].click()
# click on sort by and selecting newest 
driver.find_element(By.XPATH,"//span[@class='a-button-text a-declarative']").click()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Newest Arrivals']").click()
# clicking on checkbox of free shipping
wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[3]"))).click()
# getting the name and price of the first product
name=driver.find_element(By.XPATH,"(//h2[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal'])[1]").text
price=driver.find_element(By.XPATH,"(//span[@class='a-price-whole'])[1]").text
print(name,"=",price)
driver.close()