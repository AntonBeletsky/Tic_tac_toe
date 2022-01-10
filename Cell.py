from enum import Enum

class Cell(Enum):
    EMPTY = 0
    CROSS = 2
    ZERO = 1

    pass

#cell_dict
cell_dict  = { 'EMPTY': Cell.EMPTY.value, 
               'CROSS': Cell.CROSS.value, 
               'ZERO': Cell.ZERO.value 
               }

# print(cd['CROSS'])