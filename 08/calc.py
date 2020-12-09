import sys
import re

def run_code(instructions):
    visited = set()
    acc = 0
    ip = 0

    nop_jmp_stack = []

    while True:
        if ip in visited:
            print(f'looped: {acc}')
            return (False, acc)
        
        if ip >= len(instructions):
            print(f'terminated: {acc}')
            return (True, acc)

        visited.add(ip)
        op, number = instructions[ip]

        if op == 'jmp':
            ip += number
            continue
        
        elif op == 'acc':
            acc += number
        
        ip += 1

        

with open('input.txt') as f:
    instructions = [(l.split(' ')[0], int(l.split(' ')[1])) for l in f.readlines()]

all_changeables = [(instr[0], ix) for ix, instr in enumerate(instructions) if instr[0] in ['jmp', 'nop']]

changes = {
    'jmp': 'nop',
    'nop': 'jmp'
}

# Challenge 1:
print(f'Challenge 1: {run_code(instructions)}')
    
# Challenge 2:
for op, ix in all_changeables:
    new_instructions = [i for i in instructions]    # copy list
    new_instructions[ix] = changes[op], new_instructions[ix][1]

    res, acc = run_code(new_instructions)
    if res:
        print(f'Callenge 2: {acc}')
        break