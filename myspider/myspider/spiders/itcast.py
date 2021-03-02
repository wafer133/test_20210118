# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # ret1 = response.xpath("//div[@class='maincon']/ul/li//h2/text()").extract()
        # print(ret1)

        li_list = response.xpath("//div[@class='maincon']/ul/li")
        for li in li_list:
            item = {}
            item["name"] = li.xpath(".//h2/text()").extract_first()
            item["title"] = li.xpath(".//h2/span/text()").extract_first()
            # print(item)
            logger.warning(item)
            yield item