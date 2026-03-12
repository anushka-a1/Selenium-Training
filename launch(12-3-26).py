# opening chrome browser
""" from time import sleep

from selenium.webdriver import Chrome
driver = Chrome()
sleep(5) """

# opening edge browser
""" from time import sleep
from selenium.webdriver import Edge
driver = Edge()
sleep(5) """

""" # opening chrome browser and keeping it open after the script is executed
from selenium.webdriver import Chrome,ChromeOptions #importing the class Chrome and ChromeOptions from the selenium.webdriver module
o = ChromeOptions() #creating an object of the class ChromeOptions and storing it in the variable o
o.add_experimental_option("detach", True) #adding an experimental option to the ChromeOptions object to keep the browser open after the script is executed
driver = Chrome(options=o) #driver is the object of the class Chrome and we are passing the options to it

driver.get("https://www.google.com") #opening the google website using the get method of the driver object, return type is None

# Browser window management methods

# to maximize the browser window
driver.maximize_window() #maximizing the browser window using the maximize_window method of the driver object, return type is None

# to minimize the browser window
driver.minimize_window() #minimizing the browser window using the minimize_window method of the driver object, return type is None

# to set full screen
driver.fullscreen_window() #setting the browser window to full screen using the fullscreen_window method of the driver object, return type is None
 """

# opening amazon website and keeping it open, maximizing the window and then minimizing it
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2) #use sleep method to wait for 2 seconds before executing the next line of code, return type is None. it will do all the operations in sequence, first it will open the amazon website, then it will maximize the window, then it will wait for 2 seconds, then it will minimize the window and then it will wait for 2 seconds before closing the browser. if we are using all three methods together then the last method will be executed and the previous two methods will be overridden, so the browser will be in full screen mode.
driver.fullscreen_window() #if we are using all three methods together then the last method will be executed and the previous two methods will be overridden, so the browser will be in full screen mode. 

# page infromation methods

# fetching the title of the current page
print(driver.title) #fetching the title of the current page using the title attribute of the driver object, return type is str
# fetching the current url of the page
print(driver.current_url) #fetching the current url of the page using the current_url attribute of the driver object, return type is str
# fetching the page source of the current page
print(driver.page_source) #fetching the page source of the current page using the page_source attribute of the driver object, return type is str
# to navigate a new url
driver.back()
driver.forward()
driver.sleep()  """

# opening demoqa.com website and keeping it open, maximizing the window and then minimizing it then fetching the title, current url and page source of the current page
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://demoqa.com")
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.fullscreen_window()

print(driver.title)
print(driver.current_url)
print(driver.page_source)


# fetching the name of the browser
print(driver.name) #fetching the name of the browser using the name attribute of the driver object, return type is str

""" # closing the browser
driver.close() #closing the browser using the close method of the driver object, return type is None. it will close the current window that is opened by the driver object. if there are multiple windows opened by the driver object then it will close the current window and switch to the next window. if there is only one window opened by the driver object then it will close that window and quit the browser. if we want to close all the windows opened by the driver object then we can use the quit method of the driver object.

# quitting the browser
driver.quit() #quitting the browser using the quit method of the driver object, return type is None. it will close all the windows opened by the driver object and quit the browser. if there is only one window opened by the driver object then it will close that window and quit the browser. if there are multiple windows opened by the driver object then it will close all the windows and quit the browser. if we want to close only the current window then we can use the close method of the driver object. """

