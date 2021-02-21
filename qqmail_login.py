from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://mail.qq.com/")

driver.switch_to.frame("login_frame")

driver.find_element_by_id("u").send_keys("1084948810")

time.sleep(5)

driver.quit()