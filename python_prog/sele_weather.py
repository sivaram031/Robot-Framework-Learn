import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#//*[@id="left-content"]/div/iframe
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html"
driver.get(url)
driver.maximize_window()
driver.switch_to.frame('packageListFrame')
driver.find_element(By.LINK_TEXT,'org.openqa.selenium').click()
driver.find_element(By.XPATH,"//span[text()='Capabilities']").click()
time.sleep(20)



