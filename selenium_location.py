from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.qiushibaike.com/text/page/1/")
#
# ret1 = driver.find_elements_by_xpath("//div[@class='col1 old-style-col1']/div")
# for ret in ret1:
#     # print(ret.find_element_by_xpath(".//div[@class='content']/span").text)
#     print(ret.find_element_by_xpath(".//a[@class='contentHerf']").get_attribute("href"))
# print(ret1)
# 根据链接文字来获取链接地址
print(driver.find_element_by_link_text("下一页").get_attribute("href"))
print(driver.find_element_by_partial_link_text("下一").get_attribute("href"))
driver.quit()