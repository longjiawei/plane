import random
import sys

import pygame


class Bullet():
    pass
class Heroplane():
    def __init__(self):
        self.plane = pygame.image.load('D:\python\demo\飞机大战\图片\\1.2.png')
        self.planeRect = pygame.Rect(50,50,50,50)
        self.planex = 275
        self.planey = 740
    def planemove(self):
        if event.key == pygame.K_UP:
            self.planey -= 5
            self.planeRect[1] = self.planey
        if event.key == pygame.K_DOWN:
            self.planey += 5
            self.planeRect[1] = self.planey
        if event.key == pygame.K_LEFT:
            self.planex -= 5
            self.planeRect[0] = self.planex
        if event.key == pygame.K_RIGHT:
            self.planex += 5
            self.planeRect[0] = self.planex

class Long():
    def __init__(self):
        self.feifei = pygame.image.load('D:\python\demo\飞机大战\图片\\10.2.png')
        self.feifeiRect = pygame.Rect(65,50,65,50)
        self.feifeix = random.randint(100,500)
        self.feifeiy = -50


    def updateBee(self):
        self.feifeiy += 5
        self.feifeiRect[1] = self.feifeiy
        if self.feifeiy > 800 :
            self.feifeiy = 0
            self.feifeix = random.randint(100,500)

class Map():
    def __init__(self):

        self.background1 = pygame.image.load('D:\python\demo\飞机大战\图片\\2.1.png')
        self.background2 = pygame.image.load('D:\python\demo\飞机大战\图片\\2.1.png')
        self.bg1rect = pygame.Rect(0,0,600,900)
        self.bg2rect = pygame.Rect(0,-900,600,900)
        self.bg1y = 0
        self.bg2y = -900
    def mapmove(self):
        self.bg1y += 1
        self.bg2y += 1
        self.bg1rect[1] = self.bg1y
        self.bg2rect[1] = self.bg2y
        if self.bg1y >900:
            self.bg1y = -900
        elif self.bg2y > 900:
            self.bg2y = -900


def Display():

    screen.fill((255, 255, 255))
    screen.blit(Map.background1, (0, Map.bg1rect[1]))
    screen.blit(Map.background2, (0, Map.bg2rect[1]))
    screen.blit(Long.feifei, (Long.feifeix, Long.feifeiRect[1]))
    screen.blit(Heroplane.plane, (Heroplane.planex, Heroplane.planey))
    Map.mapmove()
    Long.updateBee()
    pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    size = width,height = 600,900
    screen = pygame.display.set_mode(size)
    pygame.key.set_repeat(10)
    Long = Long()
    Heroplane = Heroplane()
    Map = Map()
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                Heroplane.planemove()
        Display()



    pygame.quit()