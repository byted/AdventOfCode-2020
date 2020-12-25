import sys
import re
import math
from collections import defaultdict
from functools import reduce


with open('input.txt') as f:
    raw_rules, words = f.read().strip().split('\n\n')
    words = [w.strip() for w in words.split('\n')]

RULES = {}
for r in raw_rules.split('\n'):
    lhs, raw_rhs = r.split(': ')
    if raw_rhs[0] == '"':
        RULES[int(lhs)] = raw_rhs[1:-1]
    else:
        RULES[int(lhs)] = [[int(i) for i in pair.split(' ')] for pair in raw_rhs.split(' | ')]

def check_ands(rules, and_rule, word):
    for r in and_rule:
        suffix = check_depth_first_rec(rules, r, word)
        if suffix is None:
            return None
        word = suffix[0]
    return suffix[0]

def check_depth_first_rec(rules, lhs, word):
    if lhs not in rules:
        print("ERROR")
        sys.exit()
    rhs = rules[lhs]
    if type(rhs) != list:
        if len(word) == 0:
            # no input anymore to fulfill this rule
            return None
        if word[0] == rhs:
            return [word[1:]]
        return None
    
    else:
        suffixes = []
        for rx in rhs:
            suffix = check_ands(rules, rx, word)
            if suffix is not None:
                suffixes.append(suffix)
                return suffixes
        return None

def check(word):
    res = check_depth_first_rec(RULES, 0, word)
    return res is not None and len(res) == 1 and res[0] == ''

counter = 0
for w in words:
    is_valid = check(w)
    if is_valid:
        counter += 1

print(f'Challenge 1: {counter}')

# C2 solution adapted from https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/ggeybw6/
# Still have to figure out why this works exactly
def test(s,seq):
    if s == '' or seq == []:
        return s == '' and seq == [] # if both are empty, True. If only one, False.
    
    r = RULES[seq[0]]
    if type(r) == str:
        if s[0] in r:
            return test(s[1:], seq[1:]) # strip first character
        else:
            return False # wrong first character
    else:
        return any(test(s, t + seq[1:]) for t in r) # expand first term


RULES[8] = [[42], [42,8]]
RULES[11] = [[42,31], [42, 11, 31]]

print(f'Challenge 2: {sum(test(m,[0]) for m in words)}')
