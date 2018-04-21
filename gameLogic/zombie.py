import random
from gameLogic import monster


class Zombie(monster.NPC):

    def __init__(self):
        super().__init__()
        self.name = 'zombie'
        self.minattack = 0
        self.maxattack = 11
        self.weakness = 'SourStraws'
        self.health = random.randint(50,101)


    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health - (damage * 2)
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.turnperson()
        return

