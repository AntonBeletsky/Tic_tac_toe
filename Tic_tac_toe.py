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

            # print menu
            # print name
            # select x 0
            # play 
            # victory check

            game1.gameover = True

            pass

        pass

    pass


MainGame = TicTacToe()


MainGame.game1.setValueYX(0, 0, 2)
MainGame.game1.setValueYX(1, 1, 2)
MainGame.game1.setValueYX(2, 2, 2)


CIO = ConsoleIO()

human_cell = CIO.setPlayer()
ai_cell = MainGame.game1.setPlayer(human_cell)

AI = ArtificalIntelegence(MainGame.game1.ai) # добавить переменну. нолик или кресик в конструктор


CIO.demo(MainGame.game1)

gmatrix = MainGame.game1.getMatrix()

# !!!
z_arr = AI.getZeroArr(gmatrix)


r_cell = AI.makeStep(MainGame.game1)

MainGame.game1.setCellYX(r_cell, 1)

print(r_cell)

CIO.demo(MainGame.game1)

print(r_cell)

os.system("pause")

var = CIO.inputUserStep()



pass