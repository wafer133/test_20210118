import requests
import re
import json


class NeiHan:

    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
        self.temp_url = "http://www.neihanshu.net/text/index_{}.html"

    def pars_url(self,url):
        html_str = requests.get(url, headers=self.headers)
        print(html_str.status_code)
        if html_str.status_code == 404:
            return "none"
        return html_str.content.decode(encoding="utf-8")

    def get_jokes(self, html_str):
        joke_list = re.findall(r"<p>(.*?)</p>", html_str)  # 这个(.*)可以取出来需要的数据要学一下
        # 把一些没用的数据去掉
        i = 0
        # while i < len(joke_list):
        #     pass
        # print(joke_list)
        return joke_list

    def save_jokes(self, joke_list):
        with open("neihan1.txt", "a") as f:
            for joke in joke_list:
                f.write(json.dumps(joke,ensure_ascii=False))
                f.write("\n")

    def run(self):  # 用来写主要逻辑
        num = 1
        while True:
            # 1、构造url地址
            if num == 1:
                url = "http://www.neihanshu.net/text/index.html"
            else:
                url = self.temp_url.format(num)
            # 2、发送请求，获取响应
            html_str = self.pars_url(url)
            if html_str == "none":
                break
            # 3、提取段子数据
            joke_list = self.get_jokes(html_str)
            # 4、保存段子数据
            self.save_jokes(joke_list)
            num += 1


if __name__ == '__main__':
    neihan = NeiHan()
    neihan.run()