import sys
import re

def update(p, area):
    middle = ((p[1] - p[0])//2) + p[0]
    if area =='low':
        return (p[0], middle)
    if area == 'high':
        return (middle + 1, p[1])

def calc_seat(bpass):
    row = (0, 127)
    col = (0, 7)
    for c in bpass:
        if c == 'F':
            row = update(row, 'low')
        if c == 'B':
            row = update(row, 'high')
        if c == 'L':
            col = update(col, 'low')
        if c == 'R':
            col = update(col, 'high')

    return (row[0]*8) + col[0]


with open('input.txt') as f:
    seat_ids = sorted([calc_seat(bp) for bp in f.readlines()])

# Challenge 1
print(max(seat_ids))
# Challenge 2
for ix, s in enumerate(seat_ids[:-1]):
    if s+1 != seat_ids[ix+1]:
        print(f'current: {s}, next: {seat_ids[ix+1]}, missing: {s+1}')

