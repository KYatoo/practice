# 查询12306余票信息

***不算readme的readme文件，写几个爬取过程中的核心问题***

1. **爬取的URL**  

当我们在首页中填写好我们查询需要的信息后，如下图：  

![nNUofe.png](https://s2.ax1x.com/2019/09/10/nNUofe.png)    

点击查询会跳转到形如[kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=北京,BJP&ts=济南,JNK&date=2019-09-10&flag=N,N,Y](https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E6%B5%8E%E5%8D%97,JNK&date=2019-09-10&flag=N,N,Y) 的地址，但这并不是我们需要爬取的URL。  

分析：例如当我们在上面这个网址重新填写（出发地、目的地、日期）后，我们依旧可以查询到信息，而观察地址栏，先前的url是没有变化的。  

![nNw8JO.png](https://s2.ax1x.com/2019/09/10/nNw8JO.png)  

观察上图，我们出发地目的地已重新提交为杭州福州，而上面地址栏的地址还是先前搜索北京济南的地址。f12 观察网页页面内容，多了一个xhr对象。分析该对象，我们可以得到我们要get的URL： 
https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date=2019-09- 10&leftTicketDTO.from_station=HZH&leftTicketDTO.to_station=FZS&purpose_codes=ADULT   
URL中 data后面是日期；from_station、to_station对应相应的是出发地、目的地，只不过使用的是站台代码；最后purpose_codes是票的类型，成人票（ADULT）还是学生票(OXOO）

2. **关于各个站台对应的CODE**

同样在观察之前网页的内容，有一个名为'station_name.js'的内容中包含了全部站点的CODE。  
get如下url：https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9109 获取站台code，做成字典方面后续检索。

3. **关于get余票信息的内容分析**

我们get下来的内容近似一个列表，列表的每一个元素为一趟车的信息。每一趟车的信息近似一个字典嵌套字典的结构。  
处理时，可以先用eval做成字典（有一个key的value为ture，非str，记得提前处理）。某个key为'result'的内容里面就是我们要的结果。  
分析后，这部分内容形似表格。共38项信息，每两个信息用' | '分割。从前往后，各信息下标和各项信息的类型对应关系如下（UKN表示unknown，多数为在查询余票中为无效信息）  

| 下标 | 信息 |
| - | - |
| 0 | UKN |
| 1 | 备注 |
| 2 | UKN |
| 3 | 车次 |
| 4 | 始发站 |
| 5 | 终点站 |
| 6 | 出发地 |
| 7 | 目的地 |
| 8 | 发车时间 |
| 9 | 到达时间 |
| 10 | 历时 |
| 11 | 可否购票 |
| 12-22 | UKN |
| 23 | 软卧 |
| 24 | UKN |
| 25 | UKN |
| 26 | 无座 |
| 27 | UKN |
| 28 | 硬卧 |
| 29 | 硬座 |
| 30 | 二等座 |
| 31 | 一等座 |
| 32 | 商务座 |
| 33-36 | UKN |

4. **表格输出**   
使用模块 PrettyTable
