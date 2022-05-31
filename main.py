import pygame
from collections import deque
from random import choice, randrange

class Ant:
    def __init__(self, app: "Application", pos, color) -> None:
        self.app = app
        self.color = color
        self.x, self.y = pos
        self.increments = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    def run(self) -> None:
        value = self.app.grid[self.y][self.x]
        self.app.grid[self.y][self.x] = not value

        size = self.app.Cell_Size
        rect = self.x * size, self.y * size, size - 1, size - 1

        if value:
            pygame.draw.rect(self.app.screen, pygame.Color("white"), rect)
        else:
            pygame.draw.rect(self.app.screen, self.color, rect)

        self.increments.rotate(1) if value else self.increments.rotate(-1)
        dx, dy = self.increments[0]
        self.x = (self.x + dx) % self.app.cols
        self.y = (self.y + dy) % self.app.rows

class Application:
    def __init__(self, Width=1600, Height=900, Cell_Size=2) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([Width, Height])
        self.clock = pygame.time.Clock()

        self.Cell_Size = Cell_Size
        self.rows, self.cols = Height // Cell_Size, Width // Cell_Size
        self.grid = [[0 for col in range(self.cols)] for row in range(self.rows)]

        self.ants = [Ant(self, pos=[randrange(self.cols), randrange(self.rows)], color=self.get_color()) for i in range(5)]
        

    @staticmethod
    def get_color():
        channel = lambda: randrange(30, 220)
        return channel(), channel(), channel()

    def run(self) -> None:
        while True:
            [ant.run() for ant in self.ants]
            [exit(0) for i in pygame.event.get() if i.type == pygame.QUIT]

            pygame.display.flip()
            self.clock.tick()

if __name__ == '__main__':
    app = Application()
    app.run()