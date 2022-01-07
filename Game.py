import numpy
from enum import Enum

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


    pass

class Human(object):

    pass

class ArtificalIntelegence(object):

    pass
