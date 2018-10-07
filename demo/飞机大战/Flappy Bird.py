import random
import sys

import pygame


class Bird():
    def __init__(self):
        self.birdRect =  pygame.Rect(65,50,50,65)
        self.birdStatus = [pygame.image.load('D:\python\demo\飞机大战\图片\\10.1.png'),
                           pygame.image.load('D:\python\demo\飞机大战\图片\\9.1.png')]
        self.status = 0    #默认飞行状态
        self.birdx = 120   #飞行的X轴坐标，即是向右飞行的速度
        self.birdy = 300   #Y轴坐标，即上下飞行的高度
        self.jump = False   #默认自动降落
        self.jumpSpeed = 10  #跳跃高度
        self.gravity = 0  # 重力
        self.dead = False  #默认生命状态为存活

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdy -= self.jumpSpeed
        else:
            self.gravity += 0.5   #重力递增，下降加快
            self.birdy += self.gravity  #Y轴坐标增加，下降
        self.birdRect = self.birdy   #更改Y轴位置
class Pipeline():
    def __init__(self):
        self.wallx = random.randint(400,1000)  #管道初始坐标X
        self.pineup = pygame.image.load('D:\python\demo\飞机大战\图片\\13.1.png')
        self.pinedown = pygame.image.load('D:\python\demo\飞机大战\图片\\13.1.png')
    def updatePipeline(self):
        self.wallx -= 5  #管道X轴坐标递减，即管道向左移动
        #当管道运行到一定位置，小鸟飞越管道，分数加1，并且重置管道
        if self.wallx < -80:
            self.wallx = random.randint(400,1000)
            global score
            score += 1
def createMap():
    screen.fill((255,255,255,))  #填充颜色为白色
    screen.blit(background,(0,0))#填入背景
    screen.blit(Pipeline.pineup,(Pipeline.wallx,0))
    screen.blit(Pipeline.pinedown,(Pipeline.wallx,550))
    screen.blit(font.render('Score:' + str(score), -1 ,(255,255,255)),(100,50))
    Pipeline.updatePipeline()
    if Bird.dead:
        Bird.status = 1
    elif Bird.jump:
        Bird.status = 0
    screen.blit(Bird.birdStatus[0],(Bird.birdx, Bird.birdy))
    Bird.birdUpdate()
    pygame.display.update()
def checkDead():
    upRect = pygame.Rect(Pipeline.wallx,0,Pipeline.pineup.get_width(),Pipeline.pineup.get_height())
    downRect = pygame.Rect(Pipeline.wallx,550,Pipeline.pinedown.get_width(),Pipeline.pinedown.get_height())
    if upRect.colliderect(Bird.birdRect)  or downRect.colliderect(Bird.birdRect):
        Bird.dead = True
        return True
    else:
        return False
def getResutl():
    final_text1 = 'Game Over'
    final_text2 = 'Your final score is:' + str(score)
    ft1_font = pygame.font.SysFont('Arial', 70)
    ft1_surf = font.render(final_text1,1,(243,3,36))
    ft2_font = pygame.font .SysFont('Arial', 50)
    ft2_surf = font.render(final_text2,1,(253,177,6))
    screen.blit(ft1_surf,[screen.get_width()/2-ft1_surf.get_width()/2, 100])
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])
    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None,50)  #设置默认字体和大小
    size = width,height = 1266,780   #400，650
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()
    Bird = Bird()
    score = 0
    while True:
        clock.tick(60)   #每秒执行60次
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYUP  or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True  #跳跃
                Bird.gravity = 5  #重力
                Bird.jumpSpeed = 10  #跳跃速度
        background = pygame.image.load('D:\python\demo\飞机大战\图片\\12.png')
        if checkDead():
            getResutl()
        else:
            createMap()
        createMap()
    pygame.quit()