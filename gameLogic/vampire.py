import random
from gameLogic import monster

class Vampire(monster.NPC):

    def __init__(self):
        super().__init__()
        self.name = 'vampire'
        self.minattack = 10
        self.maxattack = 21
        self.weakness = 'ChocolateBars'
        self.health = random.randint(100,201)

    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.turnperson()
        return
