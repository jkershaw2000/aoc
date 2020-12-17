from timeit import default_timer as timer

def get_input():
    with open("./day17/17.in","r") as f:
        return [list(line.strip()) for line in f.readlines()]

def p1(data):
    active = list()
    # Intialy Active cubes
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col =='#':
                active.append((i,j,0)) 
    
    # Run for 6 cycles.
    for _ in range(6):
        newActive = []
        nextToCube = []
        for cube in active:
            neighbours = getNeighbours(cube)
            if len([x for x in neighbours if x in active]) in [2,3]:
                newActive.append(cube)
            # Get all cubes neighouring an active one 
            # as can only change if this is the case
            nextToCube += neighbours
        # Inactive cubes are those that arent active.
        inactive = list(set(nextToCube) - set(active))
        # Add to list if 
        newActive += [x for x in inactive if len([x for x in getNeighbours(x) if x in active]) == 3]
        active = newActive
    return len(active)

def getNeighbours(cube):
    neighbours = []    
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if not dx == dy == dz == 0:
                    neighbours.append((cube[0] + dx, cube[1] + dy, cube[2] + dz))
    
    return neighbours

def p2(data):
    active = list()
    # Intialy Active cubes
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col =='#':
                active.append((i,j,0,0)) 
    
    # Run for 6 cycles.
    for _ in range(6):
        newActive = []
        nextToCube = []
        for cube in active:
            neighbours = get4DNeighbours(cube)
            if len([x for x in neighbours if x in active]) in [2,3]:
                newActive.append(cube)
            # Get all cubes neighouring an active one 
            # as can only change if this is the case
            nextToCube += neighbours
        # Inactive cubes are those that arent active.
        inactive = list(set(nextToCube) - set(active))
        # Add to list if has 3 active cbubes next to it
        newActive += [x for x in inactive if len([x for x in get4DNeighbours(x) if x in active]) == 3]
        active = newActive
    return len(active)

def get4DNeighbours(cube):
    neighbours = []  
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1,2):
                    if not dx == dy == dz == dw == 0:
                        neighbours.append((cube[0] + dx, cube[1] + dy, cube[2] + dz, cube[3] + dw))
    return neighbours

print("Day 17: Conway Cubes")
data = get_input()
p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")