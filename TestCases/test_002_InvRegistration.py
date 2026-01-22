from Base.IntiateDriver import startbrowser,closeBrowser

def test_Invalidate_Registration():
    driver=startbrowser()
    driver.find_element('xpath', "//input[@name='firstname']").send_keys('1234')
    driver.find_element('xpath', "//input[@name='lastname']").send_keys('000')
    closeBrowser()