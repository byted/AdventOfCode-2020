import sys
import re

turn_matrix = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270
}
inverse_turn_matrix = {v:k for k,v in turn_matrix.items()}

def move_vertical(coords, distance):
    return (coords[0] + distance, coords[1], coords[2])

def move_horizontal(coords, distance):
    return (coords[0], coords[1] + distance, coords[2])

def move(mtype, coords, amount):
    if mtype in 'SW':
        amount = -amount
    if mtype in 'NS':
        coords = move_vertical(coords, amount)
    elif mtype in 'EW':
        coords = move_horizontal(coords, amount)
    return coords

def turn(coords, degrees):
    return (coords[0], coords[1], inverse_turn_matrix[(turn_matrix[coords[2]] + degrees) % 360])


def run_code(instructions):
    coords = (0, 0, 'E')

    for op_type, amount in instructions:
        if op_type in 'NSEW':
            coords = move(op_type, coords, amount)
        
        if op_type == 'F':
            coords = move(coords[2], coords, amount)

        if op_type == 'L':
            coords = turn(coords, -amount)
        if op_type == 'R':
            coords = turn(coords, amount)

    return coords

# Challenge 2

def turn_waypoint(coords, degrees):
    if degrees % 360 == 180:
        return (-coords[0], -coords[1], coords[2])
    if degrees % 360 == 90:
        return (-coords[1], coords[0], coords[2])
    if degrees % 360 == 270:
        return (coords[1], -coords[0], coords[2])
    return coords


def run_code_waypoint(instructions):
    coords = (0, 0, 'E')
    waypoint = (1, 10, None)

    for op_type, amount in instructions:
        if op_type in 'NSEW':
            waypoint = move(op_type, waypoint, amount)
        
        if op_type == 'F':
            coords = move('N' if waypoint[0] > 0 else 'S', coords, amount * abs(waypoint[0]))
            coords = move('E' if waypoint[1] > 0 else 'W', coords, amount * abs(waypoint[1]))

        if op_type == 'L':
            waypoint = turn_waypoint(waypoint, -amount)
        if op_type == 'R':
            waypoint = turn_waypoint(waypoint, amount)

    return coords

    

with open('input.txt') as f:
    instructions = [(l[0], int(l[1:])) for l in f.readlines()]

# Challenge 1:
vertical, horizontal, _ = run_code(instructions)
print(f'Challenge 1: {abs(vertical) + abs(horizontal)}')
    
# Challenge 2:
vertical, horizontal, _ = run_code_waypoint(instructions)
print(f'Challenge 1: {abs(vertical) + abs(horizontal)}')