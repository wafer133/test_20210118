import requests
from parse_url import parse_url
import json

url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E8%8B%B1%E5%89%A7&sort=recommend&page_limit=20&page_start=20"
html_str = parse_url(url)

ret1 = json.loads(html_str)
print(ret1)

with open("douban_yingju.json","w") as f:
    f.write(json.dumps(ret1,ensure_ascii=False,indent=2))