# practice
## 夏季学期爬虫随堂联系  

### 1. 刮削器0.1  
**通过输入电影名和电影年份精确匹配电影，并输出豆瓣电影ID和链接**  
文件链接：[https://github.com/KYatoo/practice/blob/master/Guaxiao2.py](https://github.com/KYatoo/practice/blob/master/Guaxiao2.py)
1. **运行环境**  
windows + python + chromedriver  
2. **操作流程**  
通过输入电影名和电影年份精确匹配电影，并输出豆瓣电影ID和链接  
3. **问题**  
通过豆瓣搜索链接对电影进行搜索时，会先有一个 searching 的短暂停留再跳转成搜索页面，导致用requests库get不到所需信息，最后不得不用了chromedriver这超蠢的方式实现。不过萌新权当练手，不指望真能用得上。如有大佬有能实现get的方法，欢迎提issue，感谢。
