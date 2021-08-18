from timeit import default_timer as timer

def get_input():
    with open("./day10/10.in","r") as f:
        return [int(line.strip()) for line in f.readlines()]

def p1(data):
    oneJolt, threeJolts = 0, 1
    currentJoltage = 0
    for adapter in data:
        if adapter - currentJoltage == 1:
            oneJolt += 1
            currentJoltage += 1
        elif adapter - currentJoltage == 3:
            threeJolts += 1
            currentJoltage += 3
    return oneJolt * (threeJolts)

def p2(data):
    data.reverse()
    path = {x:1 for x in data} # Always at least 1 known from part 1
    path.update({0:-1}) # Starting point
    path[data[0]] = 1
    for key in path:
        if key != data[0]:
            sum = 0
            for x in range(1,4): # Check all +1, +2 or +3 jolts
                if key+x in path:
                    sum = sum + path[key+x] # Add all ways to get to that point
                path[key] = sum

    return path[0]

print("Day 10: Adapter Array")

data = get_input()
data.sort()
p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")