from models.game.Entity import Entity


class LivingEntity(Entity):
    MAX_HEALTH = 100
    MIN_HEALTH = 0

    name = ""
    hp = 100
    speed = 2.5

    is_dead = False

    def __init__(self, name, position, hp, speed):
        super().__init__(position[0], position[1])
        self.name = name
        self.hp = hp
        self.speed = speed

    def heal(self, value):
        if value < 0:
            self.damage(value)
            return

        self.hp += value
        if self.hp > self.MAX_HEALTH:
            self.hp = self.MAX_HEALTH

    def damage(self, value):
        if value > 0:
            self.damage(value)
            return

        self.hp -= value
        if self.hp <= self.MIN_HEALTH:
            self.is_dead = True
