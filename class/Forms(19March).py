# is_displayed and is_enabledmethod
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(5)
ele = driver.find_element(By.XPATH,"//span[text()='Log in']")
print("Displayed:",ele.is_displayed())
print("Enabled:",ele.is_enabled())
driver.close()
 """

# example - checking the register now button on naukri.com
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium=cpc&utm_campaign=Brandcom&gclsrc=aw.ds&gad_source=1&gad_campaignid=292348446&gbraid=0AAAAADLp3cHQGK0hvfh6zjohfDHagIT1L&gclid=EAIaIQobChMI2qzSy7SrkwMV_KlmAh1QHQwZEAAYASAAEgLv9_D_BwE")
driver.maximize_window()
driver.implicitly_wait(5)
ele = driver.find_element(By.XPATH,"//button[@type='submit']")
print("Displayed:",ele.is_displayed())
print("Enabled:",ele.is_enabled())
driver.close()
 """

# is_selected method
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()
driver.implicitly_wait(5)
ele1 = driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
ele2 = driver.find_element(By.XPATH,"//input[@type='checkbox'][2]")
print("Checkbox1 is selected :",ele1.is_selected())
print("Checkbox2 is selected :",ele2.is_selected())
driver.close()
 """

# filling a form
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("Anushka")
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("Chaurasia")
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("anushka@example.com")
driver.find_element(By.XPATH,"//input[@id='gender-radio-2']").click()
driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys("1234567890")
driver.find_element(By.ID,"dateOfBirthInput").click()
driver.find_element(By.XPATH,"//div[text()='19']").click()
# uploading pictures in form
driver.find_element(By.ID,"uploadPicture").send_keys(r"C:\Users\user\OneDrive\Pictures\Untitled.png")
driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-2']").click()
driver.find_element(By.ID,"currentAddress").send_keys("Jaipur")
driver.close()