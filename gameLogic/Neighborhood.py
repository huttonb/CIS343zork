
from gameLogic.House import House
from gameLogic.observe import Observer


class Neighborhood(Observer):
    def __init__(self, gridSize):
        super().__init__()
        #TODO: Make 2d array for all these fucking houses
        self.houses = []
        self.size = gridSize
        self.housesremaining = self.size * self.size
        for i in range(0, gridSize):
            tempArr = []
            self.houses.append(tempArr)
            for j in range(0, gridSize):
                a = House()
                tempArr.append(a)
                a.add_observer(self)
                if(i > 0):
                    a.setn(self.houses[i-1][j])
                    self.houses[i-1][j].sets(a)
                if j > 0:
                    a.setw(self.houses[i][j-1])
                    self.houses[i][j-1].sete(a)
        for i in range (0, self.size):
            for j in range(0, self.size):
                self.houses[i][j].checkhouse()
         #   i.checkhouse(self)

    def getstartloc(self):
        return self.houses[0][0]

    def update(self):
        self.housesremaining -= 1
        print("HOUSES REMAINING = " + str(self.housesremaining))
        if self.housesremaining == 0:
            print("you didded it")
        return

    def map(self):
        maps = ""
        for i in range(0,self.size):
            maps += "\n"
            for j in range(0,self.size):
                maps += self.houses[i][j].getmapicon()

        print(maps)
        print("Map Legend: X=defeated house, O=undefeated house,"
              " @=player on undefeated house, *=player on defeated house")

