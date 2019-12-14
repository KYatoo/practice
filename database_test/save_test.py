import  requests
import re
import pymysql

def get_connection():
    # 连接数据库
    connect = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='wang99119.',
        db='test',
        port=3306,
        charset='utf8'
    )
    # 获取游标(指定获取的数据格式，这里设定返回dict格式)
    return connect , connect.cursor(cursor=pymysql.cursors.DictCursor)

# book_name = input("请输入电子书的名称：")
# book_num = input("请输入书本数字代号(请参看书本地址栏）：")
# url = 'https://www.biqugex.com/book_'+book_num +'/'
book_num = 79086
book_name = "AWM[绝地求生]"
url = 'https://www.biqugex.com/book_79086/'
print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
resp = requests.get(url,headers = headers).text
code=requests.get(url).encoding
print(code)
resp = resp.encode(code)
resp = resp.decode('gbk')
# with open('title.html','w',encoding='gbk') as f:
#     f.write(resp)
link_title = re.findall(r'<dd><a href ="(.*?)">(.*?)</a></dd>',resp)
link_title = [ link_title[i] for i in range(12,len(link_title))]
print(link_title)

[con,cursor] = get_connection()
cursor.execute("create database IF NOT EXISTS book character set utf8mb4;" )
cursor.execute("use book;")
cursor.execute("create table if not exists `%s` (id int,bookname char(20),bookurl char(100))character set UTF8MB4;"  % book_name )

for linkntitle in link_title:
    book_link ='https://www.biqugex.com'+linkntitle[0]
    sql ="insert into `%s` values ( %d,'%s','%s') " %(book_name,book_num,linkntitle[1],book_link)
    print(sql)
    try:
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        con.rollback()
        print('数据库插入操作错误回滚')