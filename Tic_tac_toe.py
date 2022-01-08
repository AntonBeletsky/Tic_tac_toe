import os
from Game import *
from ConsoleInputOutput import ConsoleIO


class TicTacToe(object):

    def __init__(self):
        """Constructor"""
        self.game1 = Game()
        pass

    def __del__(self):
        """Destructor"""
        pass

    def main(self):
        print("Welcome to Tic Tac Toe")
        self.game1 = Game()
        game1 = self.game1

        while(game1.gameover != False):

            game1.gameover = True

            pass
        """
        print(game1.getMatrix())

        y = 2
        x = 0
        game1.setValueYX(y, x, Cell.CROSS.value)
        print(game1.getMatrix())
        """
        # os.system("pause")
        pass

    pass


MainGame = TicTacToe()


MainGame.game1.setValueYX(0, 0, 2)
MainGame.game1.setValueYX(1, 1, 2)
MainGame.game1.setValueYX(2, 2, 2)


CIO = ConsoleIO()
CIO.demo(MainGame.game1)

ai = ArtificalIntelegence()

gmatrix = MainGame.game1.getMatrix()

a = 2 + 2

# !!!
z_arr = ai.getZeroArr(gmatrix)

#print("ZERO ARR: ")
#print(z_arr)

r_cell = ai.makeStep(MainGame.game1)




MainGame.game1.setCellYX(r_cell, 1)

print(r_cell)

CIO.demo(MainGame.game1)

print(r_cell)

os.system("pause")

var = CIO.inputUserStep()



pass