from timeit import default_timer as timer

def get_input():
    with open("./dayN/N.in","r") as f:
        return [int(line.strip()) for line in f.readlines()]

def p1(data):
    pass

def p2(data):
    pass

print("Day N: ")
data = get_input()
p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")