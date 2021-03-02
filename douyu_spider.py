from selenium import webdriver
from lxml import etree
import time


class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content(self):
        self.driver.get(self.start_url)
        time.sleep(15)   # 要睡眠一下，要不图片还没加载出来
        html_str = self.driver.page_source
        # print(html_str)
        html = etree.HTML(html_str)
        print(html)

        temp_ret = html.xpath("//main[@id='listAll']//section")
        print(temp_ret)
        ret = temp_ret[1].xpath(".//ul[@class='layout-Cover-list']/li")
        # print(len(ret))
        item_total = []
        for li in ret:
            item = {}
            item["title"] = li.xpath(".//h3/text()")
            item["game_type"] = li.xpath(".//div[@class='DyListCover-info']/span[@class='DyListCover-zone']/text()")
            item["ID"] = li.xpath(".//h2/div/text()")
            item["hotIcon"] = li.xpath(".//div[@class='DyListCover-info']/span/text()")[1]
            item["img"] = li.xpath(".//img/@src")[0]
            # item["description"] = li.xpath(".//div[@class='DyListCover-content']/span/text()")
            print(item["img"])
            # print()
            item_total.append(item)
        self.driver.quit()

        print(len(item_total))
        return item_total

    def run(self):  # 实现主逻辑
        # 1、第一个start_url
        # 2、获取斗鱼直播房间的信息
        content = self.get_content()

        item_total =self.driver.quit()


if __name__ == '__main__':
    douyu_spider = DouyuSpider()
    douyu_spider.run()
