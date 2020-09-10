import  requests
import re
import get_chapter

book_name = input("请输入电子书的名称：")
book_num = input("请输入书本数字代号(请参看书本地址栏）：")
url = 'https://www.biqugex.com/book_'+book_num +'/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
resp = requests.get(url,headers = headers).text
code=requests.get(url).encoding
resp = resp.encode(code)
resp = resp.decode('gbk')
# with open('title.html','w',encoding='gbk') as f:
#     f.write(resp)
link_title = re.findall(r'<dd><a href ="(.*?)">(.*?)</a></dd>',resp)
print(len(link_title))
# for i in range(len(link_title)-1)
link_title = [ link_title[i] for i in range(12,len(link_title))]
# print(*link_title)
#写入标题
with open(book_name+'.md','w',encoding='utf-8') as book:
    book.write("# "+book_name+'  \n')
    for i in range(len(link_title)):
        chapter_url = 'https://www.biqugex.com'+link_title[i][0]
        # print(chapter_url)
        # chapter_text = get_chapter.get_chapter(link_title[i][1],chapter_url)
        # with open(link_title[i][1]+'.md','w',encoding='utf-8') as book:
        #     book.write("### "+link_title[i][1]+ '  \n'+chapter_text+'  \n')
        f=open(link_title[i][1]+'.md',encoding='utf-8')
        fs=f.read()

        book.write("### "+link_title[i][1]+ '  \n'+fs+'  \n')


