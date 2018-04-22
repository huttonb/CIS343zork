import random
from gameLogic.Observe import Observable
from gameLogic.House import House


class Player(Observable):

    # Initializes player, creates dict of inventory, sets his location to a house, creates up to 10 items in inventory.
    def __init__(self, house1):
        Observable.__init__(self)
        self.__location = House()
        self.__name = 'Player'
        self.__health = random.randint(100, 125)
        self.__inventory = {'HersheyKisses': 999, 'SourStraws': 0, 'ChocolateBars': 0, 'NerdBombs': 0}
        self.__location = house1
        self.__location.occupy()

        x = random.randint(0, 10)
        y = random.randint(0, 10)
        z = random.randint(0, 10)
        sum = x+y+z
        sum = sum/10
        self.__inventory['SourStraws'] = int(x / sum)
        self.__inventory['ChocolateBars'] = int(y / sum)
        self.__inventory['NerdBombs'] = int(z / sum)

    # Attack is given a weapon, then returns the attack of the player times the multiplier of the weapon.
    def attack(self, weapon):
        if self.__inventory[weapon] != 0:
            if weapon == "HersheyKisses":
                return self.__getattack()
            elif weapon == 'SourStraws':
                self.__inventory["SourStraws"] -= .5
                return self.__getattack() * ((random.randint(100, 175)) / 100)
            elif weapon == 'ChocolateBars':
                self.__inventory["ChocolateBars"] -= .25
                return self.__getattack() * ((random.randint(200, 240)) / 100)
            elif weapon == 'NerdBombs':
                self.__inventory["NerdBombs"] -= 1
                return self.__getattack() * ((random.randint(350, 500)) / 100)
            else:
                #incorrect message
                return -1

    # moveplayer marks the current house as unoccupied, switches to the new house, and marks the new house as occupied.
    def moveplayer(self, house):
        self.__location.unoccupy()
        self.__location = house
        self.__location.occupy()

    # takedamage takes the damage given and subtracts it from players health. If the damage is negative, the player
    # heals for that amount, and is given one piece of candy.
    def takedamage(self, damage):
        if damage < 0:
            self.__getcandy(random.randint(0, 2))
        self.__health -= damage
        if self.__health <= 0:
            self.update_observer(self)
            return 0
    # getinventory prints out the contents of the inventory.
    def getinventory(self):
        print("Inventory is: ", self.__inventory)

    # gethealth prints out the players current health.
    def gethealth(self):
        print("Players health is:" + str(self.__health))

    # getlocation returns the house the player is currently located in.
    def getlocation(self):
        return self.__location

    # __getcandy gives the player one candy. candynum is a randomly generated number.
    def __getcandy(self, candyNum):
        if sum(self.__inventory.values())+1 < 10:
            if candyNum == 0:
                self.__inventory['SourStraws'] += 1
            elif candyNum == 1:
                self.__inventory['ChocolateBars'] += 1
            elif candyNum == 2:
                self.__inventory['NerdBombs'] += 1
            else:
                print("Incorrect #")
        else:
            print("You can't hold any more candy!")

    # __getattack returns the attack of the player between 10 and 20
    def __getattack(self):
        return random.randint(10,20)