import requests
import re
def chapter_link(book_num):
    url = 'https://www.biqugex.com/book_' + book_num + '/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    resp = requests.get(url, headers=headers).text
    #修改编码以正常显示输出中文字符
    code = requests.get(url).encoding
    # with open('title.html','w',encoding=code) as f:
    #     f.write(resp)
    resp = resp.encode(code)
    resp = resp.decode('gbk') #编码不同可能需要修改
    #提取章节的title和link
    link_title = re.findall(r'<dd><a href ="(.*?)">(.*?)</a></dd>', resp)
    #删除前十二个title（最近更新，与后面重复）
    link_title = [link_title[i] for i in range(12, len(link_title))]
    return  link_title