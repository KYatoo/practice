from function import *
from lxml import etree

def GetIndexPage(url):
    res = UrlInit(url)
    html = etree.HTML(res)
    pagelist = html.xpath('//div[@id="pages"]/a/@href')
    # print(pagelist)
    if pagelist != []:
        for page in range(len(pagelist)):
            pagelist[page] = "https://www.meituri.com" + pagelist[page]
        pagelist[0] = url
        pagelist.pop()
        # print(pagelist)
        return pagelist
    else:
        pagelist = [url]
        # print(pagelist)
        return pagelist

def GetAltasInfo(url):
    res = UrlInit(url)
    html = etree.HTML(res)
    altasurl= html.xpath('//div[@class="hezi"]/ul/li/a/@href')
    altasname = html.xpath('//div[@class="hezi"]/ul/li/p[@class="biaoti"]/a/text()')
    # print(altaslist)
    return [altasurl,altasname]

if __name__ == "__main__":
    GetIndexPage("https://www.meituri.com/x/81/")
    # GetAltasInfo("https://www.meituri.com/x/37/")