from lxml import etree
import requests
url= 'https://movie.douban.com'
resp = requests.get(url)
str = resp.content
# print(str)
et = etree.HTML(str)
node = et.xpath('//*[@id="screening"]/div[2]/ul/li[1]/ul/li[2]/a/text()')
print(node)
