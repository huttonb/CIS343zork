import random
from gameLogic.Observe import Observable

# Npc is a class that has several monster subclasses. It is observable by the house.
class NPC(Observable):

    #initializes the generic monster, makes the monster observable.
    def __init__(self):
            Observable.__init__(self)
            self.name = 'generic'
            self.minattack = 1
            self.maxattack = 2
            self.health = 0
            self.weakness = 'generic'
            self.person = False

    # getattack returns the attack of the monster between the minattack and the maxattack
    def getattack(self):
        if not self.person:
          return random.randint(self.minattack, self.maxattack)
        else:
            return -1

    # getweakness checks to see if the weapon given is the monsters weakness.
    def getweakness(self, weapon):
        if weapon == self.weakness:
            return True
        return False

    # getname returns the name of the monster
    def getname(self):
        return self.name

    # attackturn is when the monster takes damage and gives damaage. If the monster is a person, it instead gives health
    # to the player.
    def attackturn(self, weapon, damage):

        if(self.person == False):
            self.takedamage(weapon, damage)
        else:
            print("A Person gives you candy! +1 candy +1 health!")
        return self.getattack()

    # takedamage determines the damage based on the damage the player has used, and if the monster is weak to
    # the weapon the player used. If the monsters health reaches 0 it turns into a person.
    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health - damage
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.turnperson()
        return

    # turnperson updates the observer when the monster has reached 0 health, and converts the monster into a player.
    def turnperson(self):
        self.update_observer(self)
        self.name = 'person'
        self.weakness = 'none'
        self.health = 100
        self.person = True

class Ghoul(NPC):

    #initializes monster-specific values, such as attack and weaknesses.
    def __init__(self):
        super().__init__()
        self.name = 'ghoul'
        self.minattack = 15
        self.maxattack = 31
        self.weakness = "NerdBombs"
        self.health = random.randint(40,80)

    # takedamage determines the damage based on the damage the player has used, and if the monster is weak to
    # the weapon the player used. If the monsters health reaches 0 it turns into a person.
    def takedamage(self, weapon, damage):
        if self.getweakness(weapon) is True:
            self.health = self.health - int((damage * 5))
            print("Critical! The Ghoul took "+ str(int(damage*5)) + " damage from that " + weapon + ", good job!")
        else:
            self.health = self.health - damage
            print("The Ghoul took " + str(damage) + " damage from that " + weapon + ", nice!")
        if self.health <= 0:
            print("The Ghoul has turned into a person!")
            self.turnperson()
        return

class Vampire(NPC):

    #initializes monster-specific values, such as attack and weaknesses.
    def __init__(self):
        super().__init__()
        self.name = 'vampire'
        self.minattack = 10
        self.maxattack = 21
        self.weakness = 'ChocolateBars'
        self.health = random.randint(100,200)

    # takedamage determines the damage based on the damage the player has used, and if the monster is weak to
    # the weapon the player used. If the monsters health reaches 0 it turns into a person.
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

    #initializes monster-specific values, such as attack and weaknesses.
    def __init__(self):
        super().__init__()
        self.name = 'werewolf'
        self.minattack = 1
        self.maxattack = 40
        self.weakness = 'ChocolateBars'
        self.weakness2 = 'SourStraws'
        self.health = 200

    # getweakness checks to see if the weakness of the monster is the same as the weapon, returns true if it is.
    # because the werewolf has two weaknesses, it needs its own function for it.
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

    #initializes monster-specific values, such as attack and weaknesses.
    def __init__(self):
        super().__init__()
        self.name = 'zombie'
        self.minattack = 1
        self.maxattack = 11
        self.weakness = 'SourStraws'
        self.health = random.randint(50,100)

    # takedamage determines the damage based on the damage the player has used, and if the monster is weak to
    # the weapon the player used. If the monsters health reaches 0 it turns into a person.
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

