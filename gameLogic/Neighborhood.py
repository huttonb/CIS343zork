
from gameLogic.House import House
from gameLogic.Observe import Observer, Observable

# Neighborhood is an object that contains all the houses, observes all the houses, and is observable by the game.
class Neighborhood(Observer, Observable):

    # Initializes neighborhood, makes a 2d array of all the houses, as well as setting who their neighbors are and
    # adding neighborhood as their observer.
    def __init__(self, gridSize):
        super().__init__()
        Observable.__init__(self)
        self.__houses = []
        self.__size = gridSize
        self.__housesremaining = self.__size * self.__size
        for i in range(0, gridSize):
            tempArr = []
            self.__houses.append(tempArr)
            for j in range(0, gridSize):
                a = House()
                tempArr.append(a)
                a.add_observer(self)
                if(i > 0):
                    a.setn(self.__houses[i - 1][j])
                    self.__houses[i - 1][j].sets(a)
                if j > 0:
                    a.setw(self.__houses[i][j - 1])
                    self.__houses[i][j - 1].sete(a)
        for i in range (0, self.__size):
            for j in range(0, self.__size):
                self.__houses[i][j].checkhouse()


    # getstartloc returns the topleft house.
    def getstartloc(self):
        return self.__houses[0][0]

    # update prints out how many houses are remaining, if there are none it updates the game so that the player
    # can win.
    def update(self, object):
        self.__housesremaining -= 1
        print("HOUSES REMAINING = " + str(self.__housesremaining))
        if self.__housesremaining == 0:
            self.update_observer(self)
        return

    # map formats and prints a map of the neighborhood as well as where the player is.
    def map(self):
        maps = ""
        for i in range(0, self.__size):
            maps += "\n"
            for j in range(0, self.__size):
                maps += self.__houses[i][j].getmapicon()

        print(maps)
        print("Map Legend: X=defeated house, O=undefeated house,"
              " @=player on undefeated house, *=player on defeated house")

