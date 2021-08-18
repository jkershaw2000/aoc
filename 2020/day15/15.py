from timeit import default_timer as timer
from collections import defaultdict
def get_input():
    with open("./day15/15.in","r") as f:
        return [int(dig)for dig in f.read().split(',')]

def p1(data):
    lastNum = 0
    turn = 1
    spoken = defaultdict(list)
    # Set up with input
    for num in data:
        spoken[num].append(turn)
        turn += 1
        lastNum = num
    
    while turn <= 2020:
        if len(spoken[lastNum]) < 2:
            # Each turn that number was said at
            spoken[0].append(turn)
            lastNum = 0
        else:
            # Turns bwteen last two times it was said
            lastNum = spoken[lastNum][-1] - spoken[lastNum][-2]
            spoken[lastNum].append(turn)
        turn += 1
    return lastNum
    


def p2(data):
    lastNum = 0
    turn = 1
    spoken = defaultdict(list)
    # Set up with input
    for num in data:
        spoken[num].append(turn)
        turn += 1
        lastNum = num
    
    while turn <= 30000000:
        if len(spoken[lastNum]) < 2:
            # Each turn that number was said at
            spoken[0].append(turn)
            lastNum = 0
        else:
            # Turns between last two times it was said
            lastNum = spoken[lastNum][-1] - spoken[lastNum][-2]
            spoken[lastNum].append(turn)
        turn += 1
    return lastNum

print("Day 15: Rambunctious Recitation")
data = get_input()

p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")