from collections import Counter
with open("2021/day5/5.in", 'r') as f:
    data = [line.strip().split("->") for line in f.readlines()]

def plot_line_low(x0, y0, x1, y1):
    dx = x1-x0
    dy = y1-y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = (2*dy) -dx
    y = y0
    points = []
    for x in range(x0,x1+1):
        points.append((x,y))
        if D > 0:
            y = y + yi
            D += 2 * (dy-dx)
        else:
            D += 2*dy
    return points

def plot_line_high(x0, y0, x1, y1):
    dx = x1-x0 
    dy = y1-y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = (2*dx) -dy
    x = x0
    points = []
    for y in range(y0,y1+1):
        points.append((x,y))
        if D > 0:
            x+=xi
            D += 2*(dx-dy)
        else:
            D += 2*dx
    return points

def plot_line(x0, y0, x1, y1):
    if abs(y1-y0) < abs(x1-x0):
        if x0>x1:
            points = plot_line_low(x1,y1,x0,y0)
        else:
            points = plot_line_low(x0,y0,x1,y1)
    else:
        if y0 > y1:
            points = plot_line_high(x1,y1,x0,y0)
        else:
            points = plot_line_high(x0,y0,x1,y1)
    return points

grid_p1 = Counter()
grid_p2 = Counter()
for line in data:
    
    x1,y1 = line[0].split(",")
    x2,y2 = line[1].split(",")
    
    x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
    # Part 1
    if x1 == x2 or y1 == y2:
        if x1 == x2:
            points = [(x1, y) for y in range(min(y1,y2),max(y1,y2)+1)]
        else:
            points = [(x,y1) for x in range(min(x1,x2), max(x1,x2)+1)]#plot_line(x1,y1,x2,y2)
        grid_p1 += Counter(points)
        grid_p2 += Counter(points)
    
    else:
        points = plot_line(x1,y1,x2,y2)
        grid_p2 += Counter(points)


part1 = 0
for value in grid_p1.values():
    if value >= 2:
        part1 += 1

part2 = 0
for value in grid_p2.values():
    if value >= 2:
        part2 += 1

print(f"Part 2: {part1}")
print(f"Part 2: {part2}")

