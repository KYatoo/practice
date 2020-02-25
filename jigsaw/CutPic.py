from PIL import Image
import os
from function import *
from function_private import *

def CutPic(picname,level = 3,sourcepath = ".//SourcePic",targetpath = ".//Pic"):
    # print(os.listdir(sourcepath))
    # print(os.listdir(targetpath))
    filelist = os.listdir(sourcepath)
    # print(filelist)
    if picname in filelist:
        picpath = sourcepath + "//" + picname
        [mission,filefomat] = SplitFomat(picpath)
        #新建文件夹
        targetpath = MkNewDir(NamePicPath(mission,level),targetpath)
        # print(targetpath)
        im = Image.open(picpath)
        imgsize = im.size
        ( asize,bsize ) = imgsize
        maxsize = max(imgsize) #图像长边分辨率
        minsize = min(imgsize) #图像短边分辨率
        targetsize = (minsize - minsize% level) //level # 剪裁后的图片的边长分辨率
        startpointa = (asize - (targetsize*level))//2
        startpointb = (bsize - (targetsize*level))//2
        # print(targetsize)
        # print(startpointa)
        # print(startpointb)
        for num in range(1,level*level):
            coordinatea = num//level+1 if num%level !=0 else num//level
            coordinateb = num%level if num%level != 0 else level
            # print(num)
            # print((coordinatea,coordinateb))
            (a,b) = (startpointa+(coordinateb-1)*targetsize,startpointb+(coordinatea-1)*targetsize)
            # print((a,b))
            tempimg = im.crop((a,b,a+targetsize-1,b+targetsize-1))
            # print("%s//%s.%s" %(targetpath,num,filefomat))
            tempimg.save("%s//%s.%s" %(targetpath,num,filefomat))
        return [mission,level]




if __name__ == "__main__":
    CutPic("tiger.png")