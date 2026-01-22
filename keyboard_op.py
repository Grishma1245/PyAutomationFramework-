from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=Chrome()
driver.get("https://www.daraz.com.np")
driver.maximize_window()


driver.find_element(By.XPATH,'//input[@type="search"]').send_keys("Mobile", Keys.ENTER)

act=ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
time.sleep(3)
act.send_keys(Keys.ENTER).perform()


driver.find_element(By.ID,"q").send_keys("Laptop")
act.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()
time.sleep(10)
