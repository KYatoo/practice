import os,shutil

jsonpath = ".//missionlist.json"
picpath  = ".//Pic"
def ClearCache():
    if os.path.exists(jsonpath):
        os.remove(jsonpath)
    if not os.path.exists(picpath):
        os.mkdir(picpath)
    else:
        shutil.rmtree(picpath)
        os.mkdir(picpath)

if __name__ ==  "__main__":
    ClearCache()