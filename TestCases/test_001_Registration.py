from Base.IntiateDriver import startbrowser,closeBrowser
from Library.ConfigReader import ElementsRead

def test_validateRegistration():
    driver=startbrowser()
    #driver.find_element('xpath', "//input[@name='firstname']").send_keys('Grishma')
    driver.find_element('name',ElementsRead('Registration', 'fname')).send_keys("grishma")
    driver.find_element('name',ElementsRead('Registration', 'lname')).send_keys("grishma")
    closeBrowser()