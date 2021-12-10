from collections import Counter

data = [3,3,5,1,1,3,4,2,3,4,3,1,1,3,3,1,5,4,4,1,4,1,1,1,3,3,2,3,3,4,2,5,1,4,1,2,2,4,2,5,1,2,2,1,1,1,1,4,5,4,3,1,4,4,4,5,1,1,4,3,4,2,1,1,1,1,5,2,1,4,2,4,2,5,5,5,3,3,5,4,5,1,1,5,5,5,2,1,3,1,1,2,2,2,2,1,1,2,1,5,1,2,1,2,5,5,2,1,1,4,2,1,4,2,1,1,1,4,2,5,1,5,1,1,3,1,4,3,1,3,2,1,3,1,4,1,2,1,5,1,2,1,4,4,1,3,1,1,1,1,1,5,2,1,5,5,5,3,3,1,2,4,3,2,2,2,2,2,4,3,4,4,4,1,2,2,3,1,1,4,1,1,1,2,1,4,2,1,2,1,1,2,1,5,1,1,3,1,4,3,2,1,1,1,5,4,1,2,5,2,2,1,1,1,1,2,3,3,2,5,1,2,1,2,3,4,3,2,1,1,2,4,3,3,1,1,2,5,1,3,3,4,2,3,1,2,1,4,3,2,2,1,1,2,1,4,2,4,1,4,1,4,4,1,4,4,5,4,1,1,1,3,1,1,1,4,3,5,1,1,1,3,4,1,1,4,3,1,4,1,1,5,1,2,2,5,5,2,1,5]
data = dict(Counter(data))
for i in range(9):
    if i not in data.keys():
        data[i] = 0

next_age = {0:6, 1:0, 2:1,3:2, 4:3, 5:4, 6:5, 7:6, 8:7}
part1_days = 80
part2_days = 256
for i in range(part2_days):
    # Number of fish reprodcuing
    new_fish = data[0]
    data = {next_age[age]:data[age] for age in range(1,9)}
    # Fish that were born now are 8 days
    data[8] = new_fish
    # Fish that just reproduced added to fish that were  7 days
    data[6] += new_fish

    if i == part1_days - 1:
        part1 = sum(data.values())
part2 = sum(data.values())

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")