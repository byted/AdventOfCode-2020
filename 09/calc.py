import sys
import re

def is_sum(xs, number):
    xs = sorted(xs)
    for ix, n in enumerate(xs[:-1]):
        for m in xs[ix+1:]:
            if n+m > number:
                break
            if n+m == number:
                return True
    return False

def find_contiguous(xs, number):
    for ix, n in enumerate(xs[:-1]):
        acc = [n]
        for m in xs[ix+1:]:
            acc.append(m)
            current_sum = sum(acc)
            if current_sum == number:
                acc = sorted(acc)
                return acc[0]+acc[-1]
            if current_sum > number:
                break


with open('input.txt') as f:
    numbers = [int(l) for l in f.readlines()]

prefix_length = 25
for current_pos, number in enumerate(numbers[prefix_length:]):
    prefix = numbers[current_pos:(prefix_length+current_pos)]

    if not is_sum(prefix, number):
        print(f'Challenge 1: {number}')
        print(f'Challenge 2: {find_contiguous(numbers, number)}')
        break



