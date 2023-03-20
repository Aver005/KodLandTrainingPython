import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, QUIT

from models.Window import Window
from models.game.Level import Level

pygame.init()

app: Window = None
is_running = False


def run():
    global app, is_running

    app = Window()
    first_level = Level(app.width, app.height)
    app.init_level(first_level)

    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    is_running = False
            elif event.type == QUIT:
                is_running = False

        app.update()
        app.draw()


if __name__ == "__main__":
    run()
