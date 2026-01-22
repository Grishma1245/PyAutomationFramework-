from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.ui import Select
import time
chrome_options=Options()
driver=Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.facebook.com/r.php?")
driver.find_element(By.NAME, "firstname" ).send_keys("Grishma")
# driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
#driver.find_element(By.LINK_TEXT,"Already have an account?").click()

driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("hello")
#radio button
driver.find_element(By.XPATH, '//input[@value="1"]').click()
#dropdown
dropdown=Select(driver.find_element(By.NAME, "birthday_month"))
dropdown.select_by_index(1)
# dropdown.select_by_value("6")
# dropdown.select_by_visible_text("Jul")

#Select(driver.find_element(By.NAME, "birthday_month")).select_by_index(1)
time.sleep(10)

