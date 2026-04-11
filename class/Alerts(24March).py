# Alerts - A JavaScript popup that appears inside the browser.
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
# using simple alert 
driver.find_element(By.XPATH, "//button[text()='Simple Alert']").click()
sleep(2)
driver.switch_to.alert.accept()
sleep(2)
# using confirmation alert
driver.find_element(By.XPATH, "//button[text()='Confirmation Alert']").click()
sleep(2)
# driver.switch_to.alert.accept() #to use ok
driver.switch_to.alert.dismiss() #to use cancel
sleep(5)
# using prompt alert
driver.find_element(By.XPATH, "//button[text()='Prompt Alert']").click()
sleep(5)
driver.switch_to.alert.send_keys("Anushka Chaurasia")
sleep(2)
driver.switch_to.alert.accept()
sleep(2)
driver.quit()
 """

# upload and download
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions 
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.get("https://demoqa.com/upload-download")
# # to enable safe browsing
# o.add_experimental_option("safebrowsing.enabled",True)
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.ID,"uploadFile").send_keys("C:\Users\user\OneDrive\Pictures\Untitled.png")
# sleep(2)
# driver.find_element(By.ID,"downloadButton").click()
# sleep(2)
# driver.quit()  

# download python
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
driver=Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Download Python install manager']").click()
sleep(2)
 """

# disable notifications
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
driver=Chrome(options=o)
driver.get("https://www.easemytrip.com/flights.html?msclkid=e15992a0faee1eac7edffb629b94dda0&utm_source=bing&utm_medium=cpc&utm_campaign=Bing_Search_AllAudience_%20Brand%20(EaseMyTrip.Com)&utm_term=easemytrip&utm_content=EaseMyTrip%20Exact")
driver.maximize_window()
sleep(2)
driver.quit()
 """

# setting date from a date picker
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
driver=Chrome(options=o)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").click()
driver.find_element(By.XPATH,"//span[@class='ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9']").click()
driver.find_element(By.XPATH,"//a[text()='30']").click()
sleep(2)
driver.quit()
 """

# example of demoqa practice form
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
driver=Chrome(options=o)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"firstName").send_keys("Anushka")
driver.find_element(By.ID,"lastName").send_keys("Chaurasia")
driver.find_element(By.ID,"userEmail").send_keys("anushka@example.com")
driver.find_element(By.ID,"gender-radio-1").click()
driver.find_element(By.ID,"userNumber").send_keys("1234567890")
driver.find_element(By.ID,"dateOfBirthInput").click()
dropdown1=driver.find_element(By.XPATH,"(//select[@class='react-datepicker__year-select'])[1]")
select1=Select(dropdown1)
select1.select_by_visible_text("2003")
dropdown=driver.find_element(By.XPATH,"(//select[@class='react-datepicker__month-select'])[1]")
select=Select(dropdown)
select.select_by_visible_text("September")
driver.find_element(By.XPATH,"//div[text()='19']").click()
ele=driver.find_element(By.ID,"subjectsInput")
ele.send_keys("English")
# press enter key
ele.send_keys(Keys.ENTER)
driver.find_element(By.ID,"hobbies-checkbox-1").click()
driver.find_element(By.ID,"uploadPicture").send_keys(r"C:\Users\user\OneDrive\Pictures\Untitled.png")
driver.find_element(By.ID,"currentAddress").send_keys("Jaipur")
sleep(2)
