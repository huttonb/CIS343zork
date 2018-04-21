import random
from gameLogic import monster

class Werewolf(monster.NPC):

    def __init__(self):
        super().__init__()
        self.name = 'werewolf'
        self.minattack = 0
        self.maxattack = 40
        self.weakness = 'ChocolateBars'
        self.weakness2 = 'SourStraws'
        self.health = 0

     def getweakness(self, weapon):
        if weapon == self.weakness:
            return True
        elif weapon == self.weakness2:
            return True
        return False

    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.turnperson(self)
