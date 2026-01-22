from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")

MainWindow=driver.current_window_handle
print(MainWindow)

wait=WebDriverWait(driver,15)
newtab_button=driver.find_element(By.ID,"tabButton")
newtab_button.click()
wait.until(ec.number_of_windows_to_be(2))
allwindow=driver.window_handles
print(allwindow)

#iterate over all window to find new tab 
for handle in allwindow:
    if handle !=MainWindow:
        driver.switch_to.window(handle)
        break  

 #perform an action on 
newTab_heading=driver.find_element(By.ID,"sampleHeading")
print(newTab_heading.text)
time.sleep(10)
#close the newtab
driver.close()

#switch back to main window
driver.switch_to.window(MainWindow)






time.sleep(20)