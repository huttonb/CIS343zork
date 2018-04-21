import random
from gameLogic.observe import Observable


class NPC(Observable):
    def __init__(self):
        self.name = 'generic'
        self.minattack = 0
        self.maxattack = 1
        self.health = 0
        self.weakness = 'generic'
        self.person = False


    def gethealth(self):
        return self.health

    def getattack(self):
        return random.randint(self.minattack, self.maxattack )

    def getweakness(self, weapon):
        if weapon == self.weakness:
            return True
        return False


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
            self.updateObservers()
            self.turnperson()
        return

    def turnperson(self):
        self.name = 'person'
        self.weakness = 'none'
        self.health = 100
        self.minattack = -1
        self.maxattack = -2
        self.person = True
