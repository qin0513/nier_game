import pygame
import sys
from math import atan2, degrees
from bullets import Bullets
from bullet_red import BulletRed
from bullet_yellow import BulletYellow

# 检查各种事件


def check_keydown_events(event, game_settings, screen, ship, bullets, sound_obj):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_d:
        ship.moving_right = True
    # elif event.key == pygame.K_SPACE:
    #     new_bullet = Bullets(game_settings, screen, ship, ship.angle)
    #     sound_obj.play()
    #     bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_d:
        ship.moving_right = False

def check_keydown_angle_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.turn_right = True
    elif event.key == pygame.K_LEFT:
        ship.turn_left = True

def check_keyup_angle_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.turn_right = False
    elif event.key == pygame.K_LEFT:
        ship.turn_left = False

def check_shoot_events_down(event, ship):
    if event.key == pygame.K_SPACE:
        ship.shoot = True

def check_shoot_events_up(event, ship):
    if event.key == pygame.K_SPACE:
        ship.shoot = False


def check_events(game_settings, screen, ship, bullets, sound_obj, enemy, ADDENEMY, red_bullet_x,
                 ADDBULLET, angle_rx, angle_yx, yellow_bullet_x, angle_ry, red_bullet_y,
                 angle_yy, yellow_bullet_y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets, sound_obj)
            check_keydown_angle_events(event, ship)
            check_shoot_events_down(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            check_keyup_angle_events(event, ship)
            check_shoot_events_up(event, ship)
        # 添加敌人的子弹
        if event.type == ADDENEMY and enemy.y == 301:
            new_bullet_rx = BulletRed(screen, enemy, angle_rx, 2)
            red_bullet_x.add(new_bullet_rx)
            new_bullet_ry = BulletRed(screen, enemy, angle_ry, 3)
            red_bullet_y.add(new_bullet_ry)

            new_bullet_yx = BulletYellow(screen, enemy, angle_yx, 2)
            yellow_bullet_x.add(new_bullet_yx)
            new_bullet_yy = BulletYellow(screen, enemy, angle_yy, 3)
            yellow_bullet_y.add(new_bullet_yy)

        # 添加己方子弹
        if event.type == ADDBULLET and ship.shoot:
            new_bullet = Bullets(game_settings, screen, ship, ship.angle)
            bullets.add(new_bullet)
#

# def get_angle(ship, mouse_x, mouse_y):
#     pre_angle = atan2(ship.rect.centery - mouse_y, mouse_x - ship.rect.centerx)
#     angle = degrees(pre_angle)
#     return angle


def delete_balls(balls):
    """去除掉超出屏幕的sprite"""
    for ball in balls.copy():
        if ball.rect.left > 1200 or\
                ball.rect.right < 0 or\
                ball.rect.top > 750 or\
                ball.rect.bottom < 0:
            balls.remove(ball)

def bullet_hit_n(bullet_balls, bullets):
    collisions = pygame.sprite.groupcollide(bullet_balls, bullets, True, True)

def bullet_hit_m(bullet_balls, bullets):
    collisions = pygame.sprite.groupcollide(bullet_balls, bullets, False, True)

def update_screen(screen, ship, game_settings, bullets, enemy, red_bullet_x, yellow_bullet_x,
                  red_bullet_y, yellow_bullet_y):
    screen.fill(game_settings.bg_color)
    # 画出子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 画出敌方子弹
    for red_bx in red_bullet_x.sprites():
        red_bx.blitme()
    for yellow_bx in yellow_bullet_x.sprites():
        yellow_bx.blitme()
    for red_by in red_bullet_y.sprites():
        red_by.blitme()
    for yellow_by in yellow_bullet_y.sprites():
        yellow_by.blitme()
    enemy.blitme()
    ship.blitme()

    #刷新图像
    pygame.display.flip()

