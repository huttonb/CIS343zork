#Author Bryce Hutton


from gameLogic.Observe import Observer
from gameLogic.Neighborhood import Neighborhood
from gameLogic.Player import Player

# The Game controls the turn phases of the game. It observes both the player and the neighborhood.
class Game(Observer):

    #initializes objects neighborhood, player, and booleans for loops.
    def __init__(self):
            Observer.__init__(self)
            self.town = Neighborhood(4)
            self.player = Player(self.town.getstartloc())
            self.player.add_observer(self)
            self.town.add_observer(self)
            self.exit = False
            self.fight = True
            self.turn()

    # Turn is for turns on the outside map. Runs a loop that lets the player decide whether to move cardinally,
    # Or to look inside a house, enter a house, and exit a house.
    def turn(self):
        print("Welcome to Candy-Zork!")
        self.printcmds()
        while(self.exit == False):

            choice = input("")
            self.clearscreen()
            if choice == "x":
                self.exit = True
            elif choice == "w":
                if self.player.getlocation().getn() != 0:
                    self.player.moveplayer(self.player.getlocation().getn())
                    self.printcmds()
            elif choice == "a":
                if self.player.getlocation().getw() != 0:
                    self.player.moveplayer(self.player.getlocation().getw())
                    self.printcmds()
            elif choice == "s":
                if self.player.getlocation().gets() != 0:
                    self.player.moveplayer(self.player.getlocation().gets())
                    self.printcmds()
            elif choice == "d":
                if self.player.getlocation().gete() != 0:
                    self.player.moveplayer(self.player.getlocation().gete())
                    self.printcmds()
            elif choice == "c":
                self.battlePhase()
            elif choice == "f":
                self.printcmds()
                self.player.getlocation().peekhouse(True)
            else:
                self.printcmds()
                print("Invalid command.")

    # Battlephase runs a loop for the battles inside of a house. Once the player makes a choice, it determines what
    # weapon the player is using, then gathers the damage from the weapon, and sends it through the houses
    # attackHouse function, which deals with damage for each individual monster. The damage dealt by the monster
    # to the player is stored in a list, which is then dealt to the player.
    def battlePhase(self):
        self.fight = True
        while self.fight == True:
            if self.fight:
              self.segscreen()
            self.player.getlocation().peekhouse(False)
            self.player.getinventory()
            self.player.gethealth()
            self.combatcmds()
            choice = input("")
            if choice =="c":
                self.printcmds()
                self.fight = False
            if choice =="q":
                damage = self.player.getlocation().attackhouse("HersheyKisses", self.player.attack("HersheyKisses"))
                for i in damage:
                    self.player.takedamage(i)

            if choice =="w":
                if self.player.checkcandy("SourStraws"):
                    damage = self.player.getlocation().attackhouse("SourStraws", self.player.attack("SourStraws"))
                    for i in damage:
                        self.player.takedamage(i)
                else:
                    print("Not enough of that candy!")
            if choice =="e":
                if self.player.checkcandy("ChocolateBars"):
                    damage = self.player.getlocation().attackhouse("ChocolateBars", self.player.attack("ChocolateBars"))
                    for i in damage:
                        self.player.takedamage(i)
                else:
                    print("Not enough of that candy!")
            if choice =="r":
                if self.player.checkcandy("NerdBombs"):
                    damage = self.player.getlocation().attackhouse("NerdBombs", self.player.attack("NerdBombs"))
                    for i in damage:
                        self.player.takedamage(i)
                else:
                    print("Not enough of that candy!")

    # update is used for win conditions. An object is passed along, if it's the players object then the player has died,
    # if it's the neighborhood, the player has won.
    def update(self, object):
        if object == self.player:
            print("You have died :(")
            self.fight = False
            self.exit = True
            exit()
        elif object == self.town:
            print("YOU SAVED THE DAY!")
            self.fight = False
            self.exit = True
            exit()
        else:
            print("Error: Updated by non-observable")
        return

    # clearscreen creates 100 newlines for formatting purposes.
    def clearscreen(self):
        print("\n" * 100)

    # segscreen creates dashes to segment the screen for formatting purposes.
    def segscreen(self):
        print("-"*100)

    # printcmds prints the commands for the outside map.
    def printcmds(self):
        self.town.map()
        print("\nw = Move up.......a = Move left.........s = Move down...d = Move right\n"
              "c = enter house...f = peek into house...x = exit\n")

    # combadcmds prints the commands for the battlephase.
    def combatcmds(self):
        print("\nACTIONS")
        print("q:HersheyKisses...w:SourStraws...e:ChocolateBars...r:NerdBombs...c:Run")

if __name__ == '__main__':
    a = Game()
    a.turn()

