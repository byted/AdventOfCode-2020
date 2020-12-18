import sys
import re
import math
from collections import defaultdict
from functools import reduce


with open('input.txt') as f:
    lines = f.readlines()

# Challenge 1

def calc_if_possible(stack):
    if len(stack) > 2 and stack[-2] in '+*':
        right = stack.pop()
        op = stack.pop()
        left = stack.pop()
        stack.append(right + left) if op == '+' else stack.append(right * left)

together = 0
for line in lines:
    stack = []
    for c in line:
        if c == ' ':
            continue
        elif c in '1234567890':
            stack.append(int(c))
            calc_if_possible(stack)
        elif c in '+*(':
            stack.append(c)
        elif c == ')':
            del stack[-2]
            calc_if_possible(stack)
    together += stack[0]

print(f'Challenge 1: {together}')


# Challenge 1

def calc(op_stack, number_stack):
    right = number_stack.pop()
    op = op_stack.pop()
    left = number_stack.pop()
    number_stack.append(right + left) if op == '+' else number_stack.append(right * left)

together = 0
for line in lines:
    # Let's try the SHunting-Yard algorithm: https://en.wikipedia.org/wiki/Shunting-yard_algorithm
    op_stack = []
    number_stack = []
    for c in line:
        if c == ' ':
            continue
        elif c in '1234567890':
            number_stack.append(int(c))
        elif c in '+(':
            op_stack.append(c)
        elif c in '*':
            while len(op_stack) > 0 and op_stack[-1] in '+*':
                calc(op_stack, number_stack)
            # while len(op_stack) > 0 and op_stack[-1] == '*':
            #     calc(op_stack, number_stack)
            op_stack.append(c)
        elif c in ')':
            while len(op_stack) > 0 and op_stack[-1] != '(':
                calc(op_stack, number_stack)
            if op_stack[-1] != '(':
                print('ERROR')
            op_stack.pop()
    
    while len(op_stack) > 0:
        calc(op_stack, number_stack)

    together += number_stack[0]

print(f'Challenge 2: {together}')