from selenium.webdriver import Chrome
import logging
import time

driver = Chrome()

# setup logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# file handlers
warn_handler = logging.FileHandler("warninglog.txt")
warn_handler.setLevel(logging.WARNING)

info_handler = logging.FileHandler("infolog.txt")
info_handler.setLevel(logging.INFO)

# formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
warn_handler.setFormatter(formatter)
info_handler.setFormatter(formatter)

# attach handlers
log.addHandler(warn_handler)
log.addHandler(info_handler)

#selenium steps
driver.maximize_window()
driver.get("https://www.facebook.com/r.php")
log.info("[My URL is open]")
log.warn('[There is delay in opening the URL]')
time.sleep(15)


