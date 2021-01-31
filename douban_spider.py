import requests
import json


class DoubanSpider:
    def __init__(self):
        self.douban_url_list = [
            {
                "url_temp":"https://movie.douban.com/j/search_subjects?type=tv&tag=%E8%8B%B1%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                 "country":"UK"
             },
            {
                "url_temp": "https://movie.douban.com/tv/#!type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                "country": "US"
            },
            {
                "url_temp": "https://movie.douban.com/tv/#!type=tv&tag=%E6%97%A5%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                "country": "JAPAN"
            }
        ]
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        # print(response.content)
        # print(len(response.content))
        return response.content.decode()  # 返回json的字符串数据

    def parse_json(self, html_str):
        temp_str = json.loads(html_str)  # 这个得到的是个字典
        # print("------------------")
        # print(len(temp_str["subjects"]))
        # print(temp_str["subjects"])
        return temp_str["subjects"]  # 拿到字典中包含的电视剧列表

    def save_drama_list(self, drama_list, country):
        with open("douban_drama_list.txt", "a", encoding="utf-8") as f:
            for list_temp in drama_list:
                list_temp["country"] = country
                f.write(json.dumps(list_temp, ensure_ascii=False))
                f.write("\n")

    def run(self): # 实现主要逻辑
        # 1、start_url 第一个url
        for search_url in self.douban_url_list:
            print(search_url["country"])
            print("-------------------------------------------------------------------")
            num = 0  # 用来跳转页面的数字
            while True:
                start_url = search_url["url_temp"].format(num)
                if search_url["country"]=="US":
                    print(start_url)
                # 2、发送请求，获取响应
                html_str = self.parse_url(start_url)
                # 3、提取数据
                drama_list = self.parse_json(html_str)
                # print("********")
                print(len(drama_list))
                if len(drama_list) == 0:
                    break
                # 4、保存
                self.save_drama_list(drama_list, search_url["country"])
                # 5、构造下一页的url地址，进入循环
                num += 20


if __name__ == '__main__':
    doubanSpider = DoubanSpider()
    doubanSpider.run()

