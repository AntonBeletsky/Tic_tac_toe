import os
import numpy
from Game import *

class ConsoleIO(object):

    t_empty = numpy.array([ 
                        '   ', 
                        '   ', 
                        '   ',
                      ])
    t_cross = numpy.array([ 
                        '* *', 
                        ' * ', 
                        '* *',
                      ])
    t_zero = numpy.array([ 
                        ' * ', 
                        '* *', 
                        ' * ',
                      ])

    tab = ' ' * 10

    # 0 1 2

    """
    class Cell(Enum):
    EMPTY = 0
    CROSS = 2
    ZERO = 1
    pass
    """
    cells = [ t_empty, t_zero, t_cross ]

    def __init__(self):
        self.tx_matrix = numpy.array([ 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]], 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]], 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]] 
                      ])
                        
        pass

    def gmatrixToTextMatrix(self, gmatrix):
        
        # gmatrix = game.getMatrix()

        tx_matrix = numpy.array([ 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]], 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]], 
                        [[' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,], [' ' * 3,' ' * 3,' ' * 3,]] 
                      ])

        y = 0
        while(y < 3):
            x = 0
            while(x < 3):
                # cell = game.getValueYX(y, x)
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

    def demo(self, game1):
        # 
        print( 
            b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8')
        )

        tx_matrix = self.gmatrixToTextMatrix(game1.getMatrix())

        self.printMatrix(tx_matrix)

        pass

    def next_step(self, game1):
        tx_matrix = self.gmatrixToTextMatrix(game1.getMatrix())
        self.printMatrix(tx_matrix)
        pass

    def inputUserStep(self):

        # print("Input Y, X for Cell (0 - 2), example: 1 1: ")
        # var = input("Enter 2 variables: ").split()

        var = input("Input Y, X (0 - 2): ").split()

        if ( len(var) != 2):
            return self.inputUserStep()
            
        try:
            var = list(map(int, var))
        except ValueError:
            return self.inputUserStep()
            pass

        y = var[0]
        x = var[1]

        # print("y is:", y, " x is:", x)

        correct_data = (y <= 2 and y >= 0) and (x <= 2 and x >= 0)
        
        if(correct_data == False):
            return self.inputUserStep()

        # print ("coorect data: ", correct_data)

        return var
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




