import requests,re,os

#保存内容
def SaveFile(resquest,name):
    with open('%s' % name, 'wb') as f:
        f.write(resquest)

#初始化需要解析的url，获取该页面元素
def UrlInit(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
    res = requests.get(url,headers).content
    # resqust = requests.get(url, headers).content
    # SaveFile(resqust, 'res.html')
    return res

#下载一张图片
def DloadPic(url,path,name):
    for j in range(3):
        # try三次
        try:
            img = requests.get(url).content
            break
        except:
            pass
    with open('%s\\%s.jpg' % (path, name), 'wb') as f:
        f.write(img)

#下载多张图片(图片链接列表）
def DloadPics(urllist,path):
    print("正在下载...")
    for i in range(len(urllist)):
        DloadPic(urllist[i],path,str(i))

#在当前文件夹下创建一个文件夹，并获取起完整路径名
def mkdir(name):
    path_pre = os.getcwd() #获取当前路径
    path = path_pre + './%s' % name
    if not os.path.exists(path):
        os.mkdir(path)
    return path


if __name__ == "__main__":
    #只能爬取该网站（https://www.enterdesk.com/）的图集
    url = 'https://mm.enterdesk.com/bizhi/44170.html' #这里需要修改
    #url = input("请输入图集url(请包含https):")
    name = input("请输入图集名：")
    res = UrlInit(url)
    reg = r'<div class="swiper-slide">.*?src="(.*?)".*?</div>'
    urllist = re.findall(reg,res)
    print(*urllist)
    path = mkdir(name)
    DloadPics(urllist,path)