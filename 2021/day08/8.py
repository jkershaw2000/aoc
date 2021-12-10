with open("2021/day8/t2.in", "r") as f:
    data = [line.split(" | ")for line in f.readlines()]

ENCODING = {
    "abcdefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

number_segments = {2:1, 3:7, 4:4, 5:(2,3,5), 6:(0,6,9), 7:8}

outputs = [line[1].strip().split(" ") for line in data]
test_values = [line[0].strip().split(" ") for line in data]

# Part 1
def part1():
    digits = []
    for output in outputs:
        for digit in output:
            if len(digit) in number_segments.keys():
                digits.append(number_segments[len(digit)])
    return len(digits)

def part2():
    numbers = []
    for idx in range(len(test_values)):
        mapping = get_mapping(test_values[idx])
        numbers.append(calculate_output(mapping, outputs[idx]))
    
    return sum(numbers)

def get_mapping(deduce):
    # segment_mapping = {"a": None,"b": None, "c": None, "d": None, "e": None, "f": None, "g": None }

    digit_wiring = {i:{}for i in range(10)}
    for segment in deduce:
        numbers = number_segments[len(segment)]
        if type(numbers) == int:
            digit_wiring[numbers] = set(char for char in segment)

    print(digit_wiring)
    return digit_wiring

def calculate_outputs(mapping, output):
    val = ""
    for digit in output:
        digit = set(d for d in str(digit))
        for pos in mapping.keys():
            if digit == mapping[pos]:
                val += str(pos)
                break
    return val


part1 = part1()
get_mapping()
# part2 = sum(part2(i) for i in range(len(outputs)))
print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")