from pymongo import MongoClient

client = MongoClient(host="127.0.0.1",port=27017)
collection = client["test"]["t251"]

# # 插入一条数据
# ret1 = collection.insert_one({"name":"xiaowang","age":10})
# print(ret1)
#
# # 插入多条数据
# data_list = [{"name":"test{}".format(i)} for i in range(10)]
# collection.insert_many(data_list)

# 查询一个记录
t = collection.find({"name":"xiaowang1"})
print(t)

for i in t:
    print(i)

for j in t:
    print(j,"*"*100)