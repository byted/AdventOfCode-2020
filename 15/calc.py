import sys
import re
import math
from collections import defaultdict
from functools import reduce
import tqdm

def play_memory(starting_numbers, turn_limit):
    def update_turns(turn_dict, number, turn):
        turn_dict[number] = turn_dict[number][-1:] + [turn]

    spoken = defaultdict(list)
    [ update_turns(spoken, number, turn) for turn, number in enumerate(starting_numbers) ]
    last_spoken = starting_numbers[-1]

    for current_turn in tqdm.tqdm(range(len(starting_numbers), turn_limit)):
        turns = spoken[last_spoken]
        if len(turns) == 0 or (len(turns) == 1 and turns[-1] == current_turn -1):
            last_spoken = 0
        else:    
            last_spoken = abs(reduce(lambda acc,x: acc-x, spoken[last_spoken]))
        
        update_turns(spoken, last_spoken, current_turn)

    return last_spoken

print(f'Challenge 1: {play_memory([15,12,0,14,3,1], 2020)}')
print(f'Challenge 2: {play_memory([15,12,0,14,3,1], 30000000)}')

1000000
30000000
