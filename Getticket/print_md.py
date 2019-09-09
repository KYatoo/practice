num2info = ['UKN','备注','UNK','车次','始发站','终点站','出发地','目的地','发车时间','到达时间','历时','是否有票','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','UKN','软卧','UKN','UKN','无座','UKN','硬卧','硬座','二等座','一等座','商务座','UKN','UKN','UKN','UKN']
def print_md(filename,table):
    with open(filename+'.md','w',encoding='utf-8') as f:
        for i in range(37):
            f.write(num2info[i]+'  |')
        f.write('\n')
        for i in range(38):
            f.write(' - |')
        f.write('\n')
        for i in table:
            for j in i:
                f.write(j)
                f.write(' | ')
            f.write('\n')