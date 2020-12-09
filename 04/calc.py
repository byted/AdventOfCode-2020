import sys
import re

REQUIRED = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
])

OPTIONAL = set(['cid'])

def build_pp_dict(raw_passport):
    return { item[:3]: item[4:] for item in re.split(r'\s+|\n', raw_passport) }

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def all_required(passport):
    return set(passport.keys()).issuperset(REQUIRED)

def valid_format(passport):
    if not (re.match(r'^\d\d\d\d$', passport['byr']) and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
        return False

    if not (re.match(r'^\d\d\d\d$', passport['iyr']) and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
        return False

    if not (re.match(r'^\d\d\d\d$', passport['eyr']) and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
        return False

    if not re.match(r'^\d+(cm|in)$', passport['hgt']):
        return False
    
    hgt = int(passport['hgt'][:-2])
    metric = passport['hgt'][-2:]
    if not ((metric == 'cm' and hgt >= 150 and hgt <= 193) or (metric == 'in' and hgt >= 59 and hgt <= 76)):
        return False

    if not re.match(r'^#[0-9a-f]{6}$', passport['hcl']):
        return False

    if not re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl']):
        return False

    if not re.match(r'^\d{9}$', passport['pid']):
        return False  

    return True

matrix = []
with open('input.txt') as f:
    passports = f.read().split('\n\n')

valid_required = 0
valid_formated = 0
for p in passports:
    pp_dict = build_pp_dict(p)
    if not all_required(pp_dict):
        continue

    valid_required += 1
    if valid_format(pp_dict):
        valid_formated += 1

print(f'All fields: {valid_required}')
print(f'\t of which are {valid_formated} well formatted')