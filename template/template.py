from timeit import default_timer as timer

def get_input():
    with open("./dayN/N.in","r") as f:
        return [int(line.strip()) for line in f.readlines()]

def p1():
    pass

def p2():
    pass

print("Day N: )

p1start = timer()
p1 = p1()
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2()
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")