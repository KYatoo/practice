import station_info
import re

#验证输入信息生成查询url
def geturl():
    [station2cod,cod2station] = station_info.getcode()
    while True:
        stafrom = input("请输入出发地：")
        # if station2cod.has_key(stafrom):
        if stafrom in station2cod:
            stafrom_code = station2cod[stafrom]
            # print(stafrom_code)
            break
        else:
            print("未查到此站，请重新输入")
    while True:
        stato   = input("请输入目的地：")
        # if station2cod.has_key(stafrom):
        if stato in station2cod:
            stato_code = station2cod[stato]
            # print(stafrom_code)
            break
        else:
            print("未查到此站，请重新输入")
    while True:
        date = input("请输入出发日期（格式：2019-10-01)")
        if(re.match(r'^20[1-9]\d-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$',date)):
            break;
        else:
            print("格式不正确，请请重新输入")
    while True:
        stuyon  = input("是否查询学生票（Y/N)")
        if stuyon == 'Y' or stuyon == 'N':
            break
        else:
            print("输入无效，请输入'Y'表示YES，'N'表示NO")
    while True:
        hswayyon= input("是否只查询高铁动车票（Y/N）")
        if hswayyon == 'Y' or hswayyon == 'N':
            break
        else:
            print("输入无效，请输入'Y'表示YES，'N'表示NO")
    url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs='+ stafrom + ','+ stafrom_code + '&ts=' + stato +',' +stato_code +'&date='+date+'&flag='+stuyon+','+hswayyon+',Y'
    # print(url)
    return url
