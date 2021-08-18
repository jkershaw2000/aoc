from timeit import default_timer as timer
from copy import deepcopy


def get_input():
    with open("/Users/jack/Documents/Github/aoc-2020/day11/11.in", "r") as f:
        rows = [list(line.strip()) for line in f.readlines()]
    seats = {}
    for y, row in enumerate(rows):
        for x, seat in enumerate(row):
            seats[(x, y)] = seat
    return seats


EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def p1(state):
    complete = False
    nextState = deepcopy(state)
    while not complete:
        complete = True
        state = deepcopy(nextState)
        nextState = {}
        for (x, y), seat in state.items():
            numNeighbours = neighbours(state, x, y)
            if seat == EMPTY and numNeighbours == 0:
                nextState[(x, y)] = OCCUPIED
                complete = False
            elif seat == OCCUPIED and numNeighbours >= 4:
                nextState[(x, y)] = EMPTY
                complete = False
            else:
                nextState[(x, y)] = seat
    return list(nextState.values()).count(OCCUPIED)


def neighbours(grid, row, col):
    num = 0
    if grid.get((row+1, col), EMPTY) == "#":  # Bottom
        num += 1

    if grid.get((row-1, col), EMPTY) == "#":  # Top
        num += 1

    if grid.get((row, col+1), EMPTY) == "#":  # Right
        num += 1

    if grid.get((row, col-1), EMPTY) == "#":  # Left
        num += 1

    if grid.get((row+1, col+1), EMPTY) == "#":  # Bottom Right

        num += 1

    if grid.get((row-1, col+1), EMPTY) == "#":  # Top Right
        num += 1

    if grid.get((row+1, col-1), EMPTY) == "#":  # Bottom Left
        num += 1

    if grid.get((row-1, col-1), EMPTY) == "#":  # Top Left
        num += 1

    return num


def p2(state):
    complete = False
    nextState = deepcopy(state)
    while not complete:
        complete = True
        state = deepcopy(nextState)
        nextState = {}
        for (x, y), seat in state.items():
            directions = [(-1, -1), (0, -1), (1, -1),(-1, 0),(1, 0), (-1, 1), (0, 1), (1, 1)]
            numSightNeighbours = [sightNeighbours2(state, x, y, dir[0], dir[1]) for dir in directions].count('#')

            if seat == EMPTY and numSightNeighbours == 0:
                nextState[(x, y)] = OCCUPIED
                complete = False
            elif seat == OCCUPIED and numSightNeighbours >= 5:
                nextState[(x, y)] = EMPTY
                complete = False
            else:
                nextState[(x, y)] = seat
    return list(nextState.values()).count(OCCUPIED)


def sightNeighbours(grid, row, col):
    res = 0
    # Check above
    above = list(reversed([(x, y)
                           for (x, y) in grid.keys() if y < row and col == x]))
    below = list(reversed([(x, y)
                           for (x, y) in grid.keys() if y > row and col == x]))
    right = list(reversed([(x, y)
                           for (x, y) in grid.keys() if y == row and col > x]))
    left = list(reversed([(x, y)
                          for (x, y) in grid.keys() if y == row and col < x]))

    dirs = {'upRight': (1, -1), 'upLeft': (-1, -1),
           'downRight': (1, 1), 'downLeft': (-1, 1)}
    checkSeats = [[],
                  [],
                  [],
                  []]
    for seat in above:
        if grid.get(seat, FLOOR) == OCCUPIED:
            res += 1
            break
        elif grid.get(seat, FLOOR) == EMPTY:
            break
    for seat in below:
        if grid.get(seat, FLOOR) == OCCUPIED:
            res += 1
            break
        elif grid.get(seat, FLOOR) == EMPTY:
            break
    for seat in left:
        if grid.get(seat, FLOOR) == OCCUPIED:
            res += 1
            break
        elif grid.get(seat, FLOOR) == EMPTY:
            break
    for seat in right:
        if grid.get(seat, FLOOR) == OCCUPIED:
            res += 1
            break
        elif grid.get(seat, FLOOR) == EMPTY:
            break
    for check in checkSeats:
        for seat in check:
            if grid.get(seat, FLOOR) == OCCUPIED:
                res += 1
                break
            elif grid.get(seat, FLOOR) == EMPTY:
                break

    return res

def sightNeighbours2(grid, x, y, dx, dy):
    while True:
        y += dy
        x += dx
        if (x, y) not in grid.keys():
            return '.'
        seat = grid.get((x,y))
        if seat == EMPTY or seat == OCCUPIED:
            return seat

print("Day 11: Seating System")
data = get_input()
p1start = timer()
p1 = p1(data)
p1end = timer()

print(f"Part 1: {p1} in {p1end-p1start}s.")
p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.") 
