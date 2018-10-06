import sys

import pygame


class Bird():
    def __init__(self):
        pass
    def birdUpdate(self):
        pass
class Pipeline():
    def __init__(self):
        pass
    def updatePipeline(self):
        pass
def createMap():
    screen.fill((255,255,255,))  #填充颜色为白色
    screen.blit(background,(0,0))  #填入背景
    pygame.display.update()
if __name__ == '__maim__':
    pygame.init()
    size = width,heigth = 400,650
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()
    Bird = Bird()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sys.exit()
        background = pygame.image.load('D:\python\demo\飞机大战\图片\\12.png')
        createMap()
    pygame.quit()