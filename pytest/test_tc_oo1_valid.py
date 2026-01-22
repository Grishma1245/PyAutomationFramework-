from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import pytest
x=50
@pytest.fixture(scope="module")
def setPath():
    global driver
    driver=Chrome()
    yield #yield means after execution closed
    driver.close()
    



#@pytest.mark.skipif(x>40, reason="DONT execute this")
@pytest.mark.Sanity
def test_registration_valid_test(setPath):
    
    driver.get("https://www.facebook.com/r.php")
    #driver.find_element(By.NAME,"lastname").send_keys("Acharya")
    driver.maximize_window()


@pytest.mark.Smoke

def test_registration_invalid_test(setPath):
    
    driver.get("https://www.facebook.com/r.php")
    driver.maximize_window()
    assert driver.current_url=="https://www.facebook.com/r.php?"

    #assert driver.title=="Sign Up for Facebook"




@pytest.mark.Grishma
def test_invaliddata(setPath):
    
     driver.get("https://www.amazon.com")
     driver.maximize_window()
    
time.sleep(20)




#assert driver.current_url=="https://www.facebook.com/r.php?"





