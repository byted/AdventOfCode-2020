import sys
import re
import math
    
def chinese_theorem(busses):
    # General idea is based on this: http://mathforum.org/library/drmath/view/75030.html

    def is_prime(a):
        if a < 2:
            return False
        return all(a % i for i in range(2, a))  # if no smaller number divids a evenly, a is prime

    def calc_lcm(vals):
        # all vals are prime -> simply multiply all of them
        return math.prod(vals)

    # for this theorem to work, bus durations have to be [pairwise coprime](https://en.wikipedia.org/wiki/Coprime_integers#:~:text=Pairwise%20coprimality)
    # which is the case if all durations are prime numbers - and seems to be the case for all given inputs but let's double check...
    _, durations_only = zip(*busses)
    if any(not is_prime(d) for d in durations_only):
        print(f'Uh oh, bus durations are not prime - we need a different solution')
        return -1

    # calc lcms for all _other_ bus durations and append to current bus info
    # we can skip the one with remainder 0 as it will be 0 later on anyway
    lcms = [
        (remainder, duration, calc_lcm(durations_only[0:ix] + durations_only[ix+1:])) 
        for ix, (remainder, duration) in enumerate(busses) if remainder != 0
    ]
    # for each bus, solve the equation (lcm_of_other busses * n) % duration = remainder for n using [reverse modulo operation](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) 
    # see [](https://docs.python.org/3/library/functions.html#pow) for how pythons pow() can be used
    inverse_modulos = [remainder * pow(lcm, -1, duration) * lcm for remainder, duration, lcm in lcms]

    # sum all together to find a common multiple for all lcms that fullfils all of the the above equations at once
    # this might not be the smallest possible one so we take it module the lcm of all buss durations
    return sum(inverse_modulos) % math.prod(durations_only)

    # Or use a library: 
    # from sympy.ntheory.modular import crt
    # remainders, durations = zip(*busses)
    # return crt(durations, remainders)[0]


with open('input.txt') as f:
    target, busses = f.readlines()

target = int(target)
raw_busses = busses.split(',')
bus_count = len(raw_busses)

# Challenge 1
busses = [int(b) for b in raw_busses if b != 'x']
closest_times = [(b, math.ceil(target/b) * b) for b in busses]
diffs_to_target = sorted(
    [(b, arrival-target) for b, arrival in closest_times],
    key=lambda x: x[1]
)
print(f'Challenge 1: {diffs_to_target[0][0] * diffs_to_target[0][1]}')

# Challenge 2
# The algorithm based on the Chinese Remainder Theorem implicitly searches for a negative offset (e.g. bus 2 leaves 1 minute _before_ bus 1) which would give us a wrong solution.
# we "offset" the offsets: the bus expected to leave last has offset 0 and the first bus gets the offset of the last one - we "offset" the offset with the number of busses
# This means we're solving for the timestamp the last bus leaves -> we remove the offsets's offset to get timestamp of the first bus
remainder_offset = bus_count-1
busses = [(remainder_offset-ix, int(b)) for ix, b in enumerate(raw_busses) if b != 'x']

print(f'Challenge 2: {chinese_theorem(busses)-remainder_offset}')
