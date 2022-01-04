import os
from Game import *
from ConsoleInputOutput import ConsoleIO


class TicTacToe(object):
    def __init__(self):
        """Constructor"""
        pass

    def __del__(self):
        """Destructor"""
        pass

    def main(self):
        print("Welcome to Tic Tac Toe")
        game1 = Game()
        print(game1.getMatrix())

        game1.setValueYX(2,0,1)
        print(game1.getMatrix())

        # os.system("pause")
        pass

    pass


MainGame = TicTacToe()
MainGame.main()

a = Cell.CROSS.value
print ( a )

print (ConsoleIO.t_cross )
print (ConsoleIO.t_empty )
print (ConsoleIO.t_zero )

CIO = ConsoleIO()
CIO.demo()