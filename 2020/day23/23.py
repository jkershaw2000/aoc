from timeit import default_timer as timer

def get_input():
    with open("./day23/23.in","r") as f:
        return [int(data) for data in f.read()]

def p1(cups):
    for _ in range(100):
        current = cups[0]
        nextTo =  cups[1:4]
        target = current -1 if current > min(cups) else max(cups)
        while target in nextTo:
            target -= 1
            if target == 0:
                target = max(cups)
        
        targetIndex = cups.index(target)
        if targetIndex == 0:
            pass
        else:
            cups = list([cups[0]] + cups[4:targetIndex+1] + nextTo + cups[targetIndex+1:])
        # Rotate list by for next round
        cups = cups[1:] + [current]

    idx = cups.index(1)
    cups = cups[idx+1:] + cups[:idx]
    return "".join([str(c) for c in cups])

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __eq__(self, other):
        return self.label == other

def p2(cups):
    pass


print("Day 23: Crab Cups")
data = get_input()
p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")