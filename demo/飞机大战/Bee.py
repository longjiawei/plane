import random
import sys

import pygame


class Enemyplane():
    def __init__(self):
        self.enemyplane = pygame.image.load('D:\python\demo\飞机大战\图片\\14.1.png')
        self.enemyplane1 = pygame.image.load('D:\python\demo\飞机大战\图片\\14.1.png')
        self.enemyplaneRect = pygame.Rect(60,60,60,60)

        self.enemyplanex = 0

        self.enemyplaney = 0

        self.direction = 'right'
        self.speed = 1
        self.enemyplaneRect[1] = self.enemyplaney

    def enemymove(self):
        self.enemyplaney += self.speed
        if self.direction == 'right':
            self.enemyplanex += 5
        elif self.direction == 'left':
            self.enemyplanex -= 5
        if self.enemyplanex > 550 :
            self.direction = 'left'
        elif self.enemyplanex < 0 :
            self.direction = 'right'
        if self.enemyplaney > 850 :
            self.enemyplaney = 0
        self.enemyplaneRect[1] = self.enemyplaney
        self.enemyplaneRect[0] = self.enemyplanex
class Bullet():
    def __init__(self,screen):
        self.bullets = list()
        self.screen = screen
        self.bullet = pygame.image.load('D:\python\demo\飞机大战\图片\\15.1.png')
        self.bulletrect = pygame.Rect(30,30,30,30)
        self.bulletx = Heroplane.planex + 10
        self.bullety = Heroplane.planey - 20
        self.bulletspeed = 30
    def bulletdisplay(self):

        for bullet in range(5):
            self.screen.blit(Bullet.bullet, (Bullet.bulletx, Bullet.bullety))
            self.bullety -= self.bulletspeed
            if self.bullety < 0:
                self.bullety = Heroplane.planey - 20
                self.bulletx = Heroplane.planex + 10
            self.bulletrect[1] = self.bullety
            self.bulletrect[0] = self.bulletx
            self.bullets.append(bullet)
            if len(self.bullets) >100:
                self.bullets.remove(bullet)


class Heroplane():
    def __init__(self):
        self.plane = pygame.image.load('D:\python\demo\飞机大战\图片\\1.3.png')
        self.planeRect = pygame.Rect(50,50,50,50)
        self.planex = 275
        self.planey = 740
        self.herobullets = []
    def planemove(self):
        if self.planey < 0:    #限定飞机边界
            self.planey = 0
        if self.planey > 860:
            self.planey = 860
        if self.planex < 0:
            self.planex = 0
        if self.planex > 550:
            self.planex = 550
        elif event.key == pygame.K_UP:  #控制飞机移动
            self.planey -= 5
            self.planeRect[1] = self.planey
        elif event.key == pygame.K_DOWN:
            self.planey += 5
            self.planeRect[1] = self.planey
        elif event.key == pygame.K_LEFT:
            self.planex -= 5
            self.planeRect[0] = self.planex
        elif event.key == pygame.K_RIGHT:
            self.planex += 5
            self.planeRect[0] = self.planex


class Long():
    def __init__(self):
        self.feifei = pygame.image.load('D:\python\demo\飞机大战\图片\\10.3.png')
        self.feifeiRect = pygame.Rect(65,50,65,50)
        self.feifeix = random.randint(100,500)
        self.feifeiy = -50
        self.dead = False
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
        self.bg1y += 1      #背景1
        self.bg2y += 1      #背景2
        self.bg1rect[1] = self.bg1y
        self.bg2rect[1] = self.bg2y
        if self.bg1y >900:       #背景滚动效果
            self.bg1y = -900
        elif self.bg2y > 900:
            self.bg2y = -900


def Display():
    screen.fill((255, 255, 255))
    screen.blit(Map.background1, (0, Map.bg1rect[1]))   #显示背景
    screen.blit(Map.background2, (0, Map.bg2rect[1]))
    screen.blit(Enemyplane.enemyplane,(Enemyplane.enemyplanex,Enemyplane.enemyplaney))

    screen.blit(Long.feifei, (Long.feifeix, Long.feifeiRect[1]))
    screen.blit(Long.feifei1, (Long.feifei1x, Long.feifei1Rect[1]))
    screen.blit(Heroplane.plane, (Heroplane.planex, Heroplane.planey))

    if checkdead():
        getresult()
    Enemyplane.enemymove()
    Bullet.bulletdisplay()
    Map.mapmove()
    Long.updateBee()
    pygame.display.update()
def checkdead():

    if Bullet.bulletrect.colliderect(Long.feifei1Rect) or Bullet.bulletrect.colliderect(Long.feifeiRect) or Bullet.bulletrect.colliderect(Enemyplane.enemyplaneRect):
        Long.dead = True
        return True
    else:
        return False


def getresult():
    global score
    if Long.dead :
        score += 1
    final_text = 'Your final score is:' + str(score)
    ft1_font = pygame.font.SysFont('Arial', 5)
    ft1_surf = font.render(final_text,1,(243,255,255))
    screen.blit(ft1_surf, (0, 0))
    pygame.display.update()
if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)
    size = width,height = 600,900
    screen = pygame.display.set_mode(size)
    pygame.key.set_repeat(10)
    score = 0
    Long = Long()
    Heroplane = Heroplane()
    Map = Map()
    Enemyplane = Enemyplane()

    Bullet = Bullet(screen)

    clock = pygame.time.Clock()
    while True:
        clock.tick(500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                Heroplane.planemove()
        Display()



    pygame.quit()