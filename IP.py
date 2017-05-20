from bs4 import BeautifulSoup
import  requests
import urllib.request,io,os,sys
import re





class ip:
    def request(self, url):

      headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

      try:

            # newurl="http://"+url[11:100]
            start_html = requests.get(url, headers=headers,timeout=None)
            req = urllib.request.Request("http://goodyee.com/")
            f = urllib.request.urlopen(req)

            s = f.read()
            s = s.decode('gbk', 'ignore')
            print(s)
            mdir = sys.path[0] + '/'
            file = open(mdir + 'admin6.txt', 'a', 1, 'utf-8')
            file.write(s)
            file.close()
            r=requests.head(url, stream=True)
            # print(r.headers)
            start_html.raise_for_status()

            start_html.encoding = 'utf-8'
            # print(start_html.text)
            # print(start_html.status_code)
      except requests.RequestException as e :
          print(e)

      return  start_html




    def get_a(self,url):
        html=self.request(url)

        # soup = BeautifulSoup(html.text, 'lxml')

        # # regex=re.compile(r"http://www.beian.gov.cn/portal/registerSystemInf")
        #
        #
        # s = soup.find_all(href=re.compile(r"http://www.beian.gov.cn/portal/registerSystemInf"))
        #
        #
        # print(s)
        # if s:
        #  print('yes')
        # else:
        #  print('no')






ip=ip()
ip.get_a('http://goodyee.com/')




