import tkinter,os

def StartPage():
    l1 = tkinter.Label(screen, text='拼图游戏', bg='white', font=('楷体', 40), width=200, height=4)
    l2 = tkinter.Label(screen, text='按ENTER键开始', bg='white', font=('行书', 15), width=200, height=1)
    l3 = tkinter.Label(screen, text=None, bg='white', font=('行书', 15), width=200, height=50)
    l1.pack()
    l2.pack()
    # l3.pack()

def ChooseLevel():
    screen.destroy()
    l3 = tkinter.Label(screen, text='请选择难度', bg='white', font=('楷体', 20), width=200, height=4)
    l3.pack()
def GetAnyKey():
    input()
    return True



screen = tkinter.Tk()

screen.title("拼图游戏")

screen.geometry('600x600')  # 这里的乘是小x

StartPage()
if GetAnyKey():
    ChooseLevel()


# # 进入消息循环
screen.mainloop()

