import pygame
from pygame.sprite import Sprite
from math import *

class Bullets(Sprite):
    """子弹的类"""
    def __init__(self, game_settings, screen, ship, angle):

        super().__init__()
        self.screen = screen
        self.angle = angle
        self.image = pygame.image.load('images/bullet.bmp')
        self.image.set_colorkey((240, 229, 211))

        #设置初始位置
        self.rect = self.image.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.centery

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """更新子弹位置"""
        self.y -= 10 * cos(radians(self.angle % 360))
        self.rect.y = self.y
        self.x += (-10) * sin(radians(self.angle % 360))
        self.rect.x = self.x


    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        #使其绕中心点旋转
        self.image_n = pygame.transform.rotate(self.image, self.angle)
        self.new_rect = self.image_n.get_rect(center=self.rect.center)

        self.screen.blit(self.image_n, self.new_rect)



