from timeit import default_timer as timer

def get_input():
    with open("./day3/3.in","r") as f:
        return [line.strip() for line in f.readlines()]


def p1():
    res, pos = 0, 0
    data = get_input()
    for line in data:
        if line[pos] == '#':
            res += 1
        pos = (pos + 3) % len(line)
    return res

def p2():
    slopes = [  (1, 1),
                (3, 1),
                (5, 1),
                (7, 1),
                (1, 2) ]
    data = get_input()
    res = 1
    for slope in slopes:
        posX, posY = 0, 0
        temp = 0 
        while posY < len(data):
            if data[posY][posX] == '#':
                temp += 1 
            posY = posY + slope[1]
            posX = (posX+slope[0]) % len(data[0])
        res *= temp
    return res

p1start = timer()
p1 = p1()
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2()
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")