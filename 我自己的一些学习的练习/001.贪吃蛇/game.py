# game.py
import pygame
from snake import Snake
from food import Food
from settings import WIDTH, HEIGHT, GRID_SIZE, FPS, BLACK, GREEN, RED, WHITE

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        start = (WIDTH // 2 // GRID_SIZE * GRID_SIZE, HEIGHT // 2 // GRID_SIZE * GRID_SIZE)
        self.snake = Snake(start)
        self.food = Food()
        self.score = 0
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction(1, 0)

    def update(self):
        # 如果吃到食物，则增长并得分
        will_grow = (self.snake.head() == self.food.pos)
        self.snake.move(grow=will_grow)
        if will_grow:
            self.score += 1
            self.food.respawn(self.snake.body)

        # 碰撞检测（自撞）
        if self.snake.collides_with_self():
            self.running = False

    def draw_grid(self):
        # 可选：画网格帮助调试
        cols = WIDTH // GRID_SIZE
        rows = HEIGHT // GRID_SIZE
        for x in range(cols):
            for y in range(rows):
                rect = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

    def draw(self):
        self.screen.fill(WHITE)
        # self.draw_grid()
        # 画食物
        fx, fy = self.food.pos
        food_rect = pygame.Rect(fx, fy, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.screen, RED, food_rect)

        # 画蛇
        for i, (x, y) in enumerate(self.snake.body):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            color = GREEN if i == 0 else (0, 150, 0)
            pygame.draw.rect(self.screen, color, rect)

        # 分数
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        self.screen.blit(text, (5, 5))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
