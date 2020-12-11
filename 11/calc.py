import sys
import re
import curses

# Challenge 1

def get_sourroundings(rix, cix):
    return [
        (rix, cix+1), (rix, cix-1),
        (rix+1, cix), (rix-1, cix),
        (rix+1, cix+1), (rix+1, cix-1),
        (rix-1, cix+1), (rix-1, cix-1)
    ]


def apply_rules(seats, occ_seat_thresh=4):
    next_seats = [ [None] * len(row) for row in seats]
    change_happend = False

    for rix, r in enumerate(seats):
        for cix, c in enumerate(r):
            next_seats[rix][cix] = c
            if c == 'L':
                for row, col in get_sourroundings(rix, cix):
                    if row >= len(seats) or col >= len(r) or row < 0 or col < 0:
                        # out of bounds - no rule break
                        continue

                    if seats[row][col] == '#':
                        # rule broken
                        break
                else:
                    next_seats[rix][cix] = '#'
                    change_happend = True

            elif c == '#':
                occ_counter = 0
                for row, col in get_sourroundings(rix, cix):
                    if row >= len(seats) or col >= len(r) or row < 0 or col < 0:
                        # out of bounds - no rule break
                        continue

                    if seats[row][col] == '#':
                        occ_counter += 1
                
                if occ_counter >= occ_seat_thresh:
                    next_seats[rix][cix] = 'L'
                    change_happend = True

    return (change_happend, next_seats)


# 
#  Challenge 2 cleanup later
# 

def find_left(rix, cix, seats):
    return find_right_helper(seats[rix][:cix][::-1])

def find_right(rix, cix, seats):
    return find_right_helper(seats[rix][cix+1:])

def find_right_helper(row):
    for p in row:
        if p in 'L#':
            return p
    return None


def find_up(rix, cix, seats):
    i = 1
    while rix-i >= 0:
        item = seats[rix-i][cix]
        if item in 'L#':
            return item
        i += 1
    
    return None

def find_down(rix, cix, seats):
    i = 1
    while rix+i < len(seats):
        item = seats[rix+i][cix]
        if item in 'L#':
            return item
        i += 1
    
    return None


def find_bottom_right(rix, cix, seats):
    i = 1
    while rix+i < len(seats) and cix+i < len(seats[0]):
        item = seats[rix+i][cix+i]
        if item in 'L#':
            return item
        i += 1
    
    return None

def find_bottom_left(rix, cix, seats):
    i = 1
    while rix+i < len(seats) and cix-i >= 0:
        item = seats[rix+i][cix-i]
        if item in 'L#':
            return item
        i += 1
    
    return None

def find_top_right(rix, cix, seats):
    i = 1
    while rix-i >= 0 and cix+i < len(seats[0]):
        item = seats[rix-i][cix+i]
        if item in 'L#':
            return item
        i += 1
    
    return None

def find_top_left(rix, cix, seats):
    i = 1
    while rix-i >= 0 and cix-i >= 0:
        item = seats[rix-i][cix-i]
        if item in 'L#':
            return item
        i += 1
    
    return None

def get_sourroundings_extended(*args):
    return [find_left(*args), find_right(*args), find_up(*args), find_down(*args), find_top_left(*args), find_top_right(*args), find_bottom_left(*args), find_bottom_right(*args)]

def apply_rules2(seats, occ_seat_thresh=5):
    next_seats = [ [None] * len(row) for row in seats]
    change_happend = False

    for rix, r in enumerate(seats):
        for cix, c in enumerate(r):
            next_seats[rix][cix] = c
            if c == 'L':
                for p in get_sourroundings_extended(rix, cix, seats):
                    if p == '#':
                        # rule broken
                        break
                else:
                    next_seats[rix][cix] = '#'
                    change_happend = True

            elif c == '#':
                occ_counter = 0
                for p in get_sourroundings_extended(rix, cix, seats):
                    if p == '#':
                        occ_counter += 1
                
                if occ_counter >= occ_seat_thresh:
                    next_seats[rix][cix] = 'L'
                    change_happend = True

    return (change_happend, next_seats)
                        


def run(seats, fn):
    mywindow = curses.initscr()

    while True:
        changed, seats = fn(seats)
        placemap = '\n'.join(''.join(r) for r in seats)

        try:
            mywindow.addstr(0,0, placemap)
        except:
            pass
        mywindow.refresh()

        if not changed:
            curses.endwin()
            print(placemap.count('#'))
            return



with open('input.txt') as f:
    seats = [ [c for c in row.strip()] for row in f.readlines()]


run(seats, apply_rules)
run(seats, apply_rules2)