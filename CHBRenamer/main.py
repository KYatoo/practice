import function,os

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

# 将目录下指定拓展名的文件删除只保留一份并重命名
def RenameDelete(path,fname,fextension = '.jpg'):
    # print(path)
    filelist = FilterFileByType(fextension,path)
    # print(filelist)
    fpath = path + "\\%s" %fname
    # print(fpath)
    for filename in filelist:
        filepath = path + "\\%s" %filename
        if os.path.exists(fpath) and filepath != fpath:
            # print(os.path.exists(filepath))
            if os.path.exists(filepath):
                os.remove(filepath)
        else:
            # print(filepath,fpath)
            RenameFile(filepath,fpath)


# NormativeDir函数用于整理特定情况文件夹
# 通过Mp3Tag文件整理过后的音乐文件每张专辑图都是以音乐名命名的。因音乐已通过文件夹整理好，方便起见，每个文件夹下仅需保留一张即可，重命名为cover.jpg
def NormativeDir(path):
    RenameDelete(path,'cover.jpg')
    list = os.listdir(path)
    for fname in list:
        newpath = path + '\\%s' % fname
        if os.path.isdir(newpath):
            # print(newpath)
            NormativeDir(newpath)

# NormativeDir('D:\\user\\Downloads\\豆瓣音乐top250')
# NormativeDir('D:\\user\\Documents\\音乐MP3')
if __name__ == "__main__":
    while True:
        rootdir = input("请输入路径（按Q退出）：")
        if rootdir.upper() == 'Q':
            break
        NormativeDir(rootdir)
        print(rootdir + "操作完成")