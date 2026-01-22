from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver=Chrome()
#driver.get("https://www.daraz.com.np/")
driver.get("https://www.facebook.com/")
driver.maximize_window()
#act=ActionChains(driver)

#act.context_click(driver.find_element(By.XPATH,'//button[@type="submit"]')).perform()
#time.sleep(10)



#act.move_to_element(driver.find_element(By.XPATH, "//input[@id='q']")).perform()



wait = WebDriverWait(driver, 10)

element = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))
act = ActionChains(driver)
act.click(element).perform()






#drag &drop
# source = driver.find_element(By.ID, "twotabsearchtextbox")
# target = driver.find_element(By.ID, "a-page")
# act.drag_and_drop(source, target).perform()



time.sleep(15)


















#wait = WebDriverWait(driver, 10)
# element = wait.until(
#     EC.visibility_of_element_located(
#         (By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
#     )
# )

# act = ActionChains(driver)
# act.move_to_element(element).perform()

