with open("2021/day15/15.in", "r") as f:
    data = [[int(l) for l in line.strip()] for line in f.readlines()]


def expand(grid):
    expanded = [[None for _ in range(len(grid) * 5)] for _ in range(len(grid) * 5)]

    for row in range(len(grid) * 5):
        for col in range(len(grid) * 5):
            copy = grid[row % len(grid)][col % len(grid)]
            offset = row // len(grid) + col // len(grid)
            risk = (copy + offset - 1) % 9 + 1
            expanded[row][col] = risk
    return expanded


def solve(data, debug=False):
    N = len(data)
    risk = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N - 1, -1, -1):
        for x in range(N - 1, -1, -1):

            # Non Edge - general case
            if y + 1 < N and x + 1 < N:
                risk[y][x] = data[y][x] + min(risk[y + 1][x], risk[y][x + 1])
            # Bottom edge
            elif x + 1 < N:
                risk[y][x] = data[y][x] + risk[y][x + 1]
            # Right Edge
            elif y + 1 < N:
                risk[y][x] = data[y][x] + risk[y + 1][x]
            # End Point
            else:
                risk[y][x] = data[y][x]
            if debug:
                print(f"Point: {(x, y)}, Grid: {data[y][x]}, Risk: {risk[y][x]}")
                input()
    return risk[0][0] - data[0][0]


part1 = solve(data)
expanded_data = expand(data)
part2 = solve(expanded_data)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
