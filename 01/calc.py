import sys

TARGET_SUM = 2020

with open('input.txt') as f:
    lines = [int(l) for l in f.readlines()]

lines = sorted(lines)

# Challenge 1 & 2

def find_sum(outer_summands, remaining_xs, layers):
    for ix, cost in enumerate(remaining_xs):
        new_summands = outer_summands + [cost]
        mysum = sum(new_summands)

        if mysum < TARGET_SUM and layers > 1:
            find_sum(new_summands, remaining_xs[(ix+1):], layers-1)
        elif mysum > TARGET_SUM:
            print(f'sum of the two is larger - don\' go further as we\'ve sorted the list')
            break
        elif mysum == TARGET_SUM and layers == 1:
            out = 1
            for i in new_summands:
                out *= i
            print(f'that should be {out}')
            sys.exit()

find_sum([], lines, 3)
