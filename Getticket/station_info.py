import requests,re
def getcode():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9006'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    stations = requests.get(url,headers = headers).text
    # print(stations)
    station_list = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',stations)
    # station2cod = {}
    # cod2station = {}
    # for i in station_list:
    #     station2cod[i[0]] = i[1]
    #     cod2station[i[1]] = i[0]
    # print(type(stations))

    station2cod = dict(station_list)
    cod2station = {code:sta for (sta,code) in station_list}
    # print(station2cod['北京'])
    # print(cod2station['BJP'])
    return [station2cod,cod2station]