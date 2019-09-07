# coding=ISO-8859-1
import  requests
import re

url = 'http://www.yingjiesheng.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
resp = requests.get(url,headers = headers).text
code=requests.get(url).encoding
# print(code)
# with open('2.html','w',encoding= code) as f:
#     f.write(resp)
offer_list = re.findall(r'<a.*?>.*?</a>',resp)
# for i in offer_list:
#     print(i)
# with open('3.txt','a+',encoding= code) as f:
#     for i in offer_list:
#         f.write(i + '\n')
jobs = []
links = []
x = []
for i in offer_list:
    temp1 = re.findall(r'<a href="(https://.*?)" target="_blank"><span style="color: #008000;">.*?</span>.*?</a>',i)
    temp2 = re.findall(r'<a href="https://.*?" target="_blank"><span style="color: #008000;">.*?</span>(.*?)</a>',i)
    if temp1 != [] and temp2 != []:
        links.append(temp1[0])
        jobs.append(temp2[0])
# print(*jobs)
# print(*links)
with open('2.md','w',encoding= code) as f:
    for i in range(len(jobs)):
        f.write(f'[{jobs[i]}]({links[i]})  \n')
# jobs_link = dict(zip(jobs, links))
# print(jobs_link)