# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:47:03 2020

@author: HR
"""
import requests
from GetPic import  *
from lxml import etree

url1="https://www.ivsky.com/tupian/richu_riluo_v57799/"
r=respone=requests.get(url1).text
html=etree.HTML(r)
#/html/body/div[4]/div[4]/ul/li[3]/div/a
wbs=html.xpath('//ul/li/div[@class="il_img"]//@href')
print(type(wbs))
print(wbs)

for wb in wbs:
    name=wb.rsplit('/')[-1]
    print(name)
    wb="https://www.ivsky.com"+wb
    pictureget(wb,name)