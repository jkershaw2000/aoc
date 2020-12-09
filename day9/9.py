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

def p2Brute(data, ans):
    
    length = len(data)
    for i in range(length):
        for j in range(i+1, length):
            res = sum(data[i:j])
            if res == ans:
                return min(data[i:j]) + max(data[i:j])
            elif res > ans:
                break

def p2(data, ans):
    i, j = 0, 1
    sum = data[i] + data[j]
    while not sum == ans:
        while sum < ans:
            j += 1
            sum += data[j]
        while sum > ans:
            sum -= data[i]
            i += 1
    return min(data[i:j]) + max(data[i:j])

print("Day 9: Encoding Error")
data = get_input()
p1start = timer()
part1 = p1()
p1end = timer()
print(f"Part 1: {part1} in {p1end-p1start}s.")

p2Brutestart = timer()
p2Brute = p2Brute(data, part1)
p2Bruteend = timer()
print(f"Part 2: {p2Brute} in {p2Bruteend-p2Brutestart}s.")

p2Start = timer()
p2 = p2(data, part1)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2Start}s.")
