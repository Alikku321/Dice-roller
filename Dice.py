# BUTTON TO SPIN THE DICE
# SOMEHOW BUILD THE DICE
# I THINK I NEED ARRAY FOR THE DICE
# I NEED TO BUILD THE DICE
# AND RANDOMIZE

import random
import tkinter

def dice():
    dice = [1,2,3,4,5,6]
    random.shuffle(dice)
    return dice[0]



print(dice())