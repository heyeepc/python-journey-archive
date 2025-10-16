# food.py
import random
from typing import Tuple
from settings import GRID_SIZE, WIDTH, HEIGHT

Position = Tuple[int, int]

def random_position():
    cols = WIDTH // GRID_SIZE
    rows = HEIGHT // GRID_SIZE
    return (random.randrange(cols) * GRID_SIZE, random.randrange(rows) * GRID_SIZE)

class Food:
    def __init__(self):
        self.pos: Position = random_position()

    def respawn(self, occupied_positions):
        # 避免生成在蛇身上
        while True:
            p = random_position()
            if p not in occupied_positions:
                self.pos = p
                break
