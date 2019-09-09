import geturl
import requests

#输入查票信息获取url
url = geturl.geturl()
# url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=北京,BJP&ts=济南,JNK&date=2019-10-01&flag=N,N,Y'
print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
recode = requests.get(url,headers = headers)
print(recode)
request = requests.get(url,headers = headers).text
with open('requests.html','w',encoding='utf-8') as f:
    f.write(request)
# print(request)
