#该文件为开发中的过程文件，执行请运行main.py
import geturl
import requests
import re
#输入查票信息获取url
# [url, date, stafrom_code, stato_code, purpose_codes] = geturl.geturl()
#测试用URL
url = 'https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date=2019-09-11&leftTicketDTO.from_station=YCK&leftTicketDTO.to_station=DZP&purpose_codes=ADULT'
print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
# post_data = {'leftTicketDTO.train_date': date,'leftTicketDTO.from_station': stafrom_code,'leftTicketDTO.to_station': stato_code,'purpose_codes':purpose_codes}

num2info = ['UKN','备注','UNK','车次','始发站','终点站','出发地','目的地','发车时间','到达时间','历时','是否有票','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','软卧','UKN','UKN','无座','UKN','硬卧','硬座','二等座','一等座','商务座','UKN','UKN','UKN','UKN']
print(len(num2info))
recode = requests.get(url,headers = headers)
code=requests.get(url).encoding
request = requests.get(url,headers = headers).text
# with open('requests.html','w',encoding=code) as f:
#     f.write(request)
request = request.replace('true',"None")
request = eval(request)
info_list = request['data']['result']
# print(type(info_list))
atkt_info = []
atkt_info = [[x for x in string.split('|')] for string in info_list];
for i in atkt_info:
    i[0] = 'NaN'
# print(len(atkt_info))
#以表格形式写入markdown，方便get对应关系
# with open('ticket.md','w',encoding='utf-8') as f:
#     for i in range(37):
#         f.write(num2info[i]+'  |')
#     f.write('\n')
#     for i in range(38):
#         f.write(' - |')
#     f.write('\n')
#     for i in atkt_info:
#         for j in i:
#             f.write(j)
#             f.write(' | ')
#         f.write('\n')
print((atkt_info[0]))
