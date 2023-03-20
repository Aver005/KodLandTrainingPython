import pygame
from pygame import Surface, SurfaceType

from models.game.Entity import Entity
from models.game.Level import Level
from models.utils.Colors import Colors


class Window:
    screen: Surface | SurfaceType = None
    width: int = 900
    height: int = 600
    background_color: tuple[int, int, int] = Colors.BLUE_SKY

    level: Level = None

    def __init__(self, width=900, height=600):
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode([width, height])

    def draw(self):
        self.screen.fill(self.background_color)
        if self.level is not None:
            self.level.draw(self.screen)
        pygame.display.update()

    def update(self):
        keys = pygame.key.get_pressed()

        if self.level is not None:
            self.level.update(keys)

    def init_level(self, level):
        level.setup_level()
        self.level = level
