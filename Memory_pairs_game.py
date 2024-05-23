import random
import os

# Objective: make a simple memory game - turning over 2 cards from a grid at a time

# Approach: draw a grid with numbers in the console, require 2 inputs in co-ordinate system
def init_grid():
    numbers_remaining = [i for i in range(1,19)] + [i for i in range(1,19)]
    global grid
    global unguessed_numbers
    unguessed_numbers = [i for i in range(1,19)]
    grid = [[] for i in range(6)]
    j = 1
    while numbers_remaining != []:
        for i in range(6):
            for p in range(6):
                k = len(numbers_remaining)
                to_remove = random.choice([i for i in range(k)])
                grid[p].append(numbers_remaining[to_remove-1])
                numbers_remaining.pop(to_remove-1)
    print(['a','b','c','d','e','f'])
    for i in grid:
        print(f"{j}: {i}\n")
        j += 1

def printplayergrid(guessednumbers):
    #[[1,4,....],[2,3,12,...]]
    listtoprint = [[] for i in range(6)]
    colortag = 1
    for i in range(6):
        colortag = colortag * -1
        for j in range(6):
            if grid[i][j] not in guessednumbers:
                listtoprint[i].append('\033[34m' + '\u2588') if colortag == 1 else listtoprint[i].append('\033[93m' + '\u2588')
            else:
                listtoprint[i].append(f'\033[32m{grid[i][j]}')
            colortag = colortag * -1
    print('\n'.join(['\033[30m\u2588'.join(cell) for cell in listtoprint]))
def player_input():
    pass
init_grid()
printplayergrid([12])


#Need to - Flip grid, prompt player for input, reveal number at coordinate





















