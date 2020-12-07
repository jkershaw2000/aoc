from timeit import default_timer as timer
import re

def get_input():
    with open("./day4/4.in","r") as f:
        return f.read().split("\n\n")


def p1():
    res = 0
    data = get_input()
    for passport in data:
        check = [field in passport for field in ['byr', 'iyr','eyr', 'hgt', 'hcl', 'ecl', 'pid']]
        if all(check): # cid only non-required field
            res += 1
    return res

def p2():
    res = 0
    for passport in get_input():
        fields = {pair[0]:pair[1] for pair in [field.split(':') for field in passport.split()]}
        try: # If field is missing, invalid.
            check = [ 1920 <= int(fields['byr']) <= 2002,
                    2010 <= int(fields['iyr']) <= 2020,
                    2020 <= int(fields['eyr']) <= 2030,
                    (fields['hgt'][-2:] == 'cm' and int(fields['hgt'][:-2]) in range(150,194)) 
                            or (fields['hgt'][-2:] == 'in' and int(fields['hgt'][:-2]) in range(59,77)),
                    re.match(r"^#[0-9a-z]{6}", fields['hcl']),
                    fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                    len(fields['pid']) == 9,
                    True
                    ]
            if all(check):
                res += 1 
        except KeyError:
            pass
    return res

print("Day 4: Passport Processing")

p1start = timer()
p1 = p1()
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2()
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")