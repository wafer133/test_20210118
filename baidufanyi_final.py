import requests
import json
"""
由于百度反爬虫，这个程序只能爬“你好”这个单词
"""

class BaiduFanyi:
    def __init__(self, wordTofanyi):
        self.lan_detect_url = "https://fanyi.baidu.com/langdetect"
        self.lan_fanyi_url = "https://fanyi.baidu.com/v2transapi?"
        self.wordTofanyi = wordTofanyi
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36",
                          "Cookie":"BIDUPSID=916A8FEF06FEC39E7BE677337E1F29C2; PSTM=1610853061; BAIDUID=916A8FEF06FEC39EE436D30B3B47F2E4:FG=1; __yjs_duid=1_e194e91e286d0babddffe1787f2b4a521610856915888; BDUSS=1NTWjVNRGN2MTB5RG1tdXpZdEpMWjFEMU90TGpJSGdMNnlGY005VmVPaUFKaTFnSVFBQUFBJCQAAAAAAAAAAAEAAACA-dMc0KGw18H6MTMzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICZBWCAmQVgR; BDUSS_BFESS=1NTWjVNRGN2MTB5RG1tdXpZdEpMWjFEMU90TGpJSGdMNnlGY005VmVPaUFKaTFnSVFBQUFBJCQAAAAAAAAAAAEAAACA-dMc0KGw18H6MTMzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICZBWCAmQVgR; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; BAIDUID_BFESS=916A8FEF06FEC39EE436D30B3B47F2E4:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1611153378,1611673752; H_PS_PSSID=33425_33439_33344_33285_2453_33318_22160; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1611677661; PSINO=1; ab_sr=1.0.0_NjQ2ZDg4M2VmNTVhMTYwMWY3ODBhZDY0MGQwMjIzZTY1MjNiYTlhYjg2NDhjMmFkMjRiZmYwYzVlYTUxNzVjMDRmN2U1NDZmYTY2YTkxYjUyODgyNmRlODViODg3ZGI2; BA_HECTOR=00alal2la52520a59g1g10h2a0q",
                          # "Referer":"https://fanyi.baidu.com/"
        }

    def parse_url(self, url, data):
        res = requests.post(url, data=data, headers=self.headers).content.decode()
        return json.loads(res)

    def run(self):
        # 1、获取语言类型
        lan_dect_data = {"query": self.wordTofanyi}
        result_dict = self.parse_url(self.lan_detect_url, lan_dect_data)
        print(result_dict["lan"])  # 测试是否能拿到语言类型
        # 2、准备post的数据
        word_to_trans = {"query": self.wordTofanyi,
                         "from": "zh",
                         "to": "en",
                         # "transtype": "translang",
                         # # "simple_means_flag": 3,
                         "sign": "232427.485594",
                         "token": "79358f1619b5b59f70e85d9080f3a168",
                         # # "domain":"common"
                         }
        # 3、发送请求，获取响应
        trans_result = self.parse_url(self.lan_fanyi_url, word_to_trans)
        # print(trans_result)  # 测试是否拿到结果
        # 4、提取翻译结果
        print(trans_result["trans_result"]["data"][0]["dst"])
        # print(trans_result["trans"][0]["dst"])


if __name__ == '__main__':
    wordTofanyi = input("请输入要翻译的句子：")
    baidu_fanyi = BaiduFanyi(wordTofanyi)
    baidu_fanyi.run()
