from Game import Game
import numpy as np
import random
from Cell import Cell

class ArtificalIntelegence(object):
    
    def __init__(self, ai):
        self.ai = ai
        pass


    def getRandomFromArr(self, arr): 
        al = len(arr) - 1

        if(al < 1):
            return False

        index = random.randint(0, al)
        return arr[index]
        pass

    # �������� , �� ����� � ����
    # ���������� ������ 
    def makeStep(self, game1):

        return self.randomStep(game1)
        pass

    def randomStep(self, game1):
        arr = game1.getZeroArr()
        # !!!
        random_cell = self.getRandomFromArr(arr)

        return random_cell
        pass

    pass
