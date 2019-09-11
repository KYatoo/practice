import requests
import re

def get_chapter(chapter_titil,url):
    text_body = ''
    for i in range(3):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
            resp = requests.get(url, headers=headers).text
            code = requests.get(url).encoding
            resp =resp.replace('\n', '').replace('&nbsp;','')
            #写入html文件检查测试
            # with open('chapter_test.html','w',encoding='utf-8') as f:
            #     f.write(resp)
            text_body = re.findall(r'<div id="content".*?>([\s\S]*?)</div>',resp)[0]
            text_body = text_body.replace('\r<br />\r<br />','    \n').replace('<br /><br />','  \n')
            # print(text_body)
            print(chapter_titil + "下载成功")
            sucyon = True
            return [sucyon,text_body]
        except Exception as e:
            pass
    if i == 2:
        print(chapter_titil+"下载失败")
        sucyon = False
        return [sucyon,chapter_titil+"下载失败"]

if __name__ == "__main__":
    # url = 'https://www.biqugex.com/book_20765/9076607.html'
    url ='https://www.biqugex.com/book_102622/505354972.html'
    [x,text_body]=get_chapter('第80章',url)
    with open('chapter_test.txt','w',encoding='utf-8') as g:
        g.write(text_body)
    print(text_body)