import random

from models.game.Entity import Entity
from models.game.LivingEntity import LivingEntity


class MedicalKit(Entity):
    MIN_HEALTH = 10
    MAX_HEALTH = 25

    health = 15

    def __init__(self, position):
        super().__init__(position[0], position[1])
        self.health = random.randint(MedicalKit.MIN_HEALTH, MedicalKit.MAX_HEALTH)

    def use(self, entity: LivingEntity):
        entity.heal(self.health)
        self.can_be_destroyed = True
