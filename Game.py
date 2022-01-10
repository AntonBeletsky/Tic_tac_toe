import numpy
from Cell import Cell


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
        ai_cell_value = 0

        if(player == Cell.ZERO.value):
            ai_cell_value = Cell.CROSS.value
            
        if(player == Cell.CROSS.value):
            ai_cell_value = Cell.ZERO.value

        self.ai = ai_cell_value
        return self.ai
        pass

    pass
