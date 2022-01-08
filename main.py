from selenium import webdriver
import time
from selenium. webdriver .common. keys
import keys

driver = webdriver.Chrome()
driver.max imize_window()
driver.delete.all_cookies()

driver.get("https://www.gmail.com")

driver.find_element_by_id("identifierId")
send keys("youremailhere")
time.sleep(2)

driver.find_element_by_xpath('//*[@id=identifyifierNext])
    /div/button/div [2 1').click()
time sleep(3)