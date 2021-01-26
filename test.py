import requests

# import json


url = "https://fanyi.baidu.com/basetrans"
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Referer": "https://fanyi.baidu.com/?aldtype=16047",
    "Cookie": "BAIDUID=B119776656517B374BC52FFFCABD12CB:FG=1;BIDUPSID=9F4397F7EE42057CFD3D5AB6E15ECCD2;"
}
datas = {
    "query": "人生苦短，我用python",
    "from": "zh",
    "to": "en",
    "sign": "289133.35420",
    "token": "25af0fc3d37f67bb72c376f704f15292"}
response = requests.post(url, data=datas, headers=headers)

print(response)
print(response.text)