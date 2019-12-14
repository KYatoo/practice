import requests,re,os

def getpicurl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
    res = requests.get(url,headers).text
    return res

def dloadpic(urllist,path):
    print("正在下载...")
    for i in range(len(urllist)):
        # try三次
        for j in range(3):
            try:
                img = requests.get(urllist[i]).content
                break
            except:
                pass
        with open('%s\\%s.jpg' % (path,str(i)),'wb') as f:
            f.write(img)

if __name__ == "__main__":
    #只能爬取该网站（https://www.enterdesk.com/）的图集
    # url = 'https://mm.enterdesk.com/bizhi/44170.html' #这里需要修改
    url = input("请输入图集url(请包含https):")
    name = input("请输入图集名：")
    res = getpicurl(url)
    reg = r'<div class="swiper-slide">.*?src="(.*?)".*?</div>'
    urllist = re.findall(reg,res)
    print(*urllist)
    path_pre = os.getcwd()
    path = path_pre + './%s' % name
    if not os.path.exists(path):
        os.mkdir(path)
    dloadpic(urllist,path)