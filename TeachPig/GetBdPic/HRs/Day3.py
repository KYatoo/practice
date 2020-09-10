# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:38:59 2020

@author: HR
"""

import requests
import re
import os

#if __name__ == "__main__":#仅运行本脚本的时候执行，调用本脚本的时候不执行

url1="https://www.ivsky.com/tupian/richu_riluo_v57799/"
url = "https://www.ivsky.com/tupian/richu_riluo_v57799/pic_905990.html"
#os.makedirs('./img/',exist_ok=True)
html = requests.get(url1).text
#print(html)
#<h1>美丽的日出日落风景图片(13张) </h1>
rule0=r'<h1>(.*?)</h1>'
title=re.findall(rule0,html)[0]
print(title)
os.makedirs('./%s/'%title,exist_ok=True)

#< img src="//img.ivsky.com/img/tupian/t/201908/18/richu_riluo-004.jpg" alt="美丽的日出日落风景图片">
rule = r'<img.*?(//img.ivsky.com/img/tupian/t/.*?)" .*?>'
linklists= re.findall(rule, html)
print(linklists)
for linklist in linklists:
    linklist="http:"+linklist
    r=requests.get(linklist).content
    name=linklist.rsplit('/')[-1]#从右边开始切
    print(name)
    with open('./%s/%s'%(title,name) , mode='wb') as f:
        f.write(r)
        print("图片%s保存成功！"%name)