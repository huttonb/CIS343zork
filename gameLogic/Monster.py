import random
from gameLogic.Observe import Observable


class NPC(Observable):
    def __init__(self):

        Observable.__init__(self)
        self.name = 'generic'
        self.__minattack = 1
        self.__maxattack = 2
        self.__health = 0
        self.__weakness = 'generic'
        self.person = False

    def gethealth(self):
        return self.__health

    def getattack(self):
        if not self.person:
          return random.randint(self.__minattack, self.__maxattack)
        else:
            return -1

    def getweakness(self, weapon):
        if weapon == self.__weakness:
            return True
        return False

    def getname(self):
        return self.name

    def attackturn(self, weapon, damage):
        # In turn the monst takes damage then deals damage to the player.
        # if the monst turns into a friendly it deals negative damage
        if(self.person == False):
            self.takedamage(weapon, damage)
        else:
            print("A Person gives you candy! +1 candy +1 health!")
        return self.getattack()
    # if returned value is -1 then give player candy

    # Overrides to take specific damage for weakness
    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.__health = self.__health - damage
        else:
            self.__health = self.__health - damage
        if self.__health <= 0:
            self.turnperson()
        return

    def turnperson(self):
        self.update_observer(self)
        self.name = 'person'
        self.__weakness = 'none'
        self.__health = 100
        self.person = True

class Ghoul(NPC):

    def __init__(self):
        super(). __init__()
        self.name = 'ghoul'
        self.__minattack = 15
        self.__maxattack = 31
        self.__weakness = "NerdBombs"
        self.__health = random.randint(40,80)

    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.__health = self.__health - int((damage * 5))
            print("Critical! The Ghoul took "+ str(int(damage*5)) + " damage from that " + weapon + ", good job!")
        else:
            self.__health = self.__health - damage
            print("The Ghoul took " + str(damage) + " damage from that " + weapon + ", nice!")
        if self.__health <= 0:
            print("The Ghoul has turned into a person!")
            self.turnperson()
        return

class Vampire(NPC):
    def __init__(self):
        super().__init__()
        self.name = 'vampire'
        self.__minattack = 10
        self.__maxattack = 21
        self.__weakness = 'ChocolateBars'
        self.health = random.randint(100,200)

    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health
            print("Ouch! The Vampire is immune to " + weapon + "!")
        else:
            self.health = self.health - damage
            print("The Vampire took " + str(damage) + " damage from that " + weapon + ", nice!")
        if self.health <= 0:
            print("The Vampire has turned into a person!")
            self.turnperson()
        return

class Werewolf(NPC):

    def __init__(self):
        super().__init__()
        self.name = 'werewolf'
        self.minattack = 1
        self.maxattack = 40
        self.weakness = 'ChocolateBars'
        self.weakness2 = 'SourStraws'
        self.health = 200

    def getweakness(self, weapon):
        if weapon == self.weakness:
            return True
        elif weapon == self.weakness2:
            return True
        return False

    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            print("Ouch! The Werewolf is immune to " + weapon + "!")
            self.health = self.health
        else:
            print("The Werewolf took " + str(damage) + " damage from that " + weapon + ", nice!")
            self.health = self.health - damage
        if self.health <= 0:
            print("The Werewolf has turned into a person!")
            self.turnperson()

class Zombie(NPC):

    def __init__(self):
        super().__init__()
        self.name = 'zombie'
        self.minattack = 1
        self.maxattack = 11
        self.weakness = 'SourStraws'
        self.health = random.randint(50,100)


    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            print("Critical! The Zombie took " + str(int(damage*2)) + " damage from that " + weapon + ", good job!")
            self.health = self.health - int((damage * 2))
        else:
            print("The Zombie took " + str(damage) + " damage from that " + weapon + ", nice!")
            self.health = self.health - damage
        if self.health <= 0:
            print("The Zombie has turned into a person!")
            self.turnperson()
        return

