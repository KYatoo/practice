import os

#提取该目录下某文件的绝对路径
def AbsPath(fname):
    if os.path.exists(fname):
        path = os.getcwd()
        filename = filename.replace('/', '\\')
        path = path + '\\%s' % filename
        return True
    else:
        return False

#删除该文件下的一个文件（文件名）
def DeleteFile(filename):
    path = AbsPath(filename)
    if os.path.exists(path):
        os.rmmove(path)
        return  True
    return False

#重命名 os.rename(src, dst)
def RenameFile(src,dst):
    if not os.path.exists(src) & os.path.exists(dst):
        os.rename(src,dst)

#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表

# 获取文件夹下指定后缀的文件
# 默认脚本执行文件夹
def FilterFileByType(fextension,path):
    # print(path,fextension)
    dirlist = os.listdir(path)
    # print(dirlist)
    filelist = []
    for fileordir in dirlist:
        newpath = path +'\\%s' %fileordir
        if os.path.isfile(newpath):
            # print(os.path.splitext(newpath)[1])
            if os.path.splitext(newpath)[1] == fextension:
                filelist.append(fileordir)
    return filelist



if __name__ == "__main__":
    # path = os.getcwd()
    # filelist = os.listdir(path)
    # print(filelist)
    # print(type(filelist))
    # print(os.listdir())
    # print(FilterFileByType('.py','D:\\user\\Documents\\GitHub\\practice\\CHBRenamer'))
    # os.rename('D:\\user\\Documents\\GitHub\\practice\\CHBRenamer\\test','D:\\user\\Documents\\GitHub\\practice\\CHBRenamer\\test2')
    str = FilterFileByType('.jpg','D:\\user\\Downloads\\豆瓣音乐top250\\249 寻找周杰伦 - 周杰伦 2003')
    print(str)