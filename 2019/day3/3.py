def get_input():
    with open("3.in", "r") as f:
        i = [val for val in f.read().split("\n")]
        wires = [None, None]
        wires[0] = i[0].split(",")
        wires[1] = i[1].split(",")
        return wires

def calculate_all_points(wire):
    points = {}
    dX = {"L": -1, "R": 1, "U": 0, "D": 0}
    dY = {"L": 0, "R": 0, "U": 1, "D": -1}
    x, y = 0, 0
    steps = 0
    # Iterate through each command in the line, keeping track of every point that we pass through.
    for cmd in wire:
        d = cmd[0]
        n = int(cmd[1:])
        for _ in range(n):
            x += dX[d]
            y += dY[d]
            steps += 1
            if (x,y) not in points:
                points[(x,y)] = steps
    return(points)

wires = get_input()

a = calculate_all_points(wires[0])
b = calculate_all_points(wires[1])
inters = set(a.keys()) & set(b.keys())
print(inters)
print(min([abs(i[0]) + abs(i[1]) for i in inters]))

print(min([a[p] + b[p] for p in inters]))
