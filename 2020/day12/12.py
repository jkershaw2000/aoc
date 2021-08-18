from os import DirEntry
from timeit import default_timer as timer

def get_input():
    with open("./day12/12.in","r") as f:
        return [line.strip() for line in f.readlines()]

def p1(data):
    shipFacing = 1
    shipPosX = 0
    shipPosY = 0
    dx = {0:0, 1:1, 2:0, 3:-1, 'N':0, 'S': 0, 'E': 1, 'W': -1}
    dy = {0:1, 1:0, 2:-1, 3:0, 'N':1, 'S':-1, 'E':0, 'W':0}
    turn = {'L': -1, 'R':1}
    for instruction in data:
        cmd = instruction[0]
        amnt = int(instruction[1:])
        if cmd in 'NESW':
            shipPosX += dx[cmd] * amnt
            shipPosY += dy[cmd] * amnt
        elif cmd in 'LR':
            amnt /= 90
            shipFacing = (shipFacing + turn[cmd]*amnt) % 4
        elif cmd == 'F':
            shipPosX += dx[shipFacing] * amnt
            shipPosY += dy[shipFacing] * amnt
  
    return abs(shipPosX) + abs(shipPosY)
          

def p2(data):
    shipPosX = 0
    shipPosY = 0
    wx = 10
    wy = 1
    wDX = {'N': 0, 'S': 0, 'E': 1, 'W': -1}
    wDY = {'N': 1, 'S': -1, 'E': 0, 'W': 0}

    for instruction in data:
        cmd = instruction[0]
        amnt = int(instruction[1:])

        if cmd in 'NESW':
            wx += wDX[cmd] * amnt
            wy += wDY[cmd] * amnt
        elif cmd == 'L':
            for i in range(amnt // 90):
                wx, wy = -wy, wx
        elif cmd == 'R':
            for i in range(amnt//90):
                wx, wy = wy, -wx
        elif cmd == 'F':
            shipPosX += wx * amnt
            shipPosY += wy * amnt  
    return abs(shipPosX) + abs(shipPosY)


print("Day 12: Rain Risk")

data = get_input()
p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")