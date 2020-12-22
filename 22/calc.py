import sys
import re
import math
import operator
from collections import defaultdict
from functools import reduce


foods = []
with open('input.txt') as f:
    p1, p2 = [[int(num) for num in p.split('\n')[1:]] for p in f.read().strip().split('\n\n')]

def play_combat(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        if p1[0] > p2[0]:
            p1 = p1[1:] + [p1[0]] + [p2[0]]
            p2 = p2[1:]
        else:
            p2 = p2[1:] + [p2[0]] + [p1[0]]
            p1 = p1[1:]
    return p1 if len(p2) == 0 else p2

winner = play_combat(p1, p2)
winner_score = sum([ix * card for ix, card in enumerate(reversed(winner), 1)])

print(f'Challenge 1: Winner\'s score is {winner_score}')


def play_combat_rec(p1, p2, layer=0):
    seen_deck_configs = set()
    while len(p1) > 0 and len(p2) > 0:
        if (tuple(p1), tuple(p2)) in seen_deck_configs:
            return ('p1', p1)
        seen_deck_configs.add((tuple(p1), tuple(p2)))
    
        if p1[0] <= len(p1)-1 and p2[0] <= len(p2)-1:  # minus the card we just drew
            winner, _ = play_combat_rec(p1[1:p1[0]+1], p2[1:p2[0]+1])
        else:
            winner = 'p1' if p1[0] > p2[0] else 'p2'

        if winner == 'p1' :
            p1 = p1[1:] + [p1[0]] + [p2[0]]
            p2 = p2[1:]
        else:
            p2 = p2[1:] + [p2[0]] + [p1[0]]
            p1 = p1[1:]

    return ('p1', p1) if len(p2) == 0 else ('p2', p2)

_, winners_stack = play_combat_rec(p1, p2)
winner_score = sum([ix * card for ix, card in enumerate(reversed(winners_stack), 1)])

print(f'Challenge 2: Winner\'s score is {winner_score}')