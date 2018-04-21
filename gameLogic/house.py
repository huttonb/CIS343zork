import random
from gameLogic import vampire, werewolves, zombie, ghoul, observe


class House(object):
    def __init__(self):
        self.monsters = []
        numMonsters = random.randint(0,11)
        self.northNeighbor = 0
        self.southNeighbor = 0
        self.eastNeighbor = 0
        self.westNeighbor = 0

        for i in range(0, numMonsters):
            self.addmonster(self.monsters, random.randint(0,4))

        # weapon is the name of the weapon, damage is the damage provided by
        # the players modifier * weapon mod

        # creates empty array monstdamage, then calls the attackturn function for each monster in the house,
        # appending the returned value to the array, (returned value is damage the monster does to player)
        # then returns the new list.
        # TODO add something for dead monsters
    def attackhouse(self, weapon, damage):
        monstdamage=[]
        for i in self.monsters:
            monstdamage.append(i.attackturn(weapon, damage))
        return monstdamage

    def setnorth(self, nhouse):
        self.northNeighbor = nhouse

    def setsouth(self, shouse):
        self.southNeighbor = shouse

    def setwest(self, whouse):
        self.westNeighbor = whouse

    def seteast(self, ehouse):
        self.eastNeighbor = ehouse

    # Uses a number to decide what type of monster.
    # 0=zombie, 1=vampire, 2=werewolves, 3=ghoul
    def addmonster(self, list, monster):
        if monster == 0:
            a = zombie
        elif monster == 1:
            a = vampire
        elif monster == 2:
            a = werewolves
        elif monster == 3:
            a = ghoul
        else:
            print("Monster ID not Valid")
        list.append(a)
    #TODO Add observations with monsters, when it hits 0 house is freed