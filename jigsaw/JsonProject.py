import json, os
from CutPic import *

##############################
#  json样式示例
# {
#     "3":[
#         {"mission":"tiger",
#          "picpath":".//Pid//tiger_3"},
#         {"mission":"flower",
#          "picpath":".//Pid//flower_3"}
#     ]
#     "4":[
#         {"mission":"tiger",
#          "picpath":".//Pid//tiger_4"},
#         {"mission":"flower",
#          "picpath":".//Pid//flower_4"}
#     ]
#     "5":[
#         {"mission": "tiger",
#          "picpath": ".//Pid//tiger_5"},
#         {"mission": "flower",
#          "picpath": ".//Pid//flower_5"}
#     ]
# }

def JsonFormatting(mission, level, targetpath=".//Pic"):
    picpath = targetpath + "//%s_%s" % (mission, level)
    missioninfo = {"mission": mission,
                   "picpath": picpath}
    return missioninfo


def initmissionjson():
    content = {"3": [], "4": [], "5": []}
    return content


def CrtMissionList(jsonpath="missionlist.json"):
    if not os.path.exists(jsonpath):
        content = initmissionjson()
        # print(type(content))
        with open(jsonpath, 'w') as missionlist:
            json.dump(content, missionlist)
            missionlist.close()


def WtMissionList(missioninfo,jsonpath=".//missionlist.json", level=3):
    with open(jsonpath, 'r') as e:
        mission = json.load(e)
        e.close()
    with open(jsonpath, 'w') as e:
        mission["%s" %level].append(missioninfo)
        # print(mission)
        # # print(text)
        json.dump(mission, e)

if __name__ == "__main__":
    [mission,level ] = CutPic("tiger.png")
    missioninfo = JsonFormatting(mission="tiger",level=3)
    WtMissionList(missioninfo)
