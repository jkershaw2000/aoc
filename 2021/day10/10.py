from statistics import median

with open("2021/day10/10.in", "r") as f:
    data = [line.strip() for line in f.readlines()]

SYNTAX_POINTS = {")": 3,
                "]": 57,
                "}": 1197,
                ">": 25137}

COMPLETION_POINTS = {"(": 1,
                   "[": 2,
                   "{": 3,
                   "<": 4}

PAIRS = {"}": "{",
         "]": "[",
         ")": "(",
         ">": "<"}

score = 0
completion = []
for line in data:
    stack = []
    # Part 1
    for char in line:
        # Add opening brackets to stack
        if char in PAIRS.values():
            stack.append(char)
        else:
            # Closing bracket is not match, calculate score
            if stack.pop() != PAIRS[char]:
                score += SYNTAX_POINTS[char]
                break
    # Part 2
    else:
        #  Check remaining brackets on stack and calculate score
        s = 0
        for bracket in stack[::-1]:
            s =  (s * 5) + COMPLETION_POINTS[bracket]
        completion.append(s)


part1 = score
part2 = median(completion)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
