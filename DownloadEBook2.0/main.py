import chapter_link
import chap2book
import get_chapter
from deletechaptermd import deletechaptermd

book_name = input("请输入电子书的名称：")
book_num = input("请输入书本数字代号(请参看书本地址栏）：")
link_title = chapter_link.chapter_link(book_num)
titleslinks = [i[0] for i in link_title]
titles = [i[1] for i in link_title]
print("本书共有%d个章节" %len(link_title))
chapter_dfail = []
for i in range(len(link_title)):
    chapter_url = 'https://www.biqugex.com' + titleslinks[i]
    # print(chapter_url)
    [suc,chapter_text] = get_chapter.get_chapter(titles[i],chapter_url)
    with open(titles[i] + '.md', 'w', encoding='utf-8') as book:
        book.write("### " + titles[i] + '  \n' + chapter_text + '  \n')
    if suc == False:
        chapter_dfail.append(link_title)
chap2book.chap2book(titles,book_name)
deletechaptermd(titles)
#输出下载失败的章节
if chapter_dfail != []:
    print("如下章节下载失败：")
    for i in range(len(chapter_dfail)):
        print(titles[i],titleslinks[i])