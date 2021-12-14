with open("2021/day13/13.in", "r") as f:
    dots, instructions = f.read().split("\n\n")


def display_grid(dots):
    max_x = max(dot[0] for dot in dots)
    max_y = max(dot[1] for dot in dots)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for dot in dots:
        grid[dot[1]][dot[0]] = "#"
    for line in grid:
        s = "".join(line)
        print(s)


def calculate_new_points(dots, axis, pos):
    new_dots = set()
    for point in dots:
        new_pos = -1
        # Calculate where folded point ends up
        if point[axis] > pos:
            new_pos = pos - (point[axis] - pos)

        # Is there a better way to do this?
        if new_pos != -1 and axis == 0:
            new_dots.add((new_pos, point[1]))
        elif new_pos != -1 and axis == 1:
            new_dots.add((point[0], new_pos))
        else:
            new_dots.add((point[0], point[1]))

    return new_dots


dots = set(tuple(int(l) for l in line.split(",")) for line in dots.split("\n"))
folds = [i.split(" ")[-1] for i in instructions.split("\n")]

p1 = False
for fold in folds:
    axis, pos = fold.split("=")
    pos = int(pos)
    if axis == "x":
        dots = calculate_new_points(dots, 0, pos)
    elif axis == "y":
        dots = calculate_new_points(dots, 1, pos)

    #  Part 1 solution
    if not p1:
        part1 = len(dots)
        p1 = True

print(f"Part 1: {part1}")
# Part 2 - RPCKFBLR
display_grid(dots)
