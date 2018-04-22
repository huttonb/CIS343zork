#Author Bryce Hutton

import os
import platform
from gameLogic.Observe import Observer
from gameLogic.Neighborhood import Neighborhood
from gameLogic.Player import Player


class Game(Observer):
    def __init__(self):
            Observer.__init__(self)
            self.town = Neighborhood(4)
            self.player = Player(self.town.getstartloc())
            self.player.add_observer(self)
            self.town.add_observer(self)
            self.exit = False
            self.fight = True
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
                self.player.getlocation().peekHouse(True)
            else:
                self.printcmds()
                print("Invalid command.")

    def battlePhase(self):
        self.fight = True
        while self.fight == True:
            if self.fight:
              self.segscreen()
            self.player.getlocation().peekHouse(False)
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
                damage = self.player.getlocation().attackhouse("SourStraws", self.player.attack("SourStraws"))
                for i in damage:
                    self.player.takedamage(i)
            if choice =="e":
                damage = self.player.getlocation().attackhouse("ChocolateBars", self.player.attack("ChocolateBars"))
                for i in damage:
                    self.player.takedamage(i)
            if choice =="r":
                damage = self.player.getlocation().attackhouse("NerdBombs", self.player.attack("NerdBombs"))
                for i in damage:
                    self.player.takedamage(i)

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

    def clearscreen(self):
        print("\n" * 100)

    def segscreen(self):
        print("-"*100)

    def printcmds(self):
        self.town.map()
        print("\nw = Move up.......a = Move left.........s = Move down...d = Move right\n"
              "c = enter house...f = peek into house...x = exit\n")

    def combatcmds(self):
        print("\nACTIONS")
        print("q:HersheyKisses...w:SourStraws...e:ChocolateBars...r:NerdBombs...c:Run")

if __name__ == '__main__':
    a = Game()
    a.turn()




#TODO encapsulate, __combatcmds to make it private, __  to make a variable private
#TODO  comment everything, follow style guide