with open("2021/day1/1.in", "r") as f:
    data = [int(num.strip())for num in f.readlines()]

#  Start at -1 as no previous measurement for first time
part1 = -1
part2 = -1

previous_measurements = 0
previous_sums = 0
full_window = True
for idx, depth in enumerate(data):
    # End of list theres not a full window
    if idx+3 > len(data):
        full_window = False
        
    depth_sum = sum(data[idx:idx+3])
    if depth > previous_measurements:
        part1 += 1
    if full_window and depth_sum > previous_sums:
        part2 += 1
    
    previous_measurements = depth
    previous_sums = depth_sum

print(f"Part1: {part1}")
print(f"Part2: {part2}")