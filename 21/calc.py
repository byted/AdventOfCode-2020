import sys
import re
import math
import operator
from collections import defaultdict
from functools import reduce


foods = []
with open('input.txt') as f:
    for line in f.readlines():
        ingredients, allergens = line.strip().split(' (contains ')
        foods.append((
            set(ingredients.split(' ')),
            # all lines contain allergens -> we can safely remove last character which should be ')'
            allergens[:-1].split(', ')
        ))

all_ingreds = reduce(lambda x,y: x | y, [i for i, _ in foods])

allergene_to_ingreds = defaultdict(list)
for ingredients, allergens in foods:
    for a in allergens:
        allergene_to_ingreds[a].append(ingredients)

allergene_to_shared_ingreds = { a: ingreds[0].intersection(*ingreds[1:]) for a, ingreds in allergene_to_ingreds.items() }


ingred_allergen_mapping = {}
# Let's see if we have allergenes with only 1 ingredient that we can remove - and repeat until done
while len(allergene_to_shared_ingreds) > 0:
    sorted_by_num_of_ingreds = [a for a, i in sorted(allergene_to_shared_ingreds.items(), key=lambda x: len(x[1]))]
    # first element should only have a single ingred
    if len(allergene_to_shared_ingreds[sorted_by_num_of_ingreds[0]]) != 1:
        print(f'No solution possible - no ingredient is in all food items with the same allergen')
        sys.exit()

    # remove from all remaining allergens
    ingred_to_remove = allergene_to_shared_ingreds[sorted_by_num_of_ingreds[0]].pop()
    ingred_allergen_mapping[ingred_to_remove] = sorted_by_num_of_ingreds[0]
    for a in sorted_by_num_of_ingreds[1:]:
        if ingred_to_remove in allergene_to_shared_ingreds[a]:
            allergene_to_shared_ingreds[a].remove(ingred_to_remove)

    del allergene_to_shared_ingreds[sorted_by_num_of_ingreds[0]]

ingreds_wo_allergens = all_ingreds - ingred_allergen_mapping.keys()

counter = 0
for i in ingreds_wo_allergens:
    for food_i, _ in foods:
        if i in food_i:
            counter += 1

print(f'Ingredients w/o allergens occur in {counter} foods')

dangerous_ingreds = ','.join(i for i, _ in sorted(ingred_allergen_mapping.items(), key=lambda x: x[1]))

print(f'Canonical dangerous ingredient list: {dangerous_ingreds}')