from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')
dri = webdriver.Chrome(ChromeDriverManager().install())
dri.get("https://mathup.com")
dri.find_element(by.Xpath,'//*[@id="__next"]/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[3]/div[1]').click()
dri.find_element(By.)


