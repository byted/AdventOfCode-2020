import sys
import re

def is_valid_challenge1(low, high, char, pw):
    matches = len(re.findall(char, pw))
    if matches >= low and matches <= high:
            return True
    return False

def is_valid_challenge2(pos1, pos2, char, pw):
    # != is XOR: it is only true of they're different which means exactly one is True and one is false
    return (pw[pos1-1] == char) != (pw[pos2-1] == char)


good_pws_c1 = 0
good_pws_c2 = 0
lines = []
with open('input.txt') as f:
    for l in f.readlines():
        # 1-3 b: cdefg
        match = re.match(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$', l)
        if not match:
            print(f'Regex didn\'t work for line {l}')
            sys.exit()

        low, high, char, pw = match.groups()
        lines.append(())
        low = int(low)
        high = int(high)

        if is_valid_challenge1(low, high, char, pw):
            good_pws_c1 += 1
        if is_valid_challenge2(low, high, char, pw):
            good_pws_c2 += 1

print(good_pws_c1)
print(good_pws_c2)



