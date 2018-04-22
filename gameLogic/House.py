import random
from gameLogic.Monster import Vampire, Werewolf, Zombie, Ghoul
from gameLogic.Observe import Observable, Observer


class House(Observable, Observer):
    def __init__(self):
        super().__init__()
        self.monsters = []
        self.numMonsters = random.randint(0,10)
        self.northNeighbor = 0
        self.southNeighbor = 0
        self.eastNeighbor = 0
        self.westNeighbor = 0
        self.defeated = False
        self.playeroccupied = False
        for i in range(0, self.numMonsters):
            self.addmonster(random.randint(0,3))


    def attackhouse(self, weapon, damage):
        monstdamage=[]
        for i in self.monsters:
            monstdamage.append(i.attackturn(weapon, damage))
        return monstdamage

    # Uses a number to decide what type of monster.
    # 0=zombie, 1=vampire, 2=werewolves, 3=ghoul
    def addmonster(self, monster):
        if monster == 0:
            a = Zombie()
        elif monster == 1:
            a = Vampire()
        elif monster == 2:
            a = Werewolf()
        elif monster == 3:
            a = Ghoul()
        else:
            print("Monster ID is " + str(monster))
            print("Monster ID not Valid")
            return
            #TODO Check to make sure this is actually working
        a.add_observer(self)
        self.monsters.append(a)

    def update(self, object):
        self.numMonsters -=1
        if self.numMonsters == 0:
            self.defeated = True
            self.update_observer(self)

    def getmapicon(self):
        if self.playeroccupied:
            if self.defeated == True:
                return "*"
            else:
                return "@"
        else:
            if self.defeated == True:
                return "X"
            else:
                return "O"

    def peekHouse(self, peek):
        if peek:
            print("You peek through the window of the house and see...")
        else:
            print("You see:")
        zombies = 0
        ghouls = 0
        vampires = 0
        werewolves = 0
        persons = 0
        for i in self.monsters:
            if i.getname() == "ghoul":
                ghouls += 1
            elif i.getname() == "vampire":
                vampires += 1
            elif i.getname() == "werewolf":
                werewolves += 1
            elif i.getname() == "zombie":
                zombies += 1
            elif i.getname() == "person":
                persons += 1
        print(str(zombies) + " zombies, " + str(ghouls) + " ghouls, " + str(vampires) +
              " vampires, " + str(werewolves) + " werewolves, and " + str(persons) + " people.")

    def occupy(self):
        self.playeroccupied = True

    def unoccupy(self):
        self.playeroccupied = False

    def checkhouse(self):
        if self.numMonsters == 0:
            self.defeated = True
            self.update_observer(self)
        # weapon is the name of the weapon, damage is the damage provided by
        # the players modifier * weapon mod

        # creates empty array monstdamage, then calls the attackturn function for each monster in the house,
        # appending the returned value to the array, (returned value is damage the monster does to player)
        # then returns the new list.
        # TODO add something for dead monsters

    def setw(self, house):
        self.westNeighbor = house

    def sete(self, house):
        self.eastNeighbor = house

    def setn(self, house):
        self.northNeighbor = house

    def sets(self, house):
        self.southNeighbor = house

    def getw(self):
        return self.westNeighbor

    def gete(self):
        return self.eastNeighbor

    def getn(self):
        return self.northNeighbor

    def gets(self):
        return self.southNeighbor