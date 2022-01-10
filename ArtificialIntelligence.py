from Game import Game
import numpy as np
import random
# from Cell import Cell
from Cell import cell_dict as cd

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

    # походить , ј» ходит в игре
    # возвращает ¤чейку 
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
