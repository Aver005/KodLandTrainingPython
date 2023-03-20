from models.game.LivingEntity import LivingEntity


class Zombie(LivingEntity):
    DEFAULT_ZOMBIE_SPEED = 0.125

    lvl = 1
    death_drop = []

    def __init__(self, name, position, hp=100, speed=DEFAULT_ZOMBIE_SPEED, lvl=1):
        super().__init__(name, position, hp, speed)
        self.lvl = lvl
