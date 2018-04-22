
from gameLogic.House import House
from gameLogic.Observe import Observer, Observable


class Neighborhood(Observer, Observable):
    def __init__(self, gridSize):
        super().__init__()
        Observable.__init__(self)
        #TODO: Make 2d array for all these fucking houses
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
         #   i.checkhouse(self)

    def getstartloc(self):
        return self.__houses[0][0]

    def update(self, object):
        self.__housesremaining -= 1
        print("HOUSES REMAINING = " + str(self.__housesremaining))
        if self.__housesremaining == 0:
            self.update_observer(self)
        return

    def map(self):
        maps = ""
        for i in range(0, self.__size):
            maps += "\n"
            for j in range(0, self.__size):
                maps += self.__houses[i][j].getmapicon()

        print(maps)
        print("Map Legend: X=defeated house, O=undefeated house,"
              " @=player on undefeated house, *=player on defeated house")

