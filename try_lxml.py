from lxml import etree

text = ''' <div> <ul>
        <li class="item-1"><a >first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''

html = etree.HTML(text)
print(html)
# 查看element对象中包含的字符串
# print(etree.tostring(html).decode())

# 获取class为item-1 li 下的a的href
ret1 = html.xpath("//li[@class='item-1']/a/@href")
print(ret1)

ret2 = html.xpath("//li[@class='item-1']/a/text()")
print(ret2)

# ret1为地址，ret2为标题，组建一个list, 这种方法的问题是，如果其中a标签缺少了一个就会对应不上
list1 = []
list2 = []
for href in ret1:
    item = {}
    item["href"] = href
    item["title"] = ret2[ret1.index(href)]
    list1.append(item)
print(list1)

print("*******************************************************************************************************")
# 正确提取页面的思路是
ret3 = html.xpath("//li[@class='item-1']")
for ret in ret3:
    item = {}
    item["href"] = ret.xpath("./a/@href")[0] if len(ret.xpath("./a/@href")) > 0 else None
    item["title"] = ret.xpath("./a/text()")[0] if len(ret.xpath("./a/text()")) > 0 else None
    list2.append(item)

print(list2)