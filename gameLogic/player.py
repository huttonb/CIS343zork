import random

class Player(object):
    def __init__(self, house):
        self.name = 'Player'
        self.health = random.randint(100, 126)
     #   self.attack = random.randint(10,21)
        self.inventory = {'HersheyKisses': -1, 'SourStraws': 0, 'ChocolateBars': 0, 'NerdBombs': 0}
        self.location = house

        x = random.randint(0, 11)
        y = random.randint(0, 11)
        z = random.randint(0, 11)
        sum = x+y+z
        sum = sum/10
        self.inventory['SourStraws'] = int(x/sum)
        self.inventory['ChocolateBars'] = int(y/sum)
        self.inventory['NerdBombs'] = int(z/sum)

    def getattack(self):
        return random.randint(10,21)

    def attack(self, weapon):
        if self.inventory[weapon] > 0:
            if weapon == "HersheyKisses":
                return self.getattack()
            if weapon == 'SourStraws':
                self.inventory["SourStraws"] -= .5
                return self.getattack() * ((random.randint(100,176))/100)
            if weapon == 'ChocolateBars':
                self.inventory["ChocolateBars"] -= .25
                return self.getattack() * ((random.randint(200,240))/100)
            if weapon == 'NerdBombs':
                self.inventory["NerdBombs"] -= 1
                return self.getattack() * ((random.randint(350, 500))/100)
            else:
                #incorrect message
                return -1

    def movePlayer(self, house):
        self.location = house

    def takeDamage(self, damage):
        if damage < 0:
            self.getcandy(random.randint(0,3))
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
