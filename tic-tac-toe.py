#!/usr/bin/python3

import random

class Player():
    def __init__(self, name, sign):
        self._name = name
        self._sign = sign
        self.win = False

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
        if self.isFilled(position)==False:
            self._boardValues[position[0]][position[1]] = value
        else:
            print("This field is filled!")

    def isFilled(self, position):
        if self._boardValues[position[0]][position[1]]  not in ('X', 'O'):
            return False
        else:
            return True

    def printBoard(self):
        length = len(self._boardValues)
        temp = self._boardValues
        print("{}|{}|{}".format(temp[0][0], temp[0][1], temp[0][2]))
        print("-----")
        print("{}|{}|{}".format(temp[1][0],temp[1][1],temp[1][2]))
        print("-----")
        print("{}|{}|{}".format(temp[2][0], temp[2][1], temp[2][2]))

    @property
    def getBoard(self):
        return self._boardValues

class TicTacToe(object):
    def __init__(self):
        self.board = Board()

    def start(self):
        self.execute(self.menu())


    def menu(self):
        selection=0
        while (selection not in range(1,4)):
            print('###############')
            print('---Menu---')
            print('1 - Player vs Computer')
            print('2 - Player vs Player')
            print('3 - Quit')
            print('###############')
            
            selection = int(input("What do you want to do?"))
            
            try:
                print("OK")
                return selection
            except:
                print("Please enter correct value!")
                continue
    
    def _vonNeumann(self, tab):
        length = len(tab) - 1
        for x in range(length):
            for y in range(length):
                
                count = 0
                for xi in range(x-1, x+2):
                    if xi < 0 or xi > length or xi == x: 
                        continue
                    if tab[x][y] == tab[xi][y] and tab[x][y] in ('X','O'):
                        count=count+1
                
                if count == 2:
                    return True
                count = 0
                for yi in range(y-1, y+2):
                    if yi < 0 or yi > length or yi == y:
                        continue
                    if tab[x][y] == tab[x][yi] and tab[x][y] in ('X','O'):
                        count=count+1
                
                if count == 2:
                    return True
        return False

    def _diagonal(self, tab):
        if (tab[1][1] == tab[0][0] == tab[2][2] or tab[1][1] == tab[0][2] == tab[2][0]) and tab[1][1] in ('X', 'O'):
            return True
        else:
            return False

    def computerTurn(self):
        if self._getBoard[1][1] == ' ':
            self.board.changeValue('O', (1,1))
        else:
            x,y=3,3
            length = len(self.board.getBoard)
            while x not in range(0,length) and y not in range(0,length):
                x,y = random.randint(0, length-1), random.randint(0, length-1)
                if self.board.getBoard[x][y] in ('X', 'O'):
                    x,y = 3,3
                else:
                    self.board.changeValue('O', (x,y))


    def playerTurn(self, who):
        self.board.printBoard()
        axisXY = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
        print("Player ", who.returnName)
        print(who.returnSign)
        place = 0
        while place not in range(1,10):
            place = int(input("Press enter position [1 - 9]: "))
            if self.board.isFilled(axisXY.get(place)) == False:
                print("OK")
                self.board.changeValue(who.returnSign, axisXY.get(place))
            else:
                print("siema")
                place=0
                continue

    def checkStatus(self):
        if self._diagonal(self._getBoard) or self._vonNeumann(self._getBoard):
            return True
        else:
            return False

    def startPVP(self):
        status=True
        while status:
            self.playerTurn(self.playerOne)
            if self.checkStatus():
                status = False
            if status != False:
                self.playerTurn(self.playerTwo)
            if self.checkStatus():
                status = False
        self.board.printBoard()
    
    def startPVC(self):
        status=True
        while status:
            self.computerTurn()
            if self.checkStatus():
                status = False
            if status != False:
                self.playerTurn(self.playerTwo)
            if self.checkStatus():
                status = False
        self.board.printBoard()

    @property
    def _getBoard(self):
        return self.board.getBoard

    def execute(self, choice):
        if choice == 1:
            name = self.takeName(1)
            self.makePlayer(Player(name, 'X'))
            self.startPVC()
        elif choice == 2:
            name1 = self.takeName(1)
            name2 = self.takeName(2)
            self.makePlayers(Player(name1, 'X'), Player(name2, 'O'))
            self.startPVP()
        else:
            exit()

    def takeName(self, num):
        msg = "Player {} name: ".format(num)
        return input(msg)

    def makePlayer(self, first):
        self.playerTwo = first
        self.playerOne = Computer()

    def makePlayers(self, first, last):
        self.playerOne = first
        self.playerTwo = last


game = TicTacToe()
game.start()
