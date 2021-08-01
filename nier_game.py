import sys
import pygame
from settings import Settings
import game_function as gf
from ship import Ship
from pygame.sprite import Group
from bullets import Bullets
from enemy import Enemy

def run_game():
    """初始化并运行游戏"""
    #初始化游戏
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((
        game_settings.screen_width, game_settings.screen_height
    ))
    pygame.display.set_caption("NieR:Automata")

    #计算fps的时间
    fps_clock = pygame.time.Clock()

    #导入骇客飞船
    ship = Ship(screen)

    #建立敌人
    enemy = Enemy(screen)

    #创建一个表示子弹的编组
    bullets = Group()

    #创建红色子弹的编组
    red_bullet_x = Group()
    red_bullet_y = Group()

    # 创建黄色子弹的编组
    yellow_bullet_x = Group()
    yellow_bullet_y = Group()

    ADDENEMY = pygame.USEREVENT + 1
    ADDBULLET = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDENEMY, 600)
    pygame.time.set_timer(ADDBULLET, 200)

    #背景音乐
    pygame.mixer.music.load('YoRHa - Weight of the World／the End of YoRHa.mp3')
    pygame.mixer.music.play()

    sound_obj = pygame.mixer.Sound('core_8.ogg')
    sound_obj.set_volume(0.5)
    angle_rx = 45
    angle_yx = 135
    angle_ry = 225
    angle_yy = 315
    # shoot = False

    #游戏主循环
    while True:
        gf.check_events(game_settings, screen, ship, bullets, sound_obj, enemy, ADDENEMY, red_bullet_x,
                        ADDBULLET, angle_rx, angle_yx, yellow_bullet_x, angle_ry, red_bullet_y,
                        angle_yy, yellow_bullet_y)

        # #取得鼠标的坐标，得出想要转的角度
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # angle = gf.get_angle(ship, mouse_x, mouse_y)
        # gf.red_bullet_create(screen, enemy, red_bullet, ADDENEMY)

        ship.update()
        bullets.update()
        ship.update_angle()
        red_bullet_x.update()
        red_bullet_y.update()
        yellow_bullet_x.update()
        yellow_bullet_y.update()
        enemy.update()

        gf.delete_balls(bullets)
        gf.delete_balls(red_bullet_x)
        gf.bullet_hit_n(yellow_bullet_x, bullets)
        gf.bullet_hit_n(yellow_bullet_y, bullets)
        gf.bullet_hit_m(red_bullet_x, bullets)
        gf.bullet_hit_m(red_bullet_y, bullets)

        gf.update_screen(screen, ship, game_settings, bullets, enemy, red_bullet_x, yellow_bullet_x,
                         red_bullet_y, yellow_bullet_y)
        fps_clock.tick(60)

run_game()