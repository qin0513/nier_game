import pygame
from random import randint, random
from pygame.sprite import Sprite

class Enemy(Sprite):
    """表示单个敌人的类"""

    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        self.image = pygame.image.load('images/enemy.bmp')
        self.image.set_colorkey((30, 26, 21))
        self.rect = self.image.get_rect()

        self.rect.y = self.rect.height
        self.rect.x = randint(200, 800)

        self.y = self.rect.y

    def update(self):
        if self.y <= 300:
            self.y += 1
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
