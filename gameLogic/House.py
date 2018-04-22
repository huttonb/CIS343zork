import random
from gameLogic.Monster import Vampire, Werewolf, Zombie, Ghoul
from gameLogic.Observe import Observable, Observer

# House is a class that contains 0-10 monsters, and controls their attack phases for them. It observes the monsters,
# and is observable by the neighborhood.
class House(Observable, Observer):

    # initializes house, creates monsters in the house, and observes the monsters.
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

    # attackhouse creates a list for the damage that the monster deals to the player, then lets the player attack
    # every monster, with the return being the monsters damage. At the end of the players attack attackhouse returns
    # the list of damage the monsters dealt to the player.
    def attackhouse(self, weapon, damage):
        monstdamage=[]
        for i in self.monsters:
            monstdamage.append(i.attackturn(weapon, damage))
        return monstdamage

    #  Add monster creates a random monster for the house. Uses a number to decide what type of monster.
    # 0=zombie, 1=vampire, 2=werewolves, 3=ghoul. Afterwards it makes the house the observer for them.
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

        a.add_observer(self)
        self.monsters.append(a)

    # update updates whenever a monster dies. If the number of monsters in the house reaches zero, the house is declared
    # defeated and it updates the neighborhood.
    def update(self, object):
        self.numMonsters -=1
        if self.numMonsters == 0:
            self.defeated = True
            self.update_observer(self)

    # getmapicon returns a specific icon depending on whether or not it is occupied or defeated. For formatting
    # purposes.
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

    # peekhouse prints out the monsters in the house. If peek is true, you peek through a window and it displays
    # a seperate message, otherwise it assumes you are currently in combat.
    def peekhouse(self, peek):
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

    # occupy changes the house to occupied.
    def occupy(self):
        self.playeroccupied = True

    # unoccupy changes the house to unoccupied.
    def unoccupy(self):
        self.playeroccupied = False

    # checkhouse checks to see if there are any monsters left in the house, if there aren't it updates its observer.
    def checkhouse(self):
        if self.numMonsters == 0:
            self.defeated = True
            self.update_observer(self)

    # the set(direction) and get(direction) functions will set what house in the cardinal direction of this house,
    # and return what house is in the cardinal direction of this house, respectively.

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