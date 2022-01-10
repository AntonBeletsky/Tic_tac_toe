from Game import Game
import numpy
import random
from Cell import Cell

class ArtificalIntelegence(object):
    
    def __init__(self, ai):
        self.ai = ai
        pass

    # перенести в Game
    """
    def getZeroArr(self, gmatrix):

        ZeroArr = []
        
        y = 0
        while(y < 3):
            x = 0
            while(x < 3):
                cell_value = gmatrix[y, x]

                if(cell_value == Cell.EMPTY.value):
                    ZeroArr.append([y, x])
                
                x = x + 1
                pass
            y = y + 1
            pass
        
        return ZeroArr
        pass
    """


    def getRandomFromArr(self, arr): 
        al = len(arr) - 1

        if(al < 1):
            return False

        index = random.randint(0, al)
        return arr[index]
        pass

    # походить , ј» ходит в игре
    # возвращает €чейку 
    def makeStep(self, game1):

        return self.randomStep(game1)
        pass

    def randomStep(self, game1):
        # arr = self.getZeroArr(game1.gmatrix)
        arr = game1.getZeroArr()
        # !!!
        random_cell = self.getRandomFromArr(arr)

        return random_cell
        pass

    pass
