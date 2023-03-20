import random

from models.game.Entity import Entity
from models.game.Player import Player
from models.game.Zombie import Zombie


class Level:
    width = 900
    height = 600

    player_start_hp = 100
    player_start_speed = Player.DEFAULT_PLAYER_SPEED
    player_start_balance = 0

    zombie_count = 10
    zombie_start_hp = 75
    zombie_start_speed = Zombie.DEFAULT_ZOMBIE_SPEED
    zombie_start_lvl = 1

    player: Player = None
    zombies: list[Zombie] = []
    items: list[Entity] = []

    def __init__(self, width, height, player=None):
        self.width = width
        self.height = height
        self.player = player

    def setup_level(self):
        if self.player is None:
            random_name = f"Player-{random.randint(1000, 9999)}"
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.player = Player(
                name=random_name,
                position=(x, y),
                hp=self.player_start_hp,
                speed=self.player_start_speed,
                balance=self.player_start_balance
            )

        for i in range(self.zombie_count):
            random_name = f"Zombie-{random.randint(1000, 9999)}"
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            new_zombie = Zombie(
                name=random_name,
                position=(x, y),
                hp=self.zombie_start_hp,
                speed=self.zombie_start_speed,
                lvl=self.zombie_start_lvl
            )
            self.zombies.append(new_zombie)

    def draw(self, screen):
        to_draw = [*self.items, self.player, *self.zombies]
        for obj in to_draw:
            obj.draw(screen)

    def update(self, keys):
        to_update = [self.player, *self.zombies, *self.items]
        for obj in to_update:
            obj.update(keys)
