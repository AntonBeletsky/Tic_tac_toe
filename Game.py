from os import P_OVERLAY
import numpy
from enum import Enum
import random

class Cell(Enum):
    EMPTY = 0
    CROSS = 2
    ZERO = 1
    pass

"""
    https://docs.python.org/3/library/enum.html
    https://www.geeksforgeeks.org/getter-and-setter-in-python/
"""

class Game(object):

    # human = 0
    # ai = 0

    def __init__(self):
        self.gmatrix = numpy.array([ 
                        [0, 0, 0], 
                        [0, 0, 0], 
                        [0, 0, 0]
                      ])

        # true - Game Over false - play game
        self.gameover = False
        pass

    def getValueYX(self, y, x):
        cell = self.gmatrix[y, x]
        return cell
        pass
    
    def setValueYX(self, y, x, value):
        correct_data = (self.gmatrix[y, x] == Cell.EMPTY.value)
        if(correct_data):
            self.gmatrix[y, x] = value
            
        return correct_data
        pass

    def setCellYX(self, cell, value):
        y = cell[0]
        x = cell[1]
        return self.setValueYX(y, x, value)
        #self.gmatrix[y, x] = value
        pass

    def getMatrix(self):
        return self.gmatrix
        pass

    def gameover(self):
        return self.gameover
        pass

    def victory_check(self):
        result = False
        # 000 xxx

        if(result):
            self.gameover = True

        return result
        pass

    def gameover_check(self):
        # проверить есть ли пустые ячейки и есть ли победа
        # получить массив пустых ячеек
        pass

    def setPlayers(self, player):

        self.human = player
        ai = 0

        if(player == Cell.ZERO.value):
            ai = Cell.CROSS.value
            
        if(player == Cell.CROSS.value):
            ai = Cell.ZERO.value

        self.ai = ai
        return self.ai
        pass

    pass

class Human(object):

    pass

class ArtificalIntelegence(object):
    
    def __init__(self, ai):
        self.ai = ai
        pass

    # перенести в Game
    def getZeroArr(self, gmatrix):

        ZeroArr = []
        
        y = 0
        while(y < 3):
            x = 0
            while(x < 3):
                cell_value = gmatrix[y, x]

                if(cell_value == Cell.EMPTY.value):
                    ZeroArr.append([y, x])
                
                x = x + 1
                pass
            y = y + 1
            pass
        
        return ZeroArr
        pass


    def getRandomFromArr(self, arr): 
        al = len(arr) - 1

        if(al < 1):
            return False

        index = random.randint(0, al)
        return arr[index]
        pass

    # походить , АИ ходит в игре
    # возвращает ячейку 
    def makeStep(self, game1):

        return self.randomStep(game1)
        pass

    def randomStep(self, game1):
        arr = self.getZeroArr(game1.gmatrix)
        random_cell = self.getRandomFromArr(arr)

        return random_cell
        pass

    pass
