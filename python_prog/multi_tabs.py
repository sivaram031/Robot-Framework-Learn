import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://google.com')
c = driver.current_window_handle

driver.execute_script("window.open('https://yahoo.com','tab2')")
driver.switch_to.window('tab2')

driver.execute_script("window.open('https://python.org','tab3')")
driver.switch_to.window('tab3')


handle = driver.window_handles




for hand in handle:
    if driver.title != "Google":
        driver.switch_to.window(hand)
        print(driver.title)
        break
    else:
        print('window is not switched')

time.sleep(15)






