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

        if(player1 == Cell.ZERO.value):
            player2 = Cell.CROSS.value
            
        if(player1 == Cell.CROSS.value):
            player2 = Cell.ZERO.value

        return player2
        pass

    def getZeroArr(self):
        ZeroArr = []
        y = 0
        while(y < 3):
            x = 0
            while(x < 3):
                cell_value = self.gmatrix[y, x]

                if(cell_value == Cell.EMPTY.value):
                    ZeroArr.append([y, x])
                
                x = x + 1
                pass
            y = y + 1
            pass
        
        return ZeroArr

    pass
