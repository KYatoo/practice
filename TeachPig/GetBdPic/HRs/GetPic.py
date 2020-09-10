# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:37:17 2020

@author: HR
"""
import requests
import re

def pictureget(url, title):
    for i in range(0, 3):
        try:
            html = requests.get(url).text
            rule = r"<img.*?imgis.*?src='(.*?)'.*?>"
            linklist = re.findall(rule, html)
            # print(type(linklist))
            print(linklist)
            if linklist ==[]:
                continue
            link = "http:" + linklist[0]
            print(link)
            r = requests.get(link).content
            with open("%s.jpg" % title, 'wb') as f:
                f.write(r)
            print("图片%s下载成功" %title)
            return True
        except Exception as e :
            print(e)
    print("图片%s下载失败" % title)
    return False

if __name__ == "__main__":
    url = "https://www.ivsky.com/tupian/richu_riluo_v57799/pic_905990.html"
    urlfake = "http://www.baidu.com"
    name = "sun"
    print("##############################################################################################")
    print(pictureget(url,name))
    print("##############################################################################################")
    print(pictureget(urlfake,"fake"))
    print("##############################################################################################")
