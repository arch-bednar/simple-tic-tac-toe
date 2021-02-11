#!/usr/bin/python3

class Player():
    def __init__(self, name, sign):
        self._name = name
        self._sign = sign

    @property
    def returnName(self):
        return self._name

    @property
    def returnSign(self):
        return self._sign

class Computer():
    def __init__(self):
        self._name = "Computer"
        self._sign = 'O'

    @property
    def returnName(self):
        return self._name

    @property
    def returnSign(self):
        return self._sign

class Board():
    def __init__(self):
        self._boardValues=[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def changeValue(self, value, position):
        if isFilled():
            self._boardValues[position[0], position[1]] = value
        else:
            print("This field is filled!")

    def isFilled(self, position):
        if self._boardValues[position[0], position[1]]  not in ('X', 'O'):
            return False
        else:
            return True

    def printBoard(self):
        length = len(self._boardValues)
        for x in range(length):
            for y in range(length):
                if x < length - 1:
                    print (self._boardValues[x][y], " | ")
                else:
                    print (self._boardValues[x][y])

            if x < length - 1:
                for line in range(9):
                    print("-")

    @property
    def getBoard(self):
        return self._boardValues

class TicTacToe(object):
    def __init__(self):
        menu()
        execute()
        self.board = Board()


    def menu(self):
        selection=0
        while (selection not in range(1,3)):
            print('###############')
            print('---Menu---')
            print('1 - Player vs Computer')
            print('2 - Player vs Player')
            print('3 - Quit')
            print('###############')
            
            selection = int(input("What do you want to do?"))
            
            try:
                print("OK")
            except:
                print("Please enter correct value!")
                continue

    def chechStatus(self):
        pass
    
    def _vonNeumann(self, tab):
        length = len(tab)
        for x in range(length):
            for y in range(length):

                for xi in range(x-1, x+1+1)
                    if xi < 0 or xi > length or xi == x: 
                        continue
                
                for yi in range(y-1, y+1+1):



    def _diagonal(self, tab):
        if tab[1][1] == tab[0][0] == tab[2][2] or tab[1][1] == tab[0][1] == tab[2][1]:
            return True
        else:
            return False

    def startPVP(self,currBoard):
        while True:
            currBoard.printBoard()

    
    def playerTurn(self, who):
        axisXY = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
        print("Player ", who.returnName())
        print("Press enter position [1 - 9]: ")
        place = 0
        while place not in range(1,10):
            place = int(input())
            
            try:
                if isFilled(axisXY.get(place)):
                    print("OK")
                    self.board.changeValue(who.returnSign(), axisXY.get(place))

                else:
                    continue
            except:
                print("Wrong value!")
                place = 0
                continue

    def startPVC(self):
        pass

    def startPVP(self):
        while not (self._diagonal(self._getBoard()) and self._vonNeumann(self._getBoard)):
            self.playerTurn(self.playerOne)
            self.playerTurn(self.playerTwo)

    def _getBoard(self):
        return self.board.getBoard()

    def execute(self, choice):
        if choice == 1:
            name = takeName(1)
            makePlayers(name, 'X')
        elif choice == 2:
            name1 = takeName(1)
            name2 = takeName(2)
            makePlayers(Player(name1, 'X'), Player(name2, 'O'))
            startPVP()
        else:
            exit()

    def takeName(self, num):
        return input("Player " ,num, " name: ")

    def makePlayers(self, first, last):
        self.playerOne = first
        self.playerTwo = last

    def makePlayers(self, first):
        self.playerOne = first
        self.playerTwo = Computer()
