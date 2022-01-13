import os
from typing import Counter, List
from Game import Game
from ConsoleInputOutput import ConsoleIO
from ArtificialIntelligence import ArtificalIntelegence
import numpy as np
from Cell import cell_value_to_name as ctvn


## add https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html

class TicTacToe(object):

    def __init__(self):
        """Constructor"""
        self.game1 = Game()
        self.CIO = ConsoleIO()
        # self.AI = False
        pass

    def __del__(self):
        """Destructor"""
        pass

    def main(self):

        print("Welcome to Tic Tac Toe")

        human_cell = self.CIO.setPlayer()
        ai_cell = self.game1.setPlayers(human_cell)

        self.AI = ArtificalIntelegence(self.game1.ai) 

        # start matrix, first print 
        self.CIO.next_step(self.game1)

        # играть пока не будет выполнено условие концаи игры
        while(self.game1.gameover == False):

            ## input human YX
            while(self.game1.setCellYX(self.CIO.inputUserStep(), human_cell) == False):
                pass

            # ai play 
            ai_step_cell = self.AI.makeStep(self.game1)

            # закончились ¤чейки
            if(ai_step_cell == False):
                self.game1.gameover = True
            else:
                self.game1.setCellYX(ai_step_cell, ai_cell)
            
            # victory check
            if(self.game1.victory_checks()):
                print(ctvn[self.game1.winner], " WIN!")
                self.game1.gameover = True
                
            self.CIO.next_step(self.game1)
            pass
        pass
    pass



# m = np.zeros((3, 3), int)
# https://numpy.org/doc/stable/reference/generated/numpy.matrix.html

# https://www.w3schools.com/python/python_lambda.asp


MainGame = TicTacToe()
MainGame.main()

pass