with open("2021/day2/2.in", "r") as f:
    data = [line.strip().split()for line in f.readlines()]

depth_p1 = 0
depth_p2 = 0
pos = 0
aim = 0

for dir, val in data:
    if dir == "forward":
        pos += int(val)
        depth_p2 += aim * int(val)
    elif dir == "down":
        depth_p1 += int(val)
        aim += int(val)
    elif dir == "up":
        depth_p1 -= int(val)
        aim -= int(val)
        
part1 = depth_p1*pos
part2 = depth_p2*pos
print(f"Part1: {part1}")
print(f"Part2: {part2}")