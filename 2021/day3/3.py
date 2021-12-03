with open("2021/day3/3.in", "r") as f:
    data = [num.strip() for num in f.readlines()]

def count_bits(data, i):
    ones, zeros = 0, 0
    for val in data:
        if val[i] == "0":
            zeros += 1
        else:
            ones += 1  
    return zeros, ones

def get_new_search_space(search_space, i, check):
    new_space = []
    for v in search_space:
        if v[i] == check:
            new_space.append(v)
    return new_space

def part1():
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        zeros, ones = count_bits(data, i)
        if zeros > ones:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, base=2) * int(epsilon, base=2)

def part2(data, bit):
    search_space = data
    for i in range(len(data[0])):
        zeros, ones = count_bits(search_space, i)
        if zeros > ones:
            temp = get_new_search_space(search_space, i, str(int(not bit)))
        else:
            temp = get_new_search_space(search_space, i, str(int(bit)))
        search_space = temp
        if len(search_space) == 1:
            return search_space[0]

part1 = part1()
part2 = int(part2(data, True), base=2)*int(part2(data, False), base=2)
print(f"Part1: {part1}")
print(f"Part2: {part2}")
