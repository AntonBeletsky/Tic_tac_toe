import numpy as np
# from Cell import Cell
from Cell import Cell, cell_dict as cd



"""
    https://docs.python.org/3/library/enum.html
    https://www.geeksforgeeks.org/getter-and-setter-in-python/
"""

class Game(object):
    def __init__(self):

        # create matrix 3x3 # https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
        self.gmatrix = np.zeros((3, 3), int)

        # true - Game Over false - play game
        self.gameover = False

        self.winner = 0
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

    # функция вернет true если все элементы массива arr совпадают с параметром cell_player
    def arr_check(self, arr, cell_player):
        return (len(arr) == list(map(lambda lamparam : cell_player if (lamparam == cell_player) else 0, arr)).count(cell_player))
    pass

    def custum_line_check(self, start_y, start_x, delta_y, delta_x, cell_player, matrix):
        counter = 0
        y = start_y
        wy = 0
        while(wy < 3):
            x = start_x
            wx = 0
            while(wx < 3):
                # проверка matrix cell_player
                if(matrix[y,x] == cell_player):
                    counter += 1
                x += delta_x
                wx += 1
                pass
            y += delta_y
            wy += 1
            pass

        return (counter == 3)
    pass


    def horisontal_vertical_check(self, cell_player, matrix):
        i = 0
        while(i < 3):
            if(self.line_check( matrix[i, :], cell_player)):
                return True
            if(self.line_check( matrix[:, i], cell_player )):
                return True
            i += 1
            pass
        return False
        pass

    #arr3 [1, 2, 3] true false
    def line_check(self, arr_line, cell_player):
        return self.arr_check(arr_line, cell_player)
        pass

    # проверка победы заданого игрока
    def victory_check(self, cell_player):

        #horisontal #vertical
        if(self.horisontal_vertical_check(cell_player, self.gmatrix)):
            return True;

        #diagonals 

        #00 11 22 * 1 1
        if(self.custum_line_check(0, 0, 1, 1, cell_player, self.gmatrix)):
            return True;

        #20 11 02 * -1 1
        if(self.custum_line_check(2, 0, -1, 1, cell_player, self.gmatrix)):
            return True;
            
        return False;
        pass

    def victory_checks(self):
        
        if(self.victory_check(cd['CROSS'])):
            self.winner = cd['CROSS']
            return True;

        if(self.victory_check(cd['ZERO'])):
            self.winner = cd['ZERO']
            return True;

        return False
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
                
                x += 1
                pass
            y  += 1
            pass
        
        return ZeroArr

    pass
