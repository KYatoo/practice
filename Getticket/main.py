import geturl
import requests
import re
import print_md
import print_table

[url, date, stafrom_code, stato_code, purpose_codes] = geturl.geturl()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
recode = requests.get(url,headers = headers)
code=requests.get(url).encoding
request = requests.get(url,headers = headers).text
request = request.replace('true',"None")
request = eval(request)
info_list = request['data']['result']
atkt_info = []
atkt_info = [[x for x in string.split('|')] for string in info_list]
#删除表格 第一列无用信息
for i in atkt_info:
    i[0] = 'NaN'
#输出至markdown
print_md.print_md('ticket',atkt_info)
print_table.print_table(atkt_info)
