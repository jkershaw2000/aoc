import math

with open("2021/day7/7.in") as pos:
    data = [int(num)for num in pos.readline().split(",")]

min_fuel_p1 = math.inf
min_fuel_p2 = math.inf
for target in range(max(data)):
    fuel_p1 = 0
    fuel_p2 = 0
    for pos in data:
        fuel_p1 += abs(pos-target)
        n = abs(pos-target)
        fuel_p2 += (n*(n+1))/2

    if fuel_p1 < min_fuel_p1:
        min_fuel_p1 = fuel_p1
    if fuel_p2 < min_fuel_p2:
        min_fuel_p2 = int(fuel_p2)

part1 = min_fuel_p1
part2 = min_fuel_p2
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")


