from bs4 import BeautifulSoup
import requests
import time
import pymongo

# 定义数据库
client = pymongo.MongoClient('localhost', 27017)
rent_info = client['rent_info']  # 给数据库命名
sheet_table = rent_info['sheet_table']  # 创建表单
# 将数据存入数据库
data = {
'标题': 'aaaa',
'地址': 'vvvv',
'日租金': '3',
'图片': '4',
'房东头像': '3',
'房东姓名': '3',
'房东性别': '3'
}
print(data)
sheet_table.insert_one(data)
