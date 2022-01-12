import os
from typing import Counter, List
from Game import Game
from ConsoleInputOutput import ConsoleIO
from ArtificialIntelligence import ArtificalIntelegence
import numpy as np


## add https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html

class TicTacToe(object):

    def __init__(self):
        """Constructor"""
        # self.game1 = Game()
        pass

    def __del__(self):
        """Destructor"""
        pass

    def main(self):

        print("Welcome to Tic Tac Toe")

        self.game1 = Game()
        self.CIO = ConsoleIO()

        human_cell = self.CIO.setPlayer()
        ai_cell = self.game1.setPlayers(human_cell)

        AI = ArtificalIntelegence(self.game1.ai) 

        # start matrix, first print 
        self.CIO.next_step(self.game1)

        while(self.game1.gameover == False):

            # проверить есть ли пустые ¤чейки и есть ли победа !!!
            self.game1.gameover_check()
            
            ## input human YX
            while(self.game1.setCellYX(self.CIO.inputUserStep(), human_cell) == False):
                pass

            # ai play 
            ai_step_cell = AI.makeStep(self.game1)

            # закончились ¤чейки
            if(ai_step_cell == False):
                self.game1.gameover = True
            else:
                self.game1.setCellYX(ai_step_cell, ai_cell)
            
                
            # victory check
            self.game1.victory_check()

            self.CIO.next_step(self.game1)
            pass
        pass
    pass



# m = np.zeros((3, 3), int)
# https://numpy.org/doc/stable/reference/generated/numpy.matrix.html

# m = np.matrix('0 0 0; 0 0 0; 0 0 0')

#print('matrix')
#print(m)

m = np.zeros((3, 3), int)


m[0,0] = 1
m[1,0] = 1
m[2,0] = 1

#print('arr')
#print (m)

y = 0
print('y:')
while(y < 3):
    print( m[y, :] ) ## горизонталь 
    y  += 1

x = 0
while(x < 3):
    print('x')
    print( m[:, x] ) ## вертикаль
    x += 1

# print ( np.zeros((1, 3), int)[0] )

print( m[:, 0][1] )


"""
старт x старт y
delta x, delta y

0 0 1 1 2 2
0 0
1 1

0 2 1 1 2 0
0 2
1 -1
"""
def diagonalMove(start_x, start_y, delta_x, delta_y, cell_player, matrix):
    counter = 0
    y = start_y
    while(y < 3):
        x = start_x
        while(x < 3):
            # проверка matrix cell_player
            if(matrix[y,x] == cell_player):
                counter += 1
            x += delta_x
            pass
        y += delta_y
        pass

    return (counter == 3)
    pass



a = input()

#######################
"""
# map - посчитать совпадения 1 1 1
# сумма совпадений 3 - победа

# массив
arr = np.array([1,2,2])
# функция возвращает 1 в ячейку если ячейка того игрока что надо
# универсилизация результата, тк ячейки игроков имеют разніе значения
crossl = lambda cell_c : 1 if (cell_c == 2) else 0
zerol  = lambda cell_z : 1 if (cell_z == 1) else 0

# сумма универслаьных значений
crosslr = list(map(crossl, arr)).count(1)

val = 2
unla = lambda unla : 1 if (cell_z == val) else 0
## crosslr = 3 - victory
crosslr = list(map(lambda unla : 1 if (unla == val) else 0, arr)).count(1)

# arr [1, 1, 1] - true

# https://www.w3schools.com/python/python_lambda.asp


# функция вернет true если все элементы массива arr совпадают с параметром cell_player
def arr_check(arr, cell_player):
    return (len(arr) == list(map(lambda lamparam : cell_player if (lamparam == cell_player) else 0, arr)).count(cell_player))
    pass



# victory_cross = (crosslr == 3)

victory_cross = arr_check(arr, 2)

print('list map result:  ', victory_cross)

# все єлементы массива сопадают с параметром - true
print('list map result2:  ', arr_check([1,1,1], 1))
print('list map result3:  ', arr_check([2,2,2], 2))
print('list map result4:  ', arr_check([1,2,2], 2))
print('list map result5:  ', arr_check([0,0,0], 2))

a = input()
"""

###############
MainGame = TicTacToe()
MainGame.main()

pass