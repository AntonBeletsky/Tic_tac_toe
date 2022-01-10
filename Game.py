import numpy as np
# from Cell import Cell
from Cell import cell_dict as cd



"""
    https://docs.python.org/3/library/enum.html
    https://www.geeksforgeeks.org/getter-and-setter-in-python/
"""

class Game(object):
    def __init__(self):

        # create matrix 3x3 # https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
        self.gmatrix = np.zeros((3, 3), int)
                        
        
        # self.gmatrix = np.zeros((3, 3))

        # true - Game Over false - play game
        self.gameover = False
        pass

    def getValueYX(self, y, x):
        cell = self.gmatrix[y, x]
        return cell
        pass
    
    def setValueYX(self, y, x, value):
        correct_data = (self.gmatrix[y, x] == cd['EMPTY'])
        if(correct_data):
            self.gmatrix[y, x] = value
            
        return correct_data
        pass

    def setCellYX(self, cell, value):
        y = cell[0]
        x = cell[1]
        return self.setValueYX(y, x, value)
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
        ## написать поиск побед
        # 3 по вертикали, 3 по горизнтали , диагонали

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
        self.ai = self.inversePlayer(player)
        return self.ai
        pass

    def inversePlayer(self, player1):
        player2 = 0

        if(player1 == cd['ZERO']):
            player2 = cd['CROSS']
            
        if(player1 == cd['CROSS']):
            player2 = cd['ZERO']

        return player2
        pass

    def getZeroArr(self):
        ZeroArr = []
        y = 0
        while(y < 3):
            x = 0
            while(x < 3):
                cell_value = self.gmatrix[y, x]

                if(cell_value == cd['EMPTY']):
                    ZeroArr.append([y, x])
                
                x = x + 1
                pass
            y = y + 1
            pass
        
        return ZeroArr

    pass
