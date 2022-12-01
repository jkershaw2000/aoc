with open("2022/day1/1.in", "r") as f:
    elves = [sum(map(int, elf.split("\n"))) for elf in f.read().split("\n\n")]

part1 = max(elves)
print(f"{part1=}")
part2 = sum(sorted(elves)[-3:])
print(f"{part2=}")
