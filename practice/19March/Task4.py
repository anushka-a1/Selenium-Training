""" Task4: uploading single and multiple files """
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"name").send_keys("Anushka Chaurasia")
driver.find_element(By.ID,"email").send_keys("anushka@example.com")
driver.find_element(By.ID,"singleFileInput").send_keys(r"C:\Users\user\OneDrive\Pictures\Untitled.png")
driver.find_element(By.XPATH,"//button[text()='Upload Single File']").click()
# uploading multiple files 
# driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\user\OneDrive\Pictures\Screenshots\Screenshot 2026-01-22 005416.png")
# driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\user\OneDrive\Pictures\Untitled.png")
# uploading multiple files using '\n'
driver.find_element(By.ID,"multipleFilesInput").send_keys([r"C:\Users\user\OneDrive\Pictures\Screenshots\Screenshot 2026-01-22 005416.png","\n",r"C:\Users\user\OneDrive\Pictures\Untitled.png"])
driver.find_element(By.XPATH,"//button[text()='Upload Multiple Files']").click()


