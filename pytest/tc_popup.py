from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
driver=Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/entry_ad")
wait=WebDriverWait(driver,10)
model=wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"modal")))
close_btn=model.find_element(By.XPATH, '//div[@class="modal-footer"]/p')
close_btn.click()
# allWindow=driver.window_handles
# print(allWindow)
time.sleep(15)