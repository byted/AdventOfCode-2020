import sys
import re

with open('input.txt') as f:
    voltages = sorted([int(l) for l in f.readlines()])

one_counter = 0
three_counter = 0
current_out = 0

target_range = list(range(current_out+1, current_out+3+1))
for vix, v in enumerate(voltages):
    if v > target_range[-1]:
        print(f'no fitting adapter')
        sys.exit()

    for tix, target_v in enumerate(target_range):
        if v == target_v:
            target_range = list(range(v+1, v+3+1))
            if tix == 0:
                one_counter += 1
            if tix == 2:
                three_counter += 1
            break

three_counter += 1 # for our own adapter
print(f'Challenge 1: 1s: {one_counter} - 3s: {three_counter} -> {one_counter * three_counter}')


# Challenge 2
# 
# We ignore our own adapter as its always +3 from the highest adapter -> it is always included and doesn't change the number of possibilities
# If we calculate & store in how many ways a number can be reached from the last three preceding numbers (NOT values in our voltages list!)
# we can iteratively traverse the sorted! voltages list and calculate the possibilities for the next value based on our stored values

# initial known number of ways to reach spot i
# - negatives are needed as we go back to -2 if i == 1
# - we can ommit voltages[-1] itself from the range as its never read
# - use defaultdict instead but we're trying ot explain here
ways_to_reach = { i: 0 for i in  range(-2, voltages[-1]) }
# we start a 0 per definition and there is only one way to start
ways_to_reach[0] = 1

for v in voltages:
    # current number can be reached by looking up the preceding three values
    # if such a value is not in our voltages, it will be 0; thus not contribute
    # if it is in our voltages, we already calculated the ways to reach this old value and can re-use it
    ways_to_reach[v] = ways_to_reach[v-1] + ways_to_reach[v-2] + ways_to_reach[v-3]
    
print(f'Challenge 2: {ways_to_reach[voltages[-1]]}')