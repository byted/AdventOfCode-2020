import sys
import re

def yes_per_group(g):
    yeses = set()
    persons = g.split('\n')
    for person in persons:
        for yes in person:
            yeses.add(yes)
    return len(yeses)

def all_per_group(g):
    persons = g.split('\n')
    yeses = set(persons[0])
    for person in persons[1:]:
        yeses &= set(person)
    return len(yeses)
        

with open('input.txt') as f:
    groups = f.read().strip().split('\n\n')

# Challenge 1
print(f'Challenge 1: {sum(yes_per_group(g) for g in groups)}')

# Chllenge 2
print(f'Challenge 2: {sum(all_per_group(g) for g in groups)}')

