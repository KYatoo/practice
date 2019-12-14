import requests
url = ['https://static.playoverwatch.com/media/reference/genji_reference.pdf',[]]
print(*url)
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
res = requests.get(url=url[0],headers=headers)
with open('genji.pdf','wb') as f:
    f.write(res.content)