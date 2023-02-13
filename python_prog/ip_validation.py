from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

a = ['192.1.34.186','194.5.67.23','14.-12.193.45']

for ip in a:
    if ([0 <= int(i) <= 225  for i in ip.split(".")].count(True)==4):
        print("valid ip numbers: ",ip)
    else:
        print("invalid ip numbers: ", ip)
