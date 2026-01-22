from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
chrome_options=Options()
driver=Chrome(options=chrome_options)
driver.get("https://www.facebook.com/r.php?")
driver.maximize_window()
driver.find_element(By.NAME,"firstname").send_keys("Grishma")
#driver.find_element(By.NAME,"lastname").send_keys("Acharya")
#driver.find_element(By.LINK_TEXT,"Already have an account?").click()

driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("Acharya")

#working on a radio button
driver.find_element(By.XPATH, '//input[@value="2"]').click()
#working on a dropdown
dropdown=Select(driver.find_element(By.NAME, "birthday_month"))
dropdown.select_by_index(1)
#dropdown.selcet_by_value(11)
#dropdown.select_by_visible_text("2")





#driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

time.sleep(20)


