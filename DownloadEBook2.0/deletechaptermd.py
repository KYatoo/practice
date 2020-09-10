import os
#删除某一串文件
def deletechaptermd(filename): #输入为列表，元素为各个文件名
    pathnow = os.getcwd()
    for i in filename:
        if os.path.exists(pathnow+ '\\' +i+ '.md'):
            os.remove(i + '.md')
