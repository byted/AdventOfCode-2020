import sys
import re

def step(matrix, current_pos, movement, tree_counter):  
    next_pos = (
        current_pos[0] + movement[0],
        (current_pos[1] + movement[1]) % len(matrix[0])  # Assume we always have at least one row
    )
    # reached goal if outer index > len(matrix)
    if next_pos[0] >= len(matrix):
        # we're done
        return tree_counter
    else:
        if matrix[next_pos[0]][next_pos[1]] == '#':
            tree_counter += 1
        return step(matrix, next_pos, movement, tree_counter)

matrix = []
with open('input.txt') as f:
    for l in f.readlines():
        matrix.append([*l][:-1])    # remove newline

print(f'Matrix height: {len(matrix)} \t Matrix width: {len(matrix[0])}')

# Challenge 1
print(f'Challenge 1: {step(matrix, (0,0), (1, 3), 0)} trees hit')

# Challenge 2
trees_prod = 1
print('Challenge 1:')
for movement in [(1,1), (1,3), (1,5), (1,7), (2,1)]:
    trees = step(matrix, (0,0), movement, 0)
    trees_prod *= trees
    print(f'\t{movement} -> {trees} trees hit')
print(f'Product of all: {trees_prod}')