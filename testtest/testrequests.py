# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:36:21 2020

@author: HR
"""

import string#string模块，包括ascii的字符序列
import random#random模块，随机
import requests

def random_string(size=5,chars=string.ascii_letters+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
#string.ascii_uppercase=英文字母
#string.digits=阿拉伯数字
#''.join(['a','b'])将随机字符拼凑成字符串

payload={'poster':random_string(),'context':random_string(10,)}
resp = requests.post("https://paste.ubuntu.com",data=payload)
print(resp.url)
