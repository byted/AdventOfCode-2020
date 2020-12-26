import sys
import re
import math
from collections import defaultdict
from functools import reduce


with open('input.txt') as f:
    raw_tiles= f.read().strip().split('\n\n')

print(f'{len(raw_tiles)} tiles in input')

borders = defaultdict(list)
tiles = {}

tile_borders = {}
for t in raw_tiles:
    t = t.split('\n')
    tile_id = re.match(r'Tile (\d+):', t[0]).groups()[0]
    north = t[1]
    south = t[-1]
    west = ''.join(i[0] for i in t[1:])
    east = ''.join(i[-1] for i in t[1:])
    tile_borders[tile_id] = (north, east, south, west, north[::-1], east[::-1], south[::-1], west[::-1])
    tiles[tile_id] = set([north, east, south, west])
    for b in (north, east, south, west, north[::-1], east[::-1], south[::-1], west[::-1]):
        borders[b].append(tile_id)

corner_prod = 1
for tid, t in tile_borders.items():
    no_border_count = 0
    for b in t:
        if len(borders[b]) == 1:
            no_border_count += 1
    if no_border_count >= 4:
        print(f'corner piece: {tid}')
        corner_prod *= int(tid)

print(f'Challenge 1: {corner_prod}')

# Only part 1 for today
