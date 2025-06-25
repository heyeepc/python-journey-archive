import pygame

# 初始化
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((600, 400))

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # 填充背景色
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 20, 20))  # 画方块

    pygame.display.update()  # 刷新窗口
