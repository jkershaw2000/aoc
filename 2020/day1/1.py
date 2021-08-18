from timeit import default_timer as timer

from itertools import combinations

def get_input():
    with open("./day1/1.in","r") as f:
        return [int(line.strip()) for line in f.readlines()]
    
def p1():
    data = get_input()
    pairs = combinations(data,2)
    return [pair[1] * pair[0] for pair in pairs if pair[1] + pair[0] == 2020]

def p2():
    data = get_input()
    triplets = combinations(data, 3)
    return [triplet[2] * triplet[1] * triplet[0] for triplet in triplets if triplet[2] + triplet[1] + triplet[0] == 2020]

print("Day 1: Report Repair")

p1start = timer()
p1 = p1()
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2()
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")
