import os
import numpy as np
from Game import Game
from Cell import Cell

class ConsoleIO(object):

    t_empty = np.array([ 
                        '   ', 
                        '   ', 
                        '   ',
                      ])
    t_cross = np.array([ 
                        '* *', 
                        ' * ', 
                        '* *',
                      ])
    t_zero = np.array([ 
                        ' * ', 
                        '* *', 
                        ' * ',
                      ])

    tab = ' ' * 10

    # 0 1 2

    cells = [ t_empty, t_zero, t_cross ]

    def __init__(self):
        self.tx_matrix = np.array([ 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]], 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]], 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]] 
                      ])
                        
        pass

    def gmatrixToTextMatrix(self, gmatrix):

        tx_matrix = np.array([ 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]], 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]], 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]] 
                      ])

        y = 0
        while(y < 3):
            x = 0
            while(x < 3):
                cell = gmatrix[y,x]
                t_cell = self.cells[cell]
                tx_matrix[y, x] = t_cell
                x = x + 1
                pass
            y = y + 1
            pass

        return tx_matrix        
        pass

    def printMatrix(self, tx_matrix):

        print(' ')
        print('╔' + '═' * 3 + '╦'+ '═' * 3 + '╦'+ '═' * 3 + '╗') 

        print('║' + tx_matrix[0, 0, 0] + '║'+ tx_matrix[0, 1, 0] + '║'+ tx_matrix[0, 2, 0] + '║') 
        print('║' + tx_matrix[0, 0, 1] + '║'+ tx_matrix[0, 1, 1] + '║'+ tx_matrix[0, 2, 1] + '║') 
        print('║' + tx_matrix[0, 0, 2] + '║'+ tx_matrix[0, 1, 2] + '║'+ tx_matrix[0, 2, 2] + '║') 

        print('╠' + '═' * 3 + '╬'+ '═' * 3 + '╬'+ '═' * 3 + '╣')
        
        print('║' + tx_matrix[1, 0, 0] + '║'+ tx_matrix[1, 1, 0] + '║'+ tx_matrix[1, 2, 0] + '║') 
        print('║' + tx_matrix[1, 0, 1] + '║'+ tx_matrix[1, 1, 1] + '║'+ tx_matrix[1, 2, 1] + '║') 
        print('║' + tx_matrix[1, 0, 2] + '║'+ tx_matrix[1, 1, 2] + '║'+ tx_matrix[1, 2, 2] + '║') 

        print('╠' + '═' * 3 + '╬'+ '═' * 3 + '╬'+ '═' * 3 + '╣')

        print('║' + tx_matrix[2, 0, 0] + '║'+ tx_matrix[2, 1, 0] + '║'+ tx_matrix[2, 2, 0] + '║') 
        print('║' + tx_matrix[2, 0, 1] + '║'+ tx_matrix[2, 1, 1] + '║'+ tx_matrix[2, 2, 1] + '║') 
        print('║' + tx_matrix[2, 0, 2] + '║'+ tx_matrix[2, 1, 2] + '║'+ tx_matrix[2, 2, 2] + '║') 

        print('╚' + '═' * 3 + '╩'+ '═' * 3 + '╩'+ '═' * 3 + '╝')


        pass

    def next_step(self, game1):
        tx_matrix = self.gmatrixToTextMatrix(game1.getMatrix())
        self.printMatrix(tx_matrix)
        pass

    def inputUserStep(self):

        inputYX = input("Input Y, X (0 - 2): ").split()

        if ( len(inputYX) != 2):
            return self.inputUserStep()
            
        try:
            inputYX = list(map(int, inputYX))
        except ValueError:
            return self.inputUserStep()
            pass

        y = inputYX[0]
        x = inputYX[1]

        correct_data = (y <= 2 and y >= 0) and (x <= 2 and x >= 0)
        
        if(correct_data == False):
            return self.inputUserStep()

        return inputYX
        pass

    def printMenu(self):

        pass

    def setPlayer(self):

        try:
            player = int(input("SLECT CROSS 2, ZERO 1 \n"))
        except ValueError:
            return self.setPlayer()
            pass

        if((player == Cell.ZERO.value) or (player == Cell.CROSS.value)):
            return player
        else:
            return self.setPlayer()
        pass


    pass




