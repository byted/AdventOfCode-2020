import sys
import re
import math

with open('input.txt') as f:
    raw_instructions = [i.strip().split(' = ') for i in f.readlines()]

instructions = []
for op, param in raw_instructions:
    if op == 'mask':
        instructions.append((None, [c for c in param]))
    if op.startswith('mem'):
        instructions.append((
            int(op[4:-1]),
            [c for c in "{0:036b}".format(int(param))]
        ))

def write_mem(memory, memory_pos, pos, val):
    for ix in range(pos, len(memory_pos)):
        if memory_pos[ix] == 'X':
            mem_pos_0 = [i for i in memory_pos]
            mem_pos_1 = [i for i in memory_pos]
            mem_pos_0[ix] = '0'
            mem_pos_1[ix] = '1'
            write_mem(memory, mem_pos_0, ix+1, val)
            write_mem(memory, mem_pos_1, ix+1, val)
            return
    memory[int(''.join(memory_pos), 2)] = int(''.join(val), 2)
        

def run_code(instructions, mask_for='param'):
    memory = {}
    bitmask = None
    for memory_pos, param in instructions:
        if memory_pos is None:
            bitmask = param
            continue

        if mask_for == 'param':
            for ix in range(len(bitmask)):
                if bitmask[ix] != 'X':
                    param[ix] = bitmask[ix]
            memory[memory_pos] = int(''.join(param), 2)

        elif mask_for == 'memory':
            memory_pos = [c for c in "{0:036b}".format(memory_pos)]
            for ix in range(len(bitmask)):
                if bitmask[ix] == '1':
                    memory_pos[ix] = '1'
                elif bitmask[ix] == '0':
                    pass
                elif bitmask[ix] == 'X':
                    memory_pos[ix] = 'X'
            write_mem(memory, memory_pos, 0, param)
    return sum(memory.values())


# so much to optimize, so little time (ಥ﹏ಥ)
print(f'Challenge 1: {run_code(instructions)}')
print(f'Challenge 2: {run_code(instructions, mask_for="memory")}')
