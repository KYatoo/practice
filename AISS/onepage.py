from function import *
from lxml import etree

#得到某个网页的全部图片地址
def GetPicUrl(url):
    res = UrlInit(url)
    html = etree.HTML(res)
    piclist = html.xpath('//div[@class="content"]/img/@src')
    print("页面地址提取成功")
    # for i in htmldata:
    #     print(i)
    return piclist

#得到某个图集的全部网页的地址
def GetPageList(url):
    res = UrlInit(url)
    html = etree.HTML(res)
    page1 = html.xpath('//div[@id="pages"]/a[1]/@href')[0].encode().decode('utf-8')
    # print(type(page1))
    pagelistget = html.xpath('//div[@id="pages"]/a/@href')
    pagenum = []
    for i in pagelistget:
        i = i.encode().decode('utf-8')
        i = i.replace(page1, '').replace('.html', '')
        if i != '':
            pagenum.append(int(i))
    maxnum = max(pagenum)
    # print(maxnum)
    pagelist = [page1]
    if maxnum > 1 :
        for num in range(2,maxnum+1):
            pagelist.append(page1+ str(num) +".html")
    # print(pagelist)
    return pagelist

#下载该图集的全部图片
def DloadAtlas(url,name = "图集"):
    path = mkdir(name)
    pagelist = GetPageList(url)
    i = 1
    for page in range(len(pagelist)):
        print("正在下载第%d个页面,共计%d个页面" %(page+1,len(pagelist)) )
        picurllist = GetPicUrl(pagelist[page])
        for pic in picurllist:
            DloadPic(pic,path,str(i))
            i = i + 1
            print("第%d张图下载完成" %i)

if __name__ == "__main__":
    # GetPicUrl('https://www.meituri.com/a/13670/')
    DloadAtlas('https://www.meituri.com/a/13658/')
    # print (GetPageList('https://www.meituri.com/a/13658/'))