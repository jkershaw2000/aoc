import numpy as np
from collections import Counter

with open("2021/day20/20.in", "r") as f:
    image_enchancement = f.readline().strip()
    f.readline()  # Skip over line
    image = [[c for c in line.strip()] for line in f.readlines()]

# Pad image so can apply to an "infinite" area
infinite_image = np.pad(image, (5, 5), mode="constant", constant_values=".").tolist()


def get_neighbours(row, col):
    for i in row - 1, row, row + 1:
        for j in col - 1, col, col + 1:
            yield i, j


padding = (".", "#")


def solve(infinite_image, runs=2):
    for run in range(runs):
        new_image = [
            ["." for _ in range(len(infinite_image[0]))]
            for _ in range(len(infinite_image))
        ]

        for row in range(len(infinite_image)):
            for col in range(len(infinite_image)):
                neighbours = list(get_neighbours(row, col))
                sub_image = [
                    infinite_image[i][j]
                    if (i >= 0 and i < len(infinite_image))
                    and (j >= 0 and j < len(infinite_image[0]))
                    else padding[run % 2]
                    for i, j in neighbours
                ]

                lookup = "".join("0" if pixel == "." else "1" for pixel in sub_image)
                new_image[row][col] = image_enchancement[int(lookup, 2)]

        infinite_image = new_image

    count = Counter()
    for row in infinite_image:
        count += Counter(row)
    return count["#"]


part1 = solve(infinite_image, runs=2)
infinite_image = np.pad(
    image, (110, 110), mode="constant", constant_values="."
).tolist()
part2 = solve(infinite_image, runs=50)
print(f"Part 1: {part1}")
print(f"part 2: {part2}")
