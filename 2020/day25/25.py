from timeit import default_timer as timer
from typing import no_type_check_decorator

def get_input():
    with open("./day25/25.in","r") as f:
        return [int(line.strip()) for line in f.readlines()]


def p1(data):
    door = data[0]
    key = data[1]
    l = getLoop(key)
    print(l)
    return pow(door, l, 20201227)

def getLoop(key):
    loop = 1
    while True:
        if pow(7, loop, 20201227) == key:
            return loop
        loop += 1
      
print("Day 25: Combo Breaker")
data = get_input()
p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")
