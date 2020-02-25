#调用需要的库
import requests #http请求
import re #正则表达式

#构建请求头
#链接
url = "https://www.ivsky.com/tupian/richu_riluo_v57799/pic_905990.html"
#header
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"}

req = requests.get(url= url,headers = headers).content.decode(encoding="utf-8") #将二进制文件以utf8格式进行编码以得到字符串数据
# print(req)
print(type(req))

#保存成文件，方便检察元素
#open(文件名,操作,编码)
# w:写入
# utf-8 一种中文常见编码
with open("page.html",'w',encoding='utf-8') as html:
    html.write(req)

# #正则表达式的提取规则
# rule = r"<img.*?imgis.*?src='(.*?)'.*?>"
# #按照上述规则在get到的html内容中搜索以提取图片链接
# linklist = re.findall(rule ,req)
# link = "http:" + linklist[0] #构建完整链接
#
# #保存图片
# pic = requests.get(url=link,headers = headers).content
# with open("page.jpg",'wb') as jpg: # b：以二进制文件写入
#     jpg.write(pic)
#
# #1. 正则表达式需要认真学习，非常有用，在各个语言各个领域都能用
# #2. 弄明白编解码是什么意思，了解一下常见的中文编码格式
# #3. open函数要知道，看看保存不同类型的文件的时候有什么不同
# #4. 多用   print(type(变量名))   来打印变量类型看看不同函数得到的数据都是什么格式的
# #5. 把今天这个代码精简，用不到的删掉，封装成函数，留好url这一接口，后面还要用