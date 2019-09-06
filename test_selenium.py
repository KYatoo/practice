from selenium import webdriver

url = 'http://www.baidu.com'
dirver = webdriver.Chrome()
reqs = diver.get(url)
print(reqs)