import pygame
from plane_sprites import *

pygame.init()

# 创建游戏窗口 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 加载背景图像数据
bg = pygame.image.load("./images/background.png")

# blit绘制图像
# screen.blit(bg, (0, 0))

# 加载英雄图像数据
hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (150, 300))

pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:

    # 可以指定循环体内部代码执行的频率
    clock.tick(60)

    # 事件监听
    for even in pygame.event.get():

        # 判断用户是否点击关闭按钮
        if even.type == pygame.QUIT:
            print("退出游戏！")

            pygame.quit()

            # 直接退出系统
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update-让组中的精灵更新位置
    enemy_group.update()

    # draw-在screen上绘制所有的精灵
    enemy_group.draw(screen)

    # 调用update方法更新显示
    pygame.display.update()

# pygame.quit()
