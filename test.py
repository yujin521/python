import re
import random
import  requests

class download:

 def __init__(self):
    self.iplist = []  ##初始化一个list用来存放我们获取到的IP
    html = requests.get("http://haoip.cc/tiqu.htm")  ##不解释咯
    iplistn = re.findall(r'r/>(.*?)<b', html.text,
                         re.S)  ##表示从html.text中获取所有r/><b中的内容，re.S的意思是包括匹配包括换行符，findall返回的是个list哦！
    for ip in iplistn:
        i = re.sub('\n', '', ip)  ##re.sub 是re模块替换的方法，这儿表示将\n替换为空
        self.iplist.append(i.strip())  ##添加到我们上面初始化的list里面

    self.user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    def get(self, url, proxy=None):  ##给函数一个默认参数proxy为空
        UA = random.choice(self.user_agent_list)  ##从self.user_agent_list中随机取出一个字符串
        headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）

        if proxy == None:  ##当代理为空时，不使用代理获取response（别忘了response啥哦！之前说过了！！）
            response = requests.get(url, headers=headers)  ##这样服务器就会以为我们是真的浏览器了
            return response  ##返回response

        else:  ##当代理不为空
            IP = ''.join(str(random.choice(self.iplist)).strip())  ##将从self.iplist中获取的字符串处理成我们需要的格式（处理了些，什么自己看哦，这是基础呢）
            proxy = {'http': IP}  ##构造成一个代理
            response = requests.get(url, headers=headers, proxies=proxy)  ##使用代理获取response
            return response


Xz = download()  ##实例化
print(Xz.get("mzitu.com").headers)  ##打印headers