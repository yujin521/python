# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import  requests
import re
import datetime
import csv
import mysql.connector




class demo2:
    def __init__(self):

        cnx = mysql.connector.connect(user='xiaofan', password='lanke7758521', host='123.183.218.70', db='jinan')
        # cnx = mysql.connector.connect(user='root', password='yujin', host='127.0.0.1', db='test')
        self.cnx=cnx

    def select(self):
        cursor = self.cnx.cursor()
        sql="SELECT * FROM domain_cs_sjz_copy_copy WHERE city='潍坊'"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            n =0
            for row in results:
                n=n+1
                print(n)
                id=row[0]
                website=row[3]
                url_website='http://www.'+website

                print('正在更新第' + str(n) + '条数据')
                self.get_a(url_website,id)
        except BaseException as  e:
            print(e)
        self.cnx.close()


    def request(self, url):
        print(url)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        try:
            # 重新链接次数
            # requests.adapters.DEFAULT_RETRIES = 0
            start_html = requests.get(url, headers=headers, allow_redirects=False,timeout=5)
            start_html.encoding = 'utf-8'
        except requests.RequestException as e:
            start_html = 1
            print(e)
        return start_html

    def request2(self, url):
        newurl = "http://" + url[11:100]
        print(url)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        try:
            # 重新链接次数
            # requests.adapters.DEFAULT_RETRIES = 0
            start_html = requests.get(newurl, headers=headers, allow_redirects=False, timeout=5)
            start_html.encoding = 'utf-8'
        except requests.RequestException as e:
            start_html = 2
            print(e)
        return start_html
    def get_a(self, url,id):
        try:
            html = self.request(url)
            if html == 1:
                print('带www网站错误，连接失败,尝试不带www')
                newurl = "http://" + url[11:100]
                html2=self.request2(newurl)
                if html2==2:
                 print('说明带或者不带（www）都打不开')
                 cursor = self.cnx.cursor()
                 now = datetime.datetime.now()
                 now = now.strftime("%Y-%m-%d %H:%M:%S")
                 sql = "UPDATE domain_cs_sjz_copy_copy SET  close_flag=0,update_time='%s',mark_flag=2 WHERE id='%s'" % (
                 now, int(id))
                 try:
                    cursor.execute(sql)
                    self.cnx.commit()
                 except:
                    print('error222222222')
                 self.cnx.commit()
                elif html2.status_code==200:
                    self.update_mark(html2,id)
                else:
                    self.update_mark_4_5(id)
            elif html.status_code==200:
               self.update_mark(html,id)
            # 除了200之外的返回码
            else:
               self.update_mark_4_5(id)
        except 'error':
                print('get_a方法错误')
     # 返回码为其他40X 50X 开头的代码
    def update_mark_4_5(self,id):
        cursor = self.cnx.cursor()
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        sql = "UPDATE domain_cs_sjz_copy_copy SET  mark_flag=2,update_time='%s',close_flag=0 WHERE id='%s'" % (
            now, int(id))
        try:
            cursor.execute(sql)
            self.cnx.commit()
        except:
            print('error66666666666')
        self.cnx.commit()
    # 返回码为200时候的方法
    def update_mark(self,html,id):
        soup = BeautifulSoup(html.text, 'lxml')
        s = soup.find_all(href=re.compile(r"http://www.beian.gov.cn/portal/registerSystemInf"))

        if s:
            cursor = self.cnx.cursor()
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            sql = "UPDATE domain_cs_sjz_copy_copy SET  mark_flag=1,update_time='%s',close_flag=1 WHERE id='%s'" % (
            now, int(id))
            try:
                cursor.execute(sql)
                self.cnx.commit()
            except:
                print('error55555555555')
            self.cnx.commit()
        else:
            cursor = self.cnx.cursor()
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            sql = "UPDATE domain_cs_sjz_copy_copy SET  mark_flag=0,update_time='%s',close_flag=1 WHERE id='%s'" % (
            now, int(id))
            try:
                cursor.execute(sql)
                self.cnx.commit()
            except:
                print('error66666666666')
            self.cnx.commit()


Demo2=demo2()
# Demo2.read_csv('E:\jinan.csv')
# Demo2.read_excel('E:\jinan.xlsx')
Demo2.select()







