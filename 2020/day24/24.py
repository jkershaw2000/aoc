from timeit import default_timer as timer
from copy import deepcopy

EAST = 'e'
WEST = 'w'
SOUTHEAST = 'se'
SOUTHWEST = 'sw'
NORTHWEST = 'nw'
NORTHEAST = 'ne'

DIRS = {
    EAST: (+2, 0),
    WEST: (-2, 0),
    SOUTHEAST: (+1, -1),
    SOUTHWEST: (-1, -1),
    NORTHEAST: (+1, +1),
    NORTHWEST: (-1, +1),
}

def get_input():
    with open("./day24/24.in","r") as f:
        data = [line.strip() for line in f.readlines()]
    directions = []
    for line in data:
        i = 0
        tempDirections = []
        while i < len(line):
            if line.startswith((EAST,WEST), i):
                tempDirections.append(line[i])
                i += 1
            else:
                tempDirections.append(line[i:i+2])
                i += 2
        directions.append(tempDirections)
    return directions       
            
            
def p1(data):
    black = set()

    for tile in data:
        tileLocation = getTileLocation(tile)

        if tileLocation in black:
            black.remove(tileLocation)
        else:
            black.add(tileLocation)
    return len(black), black

def getTileLocation(tile):
    location = (0,0)
    for dir in tile:
        location = (location[0] + DIRS[dir][0], location[1] + DIRS[dir][1])
    return location

def getTileNeighbours(tile, black):
    return sum((1 for neigbour in [(tile[0]-d[0],tile[1]-d[1])for d in DIRS.values()] if neigbour in black))

def p2(black):
    for _ in range(100):
        nextBlack = set()
        el = black.pop()
        mx, mX = el[0], el[0]
        my, mY = el[1], el[1]
        black.add(el)
        # Get range to check all tiles against.
        for b in black:
            mx,mX = min(mx, b[0]), max(mX, b[0])
            my,mY = min(my, b[1]), max(mY, b[1])
        for x in range(mx-2, mX + 3):
            for y in range(my-1, mY +2):
                tile = (x,y)
                numNeighbours = getTileNeighbours(tile, black)
                
                if tile in black and numNeighbours in range(1,3):
                    nextBlack.add(tile)
                elif numNeighbours == 2:
                     nextBlack.add(tile)
        black = nextBlack
    return len(black)
                    


print("Day 24: Lobby Layout ")
data = get_input()
p1start = timer()
p1, black = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(black)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")