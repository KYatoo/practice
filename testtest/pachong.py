import requests
# aaa = requests.get('http://www.baidu.com')
# aaa.encode = 'utf-8'
# with open ("aaa.txt",'w',encoding='utf-8') as a:
#     a.write(aaa.text)

aa = requests.get("http://pic1.win4000.com/wallpaper/c/53cdd1f7c1f21.jpg")
with open ("photo.png",'wb') as file:
    file.write(aa.content)
