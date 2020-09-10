from selenium import webdriver

url = 'http://www.baidu.com'
driver = webdriver.Chrome()
reqs = driver.get(url)
print(reqs)
# close()