# -*- coding: utf-8 -*-
import scrapy
import json
import re


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1614616268558&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn']



    def parse(self, response):
        # 模板url
        template_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1614616268558&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        # 请求的url地址
        request_url = response.request.url
        print(request_url)
        data_dict_all = json.loads(response.text)
        data_list = data_dict_all["Data"]["Posts"]
        # print(data_list)
        for data in data_list:
            item = {}
            item['title'] = data["RecruitPostName"]
            item['positon'] = data["CategoryName"]
            item['publish_data'] = data["LastUpdateTime"]
            item['job_group'] = data["ProductName"]
            item['job_description'] = data["Responsibility"]
            yield item
        # 获取next_url
        # 先获取请求url地址中的页数数字
        num = re.search("pageIndex=(\d+)", request_url).group(1)
        num = int(num) + 1
        print(num)
        if num <= 800:
            next_url = template_url.format(num)
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )





