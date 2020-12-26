import sys
import re
import math
import operator
from collections import defaultdict
from collections import deque
from functools import reduce
import tqdm

INPUT = '394618527' 

def play_cup(cups, rounds):
    curr_ix = 0
    highest_lbl = max(cups)
    for _ in range(rounds):
        curr = cups.popleft()
        take_1, take_2, take_3 = cups.popleft(), cups.popleft(), cups.popleft()

        dst = curr - 1
        while True:
            if dst < 1:
                dst = highest_lbl
            if dst == take_1 or dst == take_2 or dst == take_3:
                dst -= 1
            else:
                dst_ix = cups.index(dst)
                break

        cups.insert(dst_ix+1, take_3)
        cups.insert(dst_ix+1, take_2)
        cups.insert(dst_ix+1, take_1)
        cups.append(curr)
    
    print(cups)
    one_index = cups.index(1)
    cups = list(cups)
    print(cups[one_index+1:] + cups[:one_index])
    return cups[one_index+1:] + cups[:one_index]

res = play_cup(deque(int(i) for i in INPUT), 100)

print(f'Challenge 1: {"".join(str(i) for i in res)}')


def play_cup_large(cups, rounds):
    curr_ix = 0
    highest_lbl = 1000000
    cups = deque(cups + [ix for ix in range(max(cups)+1, highest_lbl+1)])

    for _ in tqdm.tqdm(range(rounds)):
        curr = cups.popleft()
        take_1, take_2, take_3 = cups.popleft(), cups.popleft(), cups.popleft()

        dst = curr - 1
        while True:
            if dst < 1:
                dst = highest_lbl
            if dst == take_1 or dst == take_2 or dst == take_3:
                dst -= 1
            else:
                dst_ix = cups.index(dst)
                break

        cups.insert(dst_ix+1, take_3)
        cups.insert(dst_ix+1, take_2)
        cups.insert(dst_ix+1, take_1)
        cups.append(curr)
    
    one_index = cups.index(1)
    return cups[one_index+1] * cups[one_index+2]

# runs in a whopping 2 days
res = play_cup_large([int(i) for i in INPUT], 10000000)

print(f'Challenge 2: {res}')