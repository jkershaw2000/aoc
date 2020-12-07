from timeit import default_timer as timer
import collections

def get_input():
    with open("./day7/7.in","r") as f:
        return [line.strip() for line in f.readlines()]

def p1():
    bagsDict = collections.defaultdict(dict)
    for rule in get_input():
        rule = rule.split()
        outer = " ".join(rule[0:2])
        #inner = {" ".join(rule[4+i:4+i+2]): rule[4+i-1] for i in range(1, len(rule[4:]), 4)}
        inner = [" ".join(rule[4+i:4+i+2]) for i in range(1, len(rule[4:]), 4)]
        if  "other bags." in inner:
            bagsDict[outer] = {}
        else:
            bagsDict[outer] = inner
    
    res = [findBags(colour, bagsDict) for colour, _ in bagsDict.items()]
    return sum(res)
    
        
def findBags(colour, bagsDict):
    if "shiny gold" in bagsDict[colour]:
        return True
    if bagsDict[colour] == dict(): # Reached top of recursion
        return False
    else:
        return any([findBags(inner, bagsDict) for inner in bagsDict[colour]])


def p2():
    bagsDict = collections.defaultdict(dict)
    for rule in get_input():
        rule = rule.split()
        outer = " ".join(rule[0:2])
        inner = {" ".join(rule[4+i:4+i+2]):rule[4+i-1] for i in range(1, len(rule[4:]), 4)}
        if  "other bags." in inner:
            bagsDict[outer] = {}
        else:
            bagsDict[outer] = inner
    return findBagsCount("shiny gold", bagsDict) - 1 

def findBagsCount(colour, bagsDict):
    if bagsDict[colour] == {}:
        return 1 # Only the current bag. Bag is empty.
    else:
        return sum([int(num) * findBagsCount(internalColour, bagsDict) for internalColour, num in bagsDict[colour].items()]) + 1 # include current bag
print("Day 7: Handy Haversacks")

p1start = timer()
p1 = p1()
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2()
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")