import requests
import json

class FanyiSpider():
    def __init__(self):
        self.headers = {"user-aget":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"}
        self.url = "https://fanyi.baidu.com/v2transapi?"

    def get_fanyi(self, wdToTranslate):
        post_data = {
            "from":"zh",
            "to":"en",
            "query":wdToTranslate,
            # "sign":"548627.834594",
            # "token":"79358f1619b5b59f70e85d9080f3a168"
        }
        r = requests.post(self.url, data=post_data, headers=self.headers)
        print("-------------")
        print(r.content.decode())
        dict_ret = json.loads(r.content.decode())
        print(dict_ret)
        print(dict_ret["trans"][0]["dst"])
        return dict_ret["trans"][0]["dst"]

    def run(self):  # 写主要逻辑
        # 获取要翻译的文字
        wdToTranslate = input("请输入要翻译的词语：")
        # 获取翻译后的字典
        fanyi_result = self.get_fanyi(wdToTranslate)
        # 输出
        print(fanyi_result)


if __name__ == '__main__':
    fanyi_spider = FanyiSpider()
    fanyi_spider.run()