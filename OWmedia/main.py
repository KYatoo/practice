import requests,re

url = 'https://playoverwatch.com/zh-tw/media'
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
res = requests.get(url,headers=headers).text
# print(requests.get(url,headers=headers).encoding)
# with open('html.html','w',encoding='utf-8') as f:
#     f.write(res)
coslist = re.findall(r'<li class="column md-4 lg-3.*?" data-media-id="([^<>]*?)-cosplay">(.*?)</li>',res)
# print(*coslist)
# for i in coslist:
#     print(i[0])
urllist = []
for i in coslist:
    urllist.append(re.findall(r'(https.*?pdf)',i[1]))
for i in range(len(urllist)):
    for j in range(4):
        try:
            url = urllist[i][0]
            print(url)
            fillle = requests.get(url,headers=headers).content
            break
        except:
            print("test%d fail" %j)
            pass
    if j >2:
        print("Download fail")
        continue
    with open('%s.pdf' %coslist[i][0],'wb') as f2:
        f2.write(fillle)