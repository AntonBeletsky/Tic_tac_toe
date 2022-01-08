import os
from Game import *
from ConsoleInputOutput import ConsoleIO


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

        
        while(self.game1.gameover == False):
            
            # print matrix
            self.CIO.next_step(self.game1)

            # select x 0
            # human_arr_yx = self.CIO.inputUserStep()
            # y = human_arr_yx[0]
            # x = human_arr_yx[1]

            # проверить есть ли пустые €чейки и есть ли победа
            self.game1.gameover_check()

            while(self.game1.setCellYX(self.CIO.inputUserStep(), human_cell) == False):
                pass

            # ai play 
            ai_step_cell = AI.makeStep(self.game1)

            # закончились €чейки
            if(ai_step_cell == False):
                self.game1.gameover = True
            else:
                self.game1.setCellYX(ai_step_cell, ai_cell)
            # victory check

            self.game1.victory_check()

            # break
            pass

        pass

    pass


MainGame = TicTacToe()

MainGame.main()

######################################################
"""
MainGame.game1.setValueYX(0, 0, 2)
MainGame.game1.setValueYX(1, 1, 2)
MainGame.game1.setValueYX(2, 2, 2)
"""

# CIO = ConsoleIO()

# human_cell = CIO.setPlayer()
# ai_cell = MainGame.game1.setPlayers(human_cell)
# AI = ArtificalIntelegence(MainGame.game1.ai) 


# CIO.demo(MainGame.game1)

# gmatrix = MainGame.game1.getMatrix()

# !!!
# z_arr = AI.getZeroArr(gmatrix)

# ai_step_cell = AI.makeStep(MainGame.game1)

"""
MainGame.game1.setCellYX(ai_step_cell, ai)

print(r_cell)

CIO.demo(MainGame.game1)

print(r_cell)

os.system("pause")

var = CIO.inputUserStep()
"""

# os.system("pause")

pass