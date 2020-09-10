import json
import requests
flag = True
while flag:
    inp = input("请输入想要翻译的英文单词(q退出)：")
    if(inp == 'q'):
        break
    else:
        url = 'http://fy.iciba.com/ajax.php?a=fy'
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        # 构造请求的参数
        post_data = {"f": "auto","t": "auto","w": inp}
        resp = requests.post(url,data=post_data,headers=headers)
        sd = json.loads(resp.text)
        print(sd['content']['word_mean'][0])
