# practice
## python练习  

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

### 5. 游戏2048
**字符串界面操作的游戏2048**  
文件链接：[https://github.com/KYatoo/practice/blob/master/Game2048/game2048.py](https://github.com/KYatoo/practice/blob/master/Game2048/game2048.py)  
1. **运行环境**  
windows + python
2. **操作流程**  
运行后游戏开始，通过wsad来控制上下左右，当输入其他字符会提示“输入无效，请重新输入”，输入q结束游戏。当游戏算到2048后，提示“恭喜通关”游戏结束。  

### 6. 炸网站！
**重复向[paste.ubuntu.com](paste.ubuntu.com)网站发送随机字符串并返回链接**  
文件链接：[https://github.com/KYatoo/practice/blob/master/boomweb/boom.py](https://github.com/KYatoo/practice/blob/master/boomweb/boom.py)  
1. **运行环境**  
windows + python
2. **操作流程**  
运行程序，自动生成两个随机字符串，并分别以sender和massage发送至paste.ubuntu.com，并返回查看链接。循环往复。

### 7. 查询12306余票信息
**输入相关信息（出发地、目的地、出发时间、成人票/学生票）获取当前余票信息[详情请点击](https://github.com/KYatoo/practice/blob/master/Getticket/README.md)**  
1. **运行环境**  
windows + python + module（PrettyTable）
2. **操作流程**  
输入输入相关信息（出发地、目的地、出发时间、成人票/学生票）获取当前余票信息，余票信息会以表格的形式展示，方便直观。同时在main.py所在目录生成'ticket.md'文件，内容同样为表格，内容更加详细。
3. **效果图**
[![nN3K4s.png](https://s2.ax1x.com/2019/09/10/nN3K4s.png)](https://imgchr.com/i/nN3K4s)
[![nN3uNj.png](https://s2.ax1x.com/2019/09/10/nN3uNj.png)](https://imgchr.com/i/nN3uNj)
