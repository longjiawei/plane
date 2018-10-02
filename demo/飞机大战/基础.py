import sys

import pygame

pygame.init()
size = width,height = 1000,800    #设置窗口大小
screen = pygame.display.set_mode(size)   #显示窗口
color = (255,255,255)   #ffffff


ball = pygame.image.load('D:\python\demo\飞机大战\图片\\11.png')
ballrect = ball.get_rect()  #获取图片矩形区域

speed = [2,2]
clock = pygame.time.Clock()   #设置时钟
while True:
    clock.tick(60)       #每60秒执行一次  tick（标记）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left <0 or ballrect.right >width:
        speed[0] = -speed[0]
    if ballrect.top <0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)
    screen.blit(ball,ballrect)   #将球画到屏幕上
    pygame.display.flip()   #更新全部显示
pygame.quit()



















