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
    """
    gmatrix = numpy.array([ 
                        [0, 0, 0], 
                        [0, 0, 0], 
                        [0, 0, 0]
                      ])
                        """

    def __init__(self):
        self.gmatrix = numpy.array([ 
                        [0, 0, 0], 
                        [0, 0, 0], 
                        [0, 0, 0]
                      ])

        # true - Game Overm false - play game
        self.gameover = False
        pass

    def getValueYX(self, y, x):
        cell = self.gmatrix[y, x]
        return cell
        pass
    
    def setValueYX(self, y, x, value):
        self.gmatrix[y, x] = value
        pass

    def setCellYX(self, cell, value):
        y = cell[0]
        x = cell[1]
        self.gmatrix[y, x] = value
        pass

    def getMatrix(self):
        return self.gmatrix
        pass

    property
    def gameover(self):
        return self.gameover
        pass

    def victory_check(self):
        result = False

        return result
        pass

    def setPlayer(self, player):

        self.human = player
        self.ai = Cell.ZERO.value if player == Cell.CROSS.value else Cell.ZERO.value
        # return [self.ai, self.human]
        return self.ai
        pass

    pass

class Human(object):

    pass

class ArtificalIntelegence(object):

    def __init__(self, ai):
        self.ai = ai
        pass

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
        al = len(arr)
        index = random.randint(0, al - 1)
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
