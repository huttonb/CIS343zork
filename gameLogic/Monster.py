import random
from gameLogic.observe import Observable


class NPC(Observable):
    def __init__(self):

        Observable.__init__(self)
        self.name = 'generic'
        self.minattack = 0
        self.maxattack = 1
        self.health = 0
        self.weakness = 'generic'
        self.person = False

    def gethealth(self):
        return self.health

    def getattack(self):
        if not self.person:
          return random.randint(self.minattack, self.maxattack )
        else:
            return -1

    def getweakness(self, weapon):
        if weapon == self.weakness:
            return True
        return False

    def getname(self):
        return self.name

    def attackturn(self, weapon, damage):
        # In turn the monst takes damage then deals damage to the player.
        # if the monst turns into a friendly it deals negative damage
        if(self.person == False):
            self.takedamage(weapon, damage)

        return self.getattack()
    # if returned value is -1 then give player candy

    # Overrides to take specific damage for weakness
    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health - damage
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.turnperson()
        return

    def turnperson(self):
        self.update_observer()
        self.name = 'person'
        self.weakness = 'none'
        self.health = 100
        self.person = True

class Ghoul(NPC):

    def __init__(self):
        super(). __init__()
        self.name = 'ghoul'
        self.minattack = 15
        self.maxattack = 31
        self.weakness = "NerdBombs"
        self.health = random.randint(40,80)

    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health - (damage * 5)
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.turnperson()
        return

class Vampire(NPC):
    def __init__(self):
        super().__init__()
        self.name = 'vampire'
        self.minattack = 10
        self.maxattack = 21
        self.weakness = 'ChocolateBars'
        self.health = random.randint(100,200)

    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.turnperson()
        return

class Werewolf(NPC):

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
            self.turnperson()

class Zombie(NPC):

    def __init__(self):
        super().__init__()
        self.name = 'zombie'
        self.minattack = 0
        self.maxattack = 11
        self.weakness = 'SourStraws'
        self.health = random.randint(50,100)


    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health - (damage * 2)
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.turnperson()
        return

