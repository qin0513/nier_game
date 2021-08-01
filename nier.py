import sys
import pygame
from settings import Settings
from math import atan2, degrees
from enemy import Enemy

def run_game():
    """初始化并运行游戏"""
    #初始化游戏
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((
        game_settings.screen_width, game_settings.screen_height
    ))
    pygame.display.set_caption("NieR")

    #导入骇客飞船
    ship = pygame.image.load('images/ship.bmp')
    ship_rect = ship.get_rect()
    screen_rect = screen.get_rect()
    ship_rect.centerx = screen_rect.centerx
    ship_rect.centery = screen_rect.centery
    ship_angle = 0

    #导入子弹
    bullet_rect = pygame.Rect(0, 0, 20, 20)
    bullet_rect.centerx = ship_rect.centerx
    bullet_rect.centery = ship_rect.centery


    enemy = Enemy(screen)

    #游戏主循环
    while True:
        screen.fill(game_settings.bg_color)
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # pre_angle = atan2(ship_rect.centery - mouse_y, mouse_x - ship_rect.centerx)
        # angle = degrees(pre_angle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship_angle -= 30
                elif event.key == pygame.K_LEFT:
                    ship_angle += 30
                elif event.key == pygame.K_SPACE:
                    pygame.draw.rect(screen, (255,255,255), bullet_rect)
        bullet_rect.y -= 1
        enemy.blitme()
        pygame.draw.rect(screen, (255,255,255), bullet_rect)
        ship_n = pygame.transform.rotate(ship, ship_angle)
        screen.blit(ship_n, ship_rect)
        pygame.display.flip()

run_game()