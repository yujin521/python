from bs4 import BeautifulSoup
import os
from Download import request ##导入模块变了一下
from pymongo import MongoClient
import datetime



class mzitu():
   def __init__(self):
        client = MongoClient()  ##与MongDB建立连接（这是默认连接本地MongDB数据库）
        db = client['meinvxiezhenji']  ## 选择一个数据库
        self.meizitu_collection = db['meizitu']  ##在meizixiezhenji这个数据库中，选择一个集合
        self.title = ''  ##用来保存页面主题
        self.url = ''  ##用来保存页面地址
        self.title1 = ''  ##用来保存页面主题
        self.url1 = ''  ##用来保存页面地址
        self.img_urls = []  ##初始化一个 列表 用来保存图片地址
   def createpackages(self,path,title_name):
        print(path)
        isExists = os.path.exists(os.path.join("E:\mzitu\\" + title_name, path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("E:\mzitu\\" + title_name, path))
            os.chdir(os.path.join("E:\mzitu\\" + title_name, path))  ##切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False
   def createpackage(self,name):
        title_name = '第' + str(name) + "大页"
        isEreate = os.path.exists(os.path.join("E:\mzitu", title_name))
        if not isEreate:
            print(u'建了一个名字叫做', title_name, u'的文件夹！')
            os.makedirs(os.path.join("E:\mzitu", title_name))
            os.chdir(os.path.join("E:\mzitu", title_name))  ##切换到目录
            return True
        else:
            print(u'名字叫做', title_name, u'的文件夹已经存在了！')
            return False
   # def request(self,url):
   #      headers = {
   #          'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
   #      start_html = request.get(url, headers=headers)
   #      start_html.encoding = 'utf-8'
   #      return start_html
   def all_index_page(self,url):
        html=request.get(url, 3)
        soup = BeautifulSoup(html.text, 'lxml')
        index_max_page_href = soup.find('div', class_='page').find_all('a')[-1]
        index_max_page = index_max_page_href['href'].split('/')[2]
        all_url_page = index_max_page_href['href']
        for index_pages in range(1, int(index_max_page) + 1):
            self.createpackage(index_pages)
            title_name = '第' + str(index_pages) + "大页"
            self.title=title_name
            print(title_name)
            self.all_a(url,index_pages,title_name)
   def all_a(self,url,index_pages,title_name):
        index_max_page_url = url + '/home/' + str(index_pages)
        self.url=index_max_page_url
        print(index_max_page_url)
        index_age_html=request.get(index_max_page_url,3)
        soup_all = BeautifulSoup(index_age_html.text, 'lxml')
        all_a = soup_all.find('div', class_='pic').find_all('a', target='_blank')

        for a in all_a:
            title = a.get_text()  # 取出a标签的文本
            path = str(title).strip() + 'caib'  ##去掉空格
            self.title1=path
            self.createpackages(path,title_name)
            href = a['href']
            self.url1=href
            print('222')
            page_html=request.get(href,3)
            page_html_soup=BeautifulSoup(page_html.text,'lxml')
            max_page = page_html_soup.find('div', class_='page').find_all('a')[-2].get_text()
            max_page = int(max_page)

            self.page(href,max_page)

   def page(self,href,max_page):
        for page in range(1, int(max_page + 1)):
            page_url = href + '/' + str(page)
            # print(page_url)
            self.img(page_url,page)  ##调用img函数
   def img(self,page_url,page):
       img_html=request.get(page_url,3)
       imge_html_soup_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='content').find('img')['src']
       self.img_urls.append(imge_html_soup_url)
       self.img_save(imge_html_soup_url,page)
       post = {  ##这是构造一个字典，里面有啥都是中文，很好理解吧！
           '标题': self.title,
           '主题页面': self.url,
           '图片地址': self.img_urls,
           '获取时间': datetime.datetime.now()
       }
       self.meizitu_collection.save(post)  ##将post中的内容写入数据库。
       print(u'插入数据库成功')
   def img_save(self,imge_html_soup_url,page):
       name = str(page) + 'meizi'  ##取URL 倒数第四至第九位 做图片的名字
       img=request.get(imge_html_soup_url,3)
       f = open(name + '.jpg', 'ab')  ##写入多媒体文件必须要 b 这个参数！！必须要！！
       f.write(img.content)  ##多媒体文件要是用conctent哦！
       print(str(name) + '下载完成')
       f.close()
Mzitu = mzitu() ##实例化
Mzitu.all_index_page('http://www.mmjpg.com')












