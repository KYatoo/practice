# -*- coding: utf-8 -*-

import requests
from lxml import etree
import re

url = 'https://wall.alphacoders.com/search.php?search=d.va'
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
resp = requests.get(url,headers = headers).text

urls = re.findall(r'<div class=\'boxgrid\'>[\s\S]*?src="(https://.*?)"[\s\S]*?</div>', resp, re.DOTALL)
for url in urls:
    print(url)


# xpa = etree.HTML(resp)
# xpa.xpath('//*[@id="thread_list"]/li[2]/div[0]/div[1]/div[1]/div[0]/div[1]/div[0]/div[0]/ul/li[1]/a')for


