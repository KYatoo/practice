import json
import requests
import webbrowser
import random

while True:
    poster = random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()',5)
    poster = "".join(posterx)
    content = random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()',10)
    content = "".join(content)
    print(content)
    url = 'https://paste.ubuntu.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    post_data = {"poster": poster,"syntax": "text","expiration": "day","content": content}
    resp = requests.post(url,data=post_data,headers=headers)
    print(type(resp))
    print(resp.url)
    # webbrowser.open(resp.url)