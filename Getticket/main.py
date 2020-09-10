import geturl
import requests
import print_md
import print_table
import  station_info

[url, date, stafrom_code, stato_code, purpose_codes] = geturl.geturl()
# print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
recode = requests.get(url,headers = headers)
code=requests.get(url).encoding
request = requests.get(url,headers = headers).text
#转换成字典 {{[]}}
# print(request)
request = request.replace('true',"None").replace('false',"None")
request = eval(request)
# print(request)
#两个字典中取出key分别为['data']['result']获得信息 38行表格，|分割
info_list = request['data']['result']

#以'| '分割，成n*38的二维矩阵
atkt_info = []
atkt_info = [[x for x in string.split('|')] for string in info_list]

#车站代码->车站名
[station2cod,cod2station] = station_info.getcode()
for i in atkt_info:
    i[0] = 'NaN' #删除表格的第一列无用信息，太长了
    for j in [4,5,6,7]:
        i[j] = cod2station[i[j]]
#输出至markdown
print_md.print_md('ticket',atkt_info)
#输出表格
print_table.print_table(atkt_info)
