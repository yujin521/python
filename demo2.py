# -*- coding: utf-8 -*-
import xdrlib, sys
import xlrd
import pymongo
from bs4 import BeautifulSoup
import  requests
import re
import datetime
import csv



class demo2:
    def __init__(self):
        print('1')
        client =pymongo.MongoClient('localhost', 27017)  ##与MongDB建立连接（这是默认连接本地MongDB数据库）
        # db = client['meinvxiezhenji']  ## 选择一个数据库
        # self.meizitu_collection = db['meizitu']  ##在meizixiezhenji这个数据库中，选择一个集合
        db = client['demo']  # 给数据库命名
        test1=db['test1']
        self.collection= db['test1']
        self.ip = ''
        self.yuming = ''
        self.yumingjibie = ''
        self.isbeian=''
        self.yemianyuansu=''

    # def read_excel(self,name):
    #     workbook=xlrd.open_workbook(name)
    #     sheet= workbook.sheet_by_index(0)  # sheet索引从0开始
    #     row = sheet.nrows
    #     col = sheet.ncols
    #     for rows in range(1, row):
    #         # print(sheet2.row_values(rows))
    #         self.ip=sheet.row(rows)[0].value
    #         self.yuming=sheet.row(rows)[1].value
    #         url = 'http://www.'+self.yuming
    #         # print(sheet.row(rows)[1].value)
    #         self.get_a(url)
    def  read_csv(self,name):
        csv_reader = csv.reader(open(name))
        for row in csv_reader:
            if csv_reader.line_num==1:
                continue
            self.ip = row[0]
            self.yuming = row[1]
            self.yumingjibie=row[2]
            url = 'http://www.' + self.yuming
            n=int(csv_reader.line_num)-1
            print('正在插入第'+str(n)+'条数据')
            self.get_a(url)
    def request(self, url):
        print(url)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        try:
            # 重新链接次数
            # requests.adapters.DEFAULT_RETRIES = 0
            start_html = requests.get(url, headers=headers, allow_redirects=False,timeout=1)
            start_html.encoding = 'utf-8'
        except requests.RequestException as e:
            start_html = 1
            print(e)

        return start_html



    def get_a(self, url):
        try:
            html = self.request(url)


            if html == 1:

                self.yemianyuansu = 'http://www.beian.gov.cn/portal/registerSystemInfo'
                self.isbeian = '网站错误'
                data = {
                    'IP': self.ip,
                    '域名': self.yuming,
                    '域名级别': self.yumingjibie,
                    '是否备案': self.isbeian,
                    '页面元素': self.yemianyuansu,
                    '获取时间': datetime.datetime.now()
                }
                self.collection.save(data)
                print(self.yuming + '连接超时')


            else:
                soup = BeautifulSoup(html.text, 'lxml')
                s = soup.find_all(href=re.compile(r"http://www.beian.gov.cn/portal/registerSystemInf"))

                if s:

                    self.yemianyuansu='http://www.beian.gov.cn/portal/registerSystemInfo'
                    self.isbeian='已备案'
                    data={
                    'IP':self.ip,
                    '域名':self.yuming,
                    '域名级别':self.yumingjibie,
                    '是否备案':self.isbeian,
                    '页面元素':self.yemianyuansu,
                    '获取时间':datetime.datetime.now()
                    }
                    self.collection.save(data)
                    print(self.yuming+'已经备案')
                else:

                    self.yemianyuansu='http://www.beian.gov.cn/portal/registerSystemInfo'
                    self.isbeian='已备案'
                    data={
                    'IP':self.ip,
                    '域名':self.yuming,
                    '域名级别':self.yumingjibie,
                    '是否备案':'未备案',
                    '页面元素':self.yemianyuansu,
                    '获取时间':datetime.datetime.now()
                    }
                    self.collection.save(data)
                    print(self.yuming+'未备案')
        except 'error':
                print('get_a方法错误')


Demo2=demo2()
Demo2.read_csv('E:\jinan.csv')
#Demo2.read_excel('E:\jinan.xlsx')







