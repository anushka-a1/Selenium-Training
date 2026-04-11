# iFrames - An iFrame (inline frame) is like a mini webpage inside a webpage. It loads another HTML document within the main page.
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("http://127.0.0.1:5500/page1.html")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"input").send_keys("Anushka")
# switch by index - switch to frame2
# driver.switch_to.frame(0)
# driver.find_element(By.ID,"input").send_keys("Chaurasia")
# driver.switch_to.frame(0)
# driver.find_element(By.ID,"input").send_keys("example.com")
# switch by name
# driver.switch_to.frame("n1")
# driver.find_element(By.ID,"input").send_keys("Chaurasia")
# driver.switch_to.frame("n2")
# driver.find_element(By.ID,"input").send_keys("example.com")
# switch by id
# driver.switch_to.frame("frame1")
# driver.find_element(By.ID,"input").send_keys("Chaurasia")
# driver.switch_to.frame("frame2")
# driver.find_element(By.ID,"input").send_keys("example.com")
# switch by webelement
frame2=driver.find_element(By.ID,"frame1")
driver.switch_to.frame(frame2)
driver.find_element(By.ID,"input").send_keys("Chaurasia")
frame3=driver.find_element(By.ID,"frame2")
driver.switch_to.frame(frame3)
driver.find_element(By.ID,"input").send_keys("example.com")
# switch to parent frame
driver.switch_to.parent_frame()
driver.find_element(By.ID,"input").clear()
sleep(2)
driver.find_element(By.ID,"input").send_keys("i am back to parent frame from frame3")
# switching back to default frame
sleep(2)
driver.switch_to.parent_frame()
driver.find_element(By.ID,"input").clear()
sleep(2)
driver.find_element(By.ID,"input").send_keys("i am back to parent frame from frame2")
# moving from frame1 to frame2 again
sleep(2)
driver.switch_to.frame("frame1")
driver.find_element(By.ID,"input").clear()
sleep(2)
driver.find_element(By.ID,"input").send_keys("i am back to frame2 from frame1")
# moving from frame2 to frame3
sleep(2)
driver.switch_to.frame("frame2")
driver.find_element(By.ID,"input").clear()
sleep(2)
driver.find_element(By.ID,"input").send_keys("i am back to frame3 from frame2")
# switch to default frame - from frame3
driver.switch_to.default_content()
driver.find_element(By.ID,"input").clear()
sleep(2)
driver.find_element(By.ID,"input").send_keys("i am back to default frame from frame3")
