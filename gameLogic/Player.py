import random


from gameLogic.House import House

class Player(object):
    def __init__(self, house1):
        self.location = House()
        self.name = 'Player'
        self.health = random.randint(100, 125)
     #   self.attack = random.randint(10,21)
        self.inventory = {'HersheyKisses': -1, 'SourStraws': 0, 'ChocolateBars': 0, 'NerdBombs': 0}
        self.location = house1
        self.location.occupy()

        x = random.randint(0, 10)
        y = random.randint(0, 10)
        z = random.randint(0, 10)
        sum = x+y+z
        sum = sum/10
        self.inventory['SourStraws'] = int(x/sum)
        self.inventory['ChocolateBars'] = int(y/sum)
        self.inventory['NerdBombs'] = int(z/sum)

    def getlocation(self):
        return self.location

    def getattack(self):
        return random.randint(10,20)

    def attack(self, weapon):
        if self.inventory[weapon] != 0:
            if weapon == "HersheyKisses":
                return self.getattack()
            elif weapon == 'SourStraws':
                self.inventory["SourStraws"] -= .5
                return self.getattack() * ((random.randint(100, 175))/100)
            elif weapon == 'ChocolateBars':
                self.inventory["ChocolateBars"] -= .25
                return self.getattack() * ((random.randint(200, 240))/100)
            elif weapon == 'NerdBombs':
                self.inventory["NerdBombs"] -= 1
                return self.getattack() * ((random.randint(350, 500))/100)
            else:
                #incorrect message
                return -1

    def movePlayer(self, house):
        self.location.unoccupy()
        self.location = house
        self.location.occupy()

    def takeDamage(self, damage):
        if damage < 0:
            self.getcandy(random.randint(0,2))
        self.health -= damage
        if self.health <= 0:
            return 0
            #todo game over

    def getcandy(self, candyNum):
        if candyNum == 0:
            self.inventory['SourStraws'] += 1
        elif candyNum == 1:
            self.inventory['ChocolateBars'] += 1
        elif candyNum == 2:
            self.inventory['NerdBombs'] += 1
        else:
            print("Incorrect #")

    def getinventory(self):
        print("Inventory is: ", self.inventory)

    def gethealth(self):
        print("Players health is:" + str(self.health))
