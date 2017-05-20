import requests  ##导入requests
from bs4 import BeautifulSoup  ##导入bs4中的BeautifulSoup
import os


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.mmjpg.com/hot/'  ##开始的URL地址
start_html = requests.get(all_url,
                          headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
start_html.encoding='utf-8'
#print(start_html.text)  ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
Soup = BeautifulSoup(start_html.text, 'lxml')
#li_list = Soup.find_all('li') ##使用BeautifulSoup解析网页过后就可以用找标签呐！（find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）
#for li in li_list: ##这个不解释了。看不懂的效小哥儿回去瞅瞅基础教程
    #print(li) ##同上
#all_a = Soup.find('div', class_='pic').find_all('a') ##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签

# li_list=Soup.find_all('li')

# for li in li_list:
#     print(li)
all_a=Soup.find('div',class_='pic').find_all('a')
for a in  all_a:
    title = a.get_text()  # 取出a标签的文本
    path = str(title).strip()  ##去掉空格
    isExists = os.path.exists(os.path.join("D:\mzitu", path))
    if not isExists:
        print(u'建了一个名字叫做', path, u'的文件夹！')
        os.makedirs(os.path.join("D:\mzitu", path))
    else:
        print(u'名字叫做', path, u'的文件夹已经存在了！')
    href=a['href']
    html=requests.get(href,headers=headers)
    html.encoding='utf-8'
    html_soup=BeautifulSoup(html.text,'lxml')
    max_page=html_soup.find('div',class_='page').find_all('a')[-2].get_text()
    max_page = int(max_page)
   # print(max_page)
for page in range(1,int(max_page+1)):
    page_url=href+'/'+str(page)
    # print(page_url)
    imge_html= requests.get(page_url)
    imge_html.encoding='utf-8'
    imge_html_soup=  BeautifulSoup(imge_html.text,'lxml')
    image_url= imge_html_soup.find('div',class_='content').find('img')['src']
    name = str(page)+'meizi' ##取URL 倒数第四至第九位 做图片的名字
    img = requests.get(image_url, headers=headers)
    # print(name)
    f = open(name + '.jpg', 'ab')  ##写入多媒体文件必须要 b 这个参数！！必须要！！
    f.write(img.content)  ##多媒体文件要是用conctent哦！
    f.close()

