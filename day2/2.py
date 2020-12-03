from timeit import default_timer as timer

def get_input():
    with open("./day2/2.in", 'r') as f:
        return [line.strip() for line in f.readlines()]

def get_policy(password):
    password =  password.split(' ')
    passRange = password[0].split('-')
    char = password[1][0]
    passString = password[2]
    return char, passRange, passString


def p1():
    valid_passwords = 0
    data = get_input()
    for password in data:
        char, passRange, passString = get_policy(password)
        if passString.count(char) in range(int(passRange[0]), int(passRange[1])+1):
            valid_passwords += 1
    return valid_passwords
    

def p2():
    valid_passwords = 0
    data = get_input()
    for password in data:
        char, passPos, passString = get_policy(password)
        # Only one can be True
        if (passString[int(passPos[0])-1] == char) ^ (passString[int(passPos[1])-1]==char):
            valid_passwords += 1
    return valid_passwords

print("Day 2: Password Philosophy")  

p1start = timer()
p1 = p1()
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2()
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")
    