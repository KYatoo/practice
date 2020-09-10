import requests
import re

def unescape(s):
    return s.encode('latin-1').decode('unicode-escape');

def get_chapter(chapter_titil,url):
    text_body = ''
    for i in range(3):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
            resp = requests.get(url, headers=headers).text
            code = requests.get(url).encoding
            print(code)
            resp =resp.replace('\n', '').replace('&nbsp;','')
            #写入html文件
            with open('chapter_test.html','w',encoding='ISO-8859-1') as f:
                f.write(resp)
            text_body = re.findall(r'<div id="content".*?>([\s\S]*?)</div>',resp)[0]
            text_body = text_body.replace('\r<br />\r<br />','    \n').replace('<br /><br />','  \n')
            # print(text_body)
            return text_body
        except Exception as e:
            pass
    if text_body == '':
        print(chapter_titil+"下载失败")
        return chapter_titil+"下载失败"

if __name__ == "__main__":
    # url = 'https://www.biqugex.com/book_20765/9076607.html'
    url ='https://www.biqugex.com/book_79086/28364804.html'
    text_body=get_chapter('第80章',url)
    with open('chapter_test.txt','w',encoding='gbk') as g:
        g.write(text_body)
    print(text_body)