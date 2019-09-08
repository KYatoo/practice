import  numpy,random

#随机位置出现一个2
def creat2():
    seat = [random.randint(0,3) for _ in range(2)]
    return seat

#判断矩阵内某位置是否为空（0）
def freeyon(maxarea,seat):
    if maxarea[seat[0]][seat[1]] == 0:
        return True
    return  False

#输出矩阵
def printarea(maxarea):
    size = 4
    for i in range(size):
        for j in range(size):
            print('%d'% maxarea[i][j],end='   ')
        print('\n')
#从前往后去重
def quchong1(list_list):
    k = 0
    while True:
        if list_list[k] == list_list[k + 1]:
            list_list[k] = list_list[k] * 2
            list_list[k + 1] =0
            k = k + 2
        else:
            k = k + 1
        if k >= len(list_list)-1:
            break
    return list_list
#从后往前去重
def quchong2(list_list):
    k = len(list_list)-1
    while True:
        if list_list[k] == list_list[k-1]:
            list_list[k] = list_list[k] * 2
            list_list[k-1] =0
            k = k -2
        else:
            k = k -1
        if k <=1:
            break
    return list_list
#移位，去0
def remove0(list_list):
    real_list = []
    for i in list_list:
        if i != 0:
            real_list.append(i)
    return real_list
#取列元素
def encolu(matrix,num:int):
    colu = []
    for i in range(len(matrix)):
        colu.append(matrix[i][num])
    return colu
#移动并合并
def moveele(maxarea,action:str):
    if action == 'w':
        for j in range(size):
            colu = encolu(maxarea,j)
            colu = remove0(colu)
            colu += [0 for k in range(size - len(colu))]
            colu = quchong1(colu)
            #末尾补齐0
            colu += [ 0 for k in range(size-len(colu))]
            for i in range(size):
                maxarea[i][j] = colu[i]
    elif action == 's':
        for j in range(size):
            colu = encolu(maxarea,j)
            colu = remove0(colu)
            colu = [0 for k in range(size - len(colu))] +colu
            colu = quchong2(colu)
            #末尾补齐0
            colu = [0 for k in range(size - len(colu))] +colu
            for i in range(size):
                maxarea[i][j] = colu[i]
    elif action == 'a':
        for i in range(size):
            colu = maxarea[i]
            colu = remove0(colu)
            colu += [0 for k in range(size - len(colu))]
            colu = quchong1(colu)
            # 末尾补齐0
            colu += [0 for k in range(size - len(colu))]
            for j in range(size):
                maxarea[i][j] = colu[j]
    elif action == 'd':
        for i in range(size):
            colu = maxarea[i]
            colu = remove0(colu)
            colu = [0 for k in range(size - len(colu))] +colu
            colu = quchong2(colu)
            # 末尾补齐0
            colu = [0 for k in range(size - len(colu))] +colu
            for j in range(size):
                maxarea[i][j] = colu[j]
    return (maxarea)
#列表最大元素
def maxElem(list):
    if len(list)==1:
        return list[0]
    return list[0] if list[0]>maxElem(list[1:]) else maxElem(list[1:])
#矩阵最大元素
def maxelem2(Matrix):
    maxnum =[]
    for list in Matrix:
        maxnum.append(list[0] if list[0]>maxElem(list[1:]) else maxElem(list[1:]))
    return maxElem(maxnum)

size = 4
maxarea = numpy.zeros([size, size])
while True:
    overgame = False
    while True:
        seat = creat2()
        if freeyon(maxarea,seat):
            maxarea[seat[0]][seat[1]] = 2
            break
    printarea(maxarea)
    while True:
        action = input("请输入你的操作（wsad）(按q退出游戏）：")
        if action =='q':
            overgame = True
            break
        elif action in 'wsad':
            maxarea = moveele(maxarea, action)
            break
        else:
            print("输入无效，请重新输入")
    if overgame == True :
        break
    # print('%d'% maxelem2(maxarea))
    if maxelem2(maxarea)>=2048:
        print("游戏结束，恭喜通关")
        break