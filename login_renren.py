import requests

#  实例化一个对象
passwd = input("please input your password:")
session = requests.session()
post_url = "http://www.renren.com/ajaxLogin/login"
post_data = {"email":"1084948810@qq.com","password":passwd}
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
session.post(post_url,data=post_data,headers=headers)
r = session.get("http://zhibo.renren.com/personcenter/index",headers=headers)
with open("renren.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())

