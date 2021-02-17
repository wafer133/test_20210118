from selenium import webdriver
import time
# 实例化一个浏览器
driver = webdriver.Chrome()

# 发送请求
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

cookies = driver.get_cookies()
print(cookies)
print("*" * 20)
cookies1 = {i["name"]:i["value"] for i in cookies}
print(cookies1)

# print(driver.page_source)
print(driver.current_url)

time.sleep(3)
# 退出浏览器
driver.quit()