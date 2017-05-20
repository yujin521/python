import requests  ##导入requests
from bs4 import BeautifulSoup  ##导入bs4中的BeautifulSoup
import os

headers = { 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.mmjpg.com'  ##开始的URL地址
start_html = requests.get(all_url, headers=headers)
start_html.encoding='utf-8'
soup = BeautifulSoup(start_html.text, 'lxml')
index_max_page_href=soup.find('div',class_='page').find_all('a')[-1]
index_max_page=index_max_page_href['href'].split('/')[2]
all_url_page=index_max_page_href['href']
for index_pages in  range(1,int(index_max_page)+1):
    title_name='第'+str(index_pages)+"大页"
    isEreate = os.path.exists(os.path.join("E:\mzitu", title_name))
    if not isEreate:
        print(u'建了一个名字叫做', title_name, u'的文件夹！')
        os.makedirs(os.path.join("E:\mzitu", title_name))
        os.chdir(os.path.join("E:\mzitu", title_name))  ##切换到目录
    else:
        print(u'名字叫做', title_name, u'的文件夹已经存在了！')
    index_max_page_url=all_url+'/home/'+str(index_pages)
    index_age_html=requests.get(index_max_page_url, headers=headers)
    index_age_html.encoding='utf-8'
    soup_all=BeautifulSoup(index_age_html.text,'lxml')
    all_a=soup_all.find('div',class_='pic').find_all('a',target='_blank')
    for a in all_a:
            title = a.get_text()  # 取出a标签的文本
            path = str(title).strip()+'caib'  ##去掉空格
            isExists = os.path.exists(os.path.join("E:\mzitu\\"+title_name, path))
            if not isExists:
                print(u'建了一个名字叫做', path, u'的文件夹！')
                os.makedirs(os.path.join("E:\mzitu\\"+title_name, path))
                os.chdir(os.path.join("E:\mzitu\\"+title_name, path))  ##切换到目录
            else:
                print(u'名字叫做', path, u'的文件夹已经存在了！')
            href = a['href']
            html = requests.get(href, headers=headers)
            html.encoding = 'utf-8'
            html_soup = BeautifulSoup(html.text, 'lxml')
            max_page = html_soup.find('div', class_='page').find_all('a')[-2].get_text()
            max_page = int(max_page)
            print(max_page)
            for page in range(1, int(max_page + 1)):
                page_url = href + '/' + str(page)
                # print(page_url)
                imge_html = requests.get(page_url)
                imge_html.encoding = 'utf-8'
                imge_html_soup = BeautifulSoup(imge_html.text, 'lxml')
                image_url = imge_html_soup.find('div', class_='content').find('img')['src']
                name = str(page) + 'meizi'  ##取URL 倒数第四至第九位 做图片的名字
                img = requests.get(image_url, headers=headers)
                # print(name)
                f = open(name + '.jpg', 'ab')  ##写入多媒体文件必须要 b 这个参数！！必须要！！
                f.write(img.content)  ##多媒体文件要是用conctent哦！
                print(str(name) + '下载完成')
                f.close()


