import math

import pygame

from models.game.LivingEntity import LivingEntity
from models.utils.Keyboard import Keyboard


class Player(LivingEntity):
    DEFAULT_PLAYER_SPEED = 0.15

    balance = 0
    deaths = 0
    kills = 0
    is_running = False
    run_boost = 1.4

    def __init__(self, name, position, hp=100, speed=DEFAULT_PLAYER_SPEED, balance=0):
        super().__init__(name, position, hp, speed)
        self.balance = balance

    def rotate(self, cursor):
        dx, dy = cursor[0] - self.x, cursor[1] - self.y
        angle = -math.degrees(math.atan2(dy, dx))
        self.sprite = pygame.transform.rotate(self.sprite, angle)

    def update(self, keys):
        offset_x = 0
        offset_y = 0

        is_running = keys[Keyboard.SHIFT]
        speed = self.speed * self.run_boost if is_running else self.speed

        if keys[Keyboard.W]:
            offset_y -= speed
        if keys[Keyboard.S]:
            offset_y += speed
        if keys[Keyboard.D]:
            offset_x += speed
        if keys[Keyboard.A]:
            offset_x -= speed

        self.x += offset_x
        self.y += offset_y
