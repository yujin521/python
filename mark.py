# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import datetime
import csv
import mysql.connector


class demo2:
    def __init__(self):

        cnx = mysql.connector.connect(user='root', password='yujin', host='127.0.0.1', db='test')
        self.cnx = cnx

    def select(self):
        cursor = self.cnx.cursor()
        sql = "SELECT * FROM domain_cs_sjz "
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            n = 0
            for row in results:
                n = n + 1
                print(n)
                id = row[0]
                website = row[3]
                url_website = 'http://www.' + website
                print('正在更新第' + str(n) + '条数据')
                self.get_a(url_website, id)
        except:
            print('error')
        self.cnx.close()

    def request(self, url):
        print(url)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        try:
            # 重新链接次数
            # requests.adapters.DEFAULT_RETRIES = 0
            start_html = requests.get(url, headers=headers, allow_redirects=False, timeout=1)
            start_html.encoding = 'utf-8'
        except requests.RequestException as e:
            start_html = 1
            print(e)

        return start_html

    def get_a(self, url, id):
        try:
            html = self.request(url)

            if html == 1:
                print('网站错误，连接失败')

                # self.yemianyuansu = 'http://www.beian.gov.cn/portal/registerSystemInfo'
                # self.isbeian = '3'
                # data = {
                #     'IP': self.ip,
                #     '域名': self.yuming,
                #     '域名级别': self.yumingjibie,
                #     '是否备案': self.isbeian,
                #     '页面元素': self.yemianyuansu,
                #     '获取时间': datetime.datetime.now()
                # }
                # self.collection.save(data)
                # print(self.yuming + '连接超时')
                # cursor=self.cnx.cursor()
                # sql="UPDATE domain_cs_sjz SET  mark_flag=3 WHERE id='%s'"%(int(id))
                # try:
                #     cursor.execute(sql)
                #     self.cnx.commit()
                # except:
                #     print('error')
                # self.cnx.commit()



            else:
                soup = BeautifulSoup(html.text, 'lxml')
                s = soup.find_all(href=re.compile(r"http://www.beian.gov.cn/portal/registerSystemInf"))

                if s:

                    self.yemianyuansu = 'http://www.beian.gov.cn/portal/registerSystemInfo'
                    # self.isbeian='已备案'
                    # data={
                    # 'IP':self.ip,
                    # '域名':self.yuming,
                    # '域名级别':self.yumingjibie,
                    # '是否备案':self.isbeian,
                    # '页面元素':self.yemianyuansu,
                    # '获取时间':datetime.datetime.now()
                    # }
                    # self.collection.save(data)
                    # print(self.yuming+'已经备案')
                    cursor = self.cnx.cursor()
                    now = datetime.datetime.now()
                    now = now.strftime("%Y-%m-%d %H:%M:%S")
                    sql = "UPDATE domain_cs_sjz SET  mark_flag=1,update_time='%s' WHERE id='%s'" %(now,int(id))
                    try:
                        cursor.execute(sql)
                        self.cnx.commit()
                    except:
                        print('error')
                    self.cnx.commit()
                else:

                    # self.yemianyuansu='http://www.beian.gov.cn/portal/registerSystemInfo'
                    # self.isbeian='已备案'
                    # data={
                    # 'IP':self.ip,
                    # '域名':self.yuming,
                    # '域名级别':self.yumingjibie,
                    # '是否备案':'未备案',
                    # '页面元素':self.yemianyuansu,
                    # '获取时间':datetime.datetime.now()
                    # }
                    # self.collection.save(data)
                    # print(self.yuming+'未备案')
                    cursor = self.cnx.cursor()
                    now = datetime.datetime.now()
                    now = now.strftime("%Y-%m-%d %H:%M:%S")
                    sql = "UPDATE domain_cs_sjz SET  mark_flag=0,update_time='%s' WHERE   id='%s'" %(now,int(id))
                    try:
                        cursor.execute(sql)
                        self.cnx.commit()
                    except:
                        print('error')
                    self.cnx.commit()
        except 'error':
            print('get_a方法错误')


Demo2 = demo2()
# Demo2.read_csv('E:\jinan.csv')
# Demo2.read_excel('E:\jinan.xlsx')
Demo2.select()







