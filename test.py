import re


start_urls = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1614616268558&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=894&pageSize=10&language=zh-cn&area=cn'
template_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1614616268558&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'

num = re.search("pageIndex=(\d+)", start_urls).group(1)
print(type(num))
print(type(int(num)))
print(num)