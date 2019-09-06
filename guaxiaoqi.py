import requests
import json

url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=1'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
resp = requests.get(url,headers=headers)
sd=json.loads(resp.text)
# print(sd)
# print(sd["subjects"][0]["rate"])
while True:
    i = 0
    movie = input("请输入你想搜索的电影（按q退出）：")
    if (movie == 'q'):
        break
    else:
        for i in range(len(sd["subjects"])):
            if sd["subjects"][i]["title"] == movie:
                break
        if i == len(sd["subjects"])-1 and movie != sd["subjects"][len(sd["subjects"])-1]["title"] :
            print("没有该电影")
        else:
            print(movie,"豆瓣评分为：",sd["subjects"][i]["rate"])
