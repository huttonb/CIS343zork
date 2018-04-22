#Author Bryce Hutton

import os
import platform
from gameLogic.Neighborhood import Neighborhood
from gameLogic.Player import Player


class Game(object):
    def __init__(self):
            self.town = Neighborhood(4)
            self.player = Player(self.town.getstartloc())
            self.exit = False
            self.turn()

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
                    self.player.movePlayer(self.player.getlocation().getn())
                    self.printcmds()
            elif choice == "a":
                if self.player.getlocation().getw() != 0:
                    self.player.movePlayer(self.player.getlocation().getw())
                    self.printcmds()
            elif choice == "s":
                if self.player.getlocation().gets() != 0:
                    self.player.movePlayer(self.player.getlocation().gets())
                    self.printcmds()
            elif choice == "d":
                if self.player.getlocation().gete() != 0:
                    self.player.movePlayer(self.player.getlocation().gete())
                    self.printcmds()
            elif choice == "c":
                self.battlePhase()
            elif choice == "f":
                self.printcmds()
                self.player.getlocation().peekHouse(True)
            else:
                self.printcmds()
                print("Invalid command.")

    def battlePhase(self):
        self.fight = True
        while self.fight == True:
            self.clearscreen()
            self.player.getlocation().peekHouse(False)
            self.player.getinventory()
            self.player.gethealth()
            self.combatcmds()
            choice = input("")
            if choice =="c":
                self.printcmds()
                self.fight = False
            if choice =="q":
                self.printcmds()
                damage = self.player.getlocation().attackhouse("HersheyKisses", self.player.attack("HersheyKisses"))
                for i in damage:
                    self.player.takeDamage(i)
            if choice =="w":
                self.printcmds()
                damage = self.player.getlocation().attackhouse("SourStraws", self.player.attack("SourStraws"))
                for i in damage:
                    self.player.takeDamage(i)
            if choice =="e":
                self.printcmds()
                damage = self.player.getlocation().attackhouse("ChocolateBars", self.player.attack("ChocolateBars"))
                for i in damage:
                    self.player.takeDamage(i)
            if choice =="r":
                self.printcmds()
                damage = self.player.getlocation().attackhouse("NerdBombs", self.player.attack("NerdBombs"))
                for i in damage:
                    self.player.takeDamage(i)





        return
    def combatcmds(self):
        print("\nACTIONS")
        print("q:HersheyKisses...w:SourStraws...e:ChocolateBars...r:NerdBombs...c:Run")

    def clearscreen(self):
        print("\n" * 100)

    def printcmds(self):
        self.town.map()
        print("\nw = Move up.......a = Move left.........s = Move down...d = Move right\n"
              "c = enter house...f = peek into house...x = exit\n")

if __name__ == '__main__':
    a = Game()
    a.turn()


#TODO Add win condition, add death, add max inventory, add weapons as objects
#TODO encapsulate, __combatcmds to make it private, __  to make a variable private
#TODO  comment everything, follow style guide