import os

def SplitFomat(path):
    if os.path.exists(path):
        return [os.path.splitext(os.path.basename(path))[0],path.split(".")[-1]]
    return False

def MkNewDir(name,path):
    if os.path.exists(path):
        path = path+"//"+name
        if not os.path.exists(path):
            os.mkdir(path)
            return path
    return False

if __name__ =="__main__":
    print (SplitFomat(".//SourcePic//tiger.png"))

