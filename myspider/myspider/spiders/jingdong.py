# -*- coding: utf-8 -*-
import scrapy


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['jingdong.cn']
    start_urls = ['http://jingdong.cn/']

    def parse(self, response):
        pass
