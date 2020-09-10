import json
import requests

url = 'http://fy.iciba.com/ajax.php?a=fy'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
#构造请求函数
post_data = {"f":"auto","t":"auto","w":"hello，world"}
resp = requests.post(url=url,data=post_data,headers=headers)
sd=json.loads(resp.text)
print(type(sd))
print(sd['content']['out'])