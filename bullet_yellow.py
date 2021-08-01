import pygame
from pygame.sprite import Sprite
from math import *

class BulletYellow(Sprite):
    """黄色的子弹"""
    def __init__(self, screen, enemy, angle, b_velocity):
        super().__init__()
        self.screen = screen
        self.angle = angle
        self.b_velocity = b_velocity

        #载入黄色子弹的图像
        self.image = pygame.image.load('images/ball_y.bmp')
        self.image.set_colorkey((30, 26, 21))

        #设定子弹的初始位置
        #从image的surface中创建一个rect对象
        self.rect = self.image.get_rect()

        #这里的ship是形参ship的实例，ship.rect是ship类的一个属性
        self.rect.center = enemy.rect.center

        self.x_value = 0

    def update(self):
        """移动黄色球的位置"""
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x += (-1 * self.b_velocity) * sin(radians(self.angle % 360))
        self.y -= self.b_velocity * cos(radians(self.angle % 360))
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
