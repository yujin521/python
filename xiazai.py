import requests

import urllib

r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')	# 云音乐热歌榜

arr=r.json()['result']['tracks']

for i   in range(10):
    
    name=str(i+1)+''+arr[i]['name']+'.mp3'
    
    link=arr[i]['mp3Url']

    urllib.request.urlretrieve(link,'aaa\\'+name)
    
    print(name+'下载完成')
