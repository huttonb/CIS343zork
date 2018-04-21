import random
from gameLogic import monster

class Ghoul(monster.NPC):

    def __init__(self):
        super(). __init__()
        self.name = 'ghoul'
        self.minattack = 15
        self.maxattack = 31
        self.weakness = "NerdBombs"
        self.health = random.randint(40,81)

    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health - (damage * 5)
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.turnperson()
        return
