import os
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

            # ��������� ���� �� ������ ������ � ���� �� ������ !!!
            self.game1.gameover_check()
            
            ## input human YX
            while(self.game1.setCellYX(self.CIO.inputUserStep(), human_cell) == False):
                pass

            # ai play 
            ai_step_cell = AI.makeStep(self.game1)

            # ����������� ������
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


MainGame = TicTacToe()
MainGame.main()

pass