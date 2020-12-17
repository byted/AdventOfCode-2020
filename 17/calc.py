import sys
import re
import math
from collections import defaultdict
from functools import reduce


def get_neighbors(zix, yix, xix):
    neighbors = []
    for z in range(zix-1, zix+2):
        for y in range(yix-1, yix+2):
            for x in range(xix-1, xix+2):
                if (z,y,x) == (zix, yix, xix):
                    continue
                neighbors.append((z,y,x))
    return neighbors

def get_coord(space, coord):
    return space[coord[0]][coord[1]][coord[2]]

def is_in_current_space(space, z,y,x):
    return z in range(0, len(space)) and y in range(0, len(space[0])) and x in range(0, len(space[0][0]))

def grow(space):
    for zix, z in enumerate(space):
        for yix, y in enumerate(z):
            y.insert(0, '.')
            y.insert(len(y), '.')
        z.insert(0, ['.'] * len(z[0]))
        z.insert(len(z), ['.'] * len(z[0]))

    space.insert(0, [ ['.'] * len(space[0][0]) ] * len(space[0]))
    space.insert(len(space), [ ['.'] * len(space[0][0]) ] * len(space[0]))



def check_neighbors(space, zix, yix, xix):
    active_neighbors = 0
    
    # count neighbors that are '#'
    for n_coords in get_neighbors(zix,yix,xix):
        if not is_in_current_space(space, *n_coords):
            # outside, count as inactive by default
            continue
        if get_coord(space, n_coords) == '#':
            active_neighbors += 1
        if active_neighbors > 3:
            break
    # print(f'{zix}-{yix}-{xix} {space[zix][yix][xix]} -> {active_neighbors} => ', end ='')
    if  space[zix][yix][xix] == '#' and active_neighbors in (2,3) or space[zix][yix][xix] == '.' and active_neighbors == 3:
        return '#'
    return '.' 
    

def print_space(space):
    print('\n-----')
    for i, layer in enumerate(space):
        print(f'z={i}')
        for row in layer:
            print(''.join(row))

def count_active(space):
    counter = 0
    for z in space:
        for y in z:
            for x in y:
                if x == '#':
                    counter += 1
    return counter



# Let's go

with open('input.txt') as f:
    # space[z][y][x]
    foo = f.readlines()
    space = [[[c for c in l.strip()] for l in foo]]

for _ in range(6):
    new_space = []
    grow(space)
    for zix, z in enumerate(space):
        new_space.append([])
        for yix, y in enumerate(z):
            new_space[zix].append([])
            for xix, x in enumerate(y):
                new_space[zix][yix].append(check_neighbors(space, zix, yix, xix))

    space = new_space

print(f'Challenge 1: {count_active(space)}')
