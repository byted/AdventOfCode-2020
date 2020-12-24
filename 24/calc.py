import sys
import re
import math
import operator
from collections import defaultdict
from functools import reduce

dir_map = {
    '6': (0,1,-1),
    '3': (0,-1,1),
    '4': (-1,0,1),
    '1': (1,0,-1),
    'e': (1,-1,0),
    'w': (-1,1,0)
}

directions = []

with open('input.txt') as f:
    for l in f.readlines():
        directions.append([])
        for c in l.strip().replace('se', '3').replace('sw', '4').replace('ne', '1').replace('nw', '6'):
            # we take a 3d representation of th hex grid as described here: https://www.redblobgames.com/grids/hexagons/
            # nw-se -> x
            # ne-sw -> y
            # e-w -> z
            directions[-1].append(dir_map[c])

# white -> True
# black -> False
color_states = defaultdict(lambda: True)

for direction in directions:
    curr = (0,0,0)
    for step in direction:
        curr = tuple([i+j for i,j in zip(curr, step)])
    color_states[curr] = not color_states[curr]

print(f'Challenge 1: {len([c for c in color_states.values() if not c])}')

def get_neighbord(coords):
    x,y,z = coords
    return [
        (x, y+1, z-1), (x, y-1, z+1),
        (x+1, y, z-1), (x-1, y, z+1),
        (x+1, y-1, z), (x-1, y+1, z)
    ]

def step(color_states):
    to_flip = set()
    adjacent_to_black_tile = defaultdict(lambda: 0)
    for tile, color in [(t,c) for t,c in color_states.items() if not c]:
        adjacent_black_tiles = 0
        for neighbor in get_neighbord(tile):
            if color_states[neighbor] == True:
                adjacent_to_black_tile[neighbor] += 1
            if color_states[neighbor] == False:
                adjacent_black_tiles += 1
        
        if adjacent_black_tiles == 0 or adjacent_black_tiles > 2:
            to_flip.add(tile)
    
    for coords, count in adjacent_to_black_tile.items():
        if count == 2:
            to_flip.add(coords)
    
    for coords in to_flip:
        color_states[coords] = not color_states[coords]

    return color_states

for _ in range(100):
    color_states = step(color_states)

print(f'Challenge 2: {len([c for c in color_states.values() if not c])}')