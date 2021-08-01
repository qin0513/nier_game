import pygame

class Ship():
    """骇客飞船的类"""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.image.set_colorkey((30, 26, 21))

        #取得位置和创建rect对象
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()

        #骇客飞船在屏幕居中
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        #设置飞船的移动方向
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        #初始角度等于0
        self.angle = 0
        self.turn_right = False
        self.turn_left = False

        self.shoot = False

    def update(self):
        """根据移动标志更改骇客飞船的方向"""
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 10
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 10
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 10
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 10

    def update_angle(self):
        if self.turn_right:
            self.angle -= 5
        elif self.turn_left:
            self.angle += 5


    #将飞船绘制在屏幕中利用blit()
    def blitme(self):
        self.image_n = pygame.transform.rotate(self.image, self.angle)
        self.new_rect = self.image_n.get_rect(center = self.rect.center)

        self.screen.blit(self.image_n, self.new_rect)

