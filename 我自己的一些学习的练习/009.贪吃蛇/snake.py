# snake.py
from typing import List, Tuple
from settings import GRID_SIZE, WIDTH, HEIGHT

Position = Tuple[int, int]

class Snake:
    def __init__(self, init_pos: Position):
        self.body: List[Position] = [init_pos]  # head is body[0]
        self.direction = (1, 0)  # moving right by grid units

    def head(self) -> Position:
        return self.body[0]

    def set_direction(self, dx: int, dy: int):
        # 防止直接掉头（如果长度>1）
        if len(self.body) > 1:
            opposite = (-self.direction[0], -self.direction[1])
            if (dx, dy) == opposite:
                return
        self.direction = (dx, dy)

    def move(self, grow: bool = False):
        x, y = self.head()
        dx, dy = self.direction
        new_head = ((x + dx * GRID_SIZE) % WIDTH, (y + dy * GRID_SIZE) % HEIGHT)
        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()

    def collides_with_self(self) -> bool:
        return self.head() in self.body[1:]

    def occupies(self, pos: Position) -> bool:
        return pos in self.body
