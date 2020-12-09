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
    lines = f.readlines()

reverse_bag_map = {}
bag_map_count = {}

base_bags = set()

for line in lines:
    line = line.strip()
    if line.endswith(' bags contain no other bags.'):
        lhs = line.replace(' bags contain no other bags.', '')
        bag_map_count[lhs] = []
        base_bags.add(lhs)
        continue

    lhs, rhs = line.split(' bags contain ')
    rhs = re.sub(r' bag(s?).$', '', rhs) # remove ends
    for bag_string in re.split(r' bags?, ', rhs):
        match = re.match(r'^(\d+) ', bag_string)
        if not match:
            print(f'error parsing {rhs} - {bag_string}')
            sys.exit()
        
        amount = int(match.group(0))
        bag_type = re.sub(r'^(\d+) ', '', bag_string)

        if lhs in bag_map_count:
            bag_map_count[lhs].append((bag_type, amount))
        else:
            bag_map_count[lhs] = [(bag_type, amount)]

        if bag_type in reverse_bag_map:
            reverse_bag_map[bag_type].append(lhs)
        else:
            reverse_bag_map[bag_type] = [lhs]
        

# Challenge 1
bags = set()
stack = set()
stack.add('shiny gold')

while len(stack) > 0:
    current_bag = stack.pop()
    if current_bag in reverse_bag_map:
        stack.update(reverse_bag_map[current_bag])
        bags.update(reverse_bag_map[current_bag])

print(f'Challenge 1: {len(bags)}')


def calc(bag):
    if len(bag_map_count[bag]) == 0:
        return 0

    counter = 0
    for b, amount in bag_map_count[bag]:
        counter += amount + (amount * calc(b))
    return counter

print(f'Challenge 2: {calc("shiny gold")}')





