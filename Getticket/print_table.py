#!/usr/bin/python
# -*- coding: utf-8 -*-

from prettytable import PrettyTable

num2info = ['UKN','备注','UNK','车次','始发站','终点站','出发地','目的地','发车时间','到达时间','历时','是否有票','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','软卧','UKN','UKN','无座','UKN','硬卧','硬座','二等座','一等座','商务座','UKN','UKN','UKN','UKN']
needtoshow = [3,6,7,8,9,10,11,23,26,28,29,30,31,32]
def print_table(table):
    tabletoshow = PrettyTable(num2info[i] for i in needtoshow)
    for i in table:
        tabletoshow.add_row([i[j] for j in needtoshow])
    print(tabletoshow)
    return 0

# if __name__ == "__main__":
#     print_table()