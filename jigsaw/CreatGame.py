from JsonProject import *
from CutPic import *
import json,os

def CheckMissionList(missionlistPath = ".//missionlist.json"):
    if not os.path.exists(missionlistPath):
        CrtMissionList()
    with open(missionlistPath,"r") as e:
        prmissionlist = json.load(e)
        e.close()
    for level in [3,4,5]:
        print(prmissionlist)
        for mission in prmissionlist["%s" %level]:
            print(mission)
            for missionpath in mission["picpath"]:
                if not os.path.exists(missionpath):
                    newmissionlist = prmissionlist["%s" %level].remove(mission)
                    with open(missionlistPath, "w") as e:
                        json.dump(newmissionlist,e)
                        e.close()
    return True

def CutPicWtJson(picname,sourcepath = ".//SourcePic",targetpath = ".//Pic",level = 3,jsonpath="missionlist.json"):
    [mission, level] = CutPic(picname,sourcepath=sourcepath,level=level,targetpath = targetpath)
    print(mission,level)
    missioninfo = JsonFormatting(mission, level, targetpath=targetpath)
    if missioninfo:
        WtMissionList(missioninfo, jsonpath=jsonpath, level=level)
        return True
    return False

def CheckNewMission(sourcepath = ".//SourcePic",missionlistpath = ".//missionlist.json"):
    sourcepiclist = os.listdir(sourcepath)
    if not os.path.exists(missionlistpath):
        CrtMissionList()
    with open(missionlistpath,"r") as e:
        prmissionlist = json.load(e)
        e.close()
    for sourcepic in sourcepiclist:
        print(sourcepic)
        picname = sourcepic.split(".")[0]
        for level in [3,4,5]:
            if prmissionlist["%s" %level] == []:
                print(level)
                print(prmissionlist["%s" %level])
                print(picname)
                CutPicWtJson(sourcepic, sourcepath = sourcepath, level=level, jsonpath=missionlistpath)
            else:
                for mission in prmissionlist["%s" %level]:
                    print(mission["mission"])
                    if not mission["mission"] == picname:
                        # CutPic(picname,level=level)
                        CutPicWtJson(sourcepic,sourcepath,level=level,jsonpath=missionlistpath)

if __name__ == "__main__":
    # CheckMissionList()
    CheckNewMission()