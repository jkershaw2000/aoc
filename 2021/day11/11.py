with open("2021/day11/11.in", "r") as f:
    data = [[int(oct) for oct in line.strip()] for line in f.readlines()]


def neighbors(matrix, row, col):
    for i in row - 1, row, row + 1:
        if i < 0 or i == len(matrix):
            continue
        for j in col - 1, col, col + 1:
            if j < 0 or j == len(matrix[i]):
                continue
            if i == row and j == col:
                continue
            yield i, j


p1, p2 = False, False
steps = 1
flashes = 0
while not (p1 and p2):
    flashed = set()

    # Increment all energies by 1
    for y in range(len(data)):
        for x in range(len(data[1])):
            data[y][x] += 1

    #  See if any octopuses need to flash after initial incrementing
    to_flash = [
        True if data[y][x] > 9 else False
        for y in range(len(data[0]))
        for x in range(len(data[1]))
    ]

    while any(to_flash):
        for y in range(len(data[0])):
            for x in range(len(data[1])):
                # If octopus has not flashed and should
                if data[y][x] > 9 and (x, y) not in flashed:
                    flashed.add((x, y))
                    data[y][x] = 0

                    for border in neighbors(data, x, y):
                        # If neighbour has not flashed, increment it
                        if (border[0], border[1]) not in flashed:
                            data[border[1]][border[0]] += 1

        # End condition of the loop, check if there are any octopus that should now flash
        to_flash = [
            True if data[y][x] > 9 else False
            for y in range(len(data[0]))
            for x in range(len(data[1]))
        ]

    # Increment total flashes
    flashes += len(flashed)

    # Set all octopuses that flashed to 0
    for x, y in flashed:
        data[y][x] = 0

    # Part 1
    if steps == 100:
        p1 = True
        part1 = flashes

    # Part 2
    if all(
        True if data[y][x] == 0 else False
        for y in range(len(data[0]))
        for x in range(len(data[1]))
    ):
        part2 = steps
        p2 = True

    steps += 1


print(f"Part 1: {part1}")
print(f"Part2: {part2}")
