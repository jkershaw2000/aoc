import copy
with open("2021/day3/3.in", "r") as f:
    data = [num.strip() for num in f.readlines()]

gamma = ""
epsilon = ""

for i in range(len(data[0])):
    ones = 0
    zeros = 0
    for val in data:
        if val[i] == "0":
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

search_space = copy.deepcopy(data)
for i in range(len(data[0])):
    ones = 0
    zeros = 0
    for val in search_space:
        if val[i] == "0":
            zeros += 1
        else:
            ones += 1
    temp = []
    if zeros > ones:
        for v in search_space:
            if v[i] == "0":
                temp.append(v)
    else:
        for v in search_space:
            if v[i] == "1":
                temp.append(v)
    search_space = temp
ox = search_space[0]

search_space = copy.deepcopy(data)
for i in range(len(data[0])):
    ones = 0
    zeros = 0
    if len(search_space) == 1:
        break
    for val in search_space:
        if val[i] == "0":
            zeros += 1
        else:
            ones += 1
    temp = []
    if ones > zeros or ones == zeros:
        for v in search_space:
            if v[i] == "0":
                temp.append(v)
    else:
        for v in search_space:
            if v[i] == "1":
                temp.append(v)
    search_space = temp
    print(search_space)       

car = search_space[0]
print(int(ox, base=2), int(car, base=2))

part1 = int(gamma, base=2) * int(epsilon, base=2)
part2 = int(ox, base=2) * int(car, base=2)

print(f"Part1: {part1}")
print(f"Part2: {part2}")
