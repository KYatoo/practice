import pygame
import sys
from pygame.locals import *

BACKGROUNDCOLOR = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 40
NUMRANDOM = 100

'''显示游戏开始界面'''
def ShowStartInterface(screen ,width, height):
    screen.fill(BACKGROUNDCOLOR)
    tfont = pygame.font.Font('./font/simkai.ttf', width//4)
    cfont = pygame.font.Font('./font/simkai.ttf', width//20)
    title = tfont.render('拼图游戏', True, RED)
    content1 = cfont.render('按H或M或L键开始游戏', True, BLUE)
    content2 = cfont.render('H为5*5模式，M为4*4模式，L为3*3模式', True, BLUE)
    trect = title.get_rect()
    trect.midtop = (width/2, height/10)
    crect1 = content1.get_rect()
    crect1.midtop = (width/2, height/2.2)
    crect2 = content2.get_rect()
    crect2.midtop = (width/2, height/1.8)
    screen.blit(title, trect)
    screen.blit(content1, crect1)
    screen.blit(content2, crect2)
    pygame.display.update()
    while True:
        size = None
        for event in pygame.event.get():
            if event.type == QUIT:
                Stop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Stop()
                if event.key == ord('l'):
                    size = 3
                elif event.key == ord('m'):
                    size = 4
                elif event.key == ord('h'):
                    size = 5
        if size:
            break
    return size

pygame.init()
size = width,height = 700,700
screen = pygame.display.set_mode(size)



while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
        ShowStartInterface(screen,width,height)