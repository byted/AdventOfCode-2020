import sys
import re
import math
from collections import defaultdict
from functools import reduce
from tqdm import tqdm

# 
# Just copy/pasted - AoC becomes more like work every day
# should be generalized for any kind of dimension but I can't be bothered right now
# 

def get_neighbors(wix, zix, yix, xix):
    neighbors = []
    for w in range(wix-1, wix+2):
        for z in range(zix-1, zix+2):
            for y in range(yix-1, yix+2):
                for x in range(xix-1, xix+2):
                    if (w,z,y,x) == (wix, zix, yix, xix):
                        continue
                    neighbors.append((w,z,y,x))
    return neighbors

def get_coord(space, coord):
    return space[coord[0]][coord[1]][coord[2]][coord[3]]

def is_in_current_space(space, w, z,y,x):
    return w in range(0, len(space)) and z in range(0, len(space[0])) and y in range(0, len(space[0][0])) and x in range(0, len(space[0][0][0]))

def grow(space):
    for wix, w in enumerate(space):
        for zix, z in enumerate(w):
            for yix, y in enumerate(z):
                y.insert(0, '.')
                y.insert(len(y), '.')
            z.insert(0, ['.'] * len(z[0]))
            z.insert(len(z), ['.'] * len(z[0]))

        w.insert(0, [ ['.'] * len(space[0][0][0]) ] * len(space[0][0]))
        w.insert(len(w), [ ['.'] * len(space[0][0][0]) ] * len(space[0][0]))
    

    space.insert(0, [ [ ['.'] * len(space[0][0][0]) ] * len(space[0][0]) ] * len(space[0]))
    space.insert(len(space), [ [ ['.'] * len(space[0][0][0]) ] * len(space[0][0]) ] * len(space[0]))



def check_neighbors(space, wix, zix, yix, xix):
    active_neighbors = 0
    
    # count neighbors that are '#'
    for n_coords in get_neighbors(wix,zix,yix,xix):
        if not is_in_current_space(space, *n_coords):
            # outside, count as inactive by default
            continue
        if get_coord(space, n_coords) == '#':
            active_neighbors += 1
        if active_neighbors > 3:
            break
    # print(f'{zix}-{yix}-{xix} {space[zix][yix][xix]} -> {active_neighbors} => ', end ='')
    if  space[wix][zix][yix][xix] == '#' and active_neighbors in (2,3) or space[wix][zix][yix][xix] == '.' and active_neighbors == 3:
        return '#'
    return '.' 
    

def print_space(space):
    print('\n-----')
    for i, layer1 in enumerate(space):
        for j, layer2 in enumerate(layer1):
            print(f'w={i} z={j}')
            for row in layer2:
                print(''.join(row))

def count_active(space):
    counter = 0
    for w in space:
        for z in w:
            for y in z:
                for x in y:
                    if x == '#':
                        counter += 1
    return counter



# Let's go

with open('input.txt') as f:
    # space[w][z][y][x]
    foo = f.readlines()
    space = [[[[c for c in l.strip()] for l in foo]]]

# print_space(space)

for _ in tqdm(range(6)):
    new_space = []
    grow(space)
    for wix, w in enumerate(space):
        new_space.append([])
        for zix, z in enumerate(w):
            new_space[wix].append([])
            for yix, y in enumerate(z):
                new_space[wix][zix].append([])
                for xix, x in enumerate(y):
                    new_space[wix][zix][yix].append(check_neighbors(space, wix, zix, yix, xix))

    space = new_space
    # print_space(space)

print(f'Challenge 1: {count_active(space)}')
