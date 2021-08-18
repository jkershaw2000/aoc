from collections import Counter

pass_min = 256310
pass_max = 732746
p1 = 0
for password in range(pass_min, pass_max):
    password = str(password)
    digits = [i for i in password]
    increasing = digits == sorted(password)
    # As must be next to each other due to increasing nature,
    # total number == number in row
    adjacent_digits = 2 in Counter(password).values()
    if increasing and adjacent_digits:
        p1 += 1
print(p1)