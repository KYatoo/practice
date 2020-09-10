import requests
from lxml import etree

def searchfilm(movie_name,movie_age):
    url = 'https://www.1905.com/search/?q='+movie_name
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    resp = requests.get(url,headers=headers).text
    html = etree.HTML(resp)
    print(type(html))
    find_list = html.xpath('//*[@id="TStopPIC90"]/div[2]/div[2]/div[2]/div[1]')
    print(*find_list)
    # code = requests.get(url).encoding
    # with open('resp.html','w',encoding=code) as f:
    #     f.write(resp)

if __name__ =="__main__":
    print(searchfilm("爱宠大机密2",2019))