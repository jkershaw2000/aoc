from timeit import default_timer as timer
from itertools import combinations

def get_input():
    with open("./day9/9.in","r") as f:
        return [int(line.strip()) for line in f.readlines()]

def sums(lst):
    return set([sum(pair) for pair in combinations(lst, 2)])

def p1():
    data = get_input()
    for i in range(25, len(data)-25):
        if data[i] not in sums(data[i-25:i]):
            return data[i]

def p2(ans):
    data = get_input()
    length = len(data)
    for i in range(length):
        for j in range(i+1, length):
            res = sum(data[i:j])
            if res == ans:
                return min(data[i:j]) + max(data[i:j])
            elif res > ans:
                break

print("Day 9: Encoding Error")

p1start = timer()
part1 = p1()
p1end = timer()
print(f"Part 1: {part1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(part1)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")