with open("2021/day22/22.in", "r") as f:
    file_data = [line for line in f.readlines()]
instructions = []
for line in file_data:
    on, axis = line.split()
    axis = [tuple(a[2:].split("..")) for a in axis.split(",")]
    instructions.append((on, axis))

space_p1 = {
    (x, y, z): 0 for x in range(-50, 51) for y in range(-50, 51) for z in range(-50, 51)
}
for on, dimensions in instructions[:20]:
    coords = [
        [x, y, z]
        for x in range(int(dimensions[0][0]), int(dimensions[0][1]) + 1)
        for y in range(int(dimensions[1][0]), int(dimensions[1][1]) + 1)
        for z in range(int(dimensions[2][0]), int(dimensions[2][1]) + 1)
    ]
    for c in coords:
        # Check in range
        if c[0] < -50:
            c[0] = -50
        elif c[0] > 50:
            c[0] = 50
        if c[1] < -50:
            c[1] = -50
        elif c[1] > 50:
            c[1] = 50
        if c[2] < -50:
            c[2] = -50
        elif c[2] > 50:
            c[2] = 50

        c = tuple(c)
        if on == "on":
            space_p1[c] = 1
        elif on == "off":
            space_p1[c] = 0


part1 = sum(space_p1.values())
print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")
