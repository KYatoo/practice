from function import *
from onepage import *
from AllAtlas import *

url = input("请输入链接：")
# url = "https://www.meituri.com/x/37/"
pagelist = GetIndexPage(url)
altasurl = []
altasname = []
for page in pagelist:
    [altasurl1,altasname2] = GetAltasInfo(page)
    # print(altasurl1)
    # print(altasname2)https://www.meituri.com/x/81/
    altasurl = altasurl + altasurl1
    altasname = altasname + altasname2
# print(len(altasurl))
# print(len(altasname))

if len(altasurl) == len(altasname):
    print("解析成功，共有%d个图集" %len(altasname))
    for i in range(len(altasname)):
        # try三次
        for j in range(3):
            try:
                print("正在下载第%d个图集" % (i+1))
                url = altasurl[i]
                name = altasname[i]
                DloadAtlas(url, name)
                break
            except:
                pass
else:
    print("解析失败，请重试")