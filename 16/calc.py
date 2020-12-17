import sys
import re
import math
from collections import defaultdict
from functools import reduce


with open('input.txt') as f:
    raw_rules, raw_my_ticket, raw_close_tickets = f.read().split('\n\n')

rules = {}
for r in raw_rules.split('\n'):
    field, r1_1, r1_2, r2_1, r2_2 = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', r).groups()
    rules[field] = [range(int(r1_1), int(r1_2)+1), range(int(r2_1), int(r2_2)+1)]

nearby_tickets = [[int(i) for i in t.split(',')] for t in raw_close_tickets.strip().split('\n')[1:]]

def valid_number(rules, number):
    for r1, r2 in rules.values():
        if number in r1 or number in r2:
            return True
    else:
        return False

def valid_ticket(rules, ticket):
    for i in ticket:
        if valid_number(rules, i):
            continue
        else:
            return (False, i)
    return (True, None)

valid_tickets = []

invalid_sum = 0
for t in nearby_tickets:
    valid, number = valid_ticket(rules, t)
    if valid:
        valid_tickets.append(t)
    else:
        invalid_sum += number
    
print(f'Challenge 1: {invalid_sum}')


# Challenge 2
transposed_valid_tickets = []
for number_ix in range(len(valid_tickets[0])):
    transposed_valid_tickets.append([ticket[number_ix] for ticket in valid_tickets])

valid_cols_for_rule = defaultdict(list)
for ix, target in enumerate(transposed_valid_tickets):
    for name, ranges in rules.items():

        valid, _ = valid_ticket({name: ranges}, target)
        if valid:
            valid_cols_for_rule[name].append(ix)

col_rule_mapping = {}
to_remove = set()
while True:
    for name, cols in valid_cols_for_rule.items():
        if len(cols) == 1:
            col_rule_mapping[cols[0]] = name
            to_remove.add(cols[0])
    
    if len(to_remove) == 0:
        break

    for cols in valid_cols_for_rule.values():
        for v in to_remove:
            if v in cols:
                cols.remove(v)
    to_remove = set()

my_ticket = raw_my_ticket.split('\n')[1].split(',')
prod = math.prod(int(col) for ix, col in enumerate(my_ticket) if col_rule_mapping[ix].startswith('departure'))
print(f'Challenge 2: {prod}')
