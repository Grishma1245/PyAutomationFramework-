from selenium.webdriver import Chrome 
from takeSS import take_Screenshot
import time

driver=Chrome()
driver.maximize_window()
driver.get("https://www.linkedin.com")
take_Screenshot(driver,"Screenshot")
driver.execute_script("window.scrollTo(0,400);window.scrollTo(0,800);")
time.sleep(15)


