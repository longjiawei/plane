import random
import sys

import pygame


class Enemyplane():
    def __init__(self):
        self.enemyplane = pygame.image.load('D:\python\demo\飞机大战\图片\\14.1.png')
        self.enemyplane1 = pygame.image.load('D:\python\demo\飞机大战\图片\\14.1.png')
        self.enemyplaneRect = pygame.Rect(60,60,60,60)
        self.enemyplaneRect1 = pygame.Rect(60, 60, 60, 60)
        self.enemyplanex = 200
        self.enemyplanex1 = 400
        self.enemplaney = 200
        self.enemyplaney1 = 200
        self.enemyplaneRect[1] = self.enemplaney
        self.enemyplaneRect1[1] = self.enemyplaney1
    def enemymove(self):
        pass
class Bullet():
    def __init__(self):
        self.bullets = []
        self.bullet = pygame.image.load('D:\python\demo\飞机大战\图片\\15.1.png')
        self.bulletrect = pygame.Rect(30,30,30,30)
        self.bulletx = Heroplane.planex + 10
        self.bullety = Heroplane.planey - 20
        self.bulletspeed = 2
    def bulletmove(self):
        self.bullety -= self.bulletspeed
        if self.bullety < 0:
            self.bullety = Heroplane.planey - 20
            self.bulletx = Heroplane.planex + 10
        self.bulletrect[1] = self.bullety
        self.bulletrect[0] = self.bulletx
        for self.bullet in self.bullets:

            Bullet.bulletmove()
            self.bullets.append(self.bullet)
class Heroplane():
    def __init__(self):
        self.plane = pygame.image.load('D:\python\demo\飞机大战\图片\\1.3.png')
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
        self.feifei = pygame.image.load('D:\python\demo\飞机大战\图片\\10.3.png')
        self.feifeiRect = pygame.Rect(65,50,65,50)
        self.feifeix = random.randint(100,500)
        self.feifeiy = -50
        self.feifei1 = pygame.image.load('D:\python\demo\飞机大战\图片\\10.3.png')
        self.feifei1Rect = pygame.Rect(65, 50, 65, 50)
        self.feifei1x = random.randint(100, 500)
        self.feifei1y = -50
    def updateBee(self):
        self.feifeiy += 4
        self.feifeiRect[1] = self.feifeiy
        if self.feifeiy > 900 :
            self.feifeiy = 0
            self.feifeix = random.randint(100,500)
        self.feifei1y += 3
        self.feifei1Rect[1] = self.feifei1y
        if self.feifei1y > 900:
            self.feifei1y = 0
            self.feifei1x = random.randint(100, 500)
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
    screen.blit(Enemyplane.enemyplane,(Enemyplane.enemyplanex,Enemyplane.enemplaney))
    screen.blit(Enemyplane.enemyplane1,(Enemyplane.enemyplanex1,Enemyplane.enemyplaney1))
    screen.blit(Long.feifei, (Long.feifeix, Long.feifeiRect[1]))
    screen.blit(Long.feifei1, (Long.feifei1x, Long.feifei1Rect[1]))
    screen.blit(Heroplane.plane, (Heroplane.planex, Heroplane.planey))
    screen.blit(Bullet.bullet, (Bullet.bulletx, Bullet.bullety))
    Bullet.bulletmove()
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
    Enemyplane = Enemyplane()
    Bullet = Bullet()
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