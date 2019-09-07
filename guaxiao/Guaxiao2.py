import requests
import re
from selenium import webdriver

dirver = webdriver.Chrome()
name = input("请输入想要搜索的电影：")
age = input("请输入该电影的年份：")
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'Cookie': 'll="118221"; bid=b5LpewLdnVY; _vwo_uuid_v2=DC75B4B868FD59DEC85884806198F81A3|5a04615aaef6d6cb5f3b2b375f0677cd; __utmz=30149280.1567691959.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E9%93%B6%E6%B2%B3%E8%A1%A5%E4%B9%A0%E7%8F%AD; __utmz=223695111.1567691959.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E9%93%B6%E6%B2%B3%E8%A1%A5%E4%B9%A0%E7%8F%AD; UM_distinctid=16d01b8eccf11f-0806683fb2eb85-5f4e2917-1fa400-16d01b8ecd01a0; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1567830692%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E9%2593%25B6%25E6%25B2%25B3%25E8%25A1%25A5%25E4%25B9%25A0%25E7%258F%25AD%22%5D; _pk_ses.100001.4cf6=*; CNZZDATA1272964020=1156033415-1567690737-https%253A%252F%252Fwww.baidu.com%252F%7C1567828514; __utma=30149280.1352288175.1566450504.1567825226.1567830692.4; __utma=223695111.1060243643.1566450504.1567825226.1567831192.4; __utmb=223695111.0.10.1567831192; _pk_id.100001.4cf6=2da0fc0921a8633a.1566450507.4.1567831471.1567826439.; __utmt=1; __utmb=30149280.7.10.1567830692','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}

url = f'https://movie.douban.com/subject_search?search_text={name}&cat=1002' + '&start=' + '0'
# print(url)
resp = dirver.get(url)  # 打开浏览器
# with open(str(i) + f'{name}.html', 'w', encoding='utf-8') as f:
#     f.write(dirver.page_source)
movie_list = re.findall(r'<a.*?>.*?</a>',dirver.page_source)
title_info = []
for i in movie_list:
    tempd = re.findall(rf'<a href="https://movie.douban.com/subject/.*?class="title-text">{name}.*?\({age}\)</a>',i)
    if tempd != []:
        title_info.append(tempd[0])
if title_info == []:
    print("匹配不成功，请重新核对电影名和电影年份")
else:
    movie_id = re.findall(r"subject_id:'(.*?)'", title_info[0])
    movie_url = 'https://movie.douban.com/subject/' + movie_id[0]
    print(movie_id[0])
    print(movie_url)
dirver.close()
