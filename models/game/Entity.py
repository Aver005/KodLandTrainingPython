import pygame.image


class Entity:
    x = 0
    y = 0

    image_path = "./images/DefaultSprite.png"
    sprite = None
    is_visible = True
    can_be_destroyed = False

    def __init__(self, x, y, is_visible=True, image_path=image_path):
        self.x = x
        self.y = y
        self.is_visible = is_visible
        self.sprite = pygame.image.load(self.image_path)

    def draw(self, screen):
        if self.sprite is None:
            return
        if not self.is_visible:
            return
        screen.blit(self.sprite, (self.x, self.y))

    def update(self, keys):
        pass
