from selenium import webdriver
import time


class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content(self):
        self.driver.get(self.start_url)
        temp_list = self.driver.find_elements_by_xpath("//main[@id='listAll']/section")
        # print(len(temp_list))
        # print(temp_list
        room_list = temp_list[1].find_elements_by_xpath(".//ul[@class='layout-Cover-list']/li")
        print(room_list)
        print(len(room_list))
        print("-"*60)
        item = {}
        i = 0
        for room in room_list:
            item["title"] = room.find_element_by_xpath(".//h3").text
            print(item["title"])

            i = i + 1
            if i//10 == 0:
                time.sleep(3)


        return room_list


    def run(self):  # 实现主逻辑
        # 1、第一个start_url
        # 2、获取斗鱼直播房间的信息
        content = self.get_content()

        self.driver.quit()


if __name__ == '__main__':
    douyu_spider = DouyuSpider()
    douyu_spider.run()
