import random
from gameLogic.Observe import Observable
from gameLogic.House import House

# Player is the class for the player, it contains the inventory the player uses, as well as their stats, it is
# observable by the game.
class Player(Observable):

    # Initializes player, creates dict of inventory, sets his location to a house, creates up to 10 items in inventory.
    def __init__(self, house1):
        Observable.__init__(self)
        self.location = House()
        self.name = 'Player'
        self.health = random.randint(100, 125)
        self.inventory = {'HersheyKisses': 999, 'SourStraws': 0, 'ChocolateBars': 0, 'NerdBombs': 0}
        self.location = house1
        self.location.occupy()

        x = random.randint(0, 10)
        y = random.randint(0, 10)
        z = random.randint(0, 10)
        sum = x+y+z
        sum = sum/10
        self.inventory['SourStraws'] = int(x / sum)
        self.inventory['ChocolateBars'] = int(y / sum)
        self.inventory['NerdBombs'] = int(z / sum)

    # Attack is given a weapon, then returns the attack of the player times the multiplier of the weapon.
    def attack(self, weapon):
        if self.inventory[weapon] != 0:
            if weapon == "HersheyKisses":

                damage = self.getattack()
                return damage
            elif weapon == 'SourStraws':
                self.inventory["SourStraws"] -= .5
                damage = self.getattack() * ((random.randint(100, 175)) / 100)
                return damage
            elif weapon == 'ChocolateBars':
                self.inventory["ChocolateBars"] -= .25
                damage = self.getattack() * ((random.randint(200, 240)) / 100)
                return damage
            elif weapon == 'NerdBombs':
                self.inventory["NerdBombs"] -= 1
                damage = self.getattack() * ((random.randint(350, 500)) / 100)
                return damage
            else:
                #incorrect message
                return -1

    # moveplayer marks the current house as unoccupied, switches to the new house, and marks the new house as occupied.
    def moveplayer(self, house):
        self.location.unoccupy()
        self.location = house
        self.location.occupy()

    # takedamage takes the damage given and subtracts it from players health. If the damage is negative, the player
    # heals for that amount, and is given one piece of candy.
    def takedamage(self, damage):
        if damage < 0:
            self.getcandy(random.randint(0, 2))
        self.health -= damage
        if self.health <= 0:
            self.update_observer(self)
            return 0
    # getinventory prints out the contents of the inventory.
    def getinventory(self):
        print("Inventory is: ", self.inventory)

    # gethealth prints out the players current health.
    def gethealth(self):
        print("Players health is:" + str(self.health))

    # getlocation returns the house the player is currently located in.
    def getlocation(self):
        return self.location

    # getcandy gives the player one candy. candynum is a randomly generated number.
    def getcandy(self, candyNum):
        if sum(self.inventory.values())+1 < 10:
            if candyNum == 0:
                self.inventory['SourStraws'] += 1
            elif candyNum == 1:
                self.inventory['ChocolateBars'] += 1
            elif candyNum == 2:
                self.inventory['NerdBombs'] += 1
            else:
                print("Incorrect #")
        else:
            print("You can't hold any more candy!")

    # getattack returns the attack of the player between 10 and 20
    def getattack(self):
        return random.randint(10,20)
    def checkcandy(self, candy):
        if self.inventory[candy] >= 1:
            return True
        return False