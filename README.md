# practice
## 夏季学期爬虫随堂联系  

### 1. 刮削器0.1  
**通过输入电影名和电影年份精确匹配电影，并输出豆瓣电影ID和链接**  
文件链接：[https://github.com/KYatoo/practice/blob/master/guaxiao/Guaxiao2.py](https://github.com/KYatoo/practice/blob/master/guaxiao/Guaxiao2.py)
1. **运行环境**  
windows + python + chromedriver  
2. **操作流程**  
通过输入电影名和电影年份精确匹配电影，并输出豆瓣电影ID和链接  
3. **问题**  
通过豆瓣搜索链接对电影进行搜索时，会先有一个 searching 的短暂停留再跳转成搜索页面，导致用requests库get不到所需信息，最后不得不用了chromedriver这超蠢的方式实现。不过萌新权当练手，不指望真能用得上。如有大佬有能实现get的方法，欢迎提issue，感谢。  

### 2. 单词翻译
**输入单词，调取金山词霸获取单词翻译**  
文件链接：[https://github.com/KYatoo/practice/blob/master/word_trans/jsfy.py](https://github.com/KYatoo/practice/blob/master/word_trans/jsfy.py)
1. **运行环境**  
windows + python
2. **操作流程**  
运行程序后输入单词，即可获取单词翻译  

### 3. 豆瓣电影热门TOP200
**获取豆瓣电影热门TOP200及豆瓣评分**  
文件链接：[https://github.com/KYatoo/practice/blob/master/guaxiao/guaxiaoqi.py](https://github.com/KYatoo/practice/blob/master/guaxiao/guaxiaoqi.py)  
1. **运行环境**  
windows + python
2. **操作流程**  
运行程序后，系统爬取豆瓣电影热门Top200，输入电影，即可获取豆瓣评分 

### 4. 爬取招聘信息
**爬取[招聘网站](http://www.yingjiesheng.com/)的首页全部企业招聘信息**\
文件链接：[https://github.com/KYatoo/practice/blob/master/jobs_info/job_info.py](https://github.com/KYatoo/practice/blob/master/jobs_info/job_info.py)\
1. **运行环境**  
windows + python
2. **操作流程**  
运行job_info.py，源文件夹会生成一个jobs_link.md的文档，内含该招聘网站公司点击跳转招聘宣传链接  
